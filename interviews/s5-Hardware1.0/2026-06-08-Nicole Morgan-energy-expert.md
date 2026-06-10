# Nicole Morgan · 专业咨询（能源/公用事业） · 2026-06-08

> 受访者：Nicole Morgan（SDG&E 项目经理）；访谈人：Amber Fu（Casally；后段 Vernon Zhou 短暂代为说明）。逐字稿为英文+中文双语对照，本摘要以英文原文为准提炼。
> 转录纠错说明：在不改原始 `.txt` 的前提下，把明显的语音转录错误还原为本意，关键术语首次出现处标注原文写法。最重要的一处：受访者所在公司在逐字稿里被转录成 "SDJ / SDG / STG / SCJ / SCG / SGE / SG" 等多种写法，结合"加州、住宅能源项目、CPUC 合规"语境，判定为 **SDG&E（San Diego Gas & Electric，圣地亚哥燃气电力公司）**，下文统一写 SDG&E。

## 受访者画像
- **SDG&E 的项目经理（program manager）**，当前聚焦**住宅客户能源项目（residential customer energy programs）**，重点在**项目运营 + 监管合规（regulatory compliance）+ 跨职能协调**。
- 自述十多年在公用事业内部从事政策与合规相关工作（Amber 开场称其"spent over the decade inside ... on the policy ... side"）。
- 日常与客户项目、电网运营（grid operations）、数据分析、外部技术合作伙伴等多团队协作，确保项目达标、符合 CPUC 要求与公用事业政策；工作核心是**在客户价值与电网需求之间求平衡**。
- 工作处在"运营 / 政策 / 客户项目 / 新兴能源技术（智能温控、电池、EV 充电、其它 DER）"的交叉点。

> Casally 背景（由 Amber 介绍）：帮加州房主（尤其有太阳能 / 电池 / EV、或高电费者）看懂用能，并跨品牌自动转移 EV 充电等大负荷；当前是 App（经 API 连大负荷），计划约 3 个月～半年后推出连接电表 / 电气面板的硬件设备。

## 主题判定
判定为 **专业咨询 / 能源专家（energy-expert）** 主题，**而非目录所示的 hardware**。
- 依据：全程围绕"公用事业如何看待 DER 客户、demand response（DR）可靠性、CPUC 监管机制、NEM 3.0、并网/PTO 流程、初创公司如何与公用事业合作（pilot/POC）、CCA vs 设备厂商 vs 大型 IOU 三条路径、数据/网络安全合规要求、试点规模与时长"展开——这些是公用事业政策/监管专家咨询内容。
- 硬件只在末段以"未来上设备时公用事业关心什么"被带到一句，占比很小。
- 按技能规则"内容明显不符目录主题时以内容为准并改 slug"，slug 定为 `energy-expert`，文件改名为 `2026-06-08-Nicole Morgan-energy-expert`（仍留在原 `s5-Hardware1.0/` 目录）。

## 核心提炼

### 1. 公用事业如何看待有 solar/battery/EV 的住宅客户
- **从长期规划视角，把这类资产视为"有价值的电网资源（valuable grid resources）"**——当它们能响应价格信号或 DR 事件时，可降低 peak demand、提升电网灵活性。
- 同时它们也带来**运营复杂性**：要做负荷预测、管理**双向潮流（two-way power flows）**、保证项目合规、维持对分布式资产的**可见性（visibility）**；设备和项目越多，需要的协调越多。
- **明确不把这些客户当成本或问题**——"the industry is currently moving forward seeing them as ... part of the solution"。关键问题是：这些资源能否以**可靠且可扩展**的方式整合，从而同时给客户和电网创造价值。

### 2. 面向客户的能源项目归属（SDG&E 内部分工）
- DR、负荷转移（load shifting）、客户 DER 参与等项目，归 **Customer Programs and Clean Energy 组织**。
- **Customer programs 团队**：负责项目设计与整体绩效。
- **Regulatory affairs**：负责 CPUC 合规。
- **Grid operations & planning**：判断哪里需要灵活性、这些资源如何支撑可靠性。
- 涉及 solar/battery/EV 的项目，还要与 **DER 与电网集成（grid integration）团队**大量协作。
- "没有任何一个团队在真空里运作"——这些项目天然跨职能（客户 / 技术运营 / 监管）。

