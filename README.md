<div align="center">

# finance-trading-skill

**一个面向中文金融场景的 Codex Skill**

把“帮我看看这只票”“这个策略能不能回测”“财报有没有变好”这类自然语言问题，拆成可复现的数据、策略、回测和风险报告流程。

[在线展示页](https://qingsuluan-dotcom.github.io/finance-trading-skill/) · [Skill 入口](./SKILL.md) · [策略模板](./references/strategy-templates.md) · [风险边界](./references/risk-and-compliance.md)

</div>

---

## 一句话介绍

它不是自动炒股按钮，也不负责喊单。

它更像一个冷静但手脚很快的投研搭子：先问清楚问题，再找数据，再把假设摊开，最后给你一份能追溯、能复盘、能继续迭代的结果。

---

## 它能做什么

| 能力 | 说明 |
|---|---|
| **投研分析** | 行情强弱、财务质量、估值、公告新闻、行业催化 |
| **策略设计** | 把“双均线 / 动量 / 突破策略”翻译成明确交易规则 |
| **历史回测** | 输出收益、回撤、Sharpe、交易次数、基准对比 |
| **参数扫描** | 看参数稳定区间，而不是只挑历史表现最漂亮的点 |
| **风险检查** | 提示未来函数、幸存者偏差、过拟合、流动性、手续费和滑点 |
| **结果交付** | 生成 Markdown 报告、CSV 数据、图表或可复现 Python 脚本 |

---

## 适合的使用场景

```text
用 $finance-trading-skill 看一下宁德时代最近三个月强不强。
```

```text
用 $finance-trading-skill 回测 300750.SZ 从 2024 到现在的 20/60 日双均线策略。
```

```text
用 $finance-trading-skill 设计一个高 ROE + 动量的 A 股筛选流程，并说明风险。
```

---

## 项目结构

```text
finance-trading-skill/
  SKILL.md
  agents/openai.yaml
  references/
    intent-taxonomy.md
    data-sources.md
    strategy-templates.md
    backtest-rules.md
    risk-and-compliance.md
    report-contract.md
  scripts/
    fetch_market_data.py
    normalize_prices.py
    run_vector_backtest.py
    run_event_backtest.py
    make_tearsheet.py
  index.html
```

---

## 设计思路

这个 Skill 参考了几类成熟做法：

| 来源 | 借鉴点 |
|---|---|
| 同花顺 / 问财 | 中文金融意图拆解 |
| Tushare / AKShare | 结构化金融数据源 |
| VectorBT | 快速向量化回测 |
| Backtrader | 事件驱动回测 |
| Freqtrade | 策略工程化与风控意识 |

核心原则很简单：

> **先把问题说清楚，再让数据说话，最后让风险坐在桌边一起开会。**

---

## 静态展示页

项目里带了一个小展示页：

**[打开在线展示页](https://qingsuluan-dotcom.github.io/finance-trading-skill/)**

GitHub 仓库首页会展示 README；真正的 HTML 页面由 GitHub Pages 渲染。

---

## 安全边界

- 不执行真实交易。
- 不保存券商账号、密码或 API 密钥。
- 不承诺收益。
- 不把历史回测当未来预测。
- 不把“看起来很会涨”包装成投资建议。

---

## 这个项目适合展示什么

这个项目适合作为 **AI Agent / Skill / 金融投研工作流** 方向的作品集雏形。

它的目标不是神秘兮兮地预测市场，而是把金融分析做得更清楚、更可查、更能复盘。
