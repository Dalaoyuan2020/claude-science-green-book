# Claude Science 界面详解与配置指南（界面篇 · 重构骨架）

> 这是在吕博原稿基础上重构的结构：逻辑更清晰、格式统一、教程感更强。
> 第五、六章按此骨架落地；每个功能统一模板 = **位置 + 核心功能 + 科研场景 + 如何操作 + 推荐配置 + 注意事项**。

## 一、界面整体布局与核心状态指示器

Claude Science 采用「工作台 + 设置中心」双层架构：

- **左侧**：项目/会话列表 + 导航
- **中央**：主要对话与工作区（支持 Notebook 切换）
- **顶部/右侧状态栏**：核心功能指示器（最常用）
- **设置入口**：左下角或右上角头像/齿轮图标进入完整配置面板

### 顶部核心状态指示器（7 项，强烈建议关注）

**1. Delegation（任务委派）**
- 位置：顶部状态栏开关
- 核心功能：遇到复杂科研任务时，自动拆解步骤并调用其他工具/子模型协同完成
- 科研场景：写多篇顶刊引用的综述、做多步骤数据分析 pipeline
- 推荐配置：日常简单问答关闭；大型资料或多步骤任务开启
- 注意：开启后增加 token 消耗和响应时间

**2. Notebook（交互式代码环境）**
- 位置：顶部可点击切换按钮（显示当前状态）
- 核心功能：内置类 Jupyter 代码执行沙盒，支持 Python / R 实时运行
- 科研场景：绘制出版级图表、跑回归/统计模型、特征工程、数据验证。AI 不是给你代码，而是直接在 Notebook 里执行并展示结果
- 如何操作：AI 给出分析结论或画图代码后，立即切到 Notebook 核对数值和图表
- 优势：结果可追溯、支持交互式调试，也是项目代码资产的记录方式，便于复用

**3. Active Subagents（活跃子智能体数量）**
- 位置：顶部状态指示（如「2 active subagents」）
- 核心功能：任务复杂时自动在后台唤醒专业子代理并行工作
- 科研场景：主代理写引言时，一个子代理查 CrossRef 文献真实链接，另一个分析上传的实验数据，最后汇总
- 推荐操作：数字 > 0 时不要频繁打断，等归零再看完整结果；可点图标查看后台动作
- 提示：这是 Claude Science 多代理架构的核心体现

**4. Auto-review（自动审查）**
- 位置：顶部开关（强烈建议默认开启）
- 核心功能：后台 reviewer agent 自动检查引用格式、统计逻辑、代码报错、图表与代码一致性
- 科研价值：大幅降低人工挑错成本，尤其适合准备投稿的论文
- 注意：显著减少错误，但不能 100% 替代人工最终验证

**5. Memory（长期记忆）**
- 位置：顶部或设置中开关
- 核心功能：把论文主题、目标期刊、写作风格偏好存入长期记忆
- 优势：新开对话无需重复提供背景，直接沿用专业语气和上下文

**6. Specialist（专家模式）**
- 位置：下拉菜单（默认 None）
- 核心功能：切换专业角色提示词
- 推荐操作：写统计方法选「统计学家」，讨论分子机制选「分子生物学家」，审稿切 Reviewer

**7. Compute（计算位置）**
- 位置：顶部或设置面板
- 当前选项：Local（本地）
- 核心功能：决定代码运行和数据渲染位置。Local 模式下代码与未发表数据完全本地运行，隐私性最好

## 二、自定义配置中心（Settings）

进入方式：点击左下角或右上角设置入口。

### 第一部分：Capabilities（能力扩展模块）

**1. Skills（技能面板）** — 能力插件市场
- Featured（官方精选）/ Imported（从 GitHub 导入，右侧有 Import from GitHub 按钮）/ Personal（自编专属技能）
- 科研价值：把常用数据分析 pipeline、文献处理流程、图表模板封装成可复用技能
- 操作：搜索 → Add skill，或从 GitHub 一键导入

**2. Connectors（连接器面板）**
- 已默认开通多个学术数据库：bioRxiv、ChEMBL、Clinical Trials、PubMed（蓝色开关 + 对勾）
- 底部 Custom 可连本地服务器/内部数据库
- 科研价值：一站式文献与数据拉取，无需手动切换多个网站

**3. Specialists（专家面板）**
- 内置 Reviewer（审稿人），开启后 AI 以苛刻审稿视角审查内容
- 建议：写完重要章节临时开启审阅，再关闭

**4. Memory（记忆面板）**
- 全局开关 + Clear all；左侧建分类（About you、论文主题等），右侧加具体笔记
- 最佳实践：把目标期刊要求、常用术语表、个人写作偏好存进去

**5. Compute（计算面板）**
- SSH hosts：加自己的服务器/HPC 集群
- Cloud providers：连 Modal（推荐，有赠送算力）
- Model endpoints：连 NVIDIA BioNeMo NIM 等专业科学模型
- 数据安全：原始数据和计算尽量留在本地或自控服务器

**6. Network（网络面板）**
- Package mirror：机构用户可配 Conda / pip 镜像 + CA 证书
- Claude Science domains 白名单：精细控制允许访问的学术域名（Literature & citations 建议开，Genomics & biology 按需）

### 第二部分：Workspace（工作区配置）

**7. Permissions（权限面板）**
- Registry writes（创建/发布 skill/agent 等）+ Local compute（python/bash 调用）
- 注意：Bash 调用权限可绑定到具体 Project，精细控制风险

**8. Credentials（凭据面板）**
- 支持 AWS、GitHub、Google Cloud、Modal、NVIDIA API、Literature access 等一键 Connect
- 建议：常用科研 API 密钥统一管理

**9. Storage（存储面板）**
- 本地数据路径（可 Change location）、磁盘占用（Conda environments 通常最大头）、剩余空间
- 重要：有活跃会话时无法修改路径

**10. Usage（用量面板）**
- Token 消耗分布（Assistant prose、Tool calls、Reviewer 等占比）、最近会话记录
- 可按 24h / 7 days / 30 days 筛选

### 第三部分：General（通用设置）

- Model：Default model + Reasoning effort（科研推荐 High）+ Subagent model
- Licensing：科研用户建议选 Non-commercial use（避免触发开源组件商业授权报错）
- Appearance：字体与主题
- Contact email：填后 AI 访问 NCBI/EBI 等学术网站会自动带上邮箱（部分数据库要求）
- Check for updates：定期检查新版本

## 三、科研用户推荐配置与最佳实践

**推荐默认开启**：Auto-review + Memory + Delegation（复杂任务时）

**高价值组合**：
- Modal（算力）+ NVIDIA BioNeMo（专业模型）
- Reviewer Specialist + Auto-review 双保险
- 常用分析流程做成 Personal Skills
- Literature & citations 域名保持开启

**工作流建议**：
1. 新项目 → 先在 Memory 记录论文主题 + 目标期刊
2. 复杂分析 → 开 Delegation + Notebook
3. 写完章节 → 开 Reviewer + Auto-review 检查
4. 重要结果 → 在 Notebook 确认数值和 provenance
