# 客户端存储开销分析（Nomos vs. VQNomos）

## 1. 计量口径

本分析仅统计客户端持有的持久化元数据，不计入任何密钥材料。

按该口径：

- `Nomos` 客户端仅维护关键词到 `updateCnt` 的映射。
- `VQNomos` 客户端在此基础上，额外维护最新版本锚点
  `\mathsf{Anchor}_t = (t, R_X^{(t)}, \sigma_t)`。

不计入客户端存储的对象：

- `\mathsf{QTree}`
- `\mathsf{MPos}`
- `\mathsf{MTree}`
- 查询阶段临时生成的令牌、采样索引 `\nu=(\beta_1,\ldots,\beta_k)` 与证明转录

## 2. 公式

记：

- `|\mathcal W|` 为不同关键词个数
- `L_{\mathcal W} = \sum_{w \in \mathcal W} |w|` 为客户端存储全部关键词字符串所需的总字节数
- `b_{\text{cnt}}` 为单个 `updateCnt` 的存储字节数
- `b_{\text{anchor}}` 为单个锚点 `\mathsf{Anchor}_t` 的存储字节数

则：

### Nomos

```text
S_client^Nomos = L_W + |\mathcal W| · b_cnt
```

### VQNomos

```text
S_client^VQNomos = L_W + |\mathcal W| · b_cnt + b_anchor
```

因此，VQNomos 相比 Nomos 的客户端额外存储开销为：

```text
ΔS_client = b_anchor
```

也就是说，在不计密钥材料的前提下，VQNomos 仅比 Nomos 多一个常数大小的最新锚点。

## 3. 锚点大小

结合第四章实验原语实例化：

- `R_X^{(t)}` 由 SHA-256 输出，取 `32 B`
- `\sigma_t` 由 Ed25519 输出，取 `64 B`
- 版本号 `t` 若按 `uint64_t` 存储，取 `8 B`

则：

```text
b_anchor = 32 + 64 + 8 = 104 B
```

若版本号 `t` 按 `uint32_t` 存储，则锚点大小为：

```text
b_anchor = 32 + 64 + 4 = 100 B
```

后文默认采用更稳妥的 `uint64_t` 口径，即：

```text
b_anchor = 104 B
```

## 4. 两种数值化方式

### 4.1 工程实现口径：每个计数器按 4 B 存储

此时：

```text
b_cnt = 4 B
```

于是：

```text
S_client^Nomos = L_W + 4|\mathcal W| \text{ B}
S_client^VQNomos = L_W + 4|\mathcal W| + 104 \text{ B}
```

根据第四章数据集统计：

| 数据集 | 不同关键词数 `|\mathcal W|` | Nomos 计数器部分 | VQNomos 计数器+锚点部分 | VQNomos 额外开销 |
| --- | ---: | ---: | ---: | ---: |
| Crime | 63,659 | 254,636 B | 254,740 B | 104 B |
| Enron | 16,241 | 64,964 B | 65,068 B | 104 B |
| Wiki | 10,000 | 40,000 B | 40,104 B | 104 B |

若换算为 KiB：

| 数据集 | Nomos 计数器部分 | VQNomos 计数器+锚点部分 |
| --- | ---: | ---: |
| Crime | 248.67 KiB | 248.77 KiB |
| Enron | 63.44 KiB | 63.54 KiB |
| Wiki | 39.06 KiB | 39.16 KiB |

### 4.2 逻辑最小口径：按最大关键词频次推导计数器位宽

若只按当前数据集统计量给出理论最小位宽，可令：

```text
b_cnt^* = ceil(log2(f_max + 1)) \text{ bits}
```

其中 `f_max` 为数据集中最大关键词频次。

根据第四章表格：

- Crime: `f_max = 16644`，故 `b_cnt^* = 15 bits`
- Enron: `f_max = 26946`，故 `b_cnt^* = 15 bits`
- Wiki: `f_max = 9738`，故 `b_cnt^* = 14 bits`

于是仅统计计数器部分时：

| 数据集 | `|\mathcal W|` | 单计数器位宽 | Nomos 计数器部分 | VQNomos 计数器+锚点部分 |
| --- | ---: | ---: | ---: | ---: |
| Crime | 63,659 | 15 bits | 954,885 bits = 119,360.625 B | 119,464.625 B |
| Enron | 16,241 | 15 bits | 243,615 bits = 30,451.875 B | 30,555.875 B |
| Wiki | 10,000 | 14 bits | 140,000 bits = 17,500 B | 17,604 B |

该口径更接近理论下界，但实际实现通常仍会采用 2 B、4 B 或 8 B 的对齐整数类型，因此正文中更建议使用“4 B 计数器 + 104 B 锚点”的工程口径。

## 5. 关于关键词字符串部分

如果希望给出“客户端总存储开销”的完整数值，还需要统计：

```text
L_W = \sum_{w \in \mathcal W} |w|
```

即预处理后客户端实际保存的全部关键词字符串总字节数。

当前论文正文只给出了不同关键词个数 `|\mathcal W|`，未给出总关键词字节数，因此：

```text
L_W = 【待补充：由预处理后的词表实际统计】
```

因此，正文中可以采用如下写法：

```text
Nomos 客户端存储开销为 L_W + |\mathcal W|·b_cnt；
VQNomos 客户端存储开销为 L_W + |\mathcal W|·b_cnt + 104 B。
因此，相比 Nomos，VQNomos 仅引入一个常数大小的最新版本锚点开销。
```

## 6. 可直接写入第四章的结论

可直接表述为：

> 在不计密钥材料、仅统计客户端持久化元数据的口径下，Nomos 客户端仅需维护关键词到更新计数 `updateCnt` 的映射，其存储开销为 `L_W + |\mathcal W|·b_cnt`。VQNomos 在此基础上仅额外维护最新版本锚点 `\mathsf{Anchor}_t=(t,R_X^{(t)},\sigma_t)`。若结合本文实验实现中 SHA-256 与 Ed25519 的实例化，并将版本号按 64 位整数存储，则该锚点大小为 `104 B`。因此，VQNomos 的客户端存储开销为 `L_W + |\mathcal W|·b_cnt + 104 B`，相较 Nomos 仅增加常数级额外开销。
