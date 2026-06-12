# 用户故事：Amos 要的是"用太阳能给车充电"，而不是又一个看数据的 App

> 改写自 Amos Elberg 的三场访谈：[s1 用户痛点](../../interviews/s1-pain-point-interviews/Amos%20Elberg-pain-point.md)、[s2 Demo 1.0（2026-01-15）](../../interviews/s2-demo-1.0/2026-01-15-Amos%20Elberg-demo.md)、[s3 Demo 2.0](../../interviews/s3-demo-2.0/Amos%20Elberg-demo.md)。
> ✅ **高质量验证场次（组内分析价值最高之一）**：技术背景的跨三轮回访用户，痛点极其具体、可量化；Demo 反馈批判力度强、区分度高——直接否掉团队主推的"月度账单预算"、给出"集成充电器而非汽车"的架构建议、点破"城市附加费致竞品算错账"的差异化机会。这些都不是捧场。**唯一需打折：付费**——s2 明确"只给建议就不付费（学会即退订）"，被引导后才软化到"也许愿意"，原摘要列为弱信号；付费门槛是"必须真正接管控制"。另注一处控制权张力：s1"只给读权限、要先提议再确认" vs s2"我已经在让 NetZero 控制了、很放心"。所有事实、原话均来自访谈，未作外推。

## 画像速览
- **谁**：Amos Elberg，**科技从业者**（熟悉 PVWatts、Claude Code，会反问"为什么不 vibe code"），和妻子都是来自旧金山的 tech people，居家办公。2025 年购入北加州新房（约 3,100 平方英尺），**4 个成年人 + 1 个婴儿**同住（夫妻 + 全天带娃的岳父母）。
- **装备**：**太阳能（2025 年 11 月中旬刚并网）+ Tesla Powerwall + 一辆 Volvo EV（非 Tesla）+ Wallbox 充电桩**；电踢脚线取暖、弱智能温控、电烘干/洗衣/烤箱、**无空调**（遮荫足 + 西班牙陶土瓦屋顶自然凉）。配过 Home Assistant 但"从没弄出有用的东西"。供电 **PG&E**，另有城市级可再生能源**附加费约 20¢/kWh**。
- **在用工具**：**NetZero（约 $7/月）+ Optawatt**。
- **账单/数据**：装太阳能前约 **$300–350/月**；EV 约占用电一半；**太阳能实际日发仅 9–10 kWh，远低于 PVWatts 预期的约 26 kWh**。

## 故事
Amos 和妻子都是搞技术的，2025 年在北加州买了新房，一家四代同堂（还有个婴儿）。他们赶在年底前装了太阳能加 Powerwall、开着一辆 Volvo 电动车——动机很明确：NEM3 之后只有配电池才划算、想尽量离网、还想用太阳能给车充电，让通勤"基本免费"。

可现实给了他两记闷棍。第一记是**太阳能发电远低于预期**：PVWatts 估这个季节该日发约 26 度，他家实际只有 9 到 10 度。很晴的一天发 10 度，5 度白天自用、5 度把电池充到五六成，到晚上 8 点电池就见底。他怀疑是树荫太多、或安装方把板子朝西而不是朝南装了，正拿着 shade study 跟安装商掰扯。他甚至后悔："早知道发这么点电，我们大概就不装了。"

第二记、也是他**最核心、反复强调的痛点——"用太阳能给车充电"太难**。逻辑本该很简单：中午发电多于自用时，把富余的电优先拿去充车，而不是便宜卖回电网，省得晚高峰再贵价买电。可现实是：非 Tesla 的车配 Tesla 桩不做 charge on solar；NetZero 倒是会充，但电池充够后它把富余电**上网卖掉而不是分给车**；Optawatt 又不支持他的桩；ChargeHQ 只做这一件事还要 $10/月。"这是个非常碎片化的领域，没有一个 App 是完整的、没有一个什么都能做。"他手里同时开着 NetZero、Wallbox、ChargeHQ 三个 App——"没有一个解决问题"。他要的，是一个能跨品牌、把富余太阳能优先喂给车、还能顺带智能调度电池/烘干机/踢脚线加热器、让他"不用思考"就省钱的东西。

所以当 Casally 的 Demo 把"问题 + 原因 + 一个能按的按钮"摆出来时，他一眼就认可了那个核心交互：

> "它在给我一条洞察，同时告诉我怎么去执行这条洞察——给我一个可以按下去就解决问题的按钮。所以，我喜欢这个。"

而且他不嫌那 $12 小——"单看一次没什么，但每次充电都省 $12，累积起来就有用，无论我账单是 200 还是 300"。他要的是**每个事件、可重复的节省**。

但 Amos 之所以宝贵，是因为他同样毫不留情。他**直接否掉了团队主推的"月度账单预算"**——"我很欣赏这个设计，但这不是我思考财务的方式。我没有目标电费预算，我只想把电费花得越少越好"，并用亲身经历点出致命伤：踢脚线取暖让他冬月电费从 $80 跳到 $200，"这种季节性会让单月预算模型直接失效……你们这套在常年同温的 LA 能行，但有真实季节的地方会崩"。他认可的是**同比**——"这个月相比去年同月能不能降"。他还顺手给了几条高含金量的建议：**集成充电器而非汽车**（各家车 API 都不一样，但充电器之间有共享 API）；自动化别让我每次手按按钮（"高峰从电网取电就自动暂停充电"）；把"savings"改名"expected savings"；用量要像 NetZero 那样**拆出"房屋 vs EV"**。最锋利的一条产品情报是：**他城市那笔 20¢/kWh 的可再生能源附加费，Tesla 和 NetZero 都不知道，所以金额"算得完全错"**——这正是 Casally 的 Bill Proof 能标出来的差异化点。

