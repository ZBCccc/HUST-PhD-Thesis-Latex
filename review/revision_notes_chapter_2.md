# 第二章修订说明（bf.tex）

**修订日期**：2026-03-14
**修订依据**：review_chapter_2.md（17 个问题：5 Critical, 7 Major, 5 Minor）

---

## 已修复问题

### Critical

| 编号 | 修复内容 | 修改位置 |
|------|----------|----------|
| C1 | 补充 `AddrSet` 形式化定义：明确输入为资格标签与采样索引序列 $(\beta_1,\ldots,\beta_k)$，输出为 $k$ 个 RBF 地址的有序序列，说明确定性、安全性依赖（采样随机性 + 标签伪随机性） | 式 `\eqref{eq:addrset-def}` 后新增定义段落与式 `\eqref{eq:addrset-expand}` |
| C2 | 算法 4 客户端解密循环变量 $\ell$ 替换为 $c$，消除与 RBF 参数的符号冲突 | 算法 4 第 363–365 行 |
| C3 | 定义 4（条件完整性）补充形式化安全实验 $\mathsf{Exp}^{\mathsf{CC}}$，明确挑战者行为、对手查询能力、胜利条件与优势函数 | 定义 `\ref{def:vq-conditional-completeness}` |
| C4 | 式 (4.2) 后补充说明：明确 $F(K_X,\cdot)$ 为抽象语法层占位符，说明与 Nomos 实际代数构造的关系，声明安全分析仅依赖地址不可预测性与令牌绑定性 | 式 `\eqref{eq:xtag-abstract}` 后新增说明段落 |
| C5 | 算法 8 中"检查地址归属"步骤标注为外部前提条件（由第三章 Merkle-open 机制保证），算法说明段落补充能力边界描述 | 算法 8 第 569 行 + 算法说明段落 |

### Major

| 编号 | 修复内容 | 修改位置 |
|------|----------|----------|
| M1 | 隐私性讨论补充模拟器 $\mathsf{Sim}^{\mathsf{VQ}}$ 构造草图（三步：调用 Nomos 模拟器、独立采样 $\nu'$、$\Pi_Q$ 无需模拟），标注为 proof sketch | §4.3.1 隐私性讨论 |
| M2 | 命题 1（正确性）证明按三层校验结构展开：版本校验（签名有效 + 版本不回退）、结构校验（路径有效性）、语义校验（判定位重算 + 合取语义等价） | 命题 `\ref{prop:vq-correct}` 证明 |
| M3 | 算法 5 标题改为"承诺层初始化算法（全量构建）"，说明段落区分初始化全量构建 $O(M)$ 与动态增量更新 $O(\ell\log M)$ | 算法 5 标题 + 说明段落 |
| M4 | 算法 7 中补充 $\Pi_Q$ 聚合定义与 $\eta$ 证明索引定义 | 算法 7 末尾新增两行 |
| M5 | 为判定位方程与见证结构方程添加 `\label{}`（`eq:vq-judgment-bit`、`eq:vq-witness`、`eq:vq-judgment-bit-sec`），将证明中硬编码的"式~(4.6)"和"式~(4.7)"替换为 `\eqref{}` | 证明文本中 3 处引用 |
| M6 | 式 (4.1) 中 $\varphi(H(w))$ 统一为 $H(w)$，消除未定义符号 | §4.1.2 式 (4.1) |
| M7 | 命题 4（条件完整性）证明重写：明确声明条件完整性可归约为绑定健全性，给出从 $\mathsf{Exp}^{\mathsf{CC}}$ 到 $\mathsf{Exp}^{\mathsf{VQ\text{-}Sound}}$ 的形式化归约步骤，优势界通过归约链传递 | 命题 `\ref{prop:vq-complete}` 及其证明 |

### Minor

| 编号 | 修复内容 | 修改位置 |
|------|----------|----------|
| m1 | $F_p$ 描述从"特定版本的映射函数"统一为"模$p$伪随机函数"，补充 PRF 安全性要求 | §4.1.1 第 14 行 |
| m2 | RBF 假阳性分析处标注【待补充引用】（需 Broder & Mitzenmacher 2004 或 Mitzenmacher & Upfal 教材） | §4.1.2 假阳性推导处 |
| m3 | 定义 1（正确性）从"必然接受"改为概率界 $\Pr[\mathsf{Accept}=1 \wedge \mathsf{Out}=\mathsf{Res}(Q)]\ge 1-\mathsf{negl}(\lambda)$ | 定义 `\ref{def:vq-correctness}` |
| m4 | 算法 4 中 `flag` 初始化从 $j$ 循环外移至 $i$ 循环内，使每个非主关键词独立判定 | 算法 4 第 344–345 行 |
| m5 | 删除两处元叙述措辞："相应的交互步骤与运算逻辑直接构建系统的功能实现，并界定后续引入可验证性扩展的底层基础框架"、"以下给出承诺层的具体结构" | §4.2.1 末段、§4.2.2 首段 |

---

## 残留问题

1. **m2（RBF 假阳性引用）**：已标注【待补充引用】，需作者补充 Bloom Filter 假阳性分析的标准文献引用（建议 Broder & Mitzenmacher 2004 "Network Applications of Bloom Filters: A Survey" 或 Mitzenmacher & Upfal "Probability and Computing" 教材），并在 `ref/thesis.bib` 中添加对应条目。

2. **M1（隐私性完整证明）**：当前为 proof sketch，完整的模拟器构造与不可区分性证明需要额外条件（Nomos 模拟器的存在性假设、$\nu$ 与协议其他随机量的独立性形式化论证）。如需提升为完整命题，需补充这些条件。

3. **C4（抽象层与实例化映射）**：已补充说明声明抽象层与实例化的关系，但从 $F(K_X,\cdot)$ 到具体 xtag 代数构造的完整实例化映射仍指向第三章。如审稿人要求本章自包含，可能需要在本章补充映射细节。

---

## 编译验证

修订后文件已通过 `latexmk -xelatex` 编译，无新增错误。仅有的 warning 为其他章节的预存问题（`\cite{nomos}` 未定义、`\ref{chap:eval}` 未定义），与本次修订无关。
