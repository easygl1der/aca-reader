---
name: weather-collector
description: 采集城市气温预报数据（完整24小时）。使用 Open-Meteo API 获取不受时区影响的完整预报数据，自动保存到 Obsidian。
---

# Weather Collector - 完整版

## 使用方式

```bash
cd /Users/yueyh/.openclaw/weather-collector

# 采集今天的数据（输出到 Obsidian）
python collect_wunderground_v2.py

# 采集指定日期
python collect_wunderground_v2.py --date 2026-03-14

# 指定输出到其他位置
python collect_wunderground_v2.py --date 2026-03-14 --output ~/Desktop/weather.md
```

## 支持的城市

8个城市：
- New York
- Chicago
- Atlanta
- Dallas
- Seattle
- London
- Paris
- Seoul

## 输出位置

| 类型 | 位置 |
|------|------|
| **Markdown 报告** | `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/2026-spring/polymarket/Forecasting/{date}_weather_forecast.md` |
| 原始 JSON 缓存 | `/Users/yueyh/.openclaw/weather-collector/.firecrawl/` |

## 示例

```bash
# 采集明天的预报
python collect_wunderground_v2.py --date 2026-03-14
# 输出: Forecasting/2026-03-14_weather_forecast.md

# 采集今天的数据
python collect_wunderground_v2.py
# 输出: Forecasting/2026-03-13_weather_forecast.md
```
