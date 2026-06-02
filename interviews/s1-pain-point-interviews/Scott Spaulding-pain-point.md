# Scott Spaulding · 用户痛点 · 日期未知

## 受访者画像
- 加州居民，SCE（原文转录为 "SE"/"SC"，应为南加州爱迪生 Southern California Edison）服务区；峰时为 16:00–21:00（"peak hour for us is 4 to 9"）。
- 独栋住宅，约 1,700 平方英尺，家庭两口人。
- 两辆电动车：Model Y 和 Model 3（"two Teslas"；Model 3 为中续航版，充电 32A 而非 40A，使用一个家用 Level 2 充电桩、NEMA 14-50 插座/50A 电路）。年里程合计约 9,000–10,000 英里，"不算多"，无需每天充电。
- 太阳能：已用太阳能约 8 年；约 7–8 个月前因换新屋顶而重装了新太阳能系统，并安装了 Tesla Power Wall 3。新系统约 4.2（kW，"relatively small system"）。旧系统为 Enphase（原文转录为 "Nphase"/"NPC"/"inphase"），有 13 块板、微逆变器（micro inverters）；新系统用 Power Wall 内置逆变器，失去了微逆变器。
- 全电厨房，但供暖和热水用燃气；无空调。
- 电价计划：NEM 2（已锁定/grandfathered，约还剩 12 年），按年 true-up 结算，通常全年净正（"typically it's zero"，账单基本为零）。属本地 CCA 供电，SCE 仅负责输配。使用 TOU（time-of-use）计划。
- 电池预留（reserve）设为 20%，有时手动调到 20% 以下以多用电池。每天查看 Tesla app 多次。
- 偏好：环保意识强；倾向把钱给本地安装商而非大型公用事业/上市公司；几乎不为软件付费（自称"the exception to the rule"）；对界面设计感兴趣。

## 主题判定
判定为**用户痛点**访谈。依据：访谈由 Casally 创始人 Amber Fu 主持，围绕受访者家庭日常用电与能源系统使用展开，受访者反复、具体地描述了 Power Wall/Tesla app 的使用摩擦（手动调预留、无法设 NEM2、EV 充电误抽电池等），符合"痛点访谈"定位。需注意：受访者整体满意度较高、用量低、账单近零，多数痛点为"需要持续监控/手动操作"层面的烦扰，而非高代价痛点；且很多需求是在访谈者引导提问下确认（"那样会有用吗"→"会"），区分时已标注。

## 核心提炼

### 具体痛点清单

1. **EV 充电会误抽电池电量（最反复强调、有真实代价的痛点）**
   - 现象：充电时整套系统按设计"不在峰时充电、改用电池"运行；插车充电时会先从 Power Wall 抽电，导致电池被拉低。"my battery will be you know 60 or 70%. I'll charge and then it'll be 20% because it just sucks from that first."
   - 触发场景：他偏好白天（16:00 前）充电，因为白天电网更"绿"（renewable）。有几次"忘了"或没注意，插上就充，电池被抽空。
   - 当前应对（土办法）：充电前手动把 backup reserve 调高（如设 80%），逼系统直接从电网取电给车。"that's annoying."
   - 根因：Power Wall "不够聪明"，无法设置"充车时只用电网、不用电池"。"the Power Wall is not smart enough to do that."

2. **Tesla app 无法设置 NEM2，只能设 NEM3**
   - 现象：设置里没有 NEM2 选项，只能选 NEM3，于是系统用的是为 NEM3 定制的内置算法，与他实际的 NEM2 不匹配。
   - 情绪/评价："disappointing"，并指出"加州 NEM2 用户远多于 NEM3"，不解为何不做。"I don't know why they didn't include that."
   - 后果：这是他觉得"必须时刻监控"系统的又一原因。他判断 Tesla app "probably a not well coded"，"it's not bad, but it's not bulletproof either."

3. **需要持续手动监控/调节系统（综合性烦扰）**
   - 充电时要盯着别让电池被抽、要手动调 reserve；NEM3 算法不贴合也要盯。"I feel like I have to monitor that."

