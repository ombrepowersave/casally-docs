# Adam Rochford · 专业咨询 · 2026-02-06

## 受访者画像
- 可再生能源行业从业 14 年，背景以**商业（commercial）**领域为主，自述很多问题会延伸到住宅侧（"my background is in the commercial space, but a lot of these issues carry over to residential"）。
- 曾就职于面板制造商（逐字稿写作 "Renee Solola"，疑为转录误，正确名称未能确定，保留原样存疑）以及 **Sunrun**（逐字稿写作 "Sunrow"，按上下文为太阳能公司，疑为 Sunrun，标注"（推断）"）。
- 熟悉商业侧的信用追踪、8760 区间数据（interval data）上报、微电网控制器、数据记录仪（data logger）等工作。
- 提及与公司 **Go Electric**（中西部，后被 **Saft Batteries** 收购）合作过微电网控制器项目。

> 转录纠错说明：本逐字稿为语音转录。明显可还原项已在文中标注；机构名 "Renee Solola"、个别术语拿不准的保留原样并标注存疑。下文 "spam panel" 类未出现；"PG&C" 按上下文应为 **PG&E**（太平洋燃气电力公司），"LWP" 按上下文应为 **LADWP**（洛杉矶水电局），"BESS/PSS" 指电池储能系统，均已在文中按本意理解。

## 主题判定
判定为 **专业咨询**。依据：受访者作为 14 年可再生能源行业专家，对 Casally 产品的多个页面（账单预算、停电预警、节省/账单台账、EV 充电明细）逐一给出专业判断与建议，并就电价结构、净计量政策、停电机理、数据获取路径、合规/授权流程提供行业知识，而非作为普通用户表达使用体验。

## 核心提炼

### 一、停电预警（power outage warning）：专家的关键判断——住宅侧"提前几秒预警"对人无意义
这是本次访谈专家**反复强调、判断最明确**的部分。

- **公用事业常常无预警直接断电是真实的。** 故障触发（fault trigger）可在公用事业未察觉的情况下发生，通常只有"split second"（瞬间），不足以推送通知给任何人。
- **加州的具体机理：** 加州在 load shedding（甩负荷）上更积极；难点是"太多电被回灌到电网（too much power getting pumped back on to the grid），同时又遇到高需求"，过载某变电站会触发未知故障并快速跳闸。
- **预警能提前多久：** 专家答"seconds before the trip"（跳闸前数秒），原理是"dirty power"（脏电/异常电）会在系统断电前先回到电网。即便消费级系统也能拿到数秒预警。
- **数秒预警对谁有用——关键区分：**
  - 对**人（human）**："nothing"（毫无用处），人来不及做任何动作。
  - 对**智能电池储能系统（smart-enabled BESS）**：足够切换到备用电池电源、避免系统重启损失。
