# Chip-Packaging-Learning

> 先进封装（Advanced Packaging）方向的学习笔记与仿真实验。

## 内容

- **学习笔记**：TSV（硅通孔）、RDL（重布线层）、混合键合（Hybrid Bonding）三个核心概念，以及 2.5D / 3D 封装的区别与术语图解。
- **仿真实验**：用 Python + matplotlib 对芯片 I/O 热力分布做简化建模，生成热力色块图。
- **硬件项目**：基于 STM32 的芯片热管理模拟验证平台。

## 📁 目录结构

```
Chip-Packaging-Learning/
├── README.md                            # 项目说明（本文件）
├── LICENSE                              # MIT 许可证
├── notes/                               # 学习笔记
│   ├── 01_TSV_硅通孔.md
│   ├── 02_RDL_重布线层.md
│   ├── 03_混合键合与2.5D_3D区别.md
│   └── 术语图解_先进封装核心术语.md
├── simulation/                          # 仿真实验
│   ├── README.md
│   ├── requirements.txt
│   └── chip_thermal_map.py              # 芯片 I/O 热力色块图（matplotlib）
└── projects/                            # 硬件项目
    └── stm32_thermal_monitor/
        └── README.md
```

## 📚 学习笔记

见 [`notes/`](notes/)。主要内容：

- **TSV 硅通孔**：在硅片上垂直打孔填铜，缩短互连路径、提高集成度。
- **RDL 重布线层**：把芯片上细密的 I/O 焊盘重新分布到更稀疏的大焊盘。
- **混合键合 / 2.5D·3D**：铜对铜的高密互连，以及“平铺”与“垂直堆叠”两种封装形态的对比。

每篇笔记都配有结构简图、术语辨析和关键要点，适合对照阅读。

## 🔬 仿真实验

见 [`simulation/`](simulation/)。用 2D 稳态热扩散方程 + 有限差分，把每个 I/O Bump 当作热源、芯片四周当作散热边界，迭代求解温度场并画出热力分布。

> 基于热传导方程对封装散热路径进行了简化建模。

## 🧩 硬件项目

见 [`projects/`](projects/)。一个基于 STM32 的芯片热管理模拟验证平台，模拟多核芯片负载下的温度梯度变化。

## 🛠 环境

- Python 3.x
- `pip install -r simulation/requirements.txt`

## 📄 许可证

[LICENSE](LICENSE) · MIT
