# 方向摸底报告：轻量化工业异常检测（Lightweight Industrial Anomaly Detection）

> 实测于 2026-07-04（修订轮 1 订正空档一节与统计口径） · 数据源：OpenAlex（免费学术数据库）
> 检索式：title_and_abstract.search:"industrial anomaly detection" AND (lightweight OR efficient OR real-time OR edge)，2021-2026，命中 269 条，按引用抓 Top 50 条记录，去重后 48 篇

## 一句话定位

给工厂产线上的"视觉质检员"瘦身：模型既要看得准（漏检要命），又要跑得快（毫秒级）、装得下（边缘设备）。方向自 2023 年起爆发，2024 年达峰，仍在上升期。

## 流派地图（基于去重后 48 篇真实标题归纳）

| 流派 | 篇数 | 思路一句话 | 代表作（引用数） |
|---|---|---|---|
| 重建/生成类 | 9 | 让模型学会"画"正常品，画不像的地方就是缺陷 | MFGAN(53)、AMI-Net(34)、MiniMaxAD(6) |
| 记忆库/特征嵌入 | 6 | 把正常品特征存成"字典"，新样本查字典比对 | PNI(88)、FAPM(42)、FR-PatchCore(18) |
| 蒸馏/师生网络 | 4* | 老师见多识广，学生只学正常品；师生答案不一致=异常 | **EfficientAD(268，全场最高引)**、LPFSTNet |
| 多模态/3D | 4 | RGB 之外加深度/点云/红外，看单目看不出的缺陷 | EasyNet(52)、2M3DF(16) |
| 大模型/零样本 | 2 | 借 CLIP/SAM 的通用视觉知识，不训练直接检测 | IAD-CLIP(5)、SAM-guided(16) |
| 归一化流 | 2 | 把正常特征"压"成标准分布，落在分布外=异常 | UniFlow(7) |
| 时序/IoT 传感 | 8 | 同名不同界：检测的是设备信号曲线，不是图像 | TMANomaly(23) |

*EfficientAD 标题看不出流派，经 API 摘要核实为师生网络（"we then use a student–teacher approach"）后归入蒸馏。另有 13 篇为通用框架/主动学习/光照增强等暂不成派的散兵，未单列（7 派 35 + 散兵 13 = 48）。

## 热点判读

1. **全场最高引（268）是 EfficientAD**——"毫秒级延迟"写进标题，说明这个方向的军备竞赛已从"更准"转向"更快更小"。
2. 标题热词：unsupervised(5)、multimodal(5，含连字符写法则 6)、fusion(4)、lightweight(4)。无监督是底色，多模态/3D 是 2024-2025 的增量热点。
3. 期刊主场：IEEE Trans. Industrial Informatics、Neurocomputing、Sensors；但最高引方法都发在顶会（WACV/ICCV）。

## 可能的窗口（数据显示，非拍脑袋；修订轮 1 已按"窗口≠真空"口径订正）

窗口的意思是"刚开了个口子、还没形成气候"，不是"没人做"——下面每条都标了 48 篇内已有的先行者。

1. **轻量化 × 多模态刚合流**：多模态/3D 主力（2M3DF、CPIR 等）基本不谈部署开销；48 篇内已有先行者 LPFSTNet（2025，轻量×师生×快速 3D），但仅此一篇，窗口刚开。
2. **大模型的见识 × 轻量的身板**：零样本方法（IAD-CLIP 等）块头巨大；48 篇内已有 SAM-guided lightweight（16 引）做"大模型引导轻量模型"的苗头，但"把大模型知识蒸进轻量模型"仍未成气候。
3. **应用落地文稀缺（硬数字）**：48 篇里仅 5 篇应用文，方法卷成红海，"真实产线部署+踩坑"的工程文反而少——非科班有产线数据的人，这是你的门。
4. ~~综述真空~~ **已订正删除**：原"系统综述 2025 年才出现第一篇"为事实错误——48 篇内即有 2024《An Overview of Methods of Industrial Anomaly Detection》，宽口径下另有 2024 领域高引综述《Deep Industrial Image Anomaly Detection: A Survey》（338 引）。综述已就位，对新人的正确含义是：入门可以先读这两篇综述，不算空档。

## 给读者的下一步

Top 50 清单已在手（`step1_top50_list.tsv`，含 2 条预印本重复记录），下一章教你：不用逐篇精读，让 AI 帮你把这批文献按流派读完、建成自己的文献库。
