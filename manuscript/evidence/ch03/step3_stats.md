# Step 3 · 四维体检统计结果（实测于 2026-07-04，修订轮 1 统一去重口径）

数据源：`step1_response.json`（OpenAlex 精修查询，269 命中中按引用数抓 Top 50 条记录）
**统一口径：50 条记录去重后 48 篇**（PNI、EfficientAD 各有 arXiv 预印本+正式版两条记录，按标题归一去重，保留高引版）。以下所有统计均基于去重后 48 篇。
分析脚本：`step2_step3_analyze.py`（/usr/bin/python3，零依赖，Rev 2 已内置去重），完整输出见 `step2_step3_output.txt`

## 维度一：年份分布（48 篇，去重后）

| 年份 | 篇数 | 直方 |
|---|---|---|
| 2021 | 1 | # |
| 2022 | 3 | ### |
| 2023 | 10 | ########## |
| 2024 | 21 | ##################### |
| 2025 | 13 | ############# |

判读：2023 起爆发，2024 是峰值年（2025/2026 论文引用还没长起来，排引用榜自然吃亏）。方向处于上升期，不是夕阳方向。

## 维度二：来源期刊/会议 Top

| 篇数 | 来源 |
|---|---|
| 10 | unknown（多为顶会 proceedings，OpenAlex source 字段为空，如 EfficientAD=WACV、PNI=ICCV） |
| 3 | IEEE Transactions on Industrial Informatics |
| 3 | Neurocomputing |
| 2 | Sensors |
| 2 | IEEE Trans. on Automation Science and Engineering |
| 2 | Applied Sciences |
| 2 | IEEE Trans. on Instrumentation and Measurement |

判读：期刊侧以 IEEE 工业系 Trans + Neurocomputing 为主场；最高引方法反而在顶会（source=unknown 那批）。
注：未去重口径下 unknown 为 11、另有 arXiv 2 条（两条预印本重复各占其一）。

## 维度三：高频关键词

OpenAlex 自带 `keywords` 字段太泛（"Computer science" 49 次、"Anomaly (physics)" 33 次，没有信息量），改用标题词频（去停用词，去重后 48 篇）：

time(7) feature(7) multi(6) learning(6) multimodal(5) unsupervised(5) fusion(4) reconstruction(4) series(4) dual(4) lightweight(4) autoencoder(3) memory(3) teacher(3) student(3)

计数口径：按精确词形。multimodal 记 5，另有 1 篇连字符写法（Multi-modal digital twins），合并口径为 6（拷打轮核对后注明）。

判读：unsupervised（无监督）是底色；multimodal/fusion/3D 是近两年的增量热词；teacher/student、memory、reconstruction 对应三大技术流派。

## 维度四：内容构成（48 篇，去重后）

- OpenAlex type：article 45 / preprint 1 / review 1 / book-chapter 1
- 标题启发式：方法类 41 / 应用类 5 / 综述类 2

判读：约九成是方法创新文；综述少但**并非没有**——48 篇内有 2 篇：2024《An Overview of Methods of Industrial Anomaly Detection》（第 34 名）、2025《A systematic survey: ... industrial inspection contexts》（Frontiers in Robotics and AI，第 14 名）。另外宽口径下 2024 年已有领域级高引综述《Deep Industrial Image Anomaly Detection: A Survey》（338 引，见 step1_response_wide_FAILED.json 结果列表，拷打轮亦独立核到）。⚠️ 修订轮 1 订正：早先"系统综述 2025 年才出现第一篇"为事实错误，已从报告和章稿中删除。应用落地文少（5/48），是非科班读者的可乘之机。

## 数据质量备注（诚实边界）

1. 抓取的是 50 条记录，去重后 48 篇，全文统计统一用 48 篇口径。
2. EfficientAD 流派归属经 API 摘要核实（abstract 原文 "we then use a student–teacher approach"），不是凭记忆归类。
3. "industrial anomaly detection" 一词下混着两个几乎不往来的社区：图像检测（产品外观缺陷）和时序/IoT 传感检测（设备信号）。精修检索式的前 15 名里就有 2 篇时序论文（第 8、9 名）——收紧检索式只能保证都是"工业异常检测"，不能自动分开这两个社区（拷打轮指出，已订正章内"前 15 篇全部在靶心上"的说法）。
4. 宽查询 25,331 条的口径 = 宽搜索 + 限定 2021 年起 + 按引用排序；裸宽搜（无年份过滤）约 29,263 条（拷打轮实测）。
5. 带 mailto 的礼貌通道下连续查询仍可能吃到 HTTP 429 限速，等几秒重试即好（拷打轮实测）。
