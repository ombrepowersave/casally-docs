# Mikhail Stal · Demo 反馈 · 2026-01-21

## 受访者画像
- 加州能源用户，自有住宅，太阳能 + 储能 + EV 的成熟玩家。
- 太阳能板品牌为 Hyundai（现代）；电池/储能为特斯拉 Power Wall，且"Power Wall 基本上是管理太阳能板的"——所有太阳能进出、给家供电、余电充电池都由 Power Wall 自动完成。
- 与妻子共用现有 App 的共享功能（"I share with my wife now"）。
- 受加州政策约束：有太阳能就**不允许用电网给电池充电**（grid charge），只有"无太阳能、仅有电池"的用户才可在便宜时段电网充电（此为受访者陈述的政策理解）。
- 已有一套自己的自动化习惯：EV 充电器固定配置在午夜到早上 6 点充电；用一个自动化工具在午夜把 Power Wall 备用储备（backup reserve）设到 50%，早上 6 点再调回 10%，留出的电量供早上热泵（heat pump）取暖使用。
- 现用工具栈：
  - 之前用过 **Enphase**（转录写作 "Nphase"，结合太阳能监测语境推断为 Enphase —— 推断）的太阳能 App，有今天/昨天/一年前的历史对比。
  - 车充电器 App 为 **Emporia**，已有省钱（savings）功能，显示今日充电花费与当月节省额。
  - **NetZero**：约 $8/月的 Power Wall 自动化工具。
  - 当前实际在用的是别人做的一个 **$2/月** 工具（受访者明确表示现在没在用 NetZero），但它"非常基础"，甚至不是 App、只是个网站。
  - 特斯拉 App（Tesla app）：受访者指出它没有历史对比、也没有 savings 功能。

> 转录纠错说明：原文中 "Nphase" 推断为 Enphase（太阳能监测品牌）；多处 "eBay/pig/pick/unpick/peak" 系语音转录把 "peak / on-peak / off-peak（用电峰段）" 听错，本摘要按峰段语义还原。"ad zero / that zero / zero" 指 NetZero。"Tessa" 处访谈者口误问太阳能品牌，受访者纠正为 Hyundai。

## 主题判定
判定为 **Demo 反馈**。依据：全程是受访者在共享屏幕下逐屏（Home/事件/Savings/Profile 及多种 Home 状态卡片）试用 Casally Demo 原型并实时反馈喜欢/困惑/建议，访谈者明确说明"不解释 App，看你自然探索""任何困惑都有帮助"。

## 核心提炼

### 逐功能反应

**Home 顶部提醒条**
- 喜欢：顶部"有事需要你关注"很清楚（"at the top it's pretty clear. It says something requires my attention"）。
- 困惑/建议：从顶部看不出具体是什么，要往下滚才看到"停电警告"。建议把提醒和具体内容放一起，免得往下找（"probably best if it's together, so then I don't have to look further down"）。

**充电状态卡（EV + Power Wall 都在充电）**
- 能看懂是在提示他确保停电期间有电池电量；看到 EV 和 Power Wall 都在充电。
- 困惑：他假设充电来自太阳能，"但不是百分百清楚"（"I assume that's off solar, but it's not 100% clear"）。
- 停电事件措辞：他判断这是**未来**的事件（因为系统提示他提前充电），但措辞像是已发生，建议更新用词/时态（"just the wording or the language... probably needs to be updated"）。

**Savings 卡 / 详情**
- 喜欢图表和"预测能省多少"。
- 对一条 EV 在高价时段充电的记录：看懂了。建议补上具体数字对比，例如"你按 X 美分/度充的，若隔夜只要 Y 美分/度"，让差额一眼可见（"it would be cool if it said like you charged for [X] cents a kilowatt and then gave me a suggestion... overnight, it's only [Y] cents"）。但他随即自我修正："如果我在用这个 App，可能我已经知道了。"
- **强烈喜欢数据来源（data source）展示**："I know it's a prototype, but this is nice like I can see exactly where the data is coming from." 多次重申这增加信任，尤其若能链接到他的电力公司。
- 时间维度请求：希望 Savings 不止"按月"，能切日/周/月/年（"different time frames... not only monthly"）。

**Profile**
- 整体评价很高："Profile looks really good... it has everything I would expect."
- 喜欢：可设电价计划、阈值、通知；**分享功能（sharing）**他特别点出是亮点，"我知道不是所有（同类工具）都有共享能力"。
- 连接设备：能看到车、太阳能、Tesla Power Wall、公用事业公司账户。对数据连接他不担心，"只要安全就行"。但建议每项连接加一小段说明为什么需要这条信息（"why we need this information, like a little piece of text"）。

### Home 多状态卡片（红/黄/蓝紫）的反应
- **红色"EV 高价时段充电"警告**：理解上的**核心卡点**——读完不确定是"我现在正在充电、点 Apply 会停"还是"我的设置允许这段充电、点 Apply 会改设置"两种含义之一（"I'm not totally clear which of the two it is"）。点了之后发现是暂停了当前充电。
  - 对他本人价值有限：他 EV 固定午夜后充，若高价时段充电"是有原因的"（用无法储存的多余太阳能），他自己会知道是自己启动的，几乎不会误充。
  - 但承认对**不熟悉峰段定价的人**是个好提醒。
