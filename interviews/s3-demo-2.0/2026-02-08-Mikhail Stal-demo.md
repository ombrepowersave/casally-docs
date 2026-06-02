# Mikhail Stal · Demo 反馈 · 2026-02-08

## 受访者画像
- 加州圣地亚哥地区用户，电力公司是 **SDG&E**（原文转录为 "SDG& E"，访谈中 Amber 先误猜为 PG&E，Mikhail 纠正为 SDG&E）。提到自己的费率有"三个层级（three tiers）"，并说有些计划有四个层级（super off-peak / off-peak / mid / on-peak）。
- 设备齐全的能源家庭：有太阳能、Powerwall（power wall，特斯拉电池墙）、电动车（带车载充电器，原文 "car charger"）。家里供暖制冷全电气化，用热泵（heat pump），恒温器是 **Ecobee**（原文转录为 "EcoB"）。
- 有新旧两套系统：旧太阳能系统"过度发电（overgenerated）"，能看到累计领先的 credit；新系统"不过度发电（doesn't overgenerate）"甚至处于"发电不足（underproducing）"状态，所以现在看不清自己到底会欠多少。
- 有时在家办公（一周几天或周末），其余时间在外/上班。提到访谈时是当地晚上 9 点，刚下班加健身完。
- 是回访用户（"from our last time conversation"），此前与团队聊过。

## 主题判定
判定为 **Demo 反馈**（s3-demo-2.0 目录，slug=demo）。依据：Amber 全程屏幕共享 Casally 2.0 的 Figma 原型（home / saving / bill 等页面），逐功能讲解，Mikhail 逐一给出"喜欢/困惑/改名建议"的反应，并对照自己现用的车充 App、太阳能 App 等。属于典型的 demo 走查反馈。

> 注：访谈中确认了产品名 **Casally**（Mikhail 问发音，原文转录为 "casually"；Amber 回应发音类似 "Kathley"）。

## 核心提炼

### 逐功能反应

**1. 顶部设备连接状态条（device connected / 离线提示）**
- 正面："this is cool"，没见过类似的，认为是对状态的很好概览（"a very good overview of of the status"）。
- 问题：觉得**太小**（"It's a little bit small"），但整体"makes sense"。

**2. 月度账单预算 / Monthly bill budget（团队称这是"最大改动"）**
- 概念上喜欢："I like the concept."
- 强烈反对当前用词。当前界面写了"achieved"并带进度条，让他误以为是要去"达到或超过目标"——但这里目标恰恰是"尽量低"，方向相反。"when it says achieved and it has this bar… it makes me feel that I need to reach my goal or exceed it… that's not really the case here because the the goal is to keep it as low as possible."
- 改名建议（边想边给，多个候选，未定稿）：把当前账单数值叫 **"projected bill"**；把预算项叫 **"monthly energy budget"** 或 "monthly target (to stay below)" / "electric bill goal"；他自己车充 App 用的词是 "savings" 但他认为和这里要表达的不完全一样。理想信息结构是："monthly energy budget is 170, projected … 50/60%, $75 remaining"，外加"你这个月是往好/往坏的趋势（trending good / trending negatively）"。他也提醒三条信息可能太多（"three pieces of information is too much"）。
- Amber 印证：当天早上另一位用户也被"achieved"绕晕了，团队会改。

**3. 建议卡 / Suggestion card（理由-动作-时间窗结构）**
- 明确喜欢："This is great. I really like this."（结构是 what's happening / what to do / when）

**4. 自动 vs 手动（automatic / manual 两种执行模式）**
- 觉得有趣、能给"额外一层控制（additional level of control）"。
- 但担心**对部分用户偏复杂**（"it may be more complicated than it needs to be"）。
- 个人倾向：如果信任 App，"I honestly would probably never do manual. I would just do automatic." 他唯一会用 manual 的理由是：App 没和某平台集成、无法直接执行；或集成了但他需要微调/App 出错时。
- 建议把模式选择**收到设置里**或做成选项（三种模式：always automatic / let me pick / always manual，或简化成两种）；并建议放进 **onboarding 流程**——首次加入时按设备逐项问"是否让 Casally 自动控制特斯拉/车/电池"，可逐设备选自动或手动，让系统一开始就知道交互偏好。
- 不一致信号（弱）：嘴上认可"多给选项是好事"，但反复强调真到用时自己不会碰 manual、想要"full automation, do everything, make the decisions for me"。即"提供 manual 是好的，但他个人想要全自动"。

**5. 停电预警卡 / Power outage warning（关于可靠性而非省钱）**
- "interesting"，同样原则：信任就直接点 OK。也希望能"忽略（ignore）"不想做的建议。唯一想 manual 的场景是不同意系统建议、想自己改。