4. **无法覆盖/自定义 Power Wall 逻辑**
   - 他想要的规则（如"充车时只取电网电"）Tesla app 做不到，甚至手动也很麻烦（"kind of a pain in the ass"）。为此他去研究第三方 Net Zero（原文 "netzero"/"Net Zero"），但 Net Zero 当时转为付费，他不愿为这点小需求付费而放弃。

5. **新系统失去逐板（per-panel）产能可见性 → 信任度下降**
   - 旧 Enphase 系统因微逆变器可看每块板实时产能（"300 watts, 280 watts..."）并有可视化图形；曾据此发现某块板不产电、联系安装商远程排查。
   - 换 Power Wall 后只有整系统产能。"more unsure because... This one just has system. So I don't know how each panel is producing. It makes it a little bit more real when there's per panel."

6. **不知道系统"应该"产多少电（缺基准）**
   - "I don't really know what it should be producing"，没去核对，信任安装商。无法判断"应产 5kW 却只产 4kW"是否异常。

7. **有少量无法解释的电网取电**
   - 即使电池电量充足，偶尔小负载（如咖啡机约 1,200W）会从电网取电 5–10 分钟，他不理解为何。"grid usage should be zero... as long as there's x amount of battery." 且无设置可强制"仅用电池"。

8. **断电（outage）报告缺失/不直观**
   - 8 个月内经历 2–3 次断电（一次较长）。想知道停电的精确起止时间、期间用了多少电池电量。Tesla app 能看用了多少电，但"derivative"、要翻找，没有单一清晰报告，也不明确告知"电网已断电"。

9. **新系统换装后可能未拿满应有的扩容**
   - 在 NEM2 下做了允许的 1kW 扩容，但他怀疑因失去微逆变器，未拿到全部功率提升（"I don't know that we got the full power increase"，明确标注为他自己的不确定推断）。

### 痛的程度 / 紧迫性
- 整体偏低-中：他多次强调自己用量低、账单近零、对系统"generally pretty happy / don't really have that many complaints"。
- 真痛点（反复提、有具体代价）：**EV 充电误抽电池**——是他第一批 Reddit 发帖的起因，"learned that the hard way"，并驱动他去研究 Net Zero；**NEM2 无法设置**——明确"disappointing"。
- "annoying"用于形容手动调 reserve。
- 关于挫败感来源：他澄清最让人困扰的**不是钱、也不是失控**，系统其实"按设计运行"，问题在于"这套系统需要被管理"，而理想是 app 能全权代管。"No, it wasn't the money... It was just... the way the system works has to be managed."
- 频率量化：每天查电池/太阳能 app 4–5 次（"I'm that guy"）；查 Power Wall app "multiple times a day"。

### 触发情境 / 规律
- **季节性极强**：夏天电池约 11:00 即充满，可几乎全天离网（除 EV 充电）；冬天（当前 12 月，"the worst month / worst production"）日照不足，很少充满，明显净负。
- **峰时 16:00–21:00**：会主动把洗碗机、洗衣机等"可选时段"负载挪开峰时。
- **EV 充电误抽电池**：发生在他白天插车充电、未留意 reserve 设置时。

### 当前应对 / 替代方案
- 手动调 backup reserve（充车前调高到如 80%）逼系统走电网——可行但烦。
- Reddit 发帖求助，得到"做不到，除非手动 override"的回复。
- 研究第三方 Net Zero，但因转付费而放弃（不愿为小需求付费）。
- 旧 Enphase 时代：靠安装商远程访问排查单板故障。
- 偏好白天充电（电网更绿）。

### 未被满足的需求 / 期望
（注：以下多为访谈者提案、受访者确认"会有用"，已区分；他多次提醒"我是例外用户"）
- **可自定义/可覆盖的电池规则**，让 app 全权代管，"don't have to think about it yourself"。他自评最重要的 1–2 条规则：
  1. **充 EV 时不用电池，直接从电网取电**（最明确、最想要）。
  2. （次要）电量高于某阈值（如 30%）时不取任何电网电；以及类似"白天面板满产时持续充电池、车从电网充"的离散需求——他认为现在手动都做不到。