- **专家明确结论（反直觉、产品方向相关）：** 住宅侧即使有几秒预警也基本不靠人起作用，因为硬件本就该设计成近乎瞬时切换；用户必须依赖系统自动反应。原话见金句。当被问"对住宅/轻商业，价值更多来自超快硬件响应还是决策逻辑"时，专家答："the built-in logics"（内建逻辑）——因为根本没时间人为反应，取决于物理基础设施 + 电池系统的软件设置。
- **商业 vs 住宅的差异点：** 住宅在配电链上离变电站更远（住宅低压线路在链条更下游，商业高压更直接连变电站），因此住宅能多一点"head start"；但这非常因地而异，"street to street"（逐街道）物理基础设施都不同，难有 one-size-fits-all 方案。
- **商业侧的对照方案（凸显问题规模）：** 解决无预警断电的商业方案是**极其昂贵的微电网控制器**，要花"millions and millions of dollars"。Go Electric 的控制器快到不靠预测算法、而能对电网纳秒级（nanosecond）故障反馈实时响应，用于医疗/敏感制造设施的无损切换。对普通家庭"simply not an option"。
- **即便有 BESS，仍可能有 flicker（闪断）：** 无预警停电时一些系统仍会闪断，引发各种问题。
- **因此住宅仍推荐 UPS：** 对敏感设备（PC、智能家居、网络），即便有整屋备电电池/发电机，瞬时切换也常不够快，仍建议在敏感设备与墙插之间串接 UPS（不间断电源）。智能家居系统哪怕瞬断也可能需要重启。专家认为消费级尚未发展出足够灵敏、标准化、商业化的设备来应对突发电网故障。
- **若要让该功能"真正有用"的条件：** 必须能在系统上**触发一个工作流（workflow）**——拿到回灌断电预警后，自动执行预设的关停流程（针对智能家居/BMS）。但因高度因人而异，需要**用户自定义响应**："everyone would get the same sort of warning, but users would customize what their response function is."
- **公用事业侧 SCADA 是否能快到保护终端用户：** 专家答"still no"。最先进 SCADA 能在零点几秒内检测，但仍不足以发通知，只有级联停机时，相邻区域可能预防性获警。理论上可设"decision gate"（决策闸门，如"检测到脏电，是否执行关停？"），但他质疑现实性——若系统能读到该信号，本就该设成自动反应。

### 二、加州住宅电费的主要驱动因素
- **空调（air conditioning）是单项最大贡献者**（专家明确强调，"one of the biggest individual contributors for sure"），因加州气温因素，南北差异大。原因之一是制冷启动时的**高启动峰值（high startup costs）**；可用变频电机（variable motors）削峰（此为跨领域观察）。
- 住宅侧通常**没有需量电费（demand charge）**，但有**TOU（time of use，分时电价）**，正瞄准日中制冷高峰时段。
- 北加部分地区用电采暖/热泵（heat pumps），瞄准早晨起床、下班回家等高峰时段。
- 关于用户对驱动因素的认知（访谈者转述加州用户普遍认为 EV 充电第一、洗衣第二）：专家认可 **EV 充电确实是最大之一**；但补充洗衣/烘干也较高，**真正的问题是用户倾向同时进行多项**（周末同时洗衣、洗碗、烧水），叠加到 TOU 高峰，单项不大但月度累加"pushes it over the edge"。
- **个体 vs 聚合的张力（专家反复强调的主题）：** 聚合层面趋势可反映在现有 TOU 费率里，但落到个体行为很难精确定位，因为费率是基于很宽的聚合用户群设计的。

### 三、对产品方向的专业建议

**3.1 市场时机判断（强烈正面）**
- "perfect storm"：成本大幅上升 + 容量下降 + 全面收紧预算，专家认为 Casally **正好踩在完美时点**，且潜在终端用户面很广。
- 住宅是好起点，**小商业（small commercial，12/208V，夫妻店、餐馆、杂货店）也可能是市场**，比企业级更"approachable"。大型商业/工业则多已有更强的企业级工具。

**3.2 冷启动 / 首次体验（反复强调的具体建议）**
- 强调"first user experience is make or break"——新用户打开空 App 是致命问题。
- 建议**预加载过去 12（甚至 12–24）个月的账单 + 区间数据**，做一个类似 "Spotify Wrapped" 的用电年度回顾（"like Spotify recapped... here's your last year in power usage"），作为强力的首启钩子与初步用电画像。
- 关键限定：**月度账单数据不够**，"you really need more than monthly consumption to be kind of wowed"；必须拿到 **interval data（区间数据）** 才有价值。

