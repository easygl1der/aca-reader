---
name: polymarket-data-collector
description: 采集 Polymarket 气温预测市场数据并生成统一报告。运行后会：1) 生成 Polymarket 市场链接 2) 加载市场实时数据 3) 获取天气预报 4) 生成 Markdown 报告到 Obsidian。使用场景：用户想要获取当日气温交易数据汇总。
---

# Polymarket 气温数据采集

整合数据采集到一个命令：
1. 生成 Polymarket 市场链接 (未来3天)
2. 加载市场实时数据 (从 JSON 缓存优先，Markdown 回退)
3. 爬取天气实时数据 (Open-Meteo API)
4. 生成统一 Markdown 报告

## 使用方式

```bash
cd /Users/yueyh/.openclaw-polymarket/weather-trader

# 1. 解析 Firecrawl 数据为结构化 JSON
python parse_market_data_v2.py

# 2. 生成新格式市场报告
python generate_market_report.py

# 或运行完整流程
python collect_all_data.py
```

或使用 `/polymarket-data-collector` 命令调用此 skill。

## 数据流程

```
Firecrawl 爬取 → .firecrawl/pm-*.md (原始混乱)
                      ↓
parse_market_data_v2.py → .market_cache/*.json (结构化)
                      ↓
generate_market_report.py → Obsidian Markdown
```

## 输出文件

| 文件 | 位置 |
|------|------|
| Polymarket 链接 | `weather-trader/polymarket_links.md` |
| 市场数据 JSON | `weather-trader/.market_cache/*.json` |
| 天气数据 | `weather-trader/weather_forecast.json` |
| 市场情况报告 | `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-spring/polymarket/Forecasting/YYYY-MM-DD/YYYY-MM-DD_HHMMSS_market_situation.md` |

## 报告格式规范

### 文件命名

- 目录：`Forecasting/YYYY-MM-DD/`
- 文件名：`YYYY-MM-DD_HHMMSS_market_situation.md`
- 示例：`2026-03-11/2026-03-11_235159_market_situation.md`

### Markdown 结构

```markdown
# 气温交易数据汇总 - 2026-03-11

> 生成时间: 2026-03-11 23:51:59

---

## 市场情况

### 纽约 (NYC)

**当地时间**: 2026-03-11 11:51
**北京时间**: 2026-03-11 23:51

- [Polymarket 市场](https://polymarket.com/event/...)
- [天气预报](https://www.wunderground.com/history/...)

#### 小时气温预报

| 时间 | 温度 |
|------|------|
| 00:00 | 66°F |
| 01:00 | 65°F |
| 02:00 | 65°F |
... (每小时，共24行)

#### 市场预测

**总成交量: $52,910**

| 温度区间 | 概率 | 价格 |
|----------|------|------|
| 56°F↑ | 94.0% | $0.940 |
| 41°F↓ | 1.0% | $0.010 |
... (所有温度区间，通常9个)
```

### 城市顺序

按 config.py 中的顺序：
1. 纽约 (NYC)
2. 芝加哥
3. 亚特兰大
4. 达拉斯
5. 西雅图
6. 伦敦
7. 巴黎
8. 首尔

### 字段说明

| 字段 | 说明 | 示例 |
|------|------|------|
| 当地时间 | 城市所在时区当前时间 | 2026-03-11 11:51 |
| 北京时间 | Asia/Shanghai 时区 | 2026-03-11 23:51 |
| Polymarket 市场 | 预测市场链接 | https://polymarket.com/event/... |
| 天气预报 | Weather Underground 链接 | https://www.wunderground.com/history/... |
| 小时气温预报 | Open-Meteo API 获取的逐小时预报 | 每行：时间 + 温度(°F) |
| 市场预测 | Polymarket 市场的完整温度选项 | 温度区间 + 概率 + 价格 |

### 数据源

| 数据 | 来源 | 文件 |
|------|------|------|
| 市场数据 | .market_cache/*.json (结构化) | 解析自 .firecrawl/*.md |
| 天气数据 | weather_forecast.json | Open-Meteo API |
| 时间信息 | config.py (timezone) | pytz 计算 |
| 链接生成 | config.py (polymarket_slug, wunderground_station) | 动态生成 |

## 更新数据流程

需要更新市场数据时：

```bash
# 1. 用 Firecrawl 重新爬取原始数据
firecrawl crawl https://polymarket.com/event/... -o .firecrawl/

# 2. 解析为结构化 JSON（重要：使用 v2 版本）
python parse_market_data_v2.py

# 3. 生成市场报告
python generate_market_report.py

# 4. 运行完整采集（包含天气预报更新）
python collect_all_data.py
```

## 注意事项

- 市场数据必须使用 `.market_cache/*.json`，不能直接用 `.firecrawl/*.md`
- 必须使用 `parse_market_data_v2.py` 解析，v1 版本不完整
- 小时预报必须显示**每小时**（24行），不能只显示每3小时
- 市场预测必须包含**所有温度区间**（通常9个），不能遗漏
- 报告文件名必须包含 `_market_situation` 后缀

## 城市配置

8个城市，配置文件：`config.py`

| 城市 | 英文 | 时区 | Polymarket Slug |
|------|------|------|-----------------|
| 纽约 | New York | America/New_York | nyc |
| 芝加哥 | Chicago | America/Chicago | chicago |
| 亚特兰大 | Atlanta | America/New_York | atlanta |
| 达拉斯 | Dallas | America/Chicago | dallas |
| 西雅图 | Seattle | America/Los_Angeles | seattle |
| 伦敦 | London | Europe/London | london |
| 巴黎 | Paris | Europe/Paris | paris |
| 首尔 | Seoul | Asia/Seoul | seoul |