- 规则冲突时应**弹出提醒并询问用户怎么做**（如"充车不用电池"与"峰时不用电网"冲突时）。
- 想要规则**实时应用反馈**（如"规则在 15:15 触发"），形成反馈回路以便修正自己设的坏规则。
- **理想交互：语音/AI 指令**设规则（"I want this rule"），app 解释它理解的意图、允许口头微调、再试运行。（他自评"seems like a lot to ask"。）
- **太阳能健康/产能基准**：希望 app 告知"当前产能约为应有的 80%"，并解释原因（季节、脏污、云、阴影）。确认这"would be valuable / would like to see that"。
- **产能 vs 天气/阴影的自动对比与可视化**：他家有烟囱在一天某时段对部分板投影（季节性），希望像旧 Enphase 那样有逐板/带阴影影响的可视化。"that would be great."
- **政策变化预警**：希望 app 监控并提前预警电价/政策（如 NEM）变化。确认"that'd be great"。（背景：NEM3 近期在加州最高法院遭"judicial defeat"——受访者表述，标注为其个人说法；他对自己 NEM2 被改不担心。）
- **统一仪表盘**：把 Enphase/Tesla 等整合到单一界面。"Single interface is always better."
- **停电报告**：单一清晰显示电网断电起止时间 + 期间电池用量；若能给原因（如查新闻/公用事业网站）更好，但他认为原因很难且因地而异。
- **VPP / 车网互动（V2G/H2G）信息需求**（他主动问 Casally 是否做 V2G，表示有兴趣但还没参与 Tesla 虚拟电厂）：
  - 把收益"做实"，如"今天参与 V2G 可得 $20–25"；财务激励驱动行为。
  - 高需求事件**预测/预警**（如"明天高温，请插车"）让用户提前规划。
  - **环境效益解释**（如"昨天本区 V2G 避免了 x 量 GHG，因为没启动调峰电厂"），让用户感到为地球做了事。
  - VPP **长期收益报告**（"去年你因此赚了 $200"）。
  - 愿意贡献电量比例：电池/车约 40–50%；因开车少，车（V2G）可到 50–60%。
- **数据深度偏好**：先简单设计、按需展开细节（"design simple first, additional details on demand"）。给数字时，他个人更在意**背后原因**而非数字本身；希望图上每个点可点击看"为何此时发生"。但提醒很多用户"只要能用、不在意 why"。
- **提醒/建议**：电池到 30%/20% 的提醒，以及行为建议（"关空调/调低/峰时别充 EV"）对部分人有用；他自己不常看手机，是例外。

### 相关背景（与痛点直接相关）
- 设备组合见画像：2 台 Tesla EV、Power Wall 3、约 4.2kW 新太阳能（非 Tesla 品牌）、旧 Enphase 13 板系统、单 Level 2 充电桩。
- "where the electricity is used in the house" 是他很想要的信息，但他明确这需要**智能电箱（smart panel）**，"that's not you. And that's a whole separate thing."（即超出 app 单纯靠现有输入的能力。）
- 付费意愿：整体很低，"if I can do something without paying for it, then I will"；若价值够强会付"not much, but I would pay something"；明确表示对他个人"不确定有哪个功能能从 nice-to-have 变成值得付费"。自认是付费意愿上的例外用户。

## 关键金句
- "the Power Wall is not smart enough to do that." —— Scott Spaulding（关于充车时只取电网电）
- "my battery will be you know 60 or 70%. I'll charge and then it'll be 20% because it just sucks from that first." —— Scott Spaulding
- "The Tesla app did not allow for me to set it at NEM2. it wasn't an option in the settings which was disappointing because there's a lot more people on NEM2 than NE3 and in California." —— Scott Spaulding
- "No, it wasn't the money and it wasn't necessarily behaving. It was behaving the way it was supposed to behave. Um it was just... the way the system works has to be managed." —— Scott Spaulding
- "ideally for someone building an app like yourself you'd be able to have total control and say what do you want to do and when do you want to do it and then tell the app that then you don't have to think about it yourself." —— Scott Spaulding
- "there should be a toggle on there, you know, when when you're charging your EV, take it from the grid instead of the battery." —— Scott Spaulding
- "more unsure because... the Nphase system had per per panel production. This one just has system. So I don't know how each panel is producing. It makes it a little bit more real when there's per panel." —— Scott Spaulding
- "it's not just more information, but why is that information important and what could you possibly do with it?" —— Scott Spaulding
- "ideally it would be... a voice command where you could use AI to just say to the app itself, I want this rule. And then it could interpret that and implement it." —— Scott Spaulding
- "if there was a conflict in rules, there should be an alert saying that and asking me what I want to do." —— Scott Spaulding
- "design is probably always better to to design simple first with additional details or explanation on demand." —— Scott Spaulding
- "people are driven by financial incentives... but incorporating something like that into the app... in an easy to understand way would be helpful." —— Scott Spaulding（关于 VPP/V2G）
- "I'm not typically a paid user of almost anything. That's why I didn't subscribe to Netzero." —— Scott Spaulding