**3.3 数据获取路径（具体、可操作的建议）**
- **Utility API（公司名）**：可一键授权拉取客户过去 12 个月账单数据与区间数据，绕开收集 PDF 账单 + 授权书（letter of authorization）的痛苦流程。成本约 **$15/表（meter）**（"like 15 bucks a meter"）。
- **Green Button（绿色按钮）**：IOU（investor-owned utilities）的标准数据接口。专家在通话中即时核实并确认"**第三方使用是被允许的**"，但需通过授权工作流、且需以**企业实体（corporate entity）身份获批**才能访问。若能拿到第三方访问 Green Button 数据，则可**绕开 Utility API 的费用**，从一开始就直接采集区间数据。
- 加州 IOU——**PG&E、Southern California Edison、San Diego（SDG&E）**——TOU 费率下通常可拿到 **15 分钟级数据**，更不用说小时级 8760 数据。专家解释：TOU 费率本就要求追踪用电时刻，故公用事业必须有逐时用电日志。

**3.4 差异化与留存**
- 警示：很多用户已有 Powerwall、Tesla EV 充电器等碎片化追踪，但缺乏"intelligence"。挑战在于**说服已有部分追踪能力的用户"现有的还不够"**，需要清晰的 USP——在他们已得到的之上叠加额外智能与价值。
- 项目要保住信任的关键：用历史区间数据做出的预测，需与用户实际使用后看到的结果相符；若做预测却没有历史用电背景数据，会显得"shallow"（肤浅）。

### 四、技术 / 政策 / 术语要点
- **NEM 程序梯度：** legacy NEM 1.0 / 2.0、更新后的 net billing 程序；LADWP 用的是 net metering 程序，相对更易理解、更友好，但账单上的追踪信息仍不够 robust。各公用事业（PG&E、SDG&E、LADWP）账单上报内容各有独特问题。
- **8760 区间数据：** 全年逐小时（8760 小时）用电/发电数据，是看清"现场实际消耗 / 回灌电网 / 实际消费"的关键，住宅账单常缺这部分信息。
- **公用事业账单计算可能出错：** 专家明确指出公用事业的计算与冲抵"not always right"，商业侧用数据记录仪（data logger）拿区间级发电/用电数据来核对账单——没有硬件根本无从发现。
- **balcony/patio solar（阳台/露台太阳能）：** 德国允许约 **1.2 kW**（原话 "1.2-2 kilowatts"，数字略含糊）阳台太阳能直插墙插供电、无需走互联流程、不与公用事业打交道；正变流行，尤其租客群体。美国目前有约 **32 或 34 个州法案**在审议以放开此类。可配小电池形成"mini home micro grid"。
- **变动燃料成本调整（variable fuel cost adjustment）——对本产品至关重要的有利点：** 加州住宅 IOU 费率**不含**燃料成本调整加价；而其他市场可能有，会把一个动态未知量注入账单、打乱模式识别。（专家推测：可能某些 rural co-ops 有此项——标注为推测。）这使加州住宅费率"stable enough that pattern-based suggestion"可行。
- **加州费率虽复杂但可预测：** TOU 结构虽复杂，但"it is a structure"，可可靠依赖；有年度调整但可被上报与计划，不像逐月燃料成本调整那样零可见性/零控制。
- **租客世界（renter world）趋势：** 永久硬件安装（自动转换开关 ATS、储能）对很多人越来越难，故冰箱专用 UPS、PC/智能家居/网络 UPS 等即插式方案增多；公寓还受制于物业的变压器基础设施，住户无控制权。

### 五、对产品三阶段路线的回应
访谈者阐述三层模型（① 发生了什么=台账；② 重复行为=模式；③ 建议层，仅当模式持续出现才生成、且以"权衡 tradeoff"呈现，不评判对错）与三阶段（Phase1 软件/API；Phase2 责任台账 responsibility ledger；Phase3 代表家庭行动、承担结果、属"角色转变"而非升级）。
- 专家对"家庭能源台账（household energy ledger）"概念回应"**Absolutely**"，并称"shocking that it's not a thing already"。认为人们被公用事业的自然垄断处境"lulled"（麻痹）。
- 认可"habit = 重复 + 影响成本"的定义，并补充加州不含燃料成本调整正使该模式识别可靠。
- 对 Phase3 自动化：认可"先把台账/智能结构做扎实，再谈系统原生自动反应"，赞同不从推荐直接跳到自动化。

