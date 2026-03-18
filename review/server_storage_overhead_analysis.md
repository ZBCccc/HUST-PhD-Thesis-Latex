# 服务端存储开销分析（修正版，Bloom Filter 口径）

## 1. 计量口径

本分析采用**驻留存储（resident storage）**口径，只统计服务端在更新后实际长期持有的数据结构，不计入密钥材料。

在该口径下：

- `\mathsf{TSet}`：按条目累积增长
- `\mathsf{XSet}`：若实现为 Bloom Filter，则其空间由 Bloom Filter 的位数组长度 `M` 决定，为固定大小
- `\mathsf{QTree}`：建立在固定长度位数组上的全局认证树，大小同样由 `M` 决定
- `\mathsf{MPos}` 与 `\mathsf{MTree}`：随关系更新数线性增长

## 2. 对 Nomos 服务端存储的修正理解

### 2.1 `\mathsf{TSet}`

对单条关系更新 `(w,\mathsf{id},\mathsf{op})`，服务端在 `\mathsf{TSet}` 中存储一条记录：

- 地址 `addr`
- 值 `val`
- 代数参数 `\alpha`

因此，若总关系更新数为 `N_rel`，则：

```text
S_TSet = N_rel · (|addr| + |val| + |alpha|)
```

### 2.2 `\mathsf{XSet}`（Bloom Filter 口径）

这是需要纠正的关键点。

虽然每条关系更新会生成 `\ell` 个 XTag，并对 Bloom Filter 的 `\ell` 个位置执行置位操作，但**Bloom Filter 的驻留存储不会随着插入元素个数增长**。它始终只是一个长度为 `M` 的位数组。

因此：

```text
S_XSet = M bits
```

换算为字节：

```text
S_XSet = ceil(M / 8) bytes
```

这意味着：

- 插入更多 XTag 会增加 Bloom Filter 的占用率与误判概率
- 但不会增加 Bloom Filter 本身的总空间

## 3. Bloom Filter 实际占用空间

### 3.1 一般公式

若 `XSet` 由 `M` 个比特组成，则其逻辑存储空间为：

```text
S_BF = M bits = ceil(M / 8) bytes
```

若按 KiB / MiB 计：

```text
S_BF(KiB) = M / (8·1024)
S_BF(MiB) = M / (8·1024·1024)
```

若不直接给定 `M`，而是由“待插入元素个数 + 目标误判率”反推 Bloom Filter 大小，则标准公式为：

```text
M \approx - n \ln p / (\ln 2)^2
```

其中：

- `n`：预计插入的元素个数
- `p`：目标假阳性率

对应的最优哈希函数个数为：

```text
h \approx (M / n) \ln 2
```

因此，若实验中已经固定 `M`，则直接按 `M bits` 计量即可；只有当需要从误判率目标反推 Bloom Filter 尺寸时，才使用上述标准设计公式。

### 3.2 结合第四章默认参数

第四章参数中多次使用：

```text
M = 2^22
```

则：

```text
S_BF = 2^22 bits
     = 4,194,304 bits
     = 524,288 bytes
     = 512 KiB
     = 0.5 MiB
```

因此，若 `XSet` 实现为一个按位压缩存储的 Bloom Filter，那么它本身实际占用的空间就是：

```text
512 KiB
```

### 3.3 一个实现层说明

上面的 `512 KiB` 是**逻辑 / 理论正确的 Bloom Filter 空间**，前提是位数组按位打包存储。

若实现时错误地用“每个 bit 占 1 byte”的数组存储，则会变成：

```text
2^22 bytes = 4 MiB
```

但这不是 Bloom Filter 的标准空间计量口径。论文分析中应采用按位打包后的 `M bits` 口径。

## 4. 修正后的 Nomos 服务端存储公式

因此，在 Bloom Filter 口径下，Nomos 的服务端总存储应写为：

```text
S_S^Nomos
= N_rel · (|addr| + |val| + |alpha|)
+ ceil(M / 8) bytes
```

也可写成比特形式：

```text
S_S^Nomos
= N_rel · (|addr| + |val| + |alpha|)
+ M bits
```

这里的第二项是固定 Bloom Filter 开销，不随插入的 XTag 数量增长。

## 5. VQNomos 的服务端存储公式（基于修正后的 XSet）

VQNomos 不改变 `\mathsf{TSet}` 与 `\mathsf{XSet}` 的基础存储方式，因此：

```text
S_{TSet+XSet}^VQNomos = S_{TSet+XSet}^Nomos
```

VQNomos 的额外服务端开销来自：

- 全局 `\mathsf{QTree}`
- 线性增长的 `\mathsf{MPos}`
- 线性增长的 `\mathsf{MTree}`