- **黄色"该给 Power Wall 充电了"建议卡**：颜色与语义不一致信号——黄色让他联想到"caution/警示"，但卡片说"一切正常"，建议这种正向建议改用蓝/绿（"I probably wouldn't do yellow there"）。
  - 内容**不适用于他**：Power Wall 自动充电，他无需选择充电；且加州有太阳能不能电网充电，"我绝不会那么做"。卡片说太阳能多、建议充电池，逻辑上对他不通。
  - 给出更有意义的替代措辞：若"太阳能充足、电池预计下午 4 点充满，建议你用太阳能给车充电"——这样可利用电池存不下的余电。
- **蓝紫色"一切正常"卡**：符合预期，他认为这是"90% 时间会看到"的标准态。

### 事件（Event）列表与详情
- 优先级（受访者主动排序）：**停电（power outage）最重要**（没电池就没电）→ **恶劣天气（severe weather）**（可能引发停电）→ **太阳能设备故障（solar device breakdown）**。后两项之后是 Power Wall 高价充电、EV 充电，"知道了挺好，但不是关键"。
- **标签纠正请求**：太阳能设备故障当前标为 "unusual"，他认为应标为 "critical"（"if my solar panels don't work, then I need to know what's going on"）。
- 太阳能故障详情页（"无太阳能产生 / 系统故障 / 请检查面板和设备"）：看得懂、合理，但他说自己未必能自修、可能要叫安装方来修；对这个事件他不期待 App 给出修复动作。
- **行动按钮（call to action）请求**：
  - EV 高价充电事件：希望有"更改/调整日程（change/adjust schedule）"按钮。
  - Power Wall 高价充电事件：希望有"停止充电 / 只在便宜时段充电"动作。
  - 停电事件：若提示"把电池储备调高"会很好。
  - 天气事件：不期待修复动作。
- 事件页整体评价："this page looks good"，是不错的历史记录，可逐条展开看更多信息。

### 首次理解 / 价值认知
- 整体一眼能用：多数界面"pretty clear / looks good"。
- **最大 aha 点是"预测性通知（predictive notifications）"**，他主动反复强调这是全 App 最好的部分，且"以前没在别的应用见过"。

### 与现状对比
- 太阳能历史对比：Enphase（推断）有"今天/昨天/一年前"对比，特斯拉没有；希望 Casally 加"一年前"对比，便于看面板是否衰减/变脏。
- Savings：Emporia 已有类似功能但只给数字、无此类图表；特斯拉无。
- 自动化：现用 $2/月网站工具做储备时移，"非常基础"。NetZero $8/月。Casally 若把日志、节省、共享、天气预测、通知、设备互联整合起来，是切换的好理由（"that makes it a better reason to switch"）。

### 功能请求 / 改进建议（受访者主动提出）
1. **基于天气的预测自动化（最想要）**：
   - 预报多日下雨/无太阳能时，建议或自动把 backup reserve 调到 100%，留电给峰段（加州 4–9 PM 最贵）。
   - 预报晴天、电池预计某点充满时，提示/自动用多余太阳能给 EV 充电。对这类他甚至愿接受推送通知。
2. **自动化整个储备时移**：把他现在手动/第三方做的"午夜调 50%、早 6 点回 10%"自动化。
3. EV 续航/行程提醒：若隔夜非峰段充电达不到目标续航（如要跑 100 英里/公路旅行），提示提前开始充电。
4. Savings 多时间维度（日/周/月/年）。
5. data source 链接到电力公司以增强信任。
6. 一年前历史对比。
7. 各数据连接项加"为什么需要"说明文案。
8. 可能的话：可选的环保指标（抵消多少碳/相当于多少棵树）——他本人视为"feel-good nice-to-have"，明确说自己只看省钱数字就够，强调有些人更在意环保。
9. 颜色语义修正（正向建议不用黄色）；提醒条与内容合并；故障标签升级为 critical。

### 可用性问题 / 卡点
- 红色 EV 充电卡两种含义不清（最明显的卡点）。
- 充电是否来自太阳能不明确。
- 黄色卡颜色与"一切正常"语义冲突。
- 停电提醒措辞像已发生而非未来。

### "单卡"取舍（被问到 Home 只能放一张卡）
- 想看**太阳能 + 电池的状态**："am I getting energy? Am I saving energy? Am I using energy?"——他认为这是最重要的。
- 但被问要不要"只显示一个结论 vs 显示所有事件"时，他选**想看到全部**（影响未来 24–72 小时的建议都放 Home，宁可下滑也不想去找"怎么改我的用电"），然后由他决定是否 Apply。
- 认同 Home 平时安静、有事才显现（"that's totally fine... 90% of the time" 是正常态）。

