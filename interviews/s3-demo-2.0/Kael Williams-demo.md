# Kael Williams · Demo 反馈 · 日期未知

## 受访者画像
逐字稿未直接说明 Kael 的住房、家庭、地区等个人背景信息（未说明）。从他点评 demo 时反复使用 "we"、并具体讨论 EV 充电、太阳能、电池等场景，可推断他家中（或其设想的目标用户家庭）有相关设备配置（推断）。demo 中涉及的设备示例包括：Tesla Model 3（EV）、太阳能（solar）、Powerwall/电池（power wall / battery）。访谈以共创（co-building）口吻结束，Amber 邀请他加入真实使用的小组并测试，Kael 明确表示愿意参与。

> 注：本访谈大量内容是 Amber Fu 在逐屏讲解 demo 功能、Kael 边看边复述/确认理解，需注意区分"访谈者引导话术"与"受访者真实反应"。下面只提炼 Kael 本人的反应与判断。

## 主题判定
判定为 Demo 反馈。依据：通篇为受访者实操点击 Casally Demo 2.0 应用、逐功能给出理解与评价（首页 overpay risk / primary driver / monthly bill budget、Saving 页、Bill proof 账单核对页、top drivers 图表、与上一版 demo 的对比、付费意愿等），符合 s3-demo-2.0 目录定位。

## 核心提炼

### 逐功能反应

**首页拖动百分比（疑似某滑块/百分比控件）—— 卡点**
- Kael 一上来就试图拖动某个控件去设定他想要的百分比，但拖不动："I think this one should be I should be able to drag this towards the percentage I want. Yeah, I don't see it working. It's actually not working. I don't know where the problem is."
- Amber 解释该功能当前只是 UI 展示、非真实可交互。这是 Kael 进入 demo 后第一个、也是唯一一个明显的可用性卡点。

**Overpay risk（超额支付风险，$12）—— 理解正确，评价正面**
- Kael 能自行正确解读含义：当月预算 170，overpay 12 即本月可能付到约 182，是超出预算的额外部分。
- 认为有用，理由是它是行为改变的驱动力："they're useful actually because opening the app and seeing that on your screen that really tells you it is a it is a driver on what you should do the next conservation."（"conservation" 疑为口误，结合上下文应指"节能/下一步省钱动作"，推断）
- 主动举例说明若数字涨到 50 会促使他改变用电模式，如调整白天给 EV 充电的时机、不用时不充电。

**Primary driver（主要驱动因素）—— 理解正确**
- 自行解读为"让预算冲高的主因，是 overpay risk 的促成因素"，理解与产品意图一致。

**Monthly bill budget（月度账单预算）—— 认可概念，但明确反对放首页（重点反馈）**
- 概念上认可："I think it is a good one... very important in planning how to spend through the month"，认为有了上限、超限会收到改习惯的通知，对规划当月支出有帮助。
- 但反复、明确地表达：这是每月只设一次的东西，不该放在首页。"being that it is something that you said once a month... maybe it is not necessary on the home screen." 对比 overpay risk 是每次都在变的，所以"we don't need to be reminded about the budget every time we see you open the app. So... we can place somewhere else there not necessarily on the home screen."
- 后续被追问"30 天内只修一件事修哪个"时，他给出的答案正是：把 monthly bill budget 从首页移走、放到 profile/settings 里去设置。说明这是他全程最强的一条改进诉求。

**Tesla 集成 / Apply plan 确认流（交接给 Tesla App 确认）—— 正面，认可"先确认再执行"**
- 认为与 Tesla 集成让它"work well"，因为执行前必须在 Tesla 端确认，能避免误改计划："you have to make a confirmation from Tesla before actually... you can say it is a mistake that you change your plans."
- 被问是否想要"自动应用模式"时，明确倾向保留确认步骤："getting that confirmation before proceeding" 是个不错的计划。
- 主动指出一个潜在问题（功能性顾虑）：通知可在多个家庭成员间接收，但若收到通知的人没有 Tesla 访问权限，就无法执行更改——"that is the only problem we can have in this case."

**Saving 页（saving 与 bills 拆分；$56 风险敞口）—— 接受拆分，理解经引导后修正**
- 认可把 saving 和 bills 拆成两块："there's no problem separating the two... now we can see what you're saving and at the same time you can see what you're expected to pay."
- 对 $56：他最初理解为"按建议改习惯后可省下最多 $56"（理解偏差），Amber 纠正说这是"风险成本/风险敞口（risk exposure），不是 saving"。这是一个理解卡点信号：数字默认被读成"能省多少"，而非"再不改会多花多少"。
- 对风险趋势图（chart 显示风险敞口随时间变好/变坏）能正确理解，并自行举例"上月 186、本月 56，习惯有改善"（数字为他即兴举例）。

