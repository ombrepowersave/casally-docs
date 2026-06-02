# Amos Elberg · Demo 反馈 · 日期未知

> 转录纠错说明（不改原始 .txt）：
> - 逐字稿多处把 "NetZero"（一款竞品 App）转录为 "net zero / netzero / NetZero usage chart" 等，本摘要统一记为 **NetZero**。
> - 受访者反复提到的额外费率项，逐字稿写作 "search charge / searchcharge"，结合上下文（城市为居民统一登记可再生能源、额外每千瓦时收费）几乎可确定本意为 **surcharge（附加费）**，本摘要按 surcharge 理解并标注。
> - "PG&E / PG& / PG&A" 指同一家公用事业公司 **PG&E**（北加州）。
> - "$5 56 / five $56"（第375–376行）原文含糊，疑为某金额（如 $5.56 或 $56），数字不确定，原文照录为不确定。
> - "M4 / reverse line"（第221行）为访谈者 Amber 表述含混处，未纳入受访者观点。

## 受访者画像
- 住房：近期刚从公寓搬入自购房屋。此前公寓里有 baseboard heater（踢脚板电暖器）。
- 地区：北加州（Northern California），公用事业为 PG&E。明确区别于"住在 LA / 加州（南部）"的情形。
- 设备：有 EV——明确是 **Volvo（沃尔沃），不是 Tesla**。访谈中涉及 power wall（电池墙）、solar（太阳能）、EV charging 等场景；受访者是否实际拥有 solar/battery 未在原文明确说明（界面中出现这些功能，但受访者未自述自己装了哪些）。
- 费率背景：城市政府投票决定为全市居民统一登记可再生能源项目（鼓励更多太阳能），导致他在 PG&E 离峰电价约 34 美分/kWh 基础上，**额外再付约 20 美分/kWh**（surcharge）。
- 现用工具：Tesla app、**NetZero app**（与 PG&E 集成）。注：他没有 Tesla 车却提到用 Tesla app，原文未解释，存疑（推断可能是泛指/口误，未深究）。
- 技术取向：用 Chrome/Firefox 演示，主动反问"为什么不直接 vibe code"，对软件开发/AI 行业现状熟悉，像是有技术或产品背景的人（推断）。
- 关系：与团队"今天是第三次见面"，被邀请加入早期小群体共建，他表示"sounds fun"。

## 主题判定
判定为 **Demo 反馈**。依据：受访者全程在屏幕共享下逐屏点击 Casally Demo 2.0（attention/overpay 提示、events、monthly bill budget、saving、bill 明细与 review more/bill proof、EV charging 事件详情等），并逐功能给出喜欢/困惑/建议；同时含明确的产品方向质疑（vibe code 之问）。

## 核心提炼

### 一、逐功能反应

**1. Overpay risk 提示（attention / $12 数字）— 强烈喜欢**
- 一打开就看到"有 overpay 风险"的提示，他立刻肯定：它不仅给洞察，还**可执行（actionable）**——给出原因 + 一个可按的按钮去解决。"it's giving me an insight and it's telling me how to action the insight... I like that."
- 对 $12 这个数字：**不嫌小**。逻辑是"单次没什么，但每周/每次充电都省，累积起来就重要"。"the fact that it's only $12 doesn't bother me." 后文进一步：无论账单是 200 还是 300，"saving $12 doesn't help me. But saving $12 every time I charge the car does help me."——即他在意的是**每事件可重复的节省**，而非单月总额。
- 对"这数字让你觉得 actionable 还是 stressful"的提问：明确答 **actionable，不是压力**。"this feels straightforwardly actionable to me."

**2. Apply plan / 跳出 App 执行 — 小卡点 + 改进方向**
- 发现点 apply plan 后"不能在 App 内完成，必须离开 App 去做"。
- 针对"是否要像 Tesla app 那样跳转"：他指出自己没 Tesla（有 Volvo），并给出关键架构建议——**若用户没 Tesla，应集成充电器（charger）而非汽车**。两点理由：(a) 各家车 App 能力与 API 都不一样；(b) 充电器之间有**共享 API**可用。

**3. Events / 主动建议（charge your power wall、charge your EV）— 喜欢"主动"，但想要自动化**
- 认可这是"proactive（主动）"的做法。
- 但认为"charge your power wall""charge your EV"这类**不该需要用户每次干预**，应该能自动化，或至少能授权它自动执行。"it shouldn't need user intervention. It should be able to just automate that or... at least give it permission to automate that."

