# 绿皮书连载 · 配图设计规范 v1.0

> 2026-07-07 吕博定：所有配图延续 Day 1 视觉风格，尺寸字体统一按本规范。
> 生产方式：HTML 模板 → 无头 Chrome 截图（零错字）；插画类走 stepfun（无文字防错字）。

## 一、系列封面（每期第一张，"台标"）

| 项 | 标准 |
|---|---|
| 尺寸 | **1024 × 1024 正方形** |
| 背景 | 纯绿 `#2E6B4B` |
| 字体 | **圆体 "Yuanti SC"**，白色，加粗 |
| 三行文字 | ① `Claude Science`（92px）② `绿皮书`（150px）③ `NN · 本期短题`（62px，如 "02 · 它的助手 CSA"） |
| 画芯 | **固定星空图** `articles/assets/starry-art.png`（源：Day 1 封面裁切，全系列同一张，圆角 36px，宽 904px） |
| 模板 | `articles/assets/templates/d2-cover.html`（改第③行文字即出新一期） |
| 铁律 | 只换编号和短题，其余像素不动；它是标志，不塞信息 |

## 二、信息卡（对比卡/证据卡/流程卡）

| 项 | 标准 |
|---|---|
| 宽度 | 1000px，高度按内容 400-780px，**排满不留大白** |
| 背景 | 浅绿纸 `#F2F7F3`，卡片白/深绿 `#215E41`，强调黄 `#E9C63F`，警示红底 `#F7E9E6` |
| 字体 | 标题 "Songti SC"（26-32px），正文 "PingFang SC"（17-22px） |
| 出处 | 涉及事实/数字的卡，右下角灰字标"依据…整理 · 查证于日期"，非截图要注明"非界面截图" |
| 敏感词 | 上卡前过一遍：中转（站）、翻墙、VPN、破解 等一律替换 |

## 三、真实素材

- 官方页面/仓库截图 > 生成图（能实拍就实拍）
- 仓库截图前检查侧边栏状态（Release/Contributors）再拍
- 插画（吉祥物绿机器人等）用 stepfun，prompt 注明"画面无任何文字"

## 四、产线命令

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless --disable-gpu --no-proxy-server \
  --screenshot=输出.png --window-size=宽,高 --hide-scrollbars "file://模板.html"
```
