# 工业图像瑕疵双向转换研究综述

**范围**:工业视觉中的瑕疵双向转换——加瑕(normal→defect,为异常检测造训练样本)与去瑕(defect→normal,做修复参考或重建式检测)。综述以本项目已梳理的 18 篇种子文献谱系为骨架,经 arXiv/OpenAlex 检索补齐至 2026 年,共纳入 25 篇代表工作。三条落地约束贯穿全文并作为评价每种方法的固定维度:**少样本(单类缺陷 ≤20 张)**、**RTX 4080(16GB)显存上限**、**下游检测涨点验证**。

**数值出处约定**:标注"论文"表示取自该工作原文主张;"公开值"为社区广泛引用的数据集/基准数值;"OpenAlex"为引用数(注:多匹配到 arXiv 版本记录,应视为下界);"估算"为基于骨干网络类型与显存经验的推断,非实测;"brief"为项目背景已给出的数值。凡未标注出处的数字均不可信。

---

## 1. 问题定义与谱系全景

工业异常检测(anomaly detection, AD)的根本困境是数据不对称,即正常图像充足,而缺陷样本极度稀缺——真实产线一类产品往往只有约 20 张缺陷图(brief)。这一稀缺性同时驱动了两个互为镜像的生成方向。**加瑕**在无瑕图上合成逼真缺陷,把 20 张扩增成足以训练检测器的规模;**去瑕**消除缺陷、还原正常外观,既可作修复参考,又可支撑"重建式检测"——用重建图与输入图的差异定位异常。二者与检测端构成闭环:转换负责造数据,检测负责用数据,而生成质量的最终裁判是检测涨点(约定 4)。

谱系时间线(图 1)把这一领域的演化压缩为一张图。**加瑕方向(蓝)沿一条清晰的机制主线密集演化**:2021 年的手工合成基线,经 2023 年的 GAN 少样本,再进入 2024–2026 年的扩散生成主流,再向可控性、逻辑异常、免训练、基础模型多个前沿分叉。**去瑕方向(红)则只有孤零零的节点**——这一视觉上的稀疏对比,正是本综述反复回到的核心判断,即去瑕是一个被加瑕的繁荣所掩盖的潜在空位。

![图1 工业图像瑕疵转换方法谱系时间线]({{artifact:3da4a9cb-708b-4936-b006-15f5de39c0ca}})

*图 1:方法谱系时间线(2021–2026)。横轴为 arXiv 首次公开年份,纵轴为方法族,灰色箭头表示机制继承/增量方向,颜色区分转换方向。加瑕方向在扩散主流之后向多个前沿分叉,去瑕方向(红)仅 FAIR 一个独立节点。*

### 1.1 分类法

沿两个正交轴组织全部工作:**转换方向**(加瑕 / 去瑕 / 逻辑异常 / 3D / 评估 / 数据集)与**生成范式**(手工合成 → GAN → 扩散 → 特征空间合成 → 基础模型/智能体)。范式轴大体也是时间轴——每一代范式针对前一代的短板递进:手工合成不真实,GAN 提真实性但少样本易崩,扩散提质量与可控性但训练重,免训练/基础模型压训练代价。下文加瑕综述即按范式族展开。

---

## 2. 加瑕方向(normal→defect)深度综述

加瑕是本领域的绝对主体:纳入的 25 篇中有 20 篇属加瑕(references.csv)。按范式族逐一定位。

### 2.1 手工合成基线:真实性的地板

