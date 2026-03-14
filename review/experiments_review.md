请作为密码学方向（尤其是 searchable encryption）的专业审稿人，专门审查实验章节的严谨性。

你的重点不是语言润色，而是检查实验设计、指标定义、baseline 比较和结论解释是否成立。

请重点检查：
1. 每个 metric 是否定义清楚（测什么、单位、是否含 setup/preprocessing/communication）
2. workload / query setting / dataset scale / hardware setting 是否交代充分
3. baseline 是否可比，是否存在 leakage、trust model、functionality 不一致却直接比较的问题
4. 图表后的文字是否只是复述现象，还是解释了趋势原因和 tradeoff
5. 是否把实验结果夸大成了安全性证明
6. 是否存在不严谨词汇，如用“可忽略”描述经验开销
7. 是否有缺失信息需要标记 `【待补充】`

请按：
- 总体评价
- Critical / Major / Minor
- 优先修改的 3 个问题
的格式输出。