### 3. "可靠（reliable）"对公用事业到底意味着什么
- 举例：发起一个 DR 事件、预期削减 **10 MW** 负荷，就需要**高置信度相信届时真能削出来**。光有客户/设备"参与"不够，资源必须在 peak 或电网压力事件中**稳定地兑现**。
- 可靠性还意味着**良好可见性**：需要准确的 **telemetry（遥测）**、及时数据、以及对结果的**测量与验证（measure and verify）**能力。"if a program says it's delivering load reduction, we need to be able to quantify that with confidence."

### 4. 信任第三方技术合作伙伴的前提
- 首先要确信合作伙伴能**持续稳定地交付成果**（管 EV 充电 / 电池时，事件期间客户保持参与、设备按预期响应）。
- **数据质量是关键**：需要准确信息 + **可审计的遥测（auditable telemetry）**，否则"看不到正在发生什么，就很难信任这些资源"。

### 5. 什么让一个家庭对电网"真正有用"
- solar/battery/EV 是资产，但**有用与否取决于能否在需要时被协调起来支撑电网**：EV 能否在 peak 延迟充电？电池能否在 DR 事件放电？且这些动作能否**持续发生而无需客户每次手动干预**。
- **数据本身不提供大价值**——真正的价值是"**可控负荷 + 可预测响应 + 可衡量绩效**"三者结合，才让一个家庭成为有用的电网资源。

### 6. 最有价值的灵活负荷排序（当前 & 未来）
- **EV 充电 = 最有价值的灵活负荷**：能量体量大，且充电常可**平移数小时而不影响客户体验**。未来几年仍最重要。
- 受访者给出的 **Top 3 排名**：① EV 充电器 → ② 家用电池 → ③ HVAC 系统（以及热水器）。

### 7. 公用事业需要的数据可见性层级
- **许多传统项目用智能电表数据就够**——它能反映负荷是否转移、转移了多少；若目标只是衡量整体客户影响，电表数据"能走得挺远"。
- **设备级数据（device-level）在"主动管理/验证特定资源"时才变得有价值**：如 DR 期间预期某 EV 充电器减少充电，"确切知道这个充电器做了什么"远比从全屋数据推断更可信。
- 项目越依赖**调度与协调分布式资源**，设备级数据越有价值——理想是两者都有：**智能电表用于结算与验证（settlement and validation）**，**设备级遥测用于运营可见性（operational visibility）**。

### 8. 实时"邻里级可见性"到底有多值钱（回应 Span 智能面板的说法）
- Amber 转述 Span（智能面板公司）观点："对公用事业最有价值的是邻里级实时负荷可见数据"。
- Nicole：**方向对，但不会说它本身就是最有价值的**。实时邻里级可见性有用，因为能**改进预测、识别本地约束、让运营者更懂配电系统**，且随 EV/电池/DER 增多越来越重要。
- 但"如果问大多数公用事业人更想要什么，我通常会选一个**真能依赖去削减/转移负荷的资源**"。数据之所以有价值，是因为帮助决策与验证结果——**真正的价值在于可见性能转化为提升可靠性的运营动作**。

### 9. 监管机制：CPUC 与 NEM 3.0
- **CPUC（California Public Utilities Commission，原文转录为 "CPU/CU CPU"）主导规则与优先级**：客户项目、费率、DR 等都在 CPUC 批准的框架内运作；公用事业可提新项目/费率设计，但需经**监管审查（regulatory review）**才能广泛落地。"CPUC sets many of these rules and priorities and the utilities are just responsible for executing within those boundaries."
- **NEM 3.0（原文 "NM3/N3/M3"）的意图**：随着太阳能普及，担心客户的**上网电量补偿水平偏高、未反映电网真实需求（尤其中午光伏充裕时）**；NEM3 旨在**激励对系统更有益的行为**——把能量存进电池、把用电转移到 off-peak。
- **未来加州费率政策方向**：会继续走向"**奖励灵活性而非仅奖励发电（reward flexibility rather than just energy production）**"；预计更强调**动态定价（dynamic pricing）、managed EV charging、虚拟电厂（VPP）、需求灵活性，以及与实际电网价值挂钩的激励**。
- **该密切关注的政策转变**：① 把"灵活性"当作电网资源（而非仅能效）的持续转向；② 加州 **managed charging 与车网集成（vehicle-grid integration, VGI）** 政策的演进。

