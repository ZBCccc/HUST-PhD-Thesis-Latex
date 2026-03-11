#!/usr/bin/env python3
"""
生成第四章实验评估的全部 9 张图表，输出为 PDF 至 figures/ 目录。
用法：python3 scripts/plot_experiments.py
依赖：pip3 install numpy matplotlib
"""

import os
import numpy as np
import matplotlib
matplotlib.use("pdf")

import matplotlib.pyplot as plt
from matplotlib import rcParams

# ── 全局样式 ──────────────────────────────────────────────
rcParams.update({
    "font.family": "serif",
    "font.serif": ["Songti SC", "SimSun", "STSong", "serif"],
    "mathtext.fontset": "cm",
    "font.size": 10,
    "axes.labelsize": 10,
    "legend.fontsize": 8,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "lines.linewidth": 1.5,
    "lines.markersize": 5,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "pdf.fonttype": 42,       # TrueType 嵌入，保证可编辑
    "ps.fonttype": 42,
    "axes.unicode_minus": False,  # 用 ASCII hyphen 替代 Unicode minus
})

OUTDIR = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(OUTDIR, exist_ok=True)

FIG_W = 5.5   # 英寸，约 0.85\textwidth
FIG_H = 3.2


def savefig(fig, name):
    path = os.path.join(OUTDIR, f"{name}.pdf")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"  -> {path}")


# ══════════════════════════════════════════════════════════
# 图 1: update-time  (log-log, N vs 单次更新耗时)
# ══════════════════════════════════════════════════════════
def plot_update_time():
    N = [1e3, 1e4, 1e5, 1e6]
    # 【待补充：Nomos 方案更新耗时数据】
    baseline = [1, 1, 1, 1]
    # 【待补充：本文方案更新耗时数据】
    ours     = [1, 1, 1, 1]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.loglog(N, baseline, "o-", label="Nomos 方案")
    ax.loglog(N, ours,     "s-", label="本文方案")
    ax.set_xlabel(r"文件-关键词对总数 $N$")
    ax.set_ylabel("单次更新耗时 (ms)")
    ax.legend(loc="upper left")
    savefig(fig, "update-time")


# ══════════════════════════════════════════════════════════
# 图 2: update-breakdown  (堆叠柱状图, ℓ vs 更新开销分解)
# ══════════════════════════════════════════════════════════
def plot_update_breakdown():
    ell_vals = [10, 20, 50]
    x = np.arange(len(ell_vals))
    width = 0.5
    # 【待补充：各部分耗时】
    base   = [1, 1, 1]
    qtree  = [1, 1, 1]
    commit = [1, 1, 1]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.bar(x, base,   width, label="Nomos 原始更新")
    ax.bar(x, qtree,  width, bottom=base,
           label=r"$\mathsf{QTree}$ 路径更新")
    ax.bar(x, commit, width,
           bottom=[b + q for b, q in zip(base, qtree)],
           label="承诺计算")
    ax.set_xticks(x)
    ax.set_xticklabels([str(v) for v in ell_vals])
    ax.set_xlabel(r"$\ell$")
    ax.set_ylabel("单次更新耗时 (ms)")
    ax.legend(loc="upper left")
    savefig(fig, "update-breakdown")


# ══════════════════════════════════════════════════════════
# 图 3: search-time  (semi-log, |Cand| vs 搜索耗时)
# ══════════════════════════════════════════════════════════
def plot_search_time():
    cand = [100, 500, 1000, 5000, 10000]
    # 【待补充：检索耗时数据】
    baseline = [1, 1, 1, 1, 1]
    ours     = [1, 1, 1, 1, 1]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.semilogx(cand, baseline, "o-", label="Nomos 方案")
    ax.semilogx(cand, ours,     "s-", label="本文方案")
    ax.set_xlabel(r"候选集规模 $|\mathsf{Cand}(w_s)|$")
    ax.set_ylabel("检索耗时 (ms)")
    ax.legend(loc="upper left")
    savefig(fig, "search-time")


# ══════════════════════════════════════════════════════════
# 图 4: verify-time  (semi-log, |Cand| vs 验证耗时)
# ══════════════════════════════════════════════════════════
def plot_verify_time():
    cand = [100, 500, 1000, 5000, 10000]
    # 【待补充：验证耗时数据】
    qtree_v  = [1, 1, 1, 1, 1]
    commit_v = [1, 1, 1, 1, 1]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.semilogx(cand, qtree_v,  "o-",
                label=r"$\mathsf{QTree}$ 路径验证")
    ax.semilogx(cand, commit_v, "s-", label="承诺开封验证")
    ax.set_xlabel(r"候选集规模 $|\mathsf{Cand}(w_s)|$")
    ax.set_ylabel("验证耗时 (ms)")
    ax.legend(loc="upper left")
    savefig(fig, "verify-time")