**4. Monthly bill budget（月度账单预算）— 团队主推的"大改动"，受访者明确不买账（最重要的负面/不匹配信号）**
- 团队定位：预算是"容忍边界（tolerance boundary）"而非优化目标/承诺；不让用户乱填数字，用最近三张账单 + 当前费率方案给推荐区间；让 App 从 dashboard 变成 decision system。
- 受访者反应（反复强调）："I appreciate that design... **That isn't the way that I think about my finances.**" 他**没有目标电费预算**，只想"尽量少花电费"。"I just want to minimize how much I'm spending on electricity. I don't have a target budget."
- 自我定位为"simpler（更简单）"的用户："maybe if I was more sophisticated, maybe I would have a target budget, but I don't right now."
- 致命问题——**季节性**：他用亲身经历反驳单月预算模型。公寓时期大多数月电费约 $80，但 12 月/1 月因 baseboard heater 飙到约 $200。"that kind of effect like I just described is going to make it not work... because of the seasons." 并指出团队这套"住 LA/加州（全年温度差不多）能行"，但很多有真实季节的地区会崩。
- 他真正认可的对比方式：**同比**——若有超过一年账单，目标应是"这个月相比去年同月能不能降"。"can I reduce it this month relative to this month last year."（团队回应称这正是长期想做的，但需满一年历史数据才可靠。）
- 收尾共识（由访谈者引导、受访者点头确认）：对他这类用户，budget 不该是主交互方式；核心价值是**事件级决策**（如高峰别充电）；可把 budget 当"选项过滤器"，不在意可直接忽略，per-event 推荐照常触发。

**5. Home 屏的设备状态 / 用量可视化 — 想要更强的可视化**
- 认为用量需要"visualize better"。今天 vs 平常的对比"interesting"，但**只有两根柱子不够**，想看一周、并按"不同用电去向"拆分。
- 主动以 **NetZero** 为正面参照：NetZero 的消费图能显示**多少用电是房屋、多少是 EV**，他"really like"这一点，希望 Casally 也能区分 house vs EV 用电。

**6. Saving 页（saving vs bill 两类拆分）— 命名问题**
- 团队解释：saving 是"我方从行为/时机检测到的成本风险"，bill 是"公用事业账单上真实显示的"。
- 受访者关心 **savings 是前瞻还是回顾（prospective or retrospective）**。他期望 savings 应展示"过去一个月按我们建议你省了多少"。
- 当得知该数字其实是"风险暴露（risk exposure）"而非已实现节省，他直接给出命名建议：**应叫 "expected savings"（预期节省）**，而不是 "savings"。

**7. Bill 明细（breakdown / 主要成本驱动项 / true up）— 喜欢**
- 喜欢账单做了 breakdown，能看到"钱是怎么花在用电上的"。"I like that it does the breakdown and shows me how I was using power."
- 对"只显示三个 top driver 够不够采取行动"：**想要更多**（"I'd like more"），但同时强调现有这几个（高峰 EV 充电、solar）"都是 actionable 的"，给可执行的东西本身就是净利好。"the fact that it giving me actionable things is really a net positive."

**8. EV charging 事件详情（逐事件、bottom sheet：what/why/how/what to do next）— 喜欢，但要自动化**
- 看懂每行是"一个检测到的事件"（不是按天），可逐事件回顾。
- bottom sheet 的解释他认为**有用、布局好、语言好、界面好**。"It's nicely laid out... the interface is nice... the way that it communicates is good."
- 再次强烈表达**自动化诉求**：不想每次都按 apply 按钮，希望"告诉它替我做"——比如"高峰时段从电网取电就自动暂停充电"。"I would like it more if I didn't have to press the button every time... Just pause the charging."

**9. Bill proof / review more（核对账单行项 vs 设备观测）— 喜欢，会用**
- 团队定位：不是和预算比，而是核对账单具体行项是否与设备（solar/EV/battery）观测吻合，类比"超市核对收据"，不判对错只标"这行看起来对吗"。
- 受访者："I think this is a good idea. I would use this. This is helpful to me."
- 主动补充一个**重要的 mismatch 来源**：前述城市级可再生能源 surcharge（额外 ~20 美分/kWh）。Tesla app 和 NetZero app **都不知道这个附加费**，所以它们把金额"算得完全错"。他知道这费用的来龙去脉（城市投票决定），不会去打电话问 PG&E。提醒 Casally：找 mismatch 时，这类城市项目附加费可能正是原因。
- "Smart meter interval data"这个清单项他**不知道是什么**（"I don't know what that is"）——潜在术语困惑点。

### 二、首次理解 / 价值认知
- 对核心价值理解清晰：反复点出"**actionable insight**"是他最认可的点（按钮 + 原因 + 具体行动）。可视为他的 aha：插件式的事件级可执行建议。
- 整体评价正面："I think it's definitely coming along."

### 三、可用性问题 / 卡点
- 屏幕共享一开始分享错窗口（用户自身操作问题，非产品问题，原因是开在 Firefox 而非 Chrome）。
- apply plan 需跳出 App 执行。
- "Smart meter interval data"术语不懂。
- "savings"命名易误解为已实现节省。

### 四、功能请求 / 改进建议（受访者主动提）
1. **集成充电器而非汽车**（无 Tesla 用户场景；charger 有共享 API）。
2. **自动化 / 授权自动执行**：power wall、EV 充电等不该每次手动按按钮；可设规则如"高峰从电网取电就自动暂停充电"。
3. **更强的用量可视化**：不止两根柱，要一周趋势，并按用电去向拆分；尤其要像 NetZero 那样区分 **house vs EV** 用电。
4. **savings 改名为 "expected savings"**，并明确区分前瞻/回顾。
5. **bill 的成本驱动项展示更多**（不止三个）。
6. **同比对比**作为长期目标（这月 vs 去年同月）。