**Risk ledger / 事件明细（按 EV、solar、power wall 分类，逐事件记录）—— 理解正确，评价完整**
- 看到 "Tesla model 3 + charging during peak hour" 时主动确认这是"实际发生的描述"还是"建议"，Amber 确认是实际发生的事件记录。
- 对单事件详情（发生了什么 + 影响 + 如何计算 + what to do next 建议）评价为完整、有用："this is useful because you know the event and the impact it brought and how it brought it. Then you're also given a suggestion on what to do. So I think it is complete."

**Bill proof / 账单核对页（左：设备数据推算的预期；右：实际账单）—— 概念认可，但被 demo 里夸张差额绊住（重要不一致信号）**
- 看懂了对比逻辑，并自行点出 demo 数据里的关键驱动：预期费率 0.31、实际 0.83，差近三倍；以及太阳能出口预期 512、实际 200，差 12 kWh。
- 但对差额过大表达明显不安："this number seems quite big... that could be a big miscalculation for a month." 进而："I would not... it would be very difficult to go with it if the difference is this big... we should not be expecting such a big discrepancy."
- Amber 解释这是 demo 故意放大的差额，用于测试用户是否理解"在比什么/为何有差"，并强调真实场景差额不会这么大、且刻意不标成"错误/多收费"。
- 信号：Kael 嘴上接受"idea is good"，但被夸大的差额数字实际动摇了对该功能的信任，多次回到"差距太大"上——这是"概念认可但数字呈现引发不信任"的卡点，值得在真实数据/示例数据上谨慎设计。

**Top drivers / 年度月度趋势图 —— 正面，但点破 demo 数据不真实**
- 认可 top cost drivers 能"pinpoint"该改什么：EV peak 充电是关键贡献者就知道该攻哪里；而 solar availability"we have very less to do about this"（可控性低）。
- 认可月度趋势图（1—6 月逐月上升）能帮判断该不该改习惯。
- 但敏锐指出 demo 的逐月增长过于平滑不真实："it cannot be this smooth such a smooth increase."（Amber 确认是随机演示数据）

### 首次理解 / 价值认知
- 整体能较快看懂各模块在干嘛，且能自行复述含义（overpay risk、primary driver、bill budget、risk ledger、bill proof 均能自行解读，多数正确）。
- 价值认知集中在"诊断 + 可执行建议"：他反复强调 primary driver → risk → action 这条链，认为三者一起放首页很重要："driver and the risk it causing then the action we can take from there... having them on the home screen. When you get in you can see them first thing then you act on them."
- 没有强烈的单点"aha 时刻"，更像是稳步认可型；唯一被绊住理解的是 $56 含义（误读为可省金额）。

### 可用性问题 / 卡点
1. 首页百分比控件拖不动（实为 UI-only，但用户期待可交互）。
2. Saving 页 $56 被默认读成"能省多少"而非"风险敞口"——数字语义需更清晰标注。
3. Bill proof 页过大的差额数字引发"是不是算错了/这么大差不可接受"的不信任反应。
4. monthly bill budget 放首页让他觉得是冗余提醒。

### 功能请求 / 改进建议（受访者主动提出）
- **把 monthly bill budget 移出首页**，放到 profile/settings 里设置（最强诉求，重复多次）。
- **每周计划 / 周账单系统（weekly plan）**：被问想要周计划还是月计划时选周计划，"it should actually bring a weekly bill system"，让人知道这一周做了什么、该做什么、怎么做，按家里电器和用电方式生成时间表/schedule。
- **正向激励通知**：希望周末收到"你这周省了 $50"这类通知，"such a thing would be important"；偏好友好、鼓励式语气（"wow you did this week"），认为有激励作用、让人感到成就感，而非中性的"stay neutral"。（注："stay natural" 疑为 "stay neutral" 的转录错误，结合上下文 Amber 在问"鼓励式 vs 中性式"，推断）

### 与现状对比
- 逐字稿未涉及他当前在用什么工具/做法（未涉及），故无直接横向对比。
- 唯一的"对比"是与上一版 demo 的纵向对比：认为本版"quite improved"、"for a start it is a good one... something that you can launch it"。

