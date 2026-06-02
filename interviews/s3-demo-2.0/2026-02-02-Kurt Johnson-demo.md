# Kurt Johnson · Demo 反馈 · 2026-02-02

## 受访者画像
- 家庭住户，有太阳能 + 电池（访谈中提到 solar、battery/power wall）+ EV（Tesla）。具体住房/家庭/地区细节未说明。
- 现状用电习惯：白天尽量把高耗电活动堆到中午、靠太阳能"live off solar"；**没有电池时**（推断指访谈者复述的此前状态）一旦太阳能产出下降，家里"basically have no choice but to go back to the grid"。
- 难点场景：晚上 AC、EV 充电、加上孩子，傍晚的用电管理很难。原文转录为 "TRA charging"/"Tesla"，此处理解为 Tesla/EV 充电。
- 偏好（访谈开场确认）：当被问"想要自动帮你关设备的 app，还是清楚告诉你该怎么做、由你决定"时，明确选后者——"I'd go with the latter"。被问晚上变贵时最难的是"不知道何时切到电网"还是"不知道什么最费钱"，答"both"。

> 注意：本次访谈受访者全程因笔记本故障改用手机接入、网络多次掉线，且**始终是访谈者 Amber 共享屏幕、逐项讲解功能**，受访者主要是听讲后给出回应，而非自己自由探索点击。因此"逐功能反应"多为对讲解的认同，主动探索/卡点信号较弱，评价偏笼统正面，需打折看待。

## 主题判定
判定为 **Demo 反馈**。依据：位于 `s3-demo-2.0` 目录；正文是访谈者展示 Casally Demo 2.0 的多个界面（旧版 attention/suggestion/normal 三态 + 新版 new home、saving 页、bill 页、bill proof 页），逐屏征求受访者反应、改进建议与付费意愿。

## 核心提炼

### 测试形式（影响信号可信度）
- 访谈者准备了对照：左侧 flows 列表里 "new home" 是新方向，另有三个旧版（attention 红、suggestion 黄、normal 蓝）代表不同状态，原计划让受访者先自己点几分钟再一起过。但因受访者设备/网络问题，实际几乎全程由访谈者讲解、受访者回应。

### 逐功能反应

**Overpay risk + primary driver（旧版 attention 红）**
- 受访者认为有用："once you click on that ... overpay risk, it gives you that idea of knowing what to do and ... gives you an analysis of what really the problem is and how to move on."
- 第一眼反应是"有件事被提到我面前、需要我打开 app 去了解我该做什么"——即把它理解为一个待办/警示触发器。
- 访谈者澄清这是"风险/可能多付的预估额外成本敞口（extra cost exposure）"而非节省；受访者表示理解并认可。

**Monthly bill budget（月账单预算）**
- 这是访谈者重点解释的差异化设计：不是"把账单压到最低"的优化目标，而是一个**容忍边界**——用户设定"超过这个数就觉得不对/想要预警"。
- 受访者反应正面，认为"incredible option"，并把它理解为"relies more on savings"且"gives the client a proper plan on how to plan for their usage on a monthly basis"。
- （不一致信号）受访者说它"relies more on savings"，但访谈者反复强调这**不是**节省目标而是无意外账单的边界；受访者似乎仍把它部分理解成省钱工具，理解与设计意图存在偏差。

**Suggestion card（建议卡）+ Apply plan（人在环中控制）**
- 访谈者强调"apply"不会在后台改 Tesla/EV 设置，点了之后会把用户带到 Tesla（或其车）端自行确认，用户"stay totally in control"。
- 受访者明确认同这点："the app is just like a trigger ... It does not do away with the human control." 与他开场选"告诉我怎么做、我来决定"的偏好一致。

**Event page（事件页 / ledger）**
- "Review all" 进入事件页，记录所有发生过的事件（如高价时段 EV 充电），点进去给出 what happened / why it matters / how impact / 计算明细。
- 访谈者目标是避免被当成"black box"。受访者认可这种"触发→点进去了解某个警示→给建议+分析为什么发生/影响多大"的设计，称能给用户"peace of mind"。

**Power outage warning / Device（设备在线）/ Usage**
- 访谈者讲解这几张卡：停电预警属"可靠性"非账单；device 卡帮用户发现 solar 离线/故障；usage 卡对比今日与平均用量。受访者未对这几项单独深入评价。

**新版 new home（重点对比）**
- 访谈者列出新版改动：① 设备状态前置（顶部三个小图标：solar 在线、power wall 电量提醒）；② monthly bill budget 带"已达成 achieved"且置于首屏最上；③ suggestion card 增加 automatic / manual 两种——manual 去 Tesla 设置自己改，automatic 由 Casally 端代为执行。
- 受访者评价新版"a lot of improvements ... user interface is actually structured ... it is more of this now but with a lot of improvements"。
- 最被认可的点：**首屏信息密度高、一站式**。"I'm able to get almost everything from the homepage." 强调把 monthly bill budget 放首屏第一个、能直接看到达成度（提到 over 50% / "64 60%"，具体数字受访者口述不清），让用户"don't have to navigate through all the options"，"everything under one roof, all under one tab"，称这是"very commendable improvement"。