### 10. 为什么客户常觉得"账单/并网出错"
- 实际上多数情况是**单一问题**，根源是**涉及的系统/流程/参与方太多**（客户、安装商、公用事业运营团队、计费系统、有时还有许可机构）在交换信息；一处信息不全或不匹配就造成延迟，客户体验成"公用事业弄丢了我的文件"。
- **账单与上网电量抵免（export credits）易混淆**：涉及复杂计算、多个费率组成部分，以及**用电/上网/结算之间的时间差**——账单"技术上正确但客户难懂"，从而产生困惑。

### 11. 住宅太阳能并网 / PTO 流程（受访者高层级描述）
1. 客户与太阳能安装商签约 → 安装商设计系统并**代表客户向 SDG&E 提交并网申请**。
2. 公用事业审查申请：拟建系统是否满足技术/安全要求、文件是否齐全。
3. 系统安装完成 → 完成验收（含**当地建筑主管部门最终签字**）。
4. 安装商把最终文件与验收文档交回公用事业。
5. 公用事业**终审**：核实"实装系统与批准方案一致、各项条件满足"。
6. 通过则**签发 PTO 信（Permission To Operate）**——此刻客户才正式获准开机并向电网送电。
- **延迟通常出在三处之一**：安装商文件不全 / 验收或许可问题 / 批准设计与实装不符。
- 客户常以为是"公用事业压着不批"，但延迟多在**安装商↔检查方的交接链**上；多数客户没意识到 **PTO 是涉及多机构的协调流程，不只是公用事业一个审批方**——这也是跟踪与沟通有时很难的原因。

### 12. 公用事业怎么看"帮客户读懂账单/文件"的第三方
- **取决于做法**：帮客户更好理解账单 / PTO / 费率方案，多数公用事业**视为正面**——能减少挫败、支持项目采纳；"能源项目和计费结构令人困惑"正是公用事业的一大痛点。
- **若平台反而制造额外困惑，就会成为麻烦（headache）**。
- 第三方 App **拥有部分客户关系**：只要是"帮助客户而非制造困惑"，多数公用事业能接受。

### 13. 初创公司如何与公用事业合作（落地路径）
- **先找对内部对口团队**（与你价值主张最契合者）：DR 团队、DER 项目团队、EV 项目组、创新办公室（innovation office）、或客户能源解决方案组织。
- **从 pilot / proof of concept 起步，而非大规模部署**。公用事业天然谨慎（运营关键基础设施、对监管者负责），要看到证据：方案有效、客户确会用、能交付**可衡量结果**。
- 需提前准备回答：**数据隐私、网络安全、客户注册、绩效衡量、监管对齐**——这些议题"往往和技术本身一样重要"。
- **能拿到机会的初创，是带着"对公用事业问题的清晰答案"出现的**：别说"快用我们的平台"，要说"我们能帮你把充电参与率提升/管理 **20%**"。
- **内部 champion 至关重要**：初期靠项目经理 / 创新负责人当 champion；但要规模化，最终需要**项目运营、监管、IT、网络安全、电网规划等多方利益相关者**的支持。"building the internal champion is usually just as important as building the product itself."

### 14. POC 成功标准（受访者给出的排序）
1. **Dispatch success（调度成功率）+ 可衡量的负荷削减**——程序说能削多少，是否真削出来（首要）。
2. **客户留存（retention）与退出率（opt-out rate）**——"让客户注册是一回事，让他们持续参与是另一回事"。
3. **客户注册增长（enrollment growth）**。
4. **客户满意度 / 客户体验**——他们是否理解正在发生什么。
5. **成本效益**——尤其**每注册客户成本**与**每千瓦灵活容量的成本（cost per kW of flexible capacity）**。