因此：

```text
S_S^VQNomos
= S_S^Nomos
+ S_QTree
+ S_MPos
+ S_MTree
```

## 6. 各新增结构的空间

### 6.1 `\mathsf{QTree}`：固定大小

`QTree` 建立在全局位数组 `\mathbf{B}^{(t)} \in \{0,1\}^M` 上。若 `M` 固定，则 `QTree` 的规模固定，只更新节点值，不追加节点。

设补齐后的叶子数为：

```text
M' = 2^{ceil(log2 M)}
```

则完整二叉树节点数为：

```text
2M' - 1
```

若每个节点保存一个 `\lambda` 比特哈希值，则：

```text
S_QTree = (2M' - 1) · \lambda bits
```

当 `M = 2^22` 且 `\lambda = 256 bits` 时：

```text
S_QTree
= (2^23 - 1) · 256 bits
= 268,435,424 bytes
≈ 256 MiB
```

因此，`QTree` 是**固定的全局额外开销**。

### 6.2 `\mathsf{MPos}`：线性增长

对单条关系，`MPos` 为每个 XTag 记录：

- 位置 `r`
- 根 `\mathsf{rt}`
- 签名 `\sigma`

故单条关系的 `MPos` 开销为：

```text
S_MPos,rel = \ell · (|r| + |rt| + |sigma|)
```

若总关系更新数为 `N_rel`，则：

```text
S_MPos = N_rel · \ell · (|r| + |rt| + |sigma|)
```

### 6.3 `\mathsf{MTree}`：线性增长

对单条关系，会保存一棵包含约 `2\ell - 1` 个节点的辅助 Merkle 树。

若每个节点存一个 `\lambda` 比特哈希值，则：

```text
S_MTree,rel = (2\ell - 1) · \lambda bits
```

若总关系更新数为 `N_rel`，则：

```text
S_MTree = N_rel · (2\ell - 1) · \lambda bits
```

## 7. VQNomos 的增量开销

因此，相比 Nomos，VQNomos 的服务端增量开销为：

```text
ΔS_S
= S_QTree
+ S_MPos
+ S_MTree
```

更具体地：

```text
ΔS_S
= (2M' - 1) · \lambda bits
+ N_rel · \ell · (|r| + |rt| + |sigma|)
+ N_rel · (2\ell - 1) · \lambda bits
```

其中：

- 第一项是固定全局开销
- 后两项随关系更新数线性增长

## 8. 结合第四章默认参数的数值化

若采用：

- `\ell = 20`
- `M = 2^22`
- `\lambda = 256 bits = 32 B`
- `|sigma| = 64 B`
- `|rt| = 32 B`
- `|r| = 4 B`

则：

### 8.1 Bloom Filter（XSet）本身

```text
S_XSet = 2^22 bits = 512 KiB
```

### 8.2 `MPos` 单条关系开销

```text
S_MPos,rel = 20 · (4 + 32 + 64) = 2000 B
```

### 8.3 `MTree` 单条关系开销

```text
S_MTree,rel = (2·20 - 1) · 32 = 39 · 32 = 1248 B
```

### 8.4 单条关系的 VQNomos 额外增长

```text
ΔS_S,rel = 2000 + 1248 = 3248 B ≈ 3.17 KiB
```

### 8.5 固定全局 `QTree`

```text
S_QTree ≈ 256 MiB
```

## 9. 可直接写入第四章的结论

可直接表述为：

> 在服务端存储分析中，`\mathsf{XSet}` 不应按“累计插入了多少个 XTag”来计量，而应按其底层 Bloom Filter 的位数组长度来计量。若 Bloom Filter 长度为 `M`，则 `\mathsf{XSet}` 的驻留空间恒为 `M` 比特，即 `\lceil M/8 \rceil` 字节，与插入元素数量无关；插入更多 XTag 只会提高位数组占用率与误判概率，不会扩大 Bloom Filter 本身的总空间。以第四章默认参数 `M=2^{22}` 为例，`\mathsf{XSet}` 实际占用空间为 `2^{22}` 比特，即 `524,288` 字节，约 `512 KiB`。在此基础上，VQNomos 不改变 `\mathsf{TSet}` 与 `\mathsf{XSet}` 的基础存储格式，其新增服务端开销仅来自固定大小的全局 `\mathsf{QTree}` 与随关系更新数线性增长的 `\mathsf{MPos}`、`\mathsf{MTree}`。在 `\ell=20`、`\lambda=256` 比特、Ed25519 签名长度 `64 B` 的设定下，VQNomos 每条关系额外增加约 `3248 B` 的服务端存储，并额外需要约 `256 MiB` 的全局 `\mathsf{QTree}` 空间。