### 实时 vs 报告
- Home 要**实时**（"I need to manage my day-to-day electricity usage more. That's more important"）。
- 月报/周报"nice to see"，但通过通知或 Savings 卡里"查看报告"入口即可。

### 信任自动化的条件
- 看到建议"为我着想"、确实在省钱即可信任；带上"预计能省多少"更好。
- 顶部"estimated savings"实时显示有帮助，能看到 App 真的在帮他省。
- 详情日志（log，显示何时改了储备/充电及原因）是 nice-to-have、非首版必需。

## 购买 / 付费意愿信号（关键）
- **整体偏正向、但有明确条件，且对价格敏感**。
- 价格锚点：现用 $2/月基础工具（确定能回本）；NetZero $8/月——他批评 NetZero"没有证据证明真能省那笔钱……为什么要为不确定的东西一年付近 $100？"
- **核心付费条件 = 可验证的、超过订阅费的净节省**："if you can prove that the savings... is higher than whatever you're charging... that is the level of proof that I need." 举例：App $5/月，证明省了 $10，"净省 $5，虽小，但只要我什么都不用做，就依然值得"。
- 试用预期：默认会有 30 天免费试用；试用期内希望**每周**看到"本周因自动化省了 $X"以促成续订；后期可转月度。
- 价值对比框架（被问）：相对"无自动化基线"的省钱更有说服力。
- "光是自动储备时移、再也不用想"是否值得付费？答：**值得**（"that would be worth it, I think"）。
- 切换动机：现用工具太基础（只是网站），Casally 若功能更全且设备全打通，是切换理由。
- 激励文案偏好：纯省钱数字即可；环保指标对他非必需。

### 不一致 / 需留意的信号
- **"嘴上喜欢、对自己价值有限"**：他对 Home 上的红/黄充电类提醒多次说"对我本人不太适用"（自己已有自动化、EV 固定夜充、加州不能电网充电），认为这些主要利好"不熟悉峰段的人"。即他的真实付费驱动来自**天气预测 + 全自动储备时移 + 可验证净省**，而非这些基础提醒。
- 对省钱数字一边说"cool/想要具体差额"，一边自我修正"用这 App 的人可能早就知道了"——对教育型信息的需求弱于对自动执行的需求。
- 多次强调"以前没在别的 App 见过"预测能力，但也半信半疑别人能否做到（"may be too difficult... I don't really believe it"），暗示对 Casally 能否兑现预测承诺存疑——这是付费的关键门槛。

## 关键金句
- "the best thing is the predictive notifications... if it can predict the weather, tell me to set my backup reserve higher. Um, if it can predict that there's a lot of solar, tell me I should charge my car... I have not seen that from another application before." —— Mikhail Stal
- "I'm not totally clear which of the two it is." —— Mikhail Stal（红色 EV 充电卡含义不清）
- "if you can prove that the savings you're going to generate from the app is higher than whatever you're charging... that is the level of proof that I need." —— Mikhail Stal
- "NetZero charges $8 a month, but they have no proof that I'm actually going to save that money... why should I pay them almost $100 a year for something that I don't know?" —— Mikhail Stal
- "if I don't have to do anything, then it's still worth it." —— Mikhail Stal（净省 $5 也值，前提是零操作）
- "I can see exactly where the data is coming from." —— Mikhail Stal（data source 增强信任）
- "I would want to see the status of my solar in battery. So, am I getting energy? Am I saving energy? Am I using energy?" —— Mikhail Stal（单卡首选）
- "this is what I would expect to see 90% of the time." —— Mikhail Stal（正常态 Home）
- "I probably wouldn't do yellow there." —— Mikhail Stal（颜色语义）
- "solar device breakdown... I would put this as critical. It says unusual right now." —— Mikhail Stal

## 行动项 / 机会点
- **主打天气驱动的预测性自动化**（雨天提前抬高 backup reserve；晴天用余电充 EV），这是受访者眼中的最大差异化卖点、也是付费驱动。
- **可验证净节省**：用"无自动化基线"对比，试用期每周推送"本周省了 $X"，并在 Home 顶部实时显示 estimated savings；定价需让证明的省额明显高于订阅费（参考竞品 $2/$8 锚点）。
- 修复红色 EV 充电卡的二义性（明确"现在正在充/点 Apply 会停" vs "改设置"），并标明充电来源是否太阳能。
- 颜色语义：正向建议改用蓝/绿，黄色留给真正的警示。
- 事件标签：太阳能故障升级为 critical；为各事件加合适的行动按钮（调日程/停充/只在便宜时段充/抬高储备），天气与不可自修事件除外。
- Savings 增加日/周/月/年切换；data source 链接到电力公司；加"一年前"历史对比。
- Home 提醒条与具体内容合并；停电提醒措辞改为面向未来。
- 数据连接项加"为什么需要此信息"说明，提升信任与转化。
- 注意加州"有太阳能不可电网充电池"的政策约束，避免给此类用户推送"充电池"类建议。