### 15. 试点规模与时长门槛
- **规模**：
  - ~20 户通常**太小**（除非测某个非常具体的技术能力）。
  - **100～300 户**通常足以开始产生关于客户行为与注册的有意义洞察。
  - **500～1,000 户**时人们会更认真，因为结果更能代表更大规模部署的表现。
  - 后段进一步明确：**50 户偏少；理想约 100～300 户**就能开始与项目运营方进行更深入对话。
- **时长**：DR / 负荷转移试点**至少跑一个完整季节（夏季）**——因为加州多数最高级别电网压力事件发生在那时，能在不同条件下评估表现。

### 16. 上硬件设备后公用事业关心什么（少量硬件相关）
- **纯监测设备**（收集数据、提供洞察）：公用事业更关注**数据隐私与通信标准**，而非并网要求。
- **一旦设备开始控制负荷**（EV 充电器、电池、HVAC）：公用事业会想了解——**指令如何下发、有哪些安全保障（safeguards）、客户如何保留控制权、通信失败时会怎样**。
- 若设备**接到智能面板或电池系统**，还可能涉及**电气规范（electrical codes）与公用事业侧**的考量。
- 受访者建议这些问题"要尽早就开始想"。

### 17. 需提前准备的数据/合规要求
- **网络安全（cybersecurity）是头号大事**：公用事业要弄清你**如何保护客户数据**；访问控制如何做——"这类对话通常比初创预期的早得多就开始了"。
- **数据隐私**很重要。
- **数据质量 + 可审计遥测**：若你声称负荷削减或设备控制能力，公用事业要**一致、可审计**的数据，才能信任绩效指标。
- **客户同意**：需要清晰的客户授权与数据共享许可流程。

### 18. 三条合作路径的权衡（设备厂商 vs CCA vs 大型 IOU）
- **设备制造商（device manufacturer）**：通常**最快**——能更快拿到客户设备与可复用数据；**缺点**是常被绑进厂商生态，且更多是在证明**客户参与度**而非电网价值。
- **CCA（Community Choice Aggregator，社区选择聚合商）= 最佳折中、对初创更易上手**：他们关注客户项目、电气化、本地能源目标，**更愿意做试点**；行事谨慎、聚焦客户项目、有采纳与本地电网收益，但**审批层级比大型 IOU 少**，更容易把 pilot 跑起来、立刻出结果；可在不背全部复杂性的情况下展示真实的电网与客户收益。
- **大型 IOU（投资者所有的公用事业）**：**机会最大但最慢最复杂**——监管合规与数据治理要求更多；好处是一旦成功，**规模效应显著**。
- 受访者建议初创**先从 CCA / 聚合商 / 设备厂商入手**，而非一上来直接对接大型 IOU。