**6. 用量图（off-peak / on-peak 颜色编码）**
- "this is great"，喜欢颜色编码，一眼能看出自己几乎都在 off-peak、on-peak 用得很少。
- 提到 Figma 原型里"有个小 bug"（未细说）。
- 提醒费率层级可能是 3~4 档，颜色要够用。
- 可读性问题（重点）：数字太小、颜色太浅读不清——"the numbers are very small and the color I can't read it. It's very very light."，担心用户看不懂。
- 改进建议：图旁可加一句**解读文案**，如"你大部分用电在 off-peak，做得很好"，或全红时提示"试着把用电挪到 off-peak 省钱"；或基于历史对比（月对月/周对周）说"你现在用电看起来正常"。

**7. 账单核对 / Bill proof（设备检测值 vs 账单逐项对账）**
- 高度认可，戳中真实痛点：电力公司账单 12 页、看不懂、不知道哪些是额外费用、自己到底为什么付这么多。"this is really good because… I can't really tell… what's extra, what am I being build for"。
- 类比"超市核对小票"。
- 改名建议：把左侧 **"expected"** 改成 **"detected"**（因为是从传感器/连接数据探测到的，不是预测；"expected makes it sound like you're projecting it"）；不匹配时直接提示"mismatch detected — investigate / contact your electric"。
- 顾虑：多费率（multiple rates）下会变复杂。
- 核心价值认可："if you can make it really simple for people to understand their bill… that's great."

**8. True-up（年度结算）**
- "this is great"，他旧系统过度发电时能看到累计领先多少、有多少 credit；新系统发电不足，**他现在看不清自己会欠多少**，所以很需要这个。
- 希望看到**当前累计/预计 true-up 欠款**（如"-300"或"owe 900"）。
- 困惑点：底部三项不清楚是什么——经解释是"top cost driver（账单主要成本驱动）"，他建议**加标签** "top cost / top energy drivers"。
- 对 true-up 数字本身想要澄清：到底是"我现在欠多少"还是"当前 credit 余额"。
- 建议**标出 true-up 月份**（如"true up in June 2026"），免得自己记。

**9. Saving 页（saving vs bill 两类拆分）**
- 团队解释：saving 是 Casally 侧（从用户行为/时机检测出的成本风险），bill 是公用事业侧（实际账单）。
- 最强烈的反对点在这里：界面把 $56 标为 **"savings / at risk cost / cost exposure"**，但实际含义是"如果不改习惯、会多付的钱"。Mikhail 认为这**根本不是 savings**，而且术语太重（"too technical… too much jargon"）。
- "I would not call it at risk." / "this isn't really savings then." / "what you explained to me and what I see here does not match."
- 改写建议：用激励性、行为导向的措辞，如"shifting your usage to cheaper time of use can save you $56 a month / if you don't do this you will pay $56 extra"。把 sigma 计算等放到独立链接（"view calculations / view details"）。
- 风险账本 / Risk ledger（按 EV、solar、power 分类，可点进事件明细 ledger）：认可对**建立信任**有用（能看到数据来源），但"不会一直看（wouldn't look at this all the time）"，只要好做就值得有。

**10. Solar power 那一行（最大的概念困惑点）**
- 看到 "solar power" 列在"会多花钱"的项里，第一反应是不合理："I wouldn't pay money for solar power."
- 点进明细仍困惑：以为系统是说"不该用太阳能给 Powerwall 充电"。经 Amber 解释后才理解，真正含义是：太阳能充足时本可用来供电/充电/充电池，**没用上就是浪费/错过的省钱机会**。
- 关键改名建议：参照他其他 App 的**标准化叫法 "excess solar"（多余/过剩太阳能）**——"excess solar not used or not stored"，页面叫 "missed out energy cost"（错过的能源成本，如"用了能省 $5"）。强调跨 App 用语标准化的重要性。

**11. EV 充电那一行**
- 这个他一看就懂、认可逻辑：on-peak 充电会多付钱，"makes sense"，"I don't want to charge on peak"。
- 但建议改标签（别用 "at risk"），并加说明：这是"100% 最优"的理想目标，现实中（尤其不在家时）做不到 100% 完美——"this is your goal, but like this is 99.9% impossible"，希望 App 让用户理解这是理想上限。

### 首次理解 / 价值认知
- 整体一眼能 get 到产品价值，aha 点集中在 **bill proof（看懂账单）** 和 **整合各品牌设备**。
- 最大价值认知句："I've never seen an app quite like this that… integrates all of the different tools and I think that would solve so many problems." 痛点在于很多人不是纯特斯拉生态——车充、太阳能板各家不同。
- 多处"如果我信任 App / 信任你"为前提才接受自动化，说明价值兑现依赖信任建立。

