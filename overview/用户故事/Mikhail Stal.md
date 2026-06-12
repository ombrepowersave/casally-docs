# 用户故事：Mikhail 有全套设备，却没一个互通

> 改写自 Mikhail Stal 的三场访谈：[s1 用户痛点](../../interviews/s1-pain-point-interviews/Mikhail%20Stal-pain-point.md)、[s2 Demo 1.0（2026-01-21）](../../interviews/s2-demo-1.0/2026-01-21-Mikhail%20Stal-demo.md)、[s3 Demo 2.0（2026-02-08）](../../interviews/s3-demo-2.0/2026-02-08-Mikhail%20Stal-demo.md)。
> ✅ **高质量验证场次（组内顶尖之一）**：本职做 UX、熟悉 App 开发的跨三轮回访用户，设备最全、行为一致（自己跑着"午夜调储备、早 6 点回落"的自动化，试过 NetZero 但"没证据不盲订"）。Demo 反馈是设计级的——逐条纠正术语（expected→detected、savings→excess solar、achieved 误导）、颜色语义、标签升级、可读性，并点出"预测性通知"是他没在别处见过的最大亮点。**需留意的高信号**：基础的红/黄充电提醒"对他本人价值有限"（他已自动化、EV 固定夜充、加州有太阳能不能电网充电池），他真正的付费驱动是**天气预测 + 全自动储备时移 + 可验证净省**；且他对"预测能否真兑现"半信半疑——这是付费关键门槛。所有事实、原话均来自访谈，未作外推。

## 画像速览
- **谁**：Mikhail Stal，**UX 从业者**，和妻子住圣地亚哥约 1,200 平方英尺的房子。本人多在家办公，妻子每周约 3 天去办公室。
- **装备（少见的全套）**：**太阳能 + Tesla Powerwall + 现代（Hyundai）EV（约 77 kWh）+ Emporia 充电桩 + Ecobee 温控 + 热泵 + 电烘干/洗碗/AC/智能冰箱**；另有一辆很少开的燃油车。供电 **SDG&E，TOU5（3–4 档费率），现处 NEM3**。
- **费率/历史**：旧房曾是 NEM2 无电池、太阳能持续超发、几乎零账单还拿退费；现 NEM3、新系统**发电不足**，看不清自己会欠多少 true-up。San Diego 夏季 4–9pm 约 **70¢/kWh**。
- **动机**：主要是**财务回本**（打算住 5–7 年回本），其次 EV 便利，环保是加分项——"老实说财务是最大的事"。

## 故事
Mikhail 在圣地亚哥和妻子住，本职做 UX。他家是访谈里少见的"全套玩家"：太阳能、Tesla Powerwall、一辆现代电动车、Emporia 充电桩，还有 Ecobee、热泵、一堆智能家电。按理说这套配置该很省心——可问题恰恰是**没有一个互通**。

最具体的痛点出在电池上。他的 Powerwall 只有 10 来度电，车却有 77 度，**夜里一充车就把电池抽干**；可早上 6 点后电价又贵，这时电池已经空了。他想要的自动化很清楚：午夜把备用储备调高到四五成留着，早 6 点电价变贵时再调回 10%，让电池顶过高价时段。他自己用第三方工具硬凑出了这个效果，但 Tesla 自带 App"控制太有限"做不到——"这些系统明明很聪明，为什么就不让你这么做、为什么不自己做？"

第二个痛点在充电桩。Emporia 不支持 OCPP 协议，所以**做不了"多余太阳能充车"**——它不会在有富余太阳能时自动跟着充。要实现得另买一个约 $100 的小夹钳，他一直没买。于是他只能**天天记着白天去插车**："要是能自动就好多了。"尤其在家办公那几天，他更想白天用富余太阳能充，可现状是"三天里要跑出去插拔六次"。再加上 NEM3 之后"白天充最划算"的心智负担、账单 12 页看不懂——他手里大约三个 App，各管各的，"有点烦，但只能学着将就"。

他要的，是一个能**把这些跨品牌设备真正打通、还能基于天气提前规划**的系统：预报要下雨就提前把储备拉到 100%、留电给峰段；预报晴天、电池快充满就提示用富余太阳能充车。这种**预测性通知**，是他在 Demo 里反复强调、"以前从没在别的 App 见过"的最大亮点。

所以当他看完 Casally，给出的核心评价是：

> "我从没见过哪个 App 是这样的——它把各种不同的工具都整合到一起，我觉得这能解决太多问题。"

而作为一个 UX 专业的人，他给的反馈也精准到用词：当前页面把"会多花的钱"标成 **savings / at risk**"根本名实不符、术语太重"，该用行为激励式说法（"把用电挪到便宜时段能省你 $56"）；"expected"该改成 **detected**（是探测到的、不是预测）；"solar power"列在"花钱项"里让他一头雾水——该用各家 App 通用的标准叫法 **excess solar**（没用上的富余太阳能 = 错过的省钱机会）；月度预算的"achieved"进度条方向反了（目标是越低越好）；太阳能故障该标 **critical** 而不是 unusual；图表"数字太小、颜色太浅读不清"。他特别认可 **Bill Proof**——"电力公司账单 12 页，我根本看不出哪些是额外费用、为什么付这么多"，这个直接戳中他。

