# 截图对应表（image1–17）

> 按 `original.docx` 正文里 [图] 出现的先后顺序推断，写章前需对着 `original.docx` 原文再核一遍（图与文的精确绑定以 docx 为准）。

| 文件 | 推断对应内容 |
|---|---|
| image1.png | 主界面总览（「claude是什么」节，占位，写章时改成布局导览用图） |
| image2.png | 顶部核心状态栏全景（功能指示器） |
| image3.png | Active Subagents / 状态栏细节 |
| image4.png | 设置中心（Settings）总览 |
| image5.png | Skills 技能面板 |
| image6.png | Connectors 连接器面板（bioRxiv/PubMed 等） |
| image7.png | Specialists 专家面板（Reviewer） |
| image8.png | Memory 记忆面板 |
| image9.png | Compute 计算面板（SSH/Modal/BioNeMo） |
| image10.png | Network 网络面板（Package mirror） |
| image11.png | Network 域名白名单（Claude Science domains） |
| image12.png | Permissions 权限面板 |
| image13.png | Credentials 凭据面板 |
| image14.png | Storage 存储面板（磁盘占用） |
| image15.png | Usage 用量面板（Token 去向环形图） |
| image16.png | General 通用设置（Account/Model/Licensing） |
| image17.png | General 续（Appearance/Contact email/About/版本） |

## 隐私提醒（发布前处理）

原始截图里可能含吕博个人环境信息，发布/上传前逐张核：
- image16/17：Account 区（账号、套餐、Manage billing、组织 ID）
- image12：Permissions 里出现真实项目名
- Usage 面板：会话历史、模型名
- 任何邮箱、路径、密钥字样

公众号/小红书用图前，敏感字段打码或替换成示意图。

---

## 隐私决定（2026-07-15 吕博拍板）

- 图 5-1（fig-home-projects）、图 5-2（fig-workspace-3col）含真实课题名（工业瑕疵/DINOv3）。
- **个人出版/分享：不打码，用真名录着**。
- **正式出版：再统一打码**（工业瑕疵双向转换、DINOv3 Projector 相关项目名）。

## 已完成脱敏（2026-07-15，入公开仓库前）

绿皮书仓库是 **PUBLIC**，入库前对以下项做了替换（原始信息不再存在于任何副本）：

| 文件 | 原内容 | 替换为 |
|---|---|---|
| `fig6-1-entry.png` | 订阅邮箱（真实邮箱） | `your@email.com` |
| `fig6-1-entry.png` | 套餐 `Max plan` | `Your plan` |
| `image16.png` | 账号（本地占位账号） | `your@email.com` |
| `image16.png` | 套餐 `Max plan` | `Your plan` |
| `image12.png` / `fig6-9-permissions.png` | 真实项目名 ×3 | `Project: demo` ×3 |
| `image14.png` / `fig6-11-storage.png` | 手涂黑的本地数据路径 | `D:\ClaudeScience\data` |

**逐张体检结论**：image1–11、13、15、17 无需处理。image15（Usage）里的会话名「Claude Science 功能介绍」「自动化科研助手综述调查」是选题名而非隐私，保留。image16 的 Organization ID 是 `org_byok_000000000000`（全零占位），非真实 ID，保留。

**规矩**：以后新增截图入库前，对着上面这张表过一遍。