至于付费，他说得很直白：**只给建议，我会装但不会付钱**——"几周后我记住建议，就不需要这个 App 了"；要让他付费，**它必须真正接管控制**（充电、Powerwall、EV 充电时机）。但他也明说：要是真有东西能把 charge on solar 优化好，"**我会从 NetZero 切过去**"。

## 一句话总结
> Amos 的核心痛点是**没有一个跨品牌、真正好用的"太阳能充车"方案**（外加太阳能严重欠发、App 碎片化）。他要的不是又一个看数据的 App，而是一个**接管控制、替他跨设备调度、让他不用思考**的系统。他对 Casally 的"可执行洞察"高度认可，并给出了组内最有价值的批判（否预算、集成充电器、附加费算错账）；但付费意愿明确以"真正接管控制"为前提，纯建议型不买账。

## 拆成敏捷用户故事（验收视角）
- **作为**一个开非 Tesla 车的太阳能用户，**我想要**系统把富余的太阳能优先分配给 EV 充电（而不是卖回电网），并通过集成充电器（而非逐车 API）实现，**以便**我真正做到"用太阳能给车充电"。
- **作为**一个手里开着三四个互不协作 App 的人，**我想要**一个跨设备（太阳能/电池/EV/可控负载）自动调度、让我"不用思考"的系统，**以便**我不再在碎片化工具间手动协调。
- **作为**一个电池到晚 8 点就见底的用户，**我想要**像 Lunar/Luna AI 那样聪明地优化电池何时充、何时放，**以便**把电池用在最贵的时段。
- **作为**一个靠电踢脚线取暖的房主，**我想要**系统能连接并智能调度加热器/温控，**以便**它替我决定何时开关。
- **作为**一个被城市附加费多收 20¢/kWh 的用户，**我想要**账单核对把这类本地附加费纳入计算、并解释"账单合理偏高"的原因，**以便**我知道差额来自哪里（这是 Tesla/NetZero 都算错的地方）。
- **作为**一个不想每次手按按钮的人，**我想要**给系统授权自动执行规则（如"高峰从电网取电就自动暂停充电"），同时保留"先看明天计划、我可 override"，**以便**省心又不失控。
- **作为**一个处在强季节性地区、只想把电费最小化的用户，**我想要**用"这月 vs 去年同月"的同比，而不是固定的月度预算，**以便**对比对我真正成立（并把 savings 改叫 expected savings）。

## 关键金句
- "making it easy to charge on solar because charging on solar is really hard now." —— Amos（s1，最核心痛点）
- "it's a really fragmented space... none of them is really complete and none of them really does everything." —— Amos（s1）
- "if we knew how little power we're producing, we probably would not have done it." —— Amos（s1，太阳能欠发的后悔）
- "Right now, I have three apps. None of them solve the problem." —— Amos（s2）
- "If it's going to give me advice, I would install the app, but I wouldn't pay for it. If I'm going to pay for it, it needs to do more than give me advice." —— Amos（s2，付费门槛）
- "After a few weeks, I'm going to remember the advice and I'm not going to need the app anymore." —— Amos（s2，纯建议会退订）
- "it's giving me an insight and it's telling me how to action the insight. It's giving me a button I can press... So, I like that." —— Amos（s3，对 Casally 的核心认可）
- "saving $12 doesn't help me. But saving $12 every time I charge the car does help me." —— Amos（s3）
- "I appreciate that design. That isn't the way that I think about my finances... I just want to minimize how much I'm spending." —— Amos（s3，否掉月度预算）
- "what you would want to integrate with is the charger rather than the car... the chargers have a shared API." —— Amos（s3，架构建议）
- "the Tesla app and the net zero app are not aware of this [sur]charge... they calculate the whole thing just completely wrong." —— Amos（s3，附加费差异化点）
- "if there was something that... optimized the charge on solar, I would switch to that thing." —— Amos（s1，愿从 NetZero 切换）

## 数据强度备注
- **痛点（s1）：极强**。charge-on-solar 难、太阳能欠发（9–10 vs 26）、电池调度不智能、App 碎片化、本地附加费无人算——主动、具体、可量化、带后悔情绪。
- **产品方向验证（s2/s3）：极强、区分度最高**。否掉团队主推的月度预算、给出充电器集成与同比对比的建议、点破附加费算错账、要求自动化而非手按按钮——组内最有分析价值的批判性反馈之一。
- **付费：弱/有条件**。纯建议明确不付费（"学会即退订"），被引导后才软化到"也许"；门槛是"真正接管控制"；若优化好 charge-on-solar 愿从 NetZero 切换。$10–15/月需对应约 $100/月节省。
- **控制权张力**：s1"只给读权限、先提议再确认" vs s2"已经在让 NetZero 控制、很放心"——综合为"要接管控制 + 保留 override"，需在真实使用中确认其授权边界。
- **代表的价值线**："跨品牌 charge-on-solar（集成充电器）+ 全设备自动调度的接管型系统 + 本地费率精度（附加费）"，以及"同比对比 / expected savings 命名"。
- **额外**：他提出"为什么不直接 vibe code、跑得这么慢"——是有技术背景用户对团队节奏的外部质疑，团队需备好"能源信任不可逆、所以先确认不让人困惑再加速"的对外叙事。
- **建议**：纳入 beta（他明确愿意），重点验证"接管控制后他是否真会付费"以及授权边界。
