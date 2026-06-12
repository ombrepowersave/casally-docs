# 用户故事：Gagan 的 35 块板之谜——给我美元，别给我千瓦

> 改写自 Gagan Chawla 的两场访谈：[s1 用户痛点](../../interviews/s1-pain-point-interviews/Gagan%20Chawla-pain-point.md)、[s3 Demo 2.0](../../interviews/s3-demo-2.0/Gagan%20Chawla-demo.md)。（逐字稿中其名被转录为 "Greg Chawla"，以排程显示名 Gagan Chawla 为准。）
> ✅ **高质量验证场次（范围界定）**：跨两轮的回访用户，痛点鲜活、可量化，且有一个真实未解之谜（35 块板发电反而更少）；核心诉求"给我美元而非千瓦""实时告诉我在用太阳能还是电网"在两轮里一致复现，Demo 的 aha 真实且能回扣上一轮。**唯一需打折：付费**——被问价格时把球踢回（"你说多少？"），且高度关注自己 $60 受访报酬的到账，原摘要明确"不宜计为已验证的付费意向"。另注一处态度张力：s1 说"宁愿自己多一点控制"、s3 说"宁愿让 app 自动做、设好就不管"。所有事实、原话均来自访谈，未作外推。

## 画像速览
- **谁**：Gagan Chawla，住洛杉矶**炎热的 Chatsworth**，**3400 平方英尺**两层住宅、**上下两台独立空调**，家中 3 人。另在 **Orange County** 有一套房（前妻住），两套房都装太阳能、同一个 Tesla app 监看。
- **装备**：主房太阳能 **2012 年起租赁安装、后又加装、现共 35 块板**（原 SolarEdge，现走 Tesla）；**一辆 Tesla Model Y（今年 5 月购入，开得不多）+ 一辆燃油车**；**无 Power Wall，正在考虑装**。供电 **LADWP（洛杉矶水电局）**，两月一出账。
- **账单**：夏季约 **$900/月**；即便一人去印度两个月、家里人少，本房仍约 **$500/月**；去年 **true-up 约 $2,200**；他认为合理的月账单应是 **$200**。

## 故事
Gagan 住在洛杉矶最热的 Chatsworth，一栋 3400 平方英尺的两层房，上下两台空调常年开。他早早就投了太阳能——2012 年起租赁安装、后来又加装，如今屋顶 **35 块板**，今年还添了辆 Tesla Model Y。他当初的理解是：装了这么多太阳能，账单该"基本接近于零"。

**结果完全不是这样。** 夏天电费照样约 $900 一个月；就算有人去印度两个月、家里没什么人，本房还是要 $500；去年的 true-up 更是高达 $2,200。而最让他百思不得其解的，是一个具体的谜：**他另一套在 Orange County、板子更少的房子，发电居然比这套 35 块板的还多**——12 月一个产 203 kW、一个才 189 kW。"35 块板，肯定哪里不对，我得弄明白。"他打电话给 LADWP 和 Tesla，对方都说"一切正常"，他根本不信；二月把板子洗了一遍，也没改善。

更深一层的无力感是：**他连账单本身都没法质疑。** LADWP 的账单只给千瓦数、不给美元，复杂又难懂，月底才知道要付多少。"你拿到账单就得付……我都不知道怎么去质疑一张账单、或者这张账单到底诚不诚实。我真希望有办法能知道。"对他来说，费率年年涨、自己做对了一切（装太阳能、买 EV）却还是被系统占便宜——这种不公平感很真实。

他想要的东西，从第一次访谈到看 Demo 都没变：**逐日看到用了多少电、日均花多少钱，月底别被吓到；用美元给我，而不是一堆千瓦；最好实时告诉我此刻在用太阳能还是在买电网的电。**

所以当 Demo 把电量直接折算成美元摆在他面前时，那是他全程最强的 aha：

> "这太不可思议了。就在这儿——delivery，$140，我知道这是一个真实的美元金额，而不是我账单上那种只有'交付了多少千瓦'的东西。这太棒了，我喜欢。"

他还立刻把它接回上一轮的诉求——"给我一个美元金额，别给我 LADWP 那种只有千瓦的东西，那对我什么都说明不了。"而事件页更是直接戳中他那桩未解的太阳能谜案："这个早就能派上用场了——我老早就该知道出问题了。"他顺势提了个很具体的诉求：故障别只说"没发电"，要能告诉他**问题出在哪，比如逆变器离线**。