### 六、风险 / 坑 / 现实障碍
- **空 App 首启**：无历史数据时首次体验是 make-or-break。
- **数据获取门槛**：收集 PDF 账单 + 授权书对客户是"really big pain"；月度数据不足，必须拿区间数据；Green Button 第三方访问需企业身份获批、走授权工作流；Utility API 有 ~$15/表成本。
- **既有追踪用户的转化难题**：已有 Powerwall/Tesla 等用户需被说服"现有不够"。
- **停电预警功能的现实价值有限**：住宅侧人不可能及时反应，价值必须落在自动化工作流 + 用户自定义响应上，否则功能意义不大。
- **高度因地而异**：离变电站距离、逐街道物理基础设施差异，使"一刀切"方案困难。
- **技术准入门槛**：当前市面选项需用户具备一定技术能力，是普通人参与的障碍。

## 关键金句
- "they purposefully make these... their bills and their policies difficult to understand so that... normal everyday people aren't able to get a handle on their utility charges." —— Adam R
- （住宅几秒预警对人是否有用）"So for a human, nothing. For a smart-enabled battery energy storage system, that can be enough time to ensure you're switched over to your backup battery power." —— Adam R
- （价值来自超快硬件还是决策逻辑）"it's going to be the built-in logics. You're just not going to have enough time to react to any of that." —— Adam R
- "everyone would get the same sort of warning, but users would customize what their... response function is... based on their needs." —— Adam R
- "you guys are kind of targeting the market at the exact perfect time for this because it's a perfect storm of massively increased cost, lower capacity, and across the board, tightening of belts when it comes to budgets." —— Adam R
- "air conditioning is going to be one of the biggest individual contributors for sure." —— Adam R
- "the first time someone uses it, if there's no information from their current load profile and it's just empty, that first user experience is make or break, right?" —— Adam R
- "it's just like it's like Spotify recapped almost... hey, here's your last year in power usage." —— Adam R
- "you really need more than monthly consumption to be kind of wowed by that initial opening process." —— Adam R
- "you're not getting hit with... variable fuel cost adjustment charges like you would in a lot of other markets... that's actually really helpful in the market for what you guys are trying to do here." —— Adam R
- "It's shocking that it's not a thing already." （指家庭能源台账）—— Adam R
- "people kind of get lulled into that [utilities' natural monopoly]." —— Adam R

## 行动项 / 机会点
- **冷启动方案**：用 12（最好 12–24）个月历史区间数据，做 Spotify-Wrapped 式"用电年度回顾"作为首启体验，并据此生成初步用电画像与预测；务必拿到区间数据而非仅月度账单。
- **数据接入评估**：优先评估 **Green Button**（IOU 标准、可拿 15 分钟数据、第三方访问已确认允许但需企业实体获批 + 授权工作流），可绕开 Utility API 费用；同时把 **Utility API**（~$15/表，一键 12 个月账单+区间数据授权）作为更省事的备选。
- **聚焦 TOU + 空调 + EV + 洗衣的高峰叠加**：将"多设备同时在高峰运行导致月度累加超线"作为核心可解释场景。
- **停电预警功能重新定位**：放弃"靠人提前几秒反应"的叙事，改为"触发可自定义的自动关停工作流（对接智能家居/BMS）"，并明确突出用户自定义响应；评估是否值得作为住宅主打功能。
- **差异化叙事（USP）**：针对已有 Powerwall/Tesla 追踪的用户，明确"在你已得到的监控之上叠加额外智能"的价值主张。
- **小商业市场探索**：将 12/208V 小商业（餐馆、杂货店、夫妻店）列为住宅之外的潜在扩展市场。
- **信任与预测一致性**：确保基于历史数据的预测与用户实际结果相符，避免无背景数据导致的"肤浅预测"。
- **后续跟进**：专家表示有兴趣随产品推进再次交流。