### 五、与现状对比
- 现用 **NetZero app** 与 Tesla app。NetZero 的"house vs EV 用电拆分"是他点名想要 Casally 补齐的能力。
- 两个现有 App 的共同短板：**不感知城市级可再生能源 surcharge**，导致金额算错——这是 Casally 的潜在差异化机会（bill proof 能标出此类 mismatch）。
- 是否会换：未直接表态换不换，但同意加入早期共建小群体在真实生活中使用，"sounds fun"。

### 六、购买 / 付费意愿信号
- **未涉及**：全程未谈价格、付费意愿、愿付多少或购买条件。

### 七、维度外重点：对产品方法论的质疑（vibe code 之问）
- 受访者主动抛出 big-picture 问题：当下人人都在"vibe code"快速构建，为何 Casally **做大量 planning 和市场调研**、反其道而行？"Why don't you just vibe code this... release it and see if it attracts consumers?"（声明无意批评。）
- 这是一个值得注意的**外部视角挑战**，质疑团队节奏过慢。访谈者 Amber 的回应（团队立场，非受访者观点）：能源涉及钱、计费、设备控制，做错会立即且几乎不可逆地破坏信任，所以要"在确认不让人困惑之后再快速行动"；并称一旦看到用户像他今天这样持续秒懂并知道下一步，就会加速推进。
- 受访者听完表示"Got it"，未明确被说服或反驳，礼貌收尾。

## 关键金句
- "it's giving me an insight and it's telling me how to action the insight. It's giving me a button I can press to action the insight. So, I like that." —— Amos Elberg
- "the fact that it's only $12 doesn't bother me." —— Amos Elberg
- "saving $12 doesn't help me. But saving $12 every time I charge the car does help me. And it would help me whether my electrical bill was 200 or 300." —— Amos Elberg
- "I appreciate that design. That isn't the way that I think about my finances. So, I don't have a target electricity budget. I just want to minimize how much I'm spending on electricity." —— Amos Elberg
- "I think that kind of effect like I just described is going to make it not work... because of the seasons." —— Amos Elberg
- "The only thing... if I had more than a year of electrical bills, then my goal would be can I reduce it this month relative to this month last year." —— Amos Elberg
- "I think what you would want to integrate with is the charger rather than the car... the chargers have a shared API that you can use." —— Amos Elberg
- "I would like it more if I didn't have to press the button every time. I'd like to tell it just do this for me. Just always pause if it withdraw from the grid at peak times." —— Amos Elberg
- "one of the things that NetZero does that I really like is... it shows you how much of the consumption is the house and how much of the consumption is the EV." —— Amos Elberg
- "I would call it expected savings." —— Amos Elberg
- "I think this is a good idea. I would use this. This is helpful to me." —— Amos Elberg（指 bill proof / review more）
- "the Tesla app and the net zero app are not aware of this [sur]charge... they calculate the whole thing just completely wrong." —— Amos Elberg
- "Why don't you just vibe code this? ... everybody's just building. And you guys are doing the opposite way." —— Amos Elberg
- "I think it's definitely coming along." —— Amos Elberg

## 行动项 / 机会点
- **充电器集成优先于汽车集成**：对非 Tesla 用户（如 Volvo）走 charger 的共享 API，避免逐车 App/API 碎片化。
- **加入自动化/授权模式**：允许用户为"高峰从电网取电就暂停充电"等设规则，减少每次手动 apply。
- **用量可视化升级**：周/多日趋势 + 按用电去向拆分，至少补齐"house vs EV"拆分（对标 NetZero）。
- **重命名 "savings" → "expected savings"**，并在 UI 明确区分前瞻（风险暴露）与回顾（已实现节省）。
- **bill proof 纳入城市级可再生能源 surcharge 等"账单合理偏高"的解释**，作为 mismatch 的常见原因之一（Casally 相对 Tesla/NetZero 的差异化点）。
- **重新评估 monthly bill budget 作为主交互的定位**：对"只想最小化电费、无固定预算、且处于强季节性地区"的用户，budget 应可被忽略且不影响 per-event 推荐；推进"同比（这月 vs 去年同月）"作为更贴合的对比框架。
- **术语澄清**："Smart meter interval data"等清单项需解释，避免用户看不懂。
- **关注开发节奏的外部质疑**：有技术背景用户认为团队过于偏重 planning/调研而非快速 ship——需准备好对外的"为何谨慎"叙事（信任不可逆）。
- **不一致信号提示**：受访者口头多次说"I like / I appreciate"，但对**月度预算**这一团队主推功能，"喜欢设计"与"不符合我的使用方式/季节性会失效"并存——属于"嘴上认可、实质不会用"的不一致信号，不应据其礼貌用语高估该功能的接受度。