他也给了几条克制而中肯的判断：usage 维度"keep it simple，别加太多免得人糊涂"；新版首页那个拖拽重排卡片"太隐蔽了，点了只会高亮"，他在引导下才学会。至于自动化，他这次的偏好很明确——"我宁愿让 app 自己做，设好时间就不用管了"（注：这与他第一次访谈说"宁愿自己多一点控制"略有出入）。

## 一句话总结
> Gagan 的痛点是**重投太阳能却账单照旧高、还有一桩 35 块板发电反而更少的未解之谜，而账单只给千瓦、他既看不懂也无从质疑**。他要的核心就一句话：**把电折成美元、逐日可见、实时告诉我在用太阳能还是电网**。Casally 的美元化视图正中其下怀，aha 真实且跨两轮一致——但他的付费意愿尚未验证（回避报价、更关注受访报酬），不能当成已转化信号。

## 拆成敏捷用户故事（验收视角）
- **作为**一个月底总被账单吓到的房主，**我想要**逐日看到用了多少电、日均花了多少美元，**以便**我不再到月底才知道要付多少。
- **作为**一个看不懂千瓦的用户，**我想要**所有用电/发电都用美元呈现（千瓦为辅），**以便**我直接知道这相当于花了多少、省了多少。
- **作为**一个分不清此刻电从哪来的太阳能用户，**我想要**一句话告诉我"你现在主要在用太阳能/电网"，**以便**我据此调整用电。
- **作为**一个太阳能产出异常却查不出原因的人，**我想要**故障能定位到具体症结（如"逆变器离线"），而不只是"没发电"，**以便**我知道该修什么。
- **作为**一个不信任电力公司数字的用户，**我想要**一个能与 LADWP 账单逐项对照的用电/credit 数字，**以便**我能判断账单是否合理、该不该质疑。
- **作为**一个账单忽高忽低的房主，**我想要**把账单变化拆成"多少来自空调、多少来自其他"，**以便**我判断下月该不该少开空调。
- **作为**一个不想费心管理的用户，**我想要**设好规则后让 app 自动执行（set-and-forget），**以便**我不必每次手动操作（注：需与"保留控制权"做可选平衡）。

## 关键金句
- "my understanding was my bill would be basically close to nothing and that's not the case." —— Gagan（s1）
- "my Orange County house seems to produce more energy with less panels... With 35 panels, something is not right." —— Gagan（s1，未解之谜）
- "you get a bill you pay it... I don't know how you even question a bill or if the bill's honest... I wish there was a way to know." —— Gagan（s1，无从质疑）
- "I would love an app that could show me every day how much energy I use... my daily average expense. So I'm not surprised at the end of the month." —— Gagan（s1，核心诉求）
- "This is incredible... delivery, $140... an actual dollar amount instead of just kilowatts... I like this." —— Gagan（s3，最强 aha）
- "give me it in a dollar amount. Don't give me what LA Department of says... just kilowatts. That doesn't tell me anything." —— Gagan（s3）
- "This would have come in handy... I would have known a long time ago that something is wrong." —— Gagan（s3，事件页直击痛点）
- "if it would tell me... maybe the inverter's offline or something like that." —— Gagan（s3，故障定位诉求）
- "whether I'm using the grid or if I'm using my solar." —— Gagan（s3，"只能留一条信息"时的回答）
- "I'd rather let the app do it... set the time and just be done with it." —— Gagan（s3，自动化偏好）
- "Uh, you tell me. How much would it be?" —— Gagan（s3，付费被问时把价格抛回——付费未验证）

## 数据强度备注
- **痛点（s1）：强**。账单高得不合理、35 块板产出之谜、true-up $2,200、不信任且无从质疑账单——主动、具体、可量化、情绪真实。
- **产品方向验证（s2 无 / s3）：强且一致**。"美元而非千瓦""实时太阳能 vs 电网"跨两轮一致复现；Demo aha 真实且能回扣上一轮；并给出有质量的批判（故障定位、keep it simple、拖拽可发现性）。
- **付费：弱/未验证**。回避报价（"你说多少？"），且高度关注 $60 受访报酬到账；价值认可真诚，但无任何价格锚点或自掏腰包承诺。
- **态度张力**：s1"宁愿自己多控制" vs s3"宁愿让 app 自动做"——自动化偏好需在真实使用中再确认。
- **代表的价值线**："美元化的逐日用电 + 实时电源来源 + 太阳能故障定位 + 账单可核对"，以及"年长 EV/太阳能车主"这一可转介绍人群（他父母及其朋友圈）。
- **建议**：纳入早期 beta（他已主动留电话/邮箱），用真实账单补测愿付价位，并验证其自动化偏好。