### 购买 / 付费意愿信号
- 愿意付费有明确前置条件：要先跑满一个完整 30 天周期、看到是否真能帮省钱后再谈付费。"on the payment that one should come after maybe a whole cycle which is a 30-day cycle."
- 强 ROI 敏感：明确给出价格逻辑——若每月省 50 而订阅要 60，就不值得付，"you will be spending more than what you save."（即愿付金额需低于实际节省额）。
- 自动化偏好：目前只接受"每次询问并批准"，不愿放权自动执行（"for now asking and approving is better"）。
- 共创/留存意愿强：明确愿意加入真实使用测试小组、愿用自己的真实账单和充电习惯试用（"I'd like to be among those who are testing it"）。

## 关键金句
- "I think this one should be I should be able to drag this towards the percentage I want. Yeah, I don't see it working. It's actually not working." —— Kael Williams（首页控件卡点）
- "they're useful actually because opening the app and seeing that on your screen that really tells you it is a it is a driver on what you should do the next conservation." —— Kael Williams（overpay risk 价值）
- "being that it is something that you said once a month... it is not necessary on the home screen... we don't need to be reminded about the budget every time we see you open the app." —— Kael Williams（最强改进诉求：bill budget 移出首页）
- "I think integrating this with Tesla kind of makes it work well because you have to make a confirmation from Tesla before actually... you can say it is a mistake that you change your plans." —— Kael Williams（认可 Tesla 确认流）
- "when someone receives it and they don't have access to the Tesla so they can't affect a change... maybe that is the only problem we can have in this case." —— Kael Williams（多成员通知但无 Tesla 权限的执行漏洞）
- "this number seems quite big... that could be a big miscalculation for a month." / "it would be very difficult to go with it if the difference is this big... we should not be expecting such a big discrepancy." —— Kael Williams（bill proof 夸大差额引发不信任）
- "this is useful because you know the event and the impact it brought and how it brought it. Then you're also given a suggestion on what to do. So I think it is complete." —— Kael Williams（事件明细页评价）
- "I say it should actually bring a weekly bill system. So you can know what you that week and also the plan on what you need to do." —— Kael Williams（周计划请求）
- "Wow, you saved this. You saved like uh you saved $50 this week. I think such a thing would be important." —— Kael Williams（正向激励通知请求）
- "let's say you save 50 and the maybe the applications wants you to pay 60 per month. So there will be no need because you will be spending more than what you save." —— Kael Williams（付费 ROI 阈值）

## 行动项 / 机会点
- **把 monthly bill budget 从首页下沉到 settings/profile**——多位维度反复指向的最强诉求；首页只保留每次都在变的实时信号（overpay risk、primary driver、action）。
- **明确 Saving 页数字语义**：$56 默认被误读为"能省多少"，需在 UI 上把"风险敞口/再不改会多花"与"已省/可省"做强区分。
- **慎用夸大的示例/演示数据**：bill proof 的故意放大差额直接动摇了用户对功能的信任，即便有口头解释也未完全消解。真实/示例数据应贴近现实量级；趋势图避免"过于平滑"的假数据。
- **补齐多成员通知的执行权限链路**：收到通知者若无 Tesla 访问权限则无法执行更改，需设计权限/转交机制。
- **加入 weekly plan / 周账单与排程**：按家庭电器和用电方式生成"该做什么、何时做"的周计划。
- **加入正向、友好的成就型通知**（如"本周省了 $X"），强化留存与动机。
- **付费节点设计在 ≥1 个完整 30 天账单周期之后**，并确保订阅价显著低于实测节省额（ROI 为正）才有转化可能。
- **保持"询问—批准"为默认**，自动化为可选项，先建立信任。
- Kael 愿加入真实使用测试小组、愿用真实账单试用——可纳入早期共创/beta 名单。

## 转录纠错与不一致信号
- 转录纠错（仅在 .md 标注，不改原 .txt）：
  - "stay natural"（line 584）→ 推断为 "stay neutral"（Amber 在对比"鼓励式 vs 中性式"语气）。
  - "the next conservation"（line 79）→ 推断指"下一步节能/省钱动作"，conservation 在此语境约等于省电行为。
  - "spend uh per day... sum that all up"等口语处含转录噪声，仅作理解、未补充事实。
  - 数字（170/182/12/56/186/0.31/0.83/512/200/12kWh 等）均为 demo 内示例数据，且 Amber 多次说明是随机/故意设置，非受访者真实账单。
- 不一致信号：对 bill proof"嘴上说 idea is good，但行为/语气持续回到'差距太大、难以接受'"——表面认可、实则被数字呈现损害了信任，是本访谈最明显的"说喜欢但犹豫"信号。