# ══════════════════════════════════════════════════════════
# 图 5: comm-overhead  (分组柱状图, n vs 通信量)
# ══════════════════════════════════════════════════════════
def plot_comm_overhead():
    n_vals = [2, 3, 5]
    x = np.arange(len(n_vals))
    width = 0.3
    # 【待补充：通信量数据】
    baseline = [1, 1, 1]
    ours     = [1, 1, 1]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.bar(x - width / 2, baseline, width, label="Nomos 方案")
    ax.bar(x + width / 2, ours,     width, label="本文方案")
    ax.set_xticks(x)
    ax.set_xticklabels([str(v) for v in n_vals])
    ax.set_xlabel(r"合取关键词数 $n$")
    ax.set_ylabel("通信量 (KB)")
    ax.legend(loc="upper left")
    savefig(fig, "comm-overhead")


# ══════════════════════════════════════════════════════════
# 图 6: storage-overhead  (semi-log, N vs 存储开销)
# ══════════════════════════════════════════════════════════
def plot_storage_overhead():
    N = [1e3, 1e4, 1e5, 1e6]
    # 【待补充：存储开销数据】
    baseline = [1, 1, 1, 1]
    ours     = [1, 1, 1, 1]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.semilogx(N, baseline, "o-", label="Nomos 方案")
    ax.semilogx(N, ours,     "s-", label="本文方案")
    ax.set_xlabel(r"文件-关键词对总数 $N$")
    ax.set_ylabel("存储开销 (MB)")
    ax.legend(loc="upper left")
    savefig(fig, "storage-overhead")


# ══════════════════════════════════════════════════════════
# 图 7: param-ell  (双 Y 轴, ℓ vs 更新耗时 & 开封通信量)
# ══════════════════════════════════════════════════════════
def plot_param_ell():
    ell = [5, 10, 20, 30, 50]
    # 【待补充：更新耗时随 ℓ 变化】
    update_time = [1, 1, 1, 1, 1]
    # 【待补充：开封通信量随 ℓ 变化】
    comm        = [1, 1, 1, 1, 1]

    fig, ax1 = plt.subplots(figsize=(FIG_W, FIG_H))
    color1 = "C0"
    ln1 = ax1.plot(ell, update_time, "o-", color=color1, label="更新耗时")
    ax1.set_xlabel(r"插入侧展开次数 $\ell$")
    ax1.set_ylabel("单次更新耗时 (ms)", color=color1)
    ax1.tick_params(axis="y", labelcolor=color1)

    ax2 = ax1.twinx()
    color2 = "C1"
    ln2 = ax2.plot(ell, comm, "^--", color=color2, label="开封通信量")
    ax2.set_ylabel("开封通信量 (KB)", color=color2)
    ax2.tick_params(axis="y", labelcolor=color2)

    lns = ln1 + ln2
    ax1.legend(lns, [l.get_label() for l in lns], loc="upper left")
    savefig(fig, "param-ell")


# ══════════════════════════════════════════════════════════
# 图 8: param-k  (线图, k vs 证明生成 & 验证耗时)
# ══════════════════════════════════════════════════════════
def plot_param_k():
    k = [3, 5, 10, 15, 20]
    # 【待补充：证明生成耗时随 k 变化】
    prove  = [1, 1, 1, 1, 1]
    # 【待补充：客户端验证耗时随 k 变化】
    verify = [1, 1, 1, 1, 1]

    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
    ax.plot(k, prove,  "o-", label="证明生成")
    ax.plot(k, verify, "s-", label="客户端验证")
    ax.set_xlabel(r"查询侧采样次数 $k$")
    ax.set_ylabel("耗时 (ms)")
    ax.legend(loc="upper left")
    savefig(fig, "param-k")


# ══════════════════════════════════════════════════════════
# 图 9: param-M  (双 Y 轴, log2(M) vs 初始化耗时 & 路径长度)
# ══════════════════════════════════════════════════════════
def plot_param_M():
    log2M = [16, 18, 20, 22, 24]
    # 【待补充：QTree 初始化耗时随 M 变化】
    init_time   = [1, 1, 1, 1, 1]
    # 【待补充：路径长度随 M 变化】
    path_length = [16, 18, 20, 22, 24]

    fig, ax1 = plt.subplots(figsize=(FIG_W, FIG_H))
    color1 = "C0"
    ln1 = ax1.plot(log2M, init_time, "o-", color=color1, label="初始化耗时")
    ax1.set_xlabel(r"$\log_2 M$")
    ax1.set_ylabel(r"$\mathsf{QTree}$ 初始化耗时 (ms)", color=color1)
    ax1.tick_params(axis="y", labelcolor=color1)

    ax2 = ax1.twinx()
    color2 = "C1"
    ln2 = ax2.plot(log2M, path_length, "^--", color=color2, label="路径长度")
    ax2.set_ylabel("认证路径长度（哈希值个数）", color=color2)
    ax2.tick_params(axis="y", labelcolor=color2)

    lns = ln1 + ln2
    ax1.legend(lns, [l.get_label() for l in lns], loc="upper left")
    savefig(fig, "param-M")


# ── 主入口 ────────────────────────────────────────────────
if __name__ == "__main__":
    print("生成实验图表 ...")
    plot_update_time()
    plot_update_breakdown()
    plot_search_time()
    plot_verify_time()
    plot_comm_overhead()
    plot_storage_overhead()
    plot_param_ell()
    plot_param_k()
    plot_param_M()
    print("全部完成。")