最早的一代不学习缺陷分布,而是用图像处理算子直接"贴"出异常。**DRAEM** 用 Perlin 噪声生成异常掩码、贴到正常图上得到合成缺陷对,再训练一个判别式重建网络端到端检测([Zavrtanik 2021](https://arxiv.org/abs/2108.07610));**NSA** 则用 Poisson 图像融合把一张图的补丁无缝融进另一张,避免贴图边界的突兀([Schlüter 2022](https://arxiv.org/abs/2109.15222))。二者的共同价值在于**完全不需要真实缺陷样本**(自监督),因而天然满足少样本约束,且骨干轻、16GB 显存毫无压力(估算)。局限也同样明确:合成缺陷与真实缺陷存在分布差距,对"弱缺陷"(与正常区域高度相似)几乎无能为力——这一短板后来被 GLASS 明确作为攻击目标。手工合成至今仍是几乎所有后续工作的对照基线,其地位类似"真实性的地板"。

### 2.2 GAN 少样本生成:真实性的第一次跃升

**DFMGAN**(AAAI'23)是谱系中第一个正面攻少样本缺陷生成的工作:在 StyleGAN2 上增设缺陷感知的特征操控分支,在预训练的正常图生成器基础上,用少量缺陷样本操控特征生成缺陷及其对齐掩码([Duan 2023](https://arxiv.org/abs/2303.02389))。它把缺陷生成从"贴图"推进到"学习缺陷的特征表示",真实性显著优于手工合成,并能同时产出缺陷掩码供下游定位训练。代价是 GAN 少样本训练的固有不稳定性与模式坍缩风险。**AnomalyHybrid**(2025)是 GAN 路线的近期延续,用深度解码器与边缘解码器双分支把参考图外观注入目标图的深度与边缘结构,尤其擅长凸起、凹陷这类深度变化型缺陷,并主打域无关([Zhao 2025](https://arxiv.org/abs/2504.04340))。**FewShotConsistency/DefectDiffu**(2024)虽用扩散骨干,但其核心思想——跨产品建模背景一致性与缺陷一致性、用一致性扰动方向控制产品类型与缺陷强度——是对"单产品训练导致质量差"的直接回应([Shi 2024](https://arxiv.org/abs/2408.00372))。

### 2.3 扩散生成主流:质量、可控、掩码对齐三条线

2024 年起扩散模型成为加瑕主流,内部又沿三条可区分的线索递进。

**少样本真实性线。AnomalyDiffusion**(AAAI'24)是扩散少样本的代表,把异常拆成空间锚(掩码指定位置)与文本嵌入(指定类别),在 Stable Diffusion 上少样本生成缺陷并输出对齐的掩码-图对([Hu 2024](https://arxiv.org/abs/2312.05767),OpenAlex 引用 105)。**DualAnoDiff**(CVPR'25)针对前代"生成缺陷与掩码不对齐、缺陷与原图融合生硬、多样性不足"的痛点,换了个视角:用双分支互关联扩散**同时**生成整图与缺陷部件,从生成机制上保证掩码对齐([Jin 2025](https://arxiv.org/abs/2408.13509))。代价是双 SD 分支加 LoRA 的显存开销偏紧,估算在 14–16GB 量级,恰在 4080 上限附近(需注意)。

**强度可控线。RealNet**(CVPR'24)提出强度可控扩散异常合成(SDAS),能生成不同异常强度、更贴近真实缺陷分布的样本,并配特征选择应对预训练特征冗余([Zhang 2024](https://arxiv.org/abs/2403.05897),OpenAlex 引用 155——本语料中被引最高的加瑕工作之一)。强度可控意味着可以按检测器的难度需要生成"恰到好处"的难样本。

**特征空间合成线。GLASS**(ECCV'24)把合成同时放在特征级(全局,流形与超球约束下的梯度上升)与图像级(局部),专门扩大异常覆盖度、并攻克与正常极相似的弱缺陷,在 MVTec AD 上检测 AUROC 达 99.9%(论文)([Chen 2024](https://arxiv.org/abs/2407.09359))。GLASS 与前述工作的差异在于它不追求"逼真的可见缺陷图",而追求"对检测最有用的近分布异常"——直接面向下游。

### 2.4 Inpainting 填缺陷:局部保真与掩码严格贴合

**DefectFill**(CVPR'25)用微调的 inpainting 扩散模型,配缺陷项、物体项、注意力项三个定制损失,只需少量参考缺陷即可把细粒度局部缺陷无缝填进无瑕物体,并用低保真度筛选提质,在 MVTec AD 上使检测达到 SOTA(论文)([Song 2025](https://arxiv.org/abs/2503.13985))。**MAGIC**(2025)进一步指出 inpainting 路线的两难——全局提示会破坏正常区域,而已有 inpainting 又缺乏下游所需的分布内多样性——用高斯提示扰动防少样本过拟合、空间自适应引导对缺陷与背景施加不同引导强度、上下文感知掩码重定位来解决([Choi 2025](https://arxiv.org/abs/2507.02314))。inpainting 族的共性优势是缺陷严格贴合掩码、背景零污染;共性代价是 SD inpainting 微调的显存偏紧(估算)。

### 2.5 可控性前沿:从"能生成"到"精确指定"

这一族把控制粒度推向极致。**SARD** 用区域约束扩散(RCD)在反向去噪时冻结背景、只更新前景异常区域,从根上消除背景伪影,并加判别掩码引导保证区域保真([2025](https://arxiv.org/abs/2508.03143))。逻辑异常方向,**LogicAL**(CVPR-W'24)与 **ComponentAware/ComGEN**(2025)把生成建模为组合问题:ComGEN 先做多组件解耦,再经注意力残差映射生成违反内在逻辑约束的异常(如部件缺失、错配),填补了逻辑异常生成的空白([2025](https://arxiv.org/abs/2502.11712))。逻辑异常是结构/语义层面的缺陷,与前述纹理/结构表面缺陷正交,是可控性前沿中一个独立子空位。

### 2.6 免训练与零样本:直击"生成却要样本"的悖论

一个被 DeltaDeno 一针见血点出的矛盾:多数少样本生成方法要用缺陷样本微调,而这与"正因缺陷稀缺才要生成"自相矛盾([Xu 2025](https://arxiv.org/abs/2511.16920))。免训练路线正面化解这一悖论。**One-to-More/O2MAG**(2026)完全免训练,靠单张参考缺陷图的自注意力嫁接、并行三路扩散加异常掩码缓解前景背景查询混淆来合成更多真实缺陷([2026](https://arxiv.org/abs/2603.18093))。**DeltaDeno**(2025)更进一步做零样本、零训练:对比两条最小提示对驱动的扩散分支,累积每步去噪差分得到缺陷定位图,再引导后续潜空间 inpainting([Xu 2025](https://arxiv.org/abs/2511.16920))。免训练族对 16GB 显存最友好,仅推理、无微调(估算优势),是与本项目算力约束最契合的一支。

### 2.7 基础模型与智能体:换掉少样本范式本身

最新一代干脆质疑少样本范式。**UniDefGen/UniDG**(2026)认为 few-shot 会过拟合特定缺陷类别,转而构建 30 万条正常-异常-掩码-描述四元组数据集,训一个通用缺陷生成基础模型,支持免逐类微调的参考生成与文本指令编辑([2026](https://arxiv.org/abs/2604.08915))。**AnomalyAgent**(2026)则把生成做成带自省、知识检索、迭代优化的闭环智能体,配提示生成、图像生成、质量评估、知识检索、掩码生成五个工具([2026](https://arxiv.org/abs/2604.07900))。这两支用"大数据预训练"或"智能体闭环"替代少样本微调,理念先进,但基础模型/多工具栈的显存与工程代价偏紧(估算),与 4080 单卡约束存在张力。**3D-PNAS**(2025)把 Perlin 噪声合成搬到 3D 点云表面,填补 3D 异常生成的空白([2025](https://arxiv.org/abs/2504.12856)),随 3D 工业传感器普及而重要性上升。

---

## 3. 去瑕方向(defect→normal):文献稀疏度的量化

去瑕方向的稀疏不是印象,而是可量化的事实。在覆盖 anomaly generation / defect synthesis / few-shot diffusion 等关键词的 arXiv 检索中,加瑕方向命中数以十计并持续增长;而正面做"defect→normal 还原式转换"的工作,本综述在同等检索强度下仅稳定命中 **FAIR** 一篇独立方法(references.csv 中 direction=remove 仅 1 条,占 25 篇的 4%)。这一比例本身就是本项目判断"去瑕是潜在空位"的第一手依据。

**FAIR**(2023)是去瑕/还原式方向的代表。它指出重建式检测的核心矛盾——正常重建保真度与异常重建可区分性之间的权衡——并发现二者可借正常与异常重建误差的频率偏置差异来缓解:提出频率感知图像还原(FAIR),仅从图像的高频分量还原图像,从而精确重建正常模式、同时抑制对异常的过度泛化,用一个 vanilla U-Net 就在多个缺陷检测数据集上取得 SOTA 且更高效([Liu 2023](https://arxiv.org/abs/2309.07068),OpenAlex 引用 27)。对本项目而言 FAIR 有双重吸引力:一是 vanilla U-Net 极轻,16GB 显存毫无压力(论文强调高效);二是它示范了去瑕与重建式检测的天然耦合,即**去瑕器本身就是检测器,重建差异即异常区域**。

这一耦合把去瑕从"图像修复"重新定义为"检测的一种范式"。**AnomalySD**(2024)虽被归为检测框架,但其机制正是去瑕的反向使用:借 Stable Diffusion 的 zero/few-shot inpainting 能力,把异常区域 inpaint 还原成正常,再以重建差异判定异常,并用层级文本描述与前景掩码适配多类检测([Yan 2024](https://arxiv.org/abs/2408.01960))。换言之,**每一个能"把缺陷还原成正常"的 inpainting 模型,都潜在是一个去瑕器**——而加瑕方向积累的大量 inpainting 技术(DefectFill、MAGIC、One-to-More),其反向几乎无人系统研究。这正是空位的结构性来源:领域把 inpainting 的正向(填缺陷)做到了极致,反向(填正常)却几乎空白。

去瑕方向真正的独立价值有三:(1)**修复参考**——为人工复检提供"本该长什么样"的对照;(2)**重建式检测**——如 FAIR/AnomalySD,无需缺陷样本即可检测,与本项目 DINOv3 无监督检测线天然互补;(3)**闭环自洽**——加瑕造的假缺陷若能被去瑕器干净还原,可作为加瑕真实性的一种一致性校验。这三点在现有文献中都远未被充分开发。

---

## 4. 评估方法与数据集

### 4.1 生成质量:真实性与多样性两个维度

约定 4 要求生成质量评估必须同时覆盖真实性与多样性,二者缺一都会误导。**真实性**主流用 FID(生成与真实图在 Inception 特征空间的分布距离,越低越好),但 FID 在少样本下方差大、不稳定,KID(核化 Inception 距离)在小样本时更稳,更适合 ≤20 张的工业场景(estimate/领域共识)。针对生成异常的专门评估,种子文献 **MIRAGE**(2026)提出了一条免训练的真实性评估管线:通过 API 黑盒访问任意生成模型,用 VLM 自动生成缺陷提示,再用 CLIP 质量过滤只保留良好对齐的生成图,并附带轻量双分支语义变化检测做像素级掩码([2026](https://arxiv.org/abs/2603.13507))。**多样性**用 LPIPS(生成样本间感知距离,越高越多样)防模式坍缩,GLASS 则强调覆盖度/召回——生成分布对真实缺陷模式的覆盖广度([Chen 2024](https://arxiv.org/abs/2407.09359))。完整指标定义见 metrics_table.csv。

### 4.2 下游检测涨点:最终裁判

真实性与多样性都只是代理指标,生成的最终价值在于**喂给检测模型后能否涨点**。约定 4 把这条列为核心验收:生成数据加入训练集前后,对比 AD 模型的图像级 AUROC(检测)与像素级 AP/PRO(定位)。DefectFill、GLASS、RealNet 等都以下游 SOTA 作为主要卖点(各论文),而非仅报 FID。这一评估协议也正是转换端与检测端闭环的接口——本项目基于 DINOv3 的无监督检测线,恰可充当生成质量的统一裁判台。

### 4.3 数据集

MVTec AD(2019,OpenAlex 引用 1817)是工业 AD 的事实标准,也是少样本缺陷生成的主战场:约 5354 张、15 类(10 物体 + 5 纹理)、70+ 缺陷类型(公开值)。VisA(约 10821 张、12 类,公开值)补充复杂多实例场景。**MPDD**(约 1346 张、6 类金属件,公开值)是与本项目金属件(螺丝)资产最贴近的公开集。**Real-IAD**(CVPR'24)把规模推到约 15 万张、30 类(brief + 论文),并以多视角为差异点;其 2025 后续 Real-IAD Variety 进一步扩充类别与多样性([2025](https://arxiv.org/abs/2511.00540))。**半导体 SEM** 场景则相反——先进节点缺陷数据通常私有且样本极少(brief),这正是本项目落地场景之一的数据空位;SEM-CLIP(2025)等工作也主要在解决该场景的少样本检测([2025](https://arxiv.org/abs/2502.14884))。完整规模与出处见 datasets_metrics.csv。

---

## 5. 跨方法对照矩阵解读

图 2 把 21 个有明确方法主张的工作压成一张对照矩阵,列为对本项目最关键的七个决策维度。完整取值与逐格出处见 comparison_matrix.csv。

![图2 跨方法对照矩阵]({{artifact:5bf385ab-ea8f-455f-bc79-f240c68d402b}})

*图 2:跨方法对照矩阵。色深表示该维度的强度/可用度,单元格文字为实际取值。所有取值的出处(论文/公开/估算)见 comparison_matrix.csv。*

从矩阵可读出四条对本项目直接有用的判断:

1. **少样本几乎是全域共识**。绝大多数方法或明确主打 few-shot,或自监督无需真实缺陷——≤20 张这条硬约束在方法层面基本不构成筛选门槛,真正的筛选发生在下两条。
2. **强可控性仍是稀缺的**。强度/区域强可控只集中在 RealNet(强度)、GLASS(覆盖度)、SARD(区域)、DefectDiffu(缺陷强度)少数几家;多数扩散方法停留在"中等可控"。**少样本 + 强可控同时满足者少**——这是一个可切入的交集空位。
3. **16GB 显存是真实的过滤器**。DualAnoDiff(双 SD 分支 + LoRA)、DefectFill/MAGIC(SD inpainting 微调)、UniDefGen(MM-DiT 基础模型)、AnomalyAgent(生成器 + VLM 栈)都被标为"偏紧"(估算);而免训练的 One-to-More、DeltaDeno 与轻骨干的 FAIR、手工合成基线在 4080 上最从容。**方法先进性与显存友好度呈负相关**,选型时须权衡。
4. **下游检测验证是普遍声明、却少有统一裁判**。矩阵中几乎所有方法都声明做了下游验证(各论文),但各自用不同检测器、不同协议,横向不可比。**一个统一的下游裁判台(如本项目 DINOv3 检测线)本身就有方法学价值**。

---

## 6. 空位分析与研究机会

对照谱系(图 1)与矩阵(图 2),下列空位在现有文献中或未被占据、或仅被单点触及。每条标注"占谱系哪个空位、比最近邻方法增量在哪",供选题时对齐约定 3。

### 6.1 去瑕方向的系统化(最大空位)

**空位**:加瑕方向已积累十余种 inpainting/扩散技术,其"反向"(把缺陷还原为正常)却几乎只有 FAIR 一篇独立方法,AnomalySD 仅隐式使用。**最近邻**:FAIR(频率还原)、AnomalySD(SD inpainting 还原)。**可能的增量**:把加瑕侧成熟的掩码对齐、区域约束(SARD)、免训练自注意力嫁接(One-to-More)系统迁移到去瑕,构建"缺陷区域精确还原 + 重建差异检测"的统一框架;与本项目 DINOv3 检测线耦合做重建式检测。这是文献稀疏度最高、与项目资产最契合的方向。

### 6.2 少样本 × 强可控 × 16GB 的三角交集

**空位**:少样本是共识,强可控是稀缺,显存友好与先进性负相关——三者的交集(≤20 张即可、位置/强度精确可控、4080 单卡可跑)在矩阵中几乎无方法同时命中。**最近邻**:免训练的 One-to-More/DeltaDeno(省显存但可控性中等)、SARD(区域强可控但显存未验证)。**可能的增量**:在免训练/轻量扩散骨干上引入区域 + 强度双重显式控制,把"省显存"与"强可控"这对负相关拉到同一方法内。

### 6.3 生成-检测闭环的一致性建模

**空位**:现有工作把生成质量与下游涨点当两个割裂的评估阶段;鲜有方法把"检测器反馈"直接写进生成目标做联合优化。**最近邻**:GLASS(面向下游的近分布合成,但仍是单向)、AnomalyAgent(闭环但靠外部质量评估工具,非可微反馈)。**可能的增量**:用检测器损失作为生成器的可微监督,形成生成↔检测的可微闭环——本项目同时握有转换端与 DINOv3 检测端,具备做这件事的独特条件。

### 6.4 半导体 SEM 的少样本生成

**空位**:SEM 灰度、纳米级缺陷、先进节点数据私有且样本极少;现有加瑕方法几乎都在 RGB 自然图/MVTec 上验证,SEM 域几乎无生成工作(仅有 SEM-CLIP 等检测侧工作)。**最近邻**:SEM-CLIP(SEM 少样本检测,非生成)、通用扩散加瑕(未在 SEM 域验证)。**可能的增量**:把少样本加瑕方法迁移到 SEM 域并做域适配,直接服务 brief 中的半导体落地场景——这是一个应用驱动的清晰空位。

### 6.5 逻辑异常与 3D 的生成(次级空位)

逻辑异常生成仅 LogicAL、ComGEN 两家,3D 异常生成仅 3D-PNAS 一家,均为新兴单点。若项目资产涉及结构/装配缺陷或 3D 传感,这两处也是低竞争切入点,但与本项目核心(表面缺陷 RGB/SEM)相关性次于 6.1–6.4。

### 6.6 选题优先级建议

综合文献稀疏度、与项目资产(20 张小样本、4080、DINOv3 检测线、金属件/SEM 场景)的契合度,建议优先级为:**6.1(去瑕系统化)≈ 6.3(可微生成-检测闭环)> 6.2(三角交集)> 6.4(SEM 生成)> 6.5**。前两者既踩在文献最稀疏处,又独占本项目"同时握有转换端与检测端"的结构性优势,最可能支撑一篇有清晰差异化定位的 CVPR/AAAI 级工作。

---

## 7. 参考文献

按方向与年份排列;链接为 arXiv。完整元数据(含 OpenAlex 引用数、会议归属与出处标注)见 references.csv。

**加瑕 · 手工合成基线**
- DRAEM — A Discriminatively Trained Reconstruction Embedding for Surface Anomaly Detection (ICCV 2021). [arXiv:2108.07610](https://arxiv.org/abs/2108.07610)
- NSA — Natural Synthetic Anomalies for Self-Supervised Anomaly Detection (ECCV 2022). [arXiv:2109.15222](https://arxiv.org/abs/2109.15222)

**加瑕 · GAN 少样本**
- DFMGAN — Few-Shot Defect Image Generation via Defect-Aware Feature Manipulation (AAAI 2023). [arXiv:2303.02389](https://arxiv.org/abs/2303.02389)
- AnomalyHybrid — A Domain-agnostic Generative Framework for General Anomaly Generation (2025). [arXiv:2504.04340](https://arxiv.org/abs/2504.04340)
- DefectDiffu — Few-shot Defect Image Generation based on Consistency Modeling (2024). [arXiv:2408.00372](https://arxiv.org/abs/2408.00372)

**加瑕 · 扩散主流**
- AnomalyDiffusion — Few-Shot Anomaly Image Generation with Diffusion Model (AAAI 2024). [arXiv:2312.05767](https://arxiv.org/abs/2312.05767)
- RealNet — A Feature Selection Network with Realistic Synthetic Anomaly (CVPR 2024). [arXiv:2403.05897](https://arxiv.org/abs/2403.05897)
- GLASS — A Unified Anomaly Synthesis Strategy with Gradient Ascent (ECCV 2024). [arXiv:2407.09359](https://arxiv.org/abs/2407.09359)
- DualAnoDiff — Dual-Interrelated Diffusion Model for Few-Shot Anomaly Image Generation (CVPR 2025). [arXiv:2408.13509](https://arxiv.org/abs/2408.13509)

**加瑕 · inpainting 填缺陷**
- DefectFill — Realistic Defect Generation with Inpainting Diffusion Model (CVPR 2025). [arXiv:2503.13985](https://arxiv.org/abs/2503.13985)
- MAGIC — Few-Shot Mask-Guided Anomaly Inpainting with Prompt Perturbation (2025). [arXiv:2507.02314](https://arxiv.org/abs/2507.02314)

**加瑕 · 可控/逻辑前沿**
- SARD — Segmentation-Aware Anomaly Synthesis via Region-Constrained Diffusion (2025). [arXiv:2508.03143](https://arxiv.org/abs/2508.03143)
- LogicAL — Towards Logical Anomaly Synthesis for Unsupervised Anomaly Localization (CVPR-W 2024). [arXiv:2405.06875](https://arxiv.org/abs/2405.06875)
- ComGEN — Component-aware Unsupervised Logical Anomaly Generation (2025). [arXiv:2502.11712](https://arxiv.org/abs/2502.11712)

**加瑕 · 免训练/零样本**
- One-to-More (O2MAG) — High-Fidelity Training-Free Anomaly Generation with Attention Grafting (2026). [arXiv:2603.18093](https://arxiv.org/abs/2603.18093)
- DeltaDeno — Zero-Shot Anomaly Generation via Delta-Denoising Attribution (2025). [arXiv:2511.16920](https://arxiv.org/abs/2511.16920)

**加瑕 · 基础模型/智能体/3D**
- UniDG (UniDefGen) — Large-Scale Universal Defect Generation: Foundation Models and Datasets (2026). [arXiv:2604.08915](https://arxiv.org/abs/2604.08915)
- AnomalyAgent — Agentic Industrial Anomaly Synthesis via Tool-Augmented Reasoning (2026). [arXiv:2604.07900](https://arxiv.org/abs/2604.07900)
- 3D-PNAS — 3D Industrial Surface Anomaly Synthesis with Perlin Noise (2025). [arXiv:2504.12856](https://arxiv.org/abs/2504.12856)

**去瑕 · 还原式**
- FAIR — Frequency-aware Image Restoration for Industrial Visual Anomaly Detection (2023). [arXiv:2309.07068](https://arxiv.org/abs/2309.07068)
- AnomalySD — Few-Shot Multi-Class Anomaly Detection with Stable Diffusion (2024,去瑕反向用于检测). [arXiv:2408.01960](https://arxiv.org/abs/2408.01960)

**评估 · 数据集 · SEM**
- MIRAGE — Model-agnostic Industrial Realistic Anomaly Generation and Evaluation (2026). [arXiv:2603.13507](https://arxiv.org/abs/2603.13507)
- Real-IAD Variety — Pushing Industrial Anomaly Detection Dataset to a More Diverse Scale (2025). [arXiv:2511.00540](https://arxiv.org/abs/2511.00540)
- SEM-CLIP — Precise Few-Shot Learning for Nanoscale Defect Detection in SEM (2025). [arXiv:2502.14884](https://arxiv.org/abs/2502.14884)
- Semiconductor SEM Anomaly Detection Evaluation (2025). [arXiv:2505.07576](https://arxiv.org/abs/2505.07576)

---

## 附:交付物清单

| 文件 | 内容 |
|------|------|
| survey_defect_conversion.md | 本综述正文 |
| lineage_timeline.png | 谱系时间线图(图 1) |
| comparison_matrix.png / .csv | 跨方法对照矩阵(图 2)+ 逐格出处 |
| references.csv | 25 篇文献元数据(会议/年份/引用数/方向/出处) |
| datasets_metrics.csv | 数据集规模与出处 |
| metrics_table.csv | 评估指标定义与方向 |

*出处约定:全文数值均标注"论文/公开/OpenAlex/估算/brief";未标注者不采信。OpenAlex 引用数多匹配 arXiv 版本记录,应视为下界。显存"偏紧/可行"为基于骨干类型的估算,非 4080 实测——落地选型时需以实机跑通为准。*