### 可用性问题 / 卡点
- 字体太小、颜色太浅（顶部状态条小；图表数字小且浅，读不清）——反复强调。
- 用词造成的理解卡点：achieved（误导成要冲高）、expected（误导成预测）、savings/at risk/cost exposure（与实际含义不符、术语过重）、solar power 列（误以为太阳能要花钱）、true-up 三项无标签、true-up 数字含义不清。
- 多费率（3~4 档）场景下 bill proof / true-up 会变复杂（顾虑）。

### 功能请求 / 改进建议
- **居家办公场景的充电调度**（讲得最具体、情绪最投入）：在家办公两三天时不想夜间 off-peak 充电，想改用白天 excess solar 充。现状要反复手动拔插车充（"three days 内插拔六次"）或改设置。希望 App 够智能——知道他的日程或让他自定义日程，一句"我在家办公，只用 excess solar 充、别按夜间表充"即可。（他自己补充这场景人群不大，但应做到。）
- 加入**空调/供暖（HVAC / 热泵 / Ecobee 恒温器）**支持——Demo 里没看到，他家全电气化制冷供暖，Ecobee 有"便宜电价时制冷"等功能，认为是好的补充。
- 图表旁加解读文案；各项改名（见逐功能）；自动/手动收进设置或 onboarding。

### 与现状对比
- 反复拿自己现用的多个 App 作参照：车充 App（用 "savings" 一词）、太阳能 App（用 "excess solar" 标准叫法）。建议 Casally 在术语上向这些已有标准靠拢。
- 现状痛点：电力公司账单 12 页看不懂；新系统下看不清 true-up 欠款；为控制充电时机要手动拔插车。
- 整体评价：比旧版本好得多——"This looks much better"（重复强调）。

### 购买 / 付费意愿信号
- **未直接谈价格/付费金额**（未涉及）。
- 正面意向信号：明确想试用——"whenever there's a beta… I'd want to test it out"；Amber 提出上线后第一时间邀他用真实账单试，他答应并表示保持联系。
- 对一个月内能上线表示"pretty quick"（略带惊讶，可能隐含对落地速度的将信将疑——弱信号，原文未明说）。

## 关键金句
- "I haven't seen something like this, but I think it's a very good overview of of the status." —— Mikhail（顶部状态条）
- "when it says achieved and it has this bar… it makes me feel that I need to reach my goal or exceed it… that's not really the case here because the the goal is to keep it as low as possible." —— Mikhail（反对 achieved 用词）
- "if I trust you and I trust the app, then I honestly would probably never do manual. I would just do automatic." —— Mikhail（偏好全自动）
- "this is really good because I don't know if you've ever looked at the bills that they send us… I can't really tell what's extra, what am I being build for." —— Mikhail（bill proof 戳中痛点）
- "instead of expected… maybe like we detected, right? Because you're detecting the usage." —— Mikhail（expected → detected）
- "This isn't really savings then." / "what you explained to me and what I see here does not match." —— Mikhail（saving 标签名实不符）
- "I wouldn't pay money for solar power." —— Mikhail（solar 列困惑）
- "my other apps call it excess solar… I would just use language that is more standardized across some of these app applications." —— Mikhail（术语标准化）
- "this is your goal, but like this is 99.9% impossible." —— Mikhail（理想最优 vs 现实）
- "I've never seen an app quite like this that integrates all of the different tools and I think that would solve so many problems." —— Mikhail（核心价值）
- "I'd rather charge on my excess solar during the day. Right now I basically have to unplug the car… I don't have to go outside every single time to plug in and unplug my car six times in three days." —— Mikhail（居家办公充电痛点）
- "whenever there's a beta or something, I would want to test it out." —— Mikhail（试用意愿）
- "This looks much better." —— Mikhail（vs 旧版本）

## 行动项 / 机会点
- **改文案/用词（最高频反馈）**：achieved/bar → projected bill + monthly energy budget/target；expected → detected；savings/at risk/cost exposure → 行为激励式表述（"省 $X / 不做会多付 $X"）；solar power 行 → "excess solar"（错过的能源成本）；true-up 三项加 "top cost/energy drivers" 标签并标出 true-up 月份；把 sigma 计算移到 view details 链接。
- **可读性**：放大字号、加深颜色（状态条、用量图数字）。
- **自动/手动**：默认强调全自动，把模式选择收进设置，并在 onboarding 按设备逐项询问自动/手动偏好。
- **图表解读文案**：基于历史/峰谷占比给一句话提示。
- **新增能力**：HVAC / 热泵 / Ecobee 恒温器接入；居家办公等"日程感知"的智能充电调度（自动识别或用户可编排，避免手动拔插）。
- **信任建设**：保留 risk ledger 明细以展示数据来源；强调"理想最优 vs 现实可达"的预期管理。
- **跟进**：beta/上线后第一时间邀 Mikhail 用真实 SDG&E 账单试用，并把 bill proof 在多费率层级下做稳。