至于付费，他要求很硬也很一致：**必须能证明省下的钱高于订阅费**。他直接拿 NetZero 开刀——"$8 一个月，却没有任何证据证明我真能省到，凭什么为不确定的东西一年付近 $100？"但他也说，哪怕净省 $5，"只要我什么都不用做，就依然值得"；他甚至更偏好一次性买断硬件而非长期订阅。还有一条红线：**自动化绝不能在 4–9pm 高价时段用电**，一旦发生他立刻质疑。

## 一句话总结
> Mikhail 有全套太阳能/电池/EV/充电桩/温控，痛点不是缺设备，而是**它们各自为政、不够智能**——电池不会自动调储备、充电桩不会跟太阳能、一切都要手动惦记。他要一个**真正打通跨品牌、还能基于天气提前规划、并能证明省了多少钱**的系统。他对 Casally 的整合定位高度认可、给出设计级反馈；但他的付费门槛是"可验证净省 + 预测真能兑现"，基础提醒对他本人价值有限。

## 拆成敏捷用户故事（验收视角）
- **作为**一个设备齐全却各自为政的用户，**我想要**一个把太阳能/电池/EV/充电桩/温控真正打通的 App，**以便**我不再在三四个互不通气的 App 间手动协调。
- **作为**一个夜充把电池抽干的房主，**我想要**系统自动做"午夜调高储备、早 6 点回落"的时移，**以便**电池能顶过早上的高价时段。
- **作为**一个充电桩不支持 OCPP 的车主，**我想要**在不加 $100 硬件的前提下实现"多余太阳能充车"（或让充电功率随实时太阳能升降），**以便**我不必每天惦记去插车。
- **作为**一个想提前规划的用户，**我想要**基于天气的预测自动化（要下雨就把储备拉到 100%、晴天就用富余太阳能充车），**以便**我不必自己预判未来几天的用电。
- **作为**一个在家办公几天的人，**我想要**一句"我在家办公，只用富余太阳能充、别按夜间表"就能让系统照办，**以便**我不必三天里跑出去插拔六次。
- **作为**一个对自动化有红线的用户，**我想要**系统给建议、我来批准、且容易手动覆盖，并**绝不在 4–9pm 高价时段用电**，**以便**我既省心又不失信任。
- **作为**一个被竞品"无证据订阅"劝退的用户，**我想要**可验证、可审计、按我用量量化的省钱报告（本周/本月省了 $X、做了什么），**以便**我相信它值这个订阅费。

## 关键金句
- "the Tesla app is very limited in the control that you can have with it." —— Mikhail（s1）
- "if I charge my car overnight, it's going to drain my Tesla power wall completely... after 6 a.m. the electricity is expensive, but my power wall is empty." —— Mikhail（s1，核心痛点）
- "I cannot do excess solar charging." —— Mikhail（s1）
- "I need some evidence before I blindly commit." —— Mikhail（s1，付费门槛）
- "the best thing is the predictive notifications... I have not seen that from another application before." —— Mikhail（s2，最大亮点）
- "if you can prove that the savings... is higher than whatever you're charging... that is the level of proof that I need." —— Mikhail（s2）
- "NetZero charges $8 a month, but they have no proof that I'm actually going to save that money... why should I pay them almost $100 a year?" —— Mikhail（s2）
- "I've never seen an app quite like this that integrates all of the different tools and I think that would solve so many problems." —— Mikhail（s3，对 Casally 的核心认可）
- "instead of expected... maybe like we detected, right? Because you're detecting the usage." —— Mikhail（s3，术语纠正）
- "my other apps call it excess solar... I would just use language that is more standardized." —— Mikhail（s3）
- "I'd rather charge on my excess solar during the day... I don't have to go outside to plug in and unplug my car six times in three days." —— Mikhail（s3，在家办公充电痛点）
- "if it's using on peak energy which is the most expensive... I don't see a reason for it... that would make me raise some questions." —— Mikhail（s1，红线）

## 数据强度备注
- **痛点（s1）：极强**。Powerwall 无法自动调储备、Emporia 不能用富余太阳能充车、手动插车、NEM3 时机负担、跨品牌不通——主动、具体、可量化、行为有据（自跑第三方自动化）。
- **产品方向验证（s2/s3）：极强、设计级**。预测性通知 aha、整合价值认可、一连串精准的术语/颜色/标签/可读性修正——UX 专业带来的高质量反馈。
- **付费：正向但有硬条件**。要求可验证净省 > 订阅费（拿 NetZero "无证据" 开刀），偏好一次性买断；净省 $5 也值（前提零操作）；s3 未直接谈价。
- **高信号的"对自己价值有限"**：基础红/黄充电提醒不适用于他（已自动化、固定夜充、加州不能电网充电池），其真实付费驱动是**天气预测 + 全自动储备时移 + 可验证净省**；且他对"预测能否兑现"半信半疑——这是关键门槛。
- **红线**：自动化绝不能在 on-peak（4–9pm）用电。
- **代表的价值线**："跨品牌真整合 + 天气驱动的预测性自动化 + 可验证净省"，以及"在家办公等日程感知充电""术语/可读性的产品打磨"。
- **建议**：纳入 beta（他明确愿意、且是 UX 专业的高质量反馈源），重点验证预测能力的真实兑现与可验证省钱报告。
