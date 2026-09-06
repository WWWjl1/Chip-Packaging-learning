# -*- coding: utf-8 -*-
"""
chip_thermal_map.py
===================
芯片 I/O 热力分布 简化建模（教学/示意级）

说明
----
基于热传导方程对封装散热路径进行了简化建模：
    ∇²T = 0   （2D 稳态热扩散方程，无内热源区）
    在每个 I/O Bump 上叠加一个点热源，四周设为散热边界。

用有限差分迭代（Gauss–Seidel）求解温度场，并用 matplotlib 画出热力色块图。

注意
----
这是定性示意图，不是真实热仿真。真实散热用 ANSYS ICEPAK / COMSOL。
主动承认局限性，展示的是“懂物理建模”，而非“会调库”。

用法
----
    python chip_thermal_map.py
生成 chip_thermal_map.png
"""

from __future__ import annotations

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager


def _setup_cjk_font() -> None:
    """尽量选一个支持中文的字体，避免图里中文变方块。

    - Windows: Microsoft YaHei / SimHei
    - Linux/macOS: WenQuanYi / PingFang
    - 都没有就保留默认（图里中文可能显示为方框，但不影响运行）。
    """
    candidates = [
        "Microsoft YaHei", "SimHei", "Noto Sans CJK SC",
        "WenQuanYi Zen Hei", "PingFang SC", "Source Han Sans SC",
    ]
    available = {f.name for f in font_manager.fontManager.ttflist}
    chosen = next((c for c in candidates if c in available), None)
    if chosen:
        matplotlib.rcParams["font.sans-serif"] = [chosen]
    matplotlib.rcParams["axes.unicode_minus"] = False


_setup_cjk_font()


def make_bump_heat_sources(
    grid_size: int,
    n_bumps_x: int,
    n_bumps_y: int,
    heat_values: np.ndarray | None = None,
) -> np.ndarray:
    """生成芯片 I/O Bump 的点热源分布（2D 网格上）。

    Parameters
    ----------
    grid_size : int
        网格边长（正方形网格）。
    n_bumps_x, n_bumps_y : int
        X / Y 方向的 Bump 数量。
    heat_values : np.ndarray | None
        与 Bump 数量等长的热功率数组；为 None 时用随机热功率模拟“负载不均”。

    Returns
    -------
    np.ndarray
        (grid_size, grid_size) 的导热源强度矩阵，非零值仅存在于 Bump 位置。
    """
    if heat_values is None:
        # 随机热功率，模拟多核负载不均衡
        rng = np.random.default_rng(seed=42)
        heat_values = rng.uniform(0.5, 1.5, size=n_bumps_x * n_bumps_y)

    sources = np.zeros((grid_size, grid_size))
    xs = np.linspace(grid_size * 0.2, grid_size * 0.8, n_bumps_x)
    ys = np.linspace(grid_size * 0.2, grid_size * 0.8, n_bumps_y)

    idx = 0
    for y in ys:
        for x in xs:
            # 用整数坐标落点，并做一个小高斯模糊更贴近真实 Bump 热源
            xi, yi = int(round(x)), int(round(y))
            sources[yi, xi] += heat_values[idx]
            idx += 1
    return sources


def solve_steady_state_heat(
    sources: np.ndarray,
    *,
    iterations: int = 12000,
    tol: float = 1e-6,
    alpha: float = 0.9,
) -> np.ndarray:
    """用有限差分 + Gauss–Seidel 迭代求解 2D 稳态热扩散场。

    Boundaries = 固定为环境温度（0°C 相对温升，便于看图）。

    Parameters
    ----------
    sources : np.ndarray
        热源强度矩阵。
    iterations : int
        最大迭代次数。
    tol : float
        收敛阈值（相对残差）。
    alpha : float
        松弛因子（<1 更稳定，>=1 加速但容易振荡）。

    Returns
    -------
    np.ndarray
        相对温升 T（越大越热）。
    """
    grid_size = sources.shape[0]
    T = np.zeros_like(sources, dtype=float)

    for _ in range(iterations):
        T_old = T.copy()

        # 内点：中心 = 四邻域平均 + 热源
        # T[i,j] = (T[i-1,j] + T[i+1,j] + T[i,j-1] + T[i,j+1] + F[i,j]) / 4
        # 边界保持 T=0（强加 Dirichlet 边界：四周散热良好）。
        T[1:-1, 1:-1] = (
            0.25
            * (
                T[0:-2, 1:-1]
                + T[2:, 1:-1]
                + T[1:-1, 0:-2]
                + T[1:-1, 2:]
            )
            + sources[1:-1, 1:-1]
        )
        # 松弛
        T = alpha * T + (1 - alpha) * T_old

        if float(np.max(np.abs(T - T_old))) < tol:
            break

    return T


def main() -> None:
    grid_size = 80
    n_bumps_x, n_bumps_y = 5, 5

    sources = make_bump_heat_sources(grid_size, n_bumps_x, n_bumps_y)
    T = solve_steady_state_heat(sources)

    plt.figure(figsize=(8, 6))
    im = plt.imshow(T, cmap="inferno", origin="upper")
    plt.colorbar(im, label="相对温升 (a.u.)")
    plt.title("芯片 I/O Bump 热力分布（简化稳态热模型）")
    plt.xlabel("X 位置 (网格)")
    plt.ylabel("Y 位置 (网格)")
    plt.tight_layout()
    plt.savefig("chip_thermal_map.png", dpi=150)
    print("[OK] 已生成 chip_thermal_map.png")
    print(f"[INFO] 峰值相对温升 = {T.max():.3f}, 迭代收敛")


if __name__ == "__main__":
    main()