**Saving 页（风险/证明，而非省钱报告）**
- 访谈者强调这不是"save money report"而是"risk and proof letter"：顶部分 saving 与 bill 两 tab；saving 是 Casally 侧从用户行为+时机检测的成本风险（如示例 $56 是当前计费周期的额外成本敞口），图表看风险敞口随时间变好还是变坏；下方按 EV/solar/power wall 分类做 risk ledger，每行显示该计费周期内发生次数和估算额外成本（示例 EV 出现 4 次=4 个事件），点 detail 出 bottom sheet 给 what/why/how 计算/下一步。
- **受访者的核心疑问（重要卡点信号）**："how at risk cost is calculated." 这是他主动提出的第一个、也是唯一明确的困惑点——不理解"风险成本"怎么算出来的。访谈者解释是逐事件相加（sum of each event extra cost）、按 kWh × peak/off-peak rate 等，受访者听后说"I get it now"。

**Bill 页 + True up + Bill proof**
- bill tab：通过连接用户公用事业账户拿到真实月账单展示；下滑有 true up，下含三个 top drivers（对账单影响最大的因素）。
- bill proof 页：逐项核对账单上能识别的几条（solar/EV/battery 相关）与 Casally 检测的预期是否吻合，类比"在超市核对小票"——不是说整张账单错，只挑能清楚识别的几项问"这看起来对吗"，差额只是"值得复核"，不等于被多收。受访者认可，理解为 app 收集"预期 vs 实际账单"，示例里实际账单低于预期、相当于省了钱。

### 功能请求 / 改进建议（受访者主动提出）
1. **周用量视图**：usage 现有 hourly/daily/monthly，建议加 **weekly**——"maybe on a particular week the usage was higher"；但他自己也说不太关键、可有可无。
2. **月账单按周拆分**：在 monthly bill 上把 week 1/2/3/4 分别列出再汇总，让用户看到"哪一周用量/花费高、哪周导致超支或哪周省得多"。访谈者归纳为"breakdown"，受访者确认。
3. **首屏加 Help 按钮 / 用户指南**：他注意到首屏顶部一个图标是 notification 而非 help，问 help 在哪（被告知在 profile/旧版有）。建议在 homepage 加 help 图标 + 新手"how to navigate"的用户指南，方便没用过 app 的新用户。

### 首次理解 / 价值认知
- 总体看懂了产品在干嘛：把警示/分析/建议/账单证明整合到一处，像"个人能源管家"。受访者称看到"some really cool features"，新版让他对界面结构更满意。
- aha 点更多落在"首屏一站式 + 月预算达成度可见"和"每个警示都能点进去看为什么/影响多大"。
- 未完全 get 到的地方：月预算"边界而非省钱目标"的定位（见上不一致信号）；以及风险成本如何计算（经解释后才懂）。

### 与现状对比
- 受访者把 app 描述为"a shadow of what I would really like do manually"——即它替代/复刻了他本来想手动做的事，相当于一个"personal guide"。未提及具体在用的其他工具，也未明确"会不会从某工具切换"。

### 购买 / 付费意愿信号
- 明确正向："it is worth paying because it is like a shadow of what I would really like do manually ... it does solve many of my problems as a user. So I don't see why I shouldn't pay for it."
- 但**未给出任何价格、金额、付费门槛或具体条件**——属于笼统的"愿意付费"表态，缺乏价格敏感度数据。
- （不一致/可信度提示）付费意愿的论证中夹带"the developers and people behind it also did get paid ... I don't see why I wouldn't pay for it"，更像对开发方的礼貌性背书，而非基于自身价值算账的强购买信号。结合全程改用手机听讲、评价偏概括正面，付费意愿宜按"温和正向但未验证价格"看待。
- 受访者同意上线后做早期试用用户。

## 关键金句
- "I think it's useful because ... once you click on that ... overpay risk, it gives you that idea of knowing what to do and ... gives you an analysis of what really the problem is and how to move on." —— Kurt Johnson
- "I think it's an incredible option ... it relies more on savings and also gives the client a proper plan on how to plan for their usage on a monthly basis." —— Kurt Johnson
- "The app is just like a trigger ... It does not do away with the human control." —— Kurt Johnson
- "I'm able to get almost everything from the homepage ... everything under one roof, all under one tab kind of thing." —— Kurt Johnson
- "My question would be how at risk cost is calculated." —— Kurt Johnson
- "Maybe just a weekly usage can be added ... maybe on a particular week the usage was higher." —— Kurt Johnson
- "Add maybe a help button and maybe a user guide on how to navigate through the app." —— Kurt Johnson
- "It is worth paying because it is like a shadow of what I would really like do manually ... I don't see why I shouldn't pay for it." —— Kurt Johnson

## 行动项 / 机会点
- **解释"风险成本怎么算"是关键信任点**：这是受访者唯一主动提出的困惑。即便有 bottom sheet 明细，定义/算法的可见性仍不够直觉，值得在 saving 页更前置地展示计算逻辑。
- **月账单预算的定位需要更强的界面表达**：受访者把"容忍边界"误读成"省钱目标"。说明仅靠口头/文案讲解不够，需在 UI 上更明确区分"边界/预警"与"节省"。
- **采纳低成本改进**：① usage 加 weekly 视图；② monthly bill 按周（week 1–4）拆分再汇总，标出高用量/超支周；③ 首屏增加 help 图标 + 新手导览。
- **付费意愿数据缺口**：本次只拿到笼统"愿意付费"，未触及价格点/付费门槛；后续访谈应主动追问愿付金额与触发购买的条件。
- **信号可信度打折**：受访者全程手机听讲、未自主探索、网络多次掉线、评价偏概括正面且夹带对团队的礼貌性背书；其"易用/有用/愿付"结论缺乏行为佐证，建议邀其上线后真实试用以验证。