## 关键金句
- "I wouldn't characterize these customers as a cost or as a problem for us. The industry is currently moving forward seeing them as ... part of the solution." —— Nicole Morgan
- "If we call a demand response event and expects a 10 megawatt of load reduction, we need a high degree of confidence that those reductions will actually show up when needed." —— Nicole Morgan
- "if we can't see what's happening it's difficult for us to trust in the resources." —— Nicole Morgan
- "data by itself doesn't provide the great value. It's the combination of those controllable load, the predictable response and also the measurable performance that makes a household a useful grid resource." —— Nicole Morgan
- "EV charging is probably the most valuable flexible load because of the amount of energy involved and the fact that ... charging can ... be shifted several hours without affecting a customer experience." —— Nicole Morgan
- "the CPU sets many of these rules and priorities and the utilities are just responsible for executing within those boundaries." —— Nicole Morgan
- "California will continue moving towards rates and programs that reward flexibility rather than just energy production." —— Nicole Morgan
- "the biggest thing most customers don't realize is that the PTO is really ... a coordinated process involving multiple organizations not just the utility approver alone." —— Nicole Morgan
- "sometimes the bill is technically correct but difficult for the customer to understand. So which creates that confusion." —— Nicole Morgan
- "the startups that tend to gain traction are the ones that show up with a clear answer to utility problem ... instead of saying ... yes to our platform they say here's how we can help you ... manage charging participation by 20%." —— Nicole Morgan
- "building the internal champion is usually just as important as building the product itself." —— Nicole Morgan
- "the big one is cyber security really ... that conversation usually starts much earlier than the startups would expect." —— Nicole Morgan
- "it's easier to start with CCA and the aggregator and the device manufacturer ... they have fewer layers of approval than the large investor own utility." —— Nicole Morgan
- "if you ask the most utility people what they would rather have, I would usually choose a resource that can actually rely on to reduce the shift load ... the real value comes when the visibility can be translated into the operational actions that improve reliability." —— Nicole Morgan
- "for an early proof of concept, 20 homes is usually too small ... 100 to 300 homes is often enough ... once you get into ... 500 to 1,000 ... results begin to look more representative." —— Nicole Morgan
- "for a demand response or a load shifting pilot I would generally want to see at least one full season." —— Nicole Morgan

## 行动项 / 机会点
- **定位话术**：对公用事业别卖"平台"，要给出可量化的问题答案（如"帮你把充电参与率管理/提升 20%"），并准备好用 **dispatch 成功率 + 可衡量负荷削减**作为首要证明。
- **落地路径**：优先 **CCA / 聚合商 / 设备厂商**起步（审批层级少、更愿做试点），把大型 IOU 作为后续规模化目标；尽早物色并培养**内部 champion**（项目经理/创新负责人）。
- **试点设计**：规模瞄准 **100～300 户**（≥50 偏少），**至少跑一个完整夏季**覆盖加州高压力事件；预先对齐 POC 成功指标（调度成功率→留存/退出率→注册增长→满意度→成本效益）。
- **数据与合规**（早做）：把**网络安全**当头号工程；建立数据隐私、访问控制、**可审计遥测**、**客户授权与数据共享许可**的清晰流程；同时保留**智能电表（结算/验证）+ 设备级遥测（运营可见性）**双层数据。
- **产品价值主张**：强调"可控负荷 + 可预测响应 + 可衡量绩效"三合一，而非单纯卖可见性数据；把可见性转化为可执行的运营动作。
- **顺应费率走向**：围绕**灵活性、动态定价、managed EV charging、VPP、与电网价值挂钩的激励**布局；持续盯 **VGI / managed charging** 政策与 NEM 后续演进。
- **账单/并网价值点**：帮客户读懂账单、PTO、费率属公用事业眼中的正面价值（前提是别制造新困惑）——可作为获取客户信任与公用事业好感的切入点；理解 PTO 是多机构协调流程，延迟多在安装商↔检查方交接。
- **硬件路线图前置考量**：监测设备阶段重点解决数据隐私/通信标准；进入负荷控制后须能回答"指令如何下发、安全保障、客户控制权、通信失败处理"，并预研智能面板/电池连接涉及的电气规范与公用事业要求。
- **关系维护**：受访者愿在 Casally 成长过程中保持联系，提供公用事业侧视角。

## 待澄清 / 存疑（转录不确定项）
- 公司名在逐字稿中写法混乱（SDJ/SDG/STG/SCJ/SCG/SGE/SG），本摘要据语境判定为 **SDG&E**；如受访者实际另属他司请据原意更正。
- 受访者提到的内部团队名 "DEL programs team"（00:26）**推断为 DER programs team**（分布式能源资源项目团队）。
- "the rate and demand response and the year initiative"（00:16）中的 "year initiative" 转录不清，**含义未明**，未作推断。
- "how the devices are on 30k fed"（00:32）转录不清，疑与"设备如何接入/认证"有关，**未明**，照实存疑。
- 文件原置于 `s5-Hardware1.0/` 且原名带 `-hardware`，但内容判定为 energy-expert，已据技能规则改 slug；如需保留"硬件系列"分组归档，可改回 `-hardware`。
