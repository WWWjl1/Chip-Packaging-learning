# Chip-Packaging-Learning

> 先进封装知识打底 + 轻量仿真实战 + 简历留痕 —— 考研备考期的“知识奠基”仓库。

**状态栏一句话**：不求精通，只求留痕。✅

本仓库是个人学习沉淀，目标是让面试官/HR 点进来就能看到：

- **3 篇** 逆向理论学习笔记（TSV / RDL / 混合键合与 2.5D·3D）
- **1 份** 《先进封装核心术语图解》（面试能画图讲）
- **1 段** 模拟芯片 I/O 热力分布的 Python 代码
- **1 个** 用课设包装的“芯片热管理模拟验证平台”

---

## 📁 目录结构

```
Chip-Packaging-Learning/
├── README.md                            # 项目说明（本文件）
├── LICENSE                              # MIT 许可证
├── notes/                              # 逆向理论学习（第一步）
│   ├── 01_TSV_硅通孔.md
│   ├── 02_RDL_重布线层.md
│   ├── 03_混合键合与2.5D_3D区别.md
│   └── 术语图解_先进封装核心术语.md
├── simulation/                         # 轻量仿真实战（第二步）
│   ├── README.md
│   ├── requirements.txt
│   └── chip_thermal_map.py            # 芯片 I/O 热力色块图（matplotlib）
└── projects/                           # 课设包装（第三步）
    └── stm32_thermal_monitor/         # 芯片热管理模拟验证平台
        └── README.md
```

---

## 🎯 本仓库对应的三步走

### 第一步 · 逆向理论学习（每日早起10分钟 + 睡前20分钟）
见 [`notes/`](notes/)。读懂 **TSV、RDL、混合键合** 三大概念，和 **2.5D / 3D** 的差别，边读边画流程。

### 第二步 · 轻量仿真实战（每周日 2 小时）
见 [`simulation/`](simulation/)。用 Python + matplotlib 画芯片 Bump 引脚布局与热力分布色块图。核心说明：

> 基于热传导方程对封装散热路径进行了简化建模。

### 第三步 · 包装课设项目（碎片时间构思）
见 [`projects/`](projects/)。把大三课设改写为：

> **基于 STM32 的芯片热管理模拟验证平台** —— 模拟多核芯片负载下的温度梯度变化。

---

## 🔗 我能证明的事

- 持续学习 · 每周都有 Green dot 更新
- 会做简化热学建模，而不是只背概念
- 能把工程问题写成“散热验证”视角的简历项目

---

## 🛠 环境

- Python 3.x
- `pip install -r simulation/requirements.txt`

---

## 📄 许可证

[LICENSE](LICENSE) · MIT