## 行动项 / 机会点
- **核心机会：可自定义、可代管的电池规则引擎**。最高优先级规则——"充 EV 时只从电网取电，不动电池"，这是他亲历踩坑、上 Reddit 求助、转投 Net Zero 的真痛点。Tesla app 无此能力即是直接的差异化切入点。
- **支持 NEM2（及 TOU）原生设置**，而非只有 NEM3 算法。受访者明确指出 NEM2 用户基数更大却被 Tesla 忽视，是被低估的市场缺口。
- **规则冲突处理 + 实时规则触发反馈**：冲突时弹窗询问；规则触发可视化（含时间戳），形成"坏规则可修正"的反馈回路。
- **AI/语音设规则**：用自然语言"if this then that"设规则，app 复述理解、口头微调、试运行（受访者本人提出的理想形态）。
- **太阳能健康监测**：给出"当前 vs 应有产能（如 80%）"及原因（季节/脏污/云/阴影），最好带逐板可视化与阴影/天气叠加（弥补换装 Power Wall 后失去的 Enphase per-panel 体验，直接提升系统信任度）。
- **统一仪表盘**整合多品牌（Enphase + Tesla 等）。
- **断电报告**：单一界面显示电网断电精确起止时间 + 期间电池用量，原因为加分项（可尝试抓新闻/公用事业网站）。
- **政策/电价变化预警**（如 NEM 变动）。
- **VPP / V2G 模块**：实时把收益做实（"今天可得 $20–25"）、高需求事件预测预警（"明天高温请插车"）、环境效益叙事（GHG 避免量）、长期收益报告。受访者愿贡献电池 40–50%、车 50–60%。
- **设计原则**：默认简洁、细节按需展开；数字配"为何"，图点可点开解释。
- **变现警示**：此受访者付费意愿极低（自认例外），EV 续航/用量低、账单近零，痛点多为"烦扰"而非高代价；不宜将其作为付费转化的代表样本，但其对产品/界面的洞察质量高（自述对界面设计感兴趣）。

## 纠错 / 不一致信号
- 公用事业商名转录混乱：原文反复出现 "SE"/"SC"/"ce"，结合"NEM、peak 4–9、加州"应为 **SCE（南加州爱迪生 Southern California Edison）**（推断）。
- "NEM"/"NE"/"N3"/"AM2"/"M3"/"NM 2" 等为 NEM 2 / NEM 3 的转录变体，已统一为 NEM2/NEM3。
- "Nphase"/"NPC"/"inphase" 应为 **Enphase**（太阳能微逆变器品牌）（推断）。
- "Power Wall" 即 Tesla Powerwall（型号 3）；"web plan"/"t to plan"/"toou" 指 **TOU（time-of-use）** 计划。
- "1450 jack" / "131 Y" 等数字含糊：14-50 应为 NEMA 14-50 插座（推断）；"131 Y" 系上下文断续，疑为 Model 3 / Model Y 的口误拼接，未据此下结论。
- "Net Zero"/"netzero" 指第三方能源管理 app/服务（受访者用以指代他研究过的工具），转为付费后他放弃。
- 受访者关于"NEM3 在加州最高法院遭判决失败"为其个人陈述，未在访谈中核实，按原话保留并标注。
- 受访者本人多次强调自己是**付费意愿与使用习惯上的"例外用户"**，多处"有用吗→会"为访谈者引导式确认而非自发强需求，引用其结论时需注意此偏置。
