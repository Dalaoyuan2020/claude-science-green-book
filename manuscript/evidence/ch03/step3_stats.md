# Step 3 · 四维体检统计结果（实测于 2026-07-04）

数据源：`step1_response.json`（OpenAlex 精修查询，269 命中中按引用数取 Top 50）
分析脚本：`step2_step3_analyze.py`（/usr/bin/python3，零依赖），完整输出见 `step2_step3_output.txt`

## 维度一：年份分布（50 篇）

| 年份 | 篇数 | 直方 |
|---|---|---|
| 2021 | 1 | # |
| 2022 | 4 | #### |
| 2023 | 11 | ########### |
| 2024 | 21 | ##################### |
| 2025 | 13 | ############# |

判读：2023 起爆发，2024 是峰值年（2025/2026 论文引用还没长起来，排引用榜自然吃亏）。方向处于上升期，不是夕阳方向。

## 维度二：来源期刊/会议 Top

| 篇数 | 来源 |
|---|---|
| 11 | unknown（多为顶会 proceedings，OpenAlex source 字段为空，如 EfficientAD=WACV、PNI=ICCV） |
| 3 | IEEE Transactions on Industrial Informatics |
| 3 | Neurocomputing |
| 2 | Sensors |
| 2 | IEEE Trans. on Automation Science and Engineering |
| 2 | Applied Sciences |
| 2 | IEEE Trans. on Instrumentation and Measurement |
| 2 | arXiv 预印本 |

判读：期刊侧以 IEEE 工业系 Trans + Neurocomputing 为主场；最高引方法反而在顶会（source=unknown 那批）。

## 维度三：高频关键词

OpenAlex 自带 `keywords` 字段太泛（"Computer science" 49 次、"Anomaly (physics)" 33 次，没有信息量），改用标题词频（去停用词）：

time(7) feature(7) multi(6) learning(6) multimodal(5) unsupervised(5) fusion(4) reconstruction(4) series(4) dual(4) lightweight(4) autoencoder(3) memory(3) teacher(3) student(3)

判读：unsupervised（无监督）是底色；multimodal/fusion/3D 是近两年的增量热词；teacher/student、memory、reconstruction 对应三大技术流派。

## 维度四：内容构成

- OpenAlex type：article 45 / preprint 3 / review 1 / book-chapter 1
- 标题启发式：方法类 43 / 应用类 5 / 综述类 2

判读：九成是方法创新文，综述极少（2025 年 Frontiers in Robotics and AI 有一篇系统综述可当入门读物）。应用落地文少，是非科班读者的可乘之机。

## 数据质量备注（诚实边界）

1. Top 50 里 PNI 和 EfficientAD 各出现两次（arXiv 预印本 + 正式版被 OpenAlex 当两条记录），实际去重后约 48 篇。
2. EfficientAD 流派归属经 API 摘要核实（abstract 原文 "we then use a student–teacher approach"），不是凭记忆归类。
3. "industrial anomaly detection" 一词下混着两个几乎不往来的社区：图像检测（做产品外观缺陷）和时序/IoT 传感检测（做设备信号），检索时必须自己分辨。
