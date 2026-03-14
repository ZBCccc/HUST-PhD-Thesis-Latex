# 第一章（绪论）修订说明

**修订日期**：2026-03-14
**修订依据**：`review/review_chapter_1.md`（18 个问题：3 Critical, 7 Major, 8 Minor）

---

## 已修复问题清单

### Critical

**C1 + C2：表 `tab:vsse-compare` 符号未定义 + 比较维度不对等**
- 修改内容：
  - 表注中补充了 $M$（QTree 叶子数）、$\ell$（XTag 维度）、$k$（采样位置数）、$n$（合取关键词数）、$|\mathsf{Cand}|$（候选集规模）的定义
  - 增加"验证对象"列，区分已有方案的"结果集"验证与本方案的"资格检验+地址绑定"验证
  - Cheng 15 的"不可部署"改为 $O(N \cdot \mathsf{poly}(\lambda))$（修复 m6）
  - 表后段落明确说明渐近表达式不可直接比较量级，并给出典型参数关系（$k \ll \ell$，$|\mathsf{Cand}| \leq |\mathsf{Res}|$）

**C3：可验证性安全目标未精确区分**
- 修改内容：在 §1.1 第三段引入可验证性问题时，明确区分三类独立安全目标：正确性（correctness）、完整性（completeness）、健全性（soundness），并给出每个属性的直觉含义

### Major

**M1：semi-honest 模型引用错误**
- 修改内容：将 `\cite{rivest1978data}` 替换为 `\cite{goldreich2004foundations}`
- 残留：需确认 `goldreich2004foundations` 在 `thesis.bib` 中存在且指向 Goldreich 的 *Foundations of Cryptography* 教材

**M2：合规/政策语言过重**
- 修改内容：将法规引用从独立分句缩减为背景提及（"各国数据保护法规亦对云环境下的数据机密性与完整性保护提出了明确要求"），删除"从合规层面"等政策报告风格表述

**M3："Wuhan University 研究团队"表述不规范**
- 修改内容：改为"Zhao 等人\cite{zhao2025efficient}提出的 FB-VDSSE 方案"

**M4：缺少明确的"创新点"小节**
- 状态：agent 在处理 C3 时已在 §1.1 中增加了安全目标区分，但未在 §1.3 中增加独立的编号贡献列表
- 残留：建议在 §1.3 中补充 2-3 条可检验的贡献声明

**M5：文献综述缺少泄露维度讨论**
- 修改内容：在 §1.2.3 末尾新增一段泄露配置（leakage profile）角度的系统性讨论，涵盖 search pattern、access pattern、update pattern 等维度，并说明本文方案的泄露定位

**M6："消除假阳性"声明过强**
- 状态：未在 diff 中发现对应修改
- 残留：§1.3 中"消除假阳性导致的错误拒绝风险"表述仍需弱化

**M7：技术路线图过于简略**
- 状态：未在 diff 中发现对应修改
- 残留：图 `fig:intro-tech-roadmap` 仍为简略形式，建议后续扩展或在图后补充文字说明

### Minor

**m1：Sophos 方案名称 LaTeX 渲染**
- 修改内容：改为 `\textit{Sophos}（$\Sigma o\phi o\varsigma$）`，先给出可读名称再注明希腊字母拼写

**m2：APT 术语引入后未再使用**
- 修改内容：删除"高级持续性威胁（Advanced Persistent Threat, APT）"缩写，改为"外部持续性攻击"

**m3：Baek 等人工作定位模糊**
- 修改内容：补充具体贡献描述（"针对公钥可搜索加密场景提出了更强的安全模型并讨论了结果一致性验证问题"）

**m4：Nomos 方案描述中使用方案特定术语**
- 修改内容：将"令牌化多客户端供给机制（Tokenised Multi-client Provisioning）""Gatekeeper 角色""将授权与查询解耦"改为通用描述（"引入可信授权管理方与 OPRF 协议，在保护查询隐私的同时实现了多用户动态 SSE 的高效构建"）

**m5：§1.4 中"创新点"与正文不一致**
- 状态：未在 diff 中发现对应修改
- 残留：需与 M4 一并处理

**m6：Cheng 15 "不可部署"表述**
- 修改内容：已在 C1+C2 修复中一并处理，改为 $O(N \cdot \mathsf{poly}(\lambda))$

**m7："数据规模"表述不精确**
- 修改内容：改为"其通信与计算开销随密文总量线性增长"

**m8：µSE 的 Unicode 符号**
- 修改内容：改为 `$\mu$SE`

---

## 残留问题

| 编号 | 问题 | 状态 | 说明 |
|------|------|------|------|
| M1 | `goldreich2004foundations` bib 条目 | 需确认 | 需检查 thesis.bib 中是否存在该引用键 |
| M4 | §1.3 缺少编号贡献列表 | 未修复 | 建议补充 2-3 条可检验的贡献声明 |
| M6 | "消除假阳性"声明过强 | 未修复 | 需弱化为条件性表述 |
| M7 | 技术路线图过于简略 | 未修复 | 建议扩展或补充文字说明 |
| m5 | §1.4 "创新点"与正文不一致 | 未修复 | 需与 M4 一并处理 |
