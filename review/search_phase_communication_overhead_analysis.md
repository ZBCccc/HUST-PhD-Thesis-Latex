# 搜索阶段通信开销分析（Nomos vs. VQNomos）

## 1. 计量口径

本分析仅统计**搜索阶段**的客户端与服务器之间通信，不包含客户端与授权管理方在令牌生成阶段的交互。

同时采用如下严格区分：

1. **客户端通信开销**：仅统计 `client -> server` 的上传开销
2. **服务器通信开销**：仅统计 `server -> client` 的下载开销

即：

```text
Client communication overhead = upload only
Server communication overhead = download only
```

为便于表述，记：

- `m = |\mathsf{Cand}(w_s)| = \mathsf{UpdateCnt}[w_s]`
- `n = |Q|`
- `k` 为查询侧采样参数
- `N_+` 为单次查询中 Positive 关系数量
- `N_-` 为单次查询中 Negative 关系数量

## 2. Nomos 的搜索阶段通信开销

### 2.1 客户端通信开销（上传）

根据搜索算法，客户端在搜索阶段向服务器发送：

- `m` 个主项搜索标签 `\mathsf{bstag}_j`
- `m(n-1)k` 个交叉令牌 `\mathsf{xtoken}_{i,j}^{(t)}`
- 一份认证封装 `\mathsf{env}`

因此，Nomos 的客户端通信开销为：

```text
C_client^Nomos
= m·|bstag|
+ m(n-1)k·|xtoken|
+ |env|
```

若 `\mathsf{bstag}` 与 `\mathsf{xtoken}` 都按群元素计，则可写为：

```text
C_client^Nomos
≈ m·(1 + (n-1)k)·|G| + |env|
```

因此其主导项为：

```text
C_client^Nomos = O(m(n-1)k·|G|)
```

### 2.2 服务器通信开销（下载）

服务器在搜索阶段向客户端返回 `\mathsf{sEOpList}`，其中共有 `m` 条记录，每条记录包含：

- 索引 `j`
- 加密值 `\mathsf{sval}_j`
- 计数 `\mathsf{cnt}_j`

因此，Nomos 的服务器通信开销为：

```text
C_server^Nomos
= m·(|j| + |sval| + |cnt|)
```

若这些字段长度固定，则：

```text
C_server^Nomos = O(m)
```

这与客户端上传开销的量级不同，不能再将其与上传部分混写为同一个“总通信式”。

## 3. VQNomos 的搜索阶段通信开销

### 3.1 客户端通信开销（上传）

VQNomos 的增强令牌为：

```text
\tau_VQ = (\tau_Nomos, t, \nu)
```

相较于 Nomos，搜索阶段上传只增加：

- 版本号 `t`
- 采样索引序列 `\nu = (\beta_1,\ldots,\beta_k)`

因此：

```text
C_client^VQNomos
= C_client^Nomos + |t| + k·ceil(log2 \ell)
```

故其渐近主导项仍为：

```text
C_client^VQNomos = O(m(n-1)k·|G|)
```

也就是说，在搜索阶段，VQNomos 对客户端上传开销的影响仅为一个很小的加性项。

### 3.2 服务器通信开销（下载）

VQNomos 的下载由四部分构成：

#### (1) Nomos 基础响应

仍然包含基础的 `\mathsf{sEOpList}`：

```text
m·(|j| + |sval| + |cnt|)
```

#### (2) 版本锚点

额外返回一个锚点：

```text
|Anchor_t| = |t| + |R_X^{(t)}| + |\sigma_t|
```

#### (3) QTree 证明下载

对于每个关系 `(j,\mathsf{id})`，若为 Positive 证据则返回 `k` 条路径，若为 Negative 证据则返回 `1` 条路径。

因此额外下载为：

```text
C_server,QTree^add
= O((N_+·k + N_-)·\lambda·log M)
```

#### (4) Merkle-open 下载

对于每个关系 `(j,\mathsf{id})`，服务器返回：

- 一个根认证对象 `\mathsf{Auth}_{j,\mathsf{id}} = (\mathsf{rt}, \sigma)`
- `k` 个开封三元组
  `(\beta_t, \mathsf{xtag}^{(\beta_t)}, \pi^{(\beta_t)})`

论文中已给出单个关系的附加开封通信量：

```text
O(k·(|G| + \lambda·log \ell))
```

而关系域大小为：

```text
|\mathcal R(Q)| = m(n-1)
```

因此 Merkle-open 的总下载开销为：

```text
C_server,MO^add
= O(m(n-1)k·(|G| + \lambda·log \ell))
```

### 3.3 VQNomos 的服务器通信开销总式

综上：

```text
C_server^VQNomos
= m·(|j| + |sval| + |cnt|)
+ |Anchor_t|
+ O((N_+·k + N_-)·\lambda·log M)
+ O(m(n-1)k·(|G| + \lambda·log \ell))
```

在最坏情形 `N_+ = m(n-1), N_- = 0` 下，可写为：

```text
C_server^VQNomos
= m·(|j| + |sval| + |cnt|)
+ |Anchor_t|
+ O(m(n-1)k·(\lambda·log M + |G| + \lambda·log \ell))
```

## 4. Nomos 与 VQNomos 的对比结论

### 4.1 客户端通信开销

```text
C_client^Nomos
= m·|bstag| + m(n-1)k·|xtoken| + |env|
```

```text
C_client^VQNomos
= C_client^Nomos + |t| + k·ceil(log2 \ell)
```

因此：

- Nomos 与 VQNomos 的客户端通信开销主导项相同；
- VQNomos 仅比 Nomos 多一个常数级版本号与 `k` 个采样索引的上传。

### 4.2 服务器通信开销

```text
C_server^Nomos
= m·(|j| + |sval| + |cnt|)
```

```text
C_server^VQNomos
= C_server^Nomos
+ |Anchor_t|
+ O((N_+·k + N_-)·\lambda·log M)
+ O(m(n-1)k·(|G| + \lambda·log \ell))
```

因此：

- Nomos 的服务器通信开销仅线性依赖于 `m`
- VQNomos 的服务器通信开销显著增加，主要来自：
  - `QTree` 认证路径下载
  - Merkle-open 选择性开封材料下载

## 5. 可直接写入第四章的结论

可直接表述为：

> 在搜索阶段，本文将通信开销区分为客户端通信开销与服务器通信开销两类，其中前者仅统计客户端向服务器上传的检索材料，后者仅统计服务器向客户端返回的响应与证明材料。对 Nomos 而言，客户端上传 `m` 个主项标签与 `m(n-1)k` 个交叉令牌，因此客户端通信开销的主导项为 `O(m(n-1)k·|\mathbb G|)`；服务器仅返回 `m` 条 `\mathsf{sEOpList}` 记录，因此服务器通信开销为 `O(m)`。对 VQNomos 而言，客户端上传仅在 Nomos 基础上额外携带版本号 `t` 与采样索引序列 `\nu`，因此其客户端通信开销与 Nomos 保持同阶；服务器则需额外返回版本锚点、`\mathsf{QTree}` 认证路径以及 Merkle-open 选择性开封材料，因此服务器通信开销增加为 `C_server^Nomos + O((N_+k+N_-)\lambda\log M) + O(m(n-1)k(|\mathbb G|+\lambda\log\ell))`。由此可见，VQNomos 在搜索阶段的通信增量主要体现在服务器下载方向，而非客户端上传方向。
