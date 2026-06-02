# Michael Herzog · 专业咨询 · 2026-03-05

> 转录纠错说明：逐字稿为语音转录，存在同音/听错词。本摘要内部已还原明显错误以便理解，关键纠正如下：
> - "NEM one 123 / name to one two three" → NEM 1/2/3（加州净计量代次）
> - "PUC the CPU" → CPUC（加州公用事业委员会）
> - "IUS / I big IUS" → IOU（Investor-Owned Utility，投资者所有的公用事业）
> - "LA power water and light" → LADWP（洛杉矶水电局）；"SMUD" 原文即 SMUD（萨克拉门托市政公用事业区）
> - "AMI metering" → AMI（高级计量基础设施，智能电表）
> - "CT clamp / city clam / collared meter" → CT clamp（电流互感器钳）/ collar meter（表座套环式电表）
> - "CNI" → C&I（商业与工业 Commercial & Industrial）
> - "avoid cost / avoided cost" → avoided cost（避免成本）
> - "tariff / Terra / terror / terraform" 在原文多处指 tariff（电价/费率方案）
> - "true up / trap settlement" → true-up（净计量年度结算）
> - "wildlife fund" → wildfire fund（加州山火基金附加费，推断）
> - 注：受访者本名 Michael（Mike），访谈中 Amber 多次口误称其为 "Max"。

## 受访者画像

- 显示名 Michael Herzog（自称 Mike）。
- 背景：有公用事业（utility）直接从业经验，自述其直接 utility 经验在美国中部（"the middle part of the country"）。目前从事覆盖全美范围的咨询工作：Midwest、Northeast、Texas、West Coast / California 等。
- 还做过国际咨询，提到近期在 Malaysia 做过咨询工作（马来西亚负荷曲线很平、刚开始上 TOU 费率，与美国差别很大）。
- 熟悉多种市场模型：regulated / deregulated 州、investor-owned utility（IOU）与 publicly owned utility。
- 自我定位偏"更技术的解决方案"（"I'm looking at more technical solutions"），做过为 utility 计算此类节省值的工作。
- 访谈尾声表示愿意以私人咨询/顾问（advisor）形式继续支持 Casally，可走 Upwork 或其他形式，提供工程、tariff、bill 方面支持。

## 主题判定

判定为 **专业咨询**。依据：Amber（产品方向）与 Ling/"Link"（技术负责人，原文 "Ling is our technic lead"）向受访者逐屏演示 Casally Demo 2.0，围绕计费重建、interval 数据、TOU 费率、NEM/true-up、export credit、固定费用结构等提出大量技术与行业问题，受访者以其 utility 与 tariff 从业经验给出判断与建议。属能源专家对产品的咨询，而非用户痛点访谈或 demo 用户反馈。

## 核心提炼

### 一、数据需求与计费重建（专业观点 + 产品建议）

- **重建账单所需的最小数据集**：受访者认为只需"几个数据点"——energy consumption（用电量）、instantaneous power（瞬时功率，KW）、以及对应的 time stamp（时间戳），再配合 tariff/billing 语言即可自行重建账单。原文："I think you would just need a couple of data points... energy consumption, instantaneous power in like a 15 minute interval and a time stamp on all of those... you could use the tariff language, the billing language and reconstruct it on your own."
- **interval 标准粒度**：美国大多数地方现行标准是 **15 分钟 interval**；能更细更好。市场参与、估值、ratcheted demand rates 等大多按 15 分钟 interval 计算。"the standard right now in most places is 15 minute interval... if you can go lower than that you're probably going to be okay."
- **时间戳关键性上升**：因 TOU（time of use）定价在美国越来越普遍，理解各事件发生的时间变得很重要。
- **必需 vs 非必需数据源**：新装太阳能系统通常自带时间戳和发电输出数据，"almost down to the panel"（视逆变器串配置）；电池备份系统同样有这一级信息。但产品**不需要**每个电芯的健康/输出，只需 **aggregate total output 与 demand** 的聚合值。
- **关键缺口 = 整户用电量（home/premise consumption）**：受访者反复强调，做成本分析与偏移（offset）分析、重建账单时，**必须知道整户实际进户用电（energy delta）**，否则难以算出"没有本产品时账单会是多少"。原文："you'd need the actual energy consumption of the premise."——这是他眼中重建账单的"critical"前提。
- **设备 API 优先于自装硬件**：若设备今天已有 API/app，就直接用，没理由不用。"5-10 years ago you would have to put your own device on there... but in today's world everything has an app already, everything has an API, just use it if you have it."
- **第一阶段仅 API、第二阶段加硬件**的路线：产品方说明此规划；受访者据此讨论硬件形态（见"硬件"部分）。

### 二、TOU 费率结构与行为敏感度（行业知识 + 数字）

- **美国 TOU 模型有非常陡峭的峰（"very drastic / very sharp peaks"）**，峰时与非峰时电价差异很大——"double, triple, sometimes four times as much" during critical peak / TOU periods。
- **加州具体数字（受访者明确提示可能记不准，"I'll get the numbers wrong off the top of my head"）**：加州当前平均电价约 **28 cents/kWh**；critical peak pricing 可达 **50 cents、75 cents**，可能非常贵。
- **行为转移确实重要**：在 TOU 下边际成本差异足以让行为转移产生意义。EV 充电这类在峰时累积较多 kWh 的行为"would be noticeable"——"not hundreds of dollars a month necessarily, but tens, 20s, $50 a month."
- **TOU 通常落在 delivery（输配）侧而非 generation（发电）侧**："most of the time it's on delivery."加州不一定，但像 Texas 这种高度去管制（deregulated）的州，用户可"玩市场"按实际能源价格行事；多数情况 TOU 更聚焦 delivery。
- **加州账单 TOU 呈现方式**：按 period 逐行（line by line）拆分，分别列出各时段消耗的 kWh 与太阳能各时段发电。建议去 SDG&E、Southern California Edison、PG&E 官网看 sample net metering bill 学习行项目结构。
- **季节性 / 工作日 / 节假日影响 TOU 映射**：
  - 节假日（holidays）、周末（weekends）会被单独区分、预编程进计量并在 tariff 中明文规定。
  - 季节性：冬季 / 夏季费率是最大的拆分点（"winter pricing and summer pricing"），时段可能在冬夏各偏移几小时。
  - **Daylight Savings Time（夏令时）**：受访者称没怎么见过 DST 对此有大影响，并明确表示对 DST 如何处理"I'm not 100% sure to be honest"——他认为这是个好问题、之前没想过，会记下来（"I'm going to write that down"）。→ 属专家明确承认不确定的点。
- **TOU 映射是实时直接做、非事后估算**：由 AMI 计量（5 分钟 / 15 分钟 interval 实时数据）支撑，不是事后套公式。"that's one of the things in the past 10 to 15 years that's really facilitated time of use rates."

### 三、节省值计算与"可辩护性（defensible）"（行业方法）

- **最佳基线 = 历史账单数据**：以过去几期账单为起点，结合天气调整推算同条件下用电，再比当前——"under similar conditions they used this much power before, nothing else changed except our app."受访者称这从 regulator 角度看是"very straightforward / very defensible"。
- **建议至少 24 个月历史**：仅看过去一年偏难（季节性）；能拿到 24 个月 in arrears 更有帮助。温和气候、波动小的地区，跨月对比也可接受。
- **天气归一化（weather normalization）方法**：用 **heating degree days / cooling degree days（HDD/CDD）**——基于国家气象预报信息，以 **65°F** 为分界（>65°F 需制冷、<65°F 可能需制热），衡量某月/周/日的气候是冷是热，从而归一化负荷。"a quick way to scale that... we normalized — it was an average May, it was a hot May, it was a cool May."不必复杂。
- **utility 自身也这样算节省**：尤其用于 peak demand reduction（削峰）——削峰可避免新建基础设施/项目，比单纯卖能源更有价值（utility 本质在"selling energy"=卖钱，所以削峰减少的能源销售对 utility 是另一笔账）。weather normalization 是预测"若不做会怎样"的几乎唯一方法。
- **可辩护基线建议（counterfactual）**：month-to-month + 简单 weather normalization，并把任何 tariff 变更纳入。"if there were any changes in tariffs... obviously that has to be included."

### 四、固定费用 vs 可变能源费用：加州监管转向（重点行业判断）

- **巨大困惑点**：销售常宣称"装够太阳能就永远没电费了"，但 **固定成本（fixed costs）使账单永远不会低于某个底线**。受访者强调把固定项与可变项拆开、并多花一两句话解释"these cost items are not going away"非常重要。
- **加州去年秋天（past fall）通过立法**，**大幅提高账单固定服务费（fixed service charge）、同时降低可变能源成本**。（受访者主动询问产品方是否知道此立法。）
- **结构反转**：过去经验法则约 **固定 25% / 可变 75%**（约四分之一账单是固定服务费，四分之三是按用量的可变能源），现在"starting to flop on its head, almost completely turning over"——更多向固定费用倾斜，让用户真正为维护系统付费。
- **对太阳能的影响（负面）**：固定费占比上升会**降低安装太阳能的激励**与太阳能价值（"unfortunately... you get less value"）。对加州大 utility，NEM 下本就不是按 retail 而是 avoided cost 结算；其他 NEM 结构下回购价更低。
- **预期趋势**：受访者预计加州会继续向固定费用倾斜，全美更多地区也会更重固定成本、轻可变能源成本；但这是"a big step"，短期内不会再有大变动。
- **产品价值点**：受访者"100%"认为这类工具能弥合"installer 承诺 vs homeowner 实际体验"的差距，尤其在账单越来越偏固定费用时更重要。

### 五、NEM / true-up / export credit（净计量与结算）

- **NEM 1/2/3 的 true-up**：受访者**认为三者 true-up 相同**，但坦言记不准、不确定是按月还是按年，"I don't know it off the top of my head"——属不确定点。规则发布在各 NEM 文件中。
- **谁须遵守 NEM 规则**：受 CPUC 监管的大 IOU 必须遵守；非 CPUC 监管的较小 utility（如 LADWP、SMUD 等市政/公营）**不必**遵守，可自定。
- **true-up 跟踪建议**：能按月跟踪就按月，明确告知用户 true-up 周期、并基于历史账单给出投影（projection），"project it out."
- **export credit 的结算层级**：存在分块（block）结算——账单额度以内（at your bill or below）按 retail rate 回购；超出部分按 avoided cost。受访者举例："10 to 25 cents per kWh at this first block and then 3 to 7 cents at the block below it."——但他认为这种 retail/avoided-cost 块差异**更多是 Midwest 现象，加州 IOU 不太会出现**（"I don't think that comes up... that's more of a Midwest thing"）。→ 推断/限定性判断。
- **import/export 计量方式决定计算**：有独立计量（separate metering / 老系统的 import meter + export meter）则分开算；若是单台双向（bidirectional）净表，则按 interval 累计净用电。
- **tier threshold 与 TOU 谁先适用**：受访者"believe"是 **TOU 费率先适用**（两次说 "I believe"）。→ 不确定点。
- **settlement 走 NEM 还是 net billing**：受访者"think net"，但明确说这是他希望更了解、无法给确定答案的点。

### 六、账单异常 / 高额 true-up / 账单不符（坑与现实障碍）

- **"度假月账单仍很高、各方都说没算错"类困惑**：受访者坦承"I don't know why those would be so different"，脑中第一反应是**设备故障 / 维护问题 / 失准（calibration）**——逆变器串或组件坏、设备老化等。
- **故障常见诱因**：premature failure 多来自 power surges、faults、lightning strikes 等；"technology just fails."但他强调"doesn't happen very often."
- **计量等级与"谁说了算"**：tariff 语言全部写在 metering specs / manuals 里，"whatever the meter says is what it is"。revenue-grade（计费级）计量设备容差更严、带宽更窄，比 API 上拿到的、装在太阳能板上的小监测器**精度高得多**。还可能有表后问题（behind the meter）、用户家中问题、vampire load 等。"typically most of the time the utility is going to win if they say this is what the meter said."
- **首几个月的"惊吓"**：多源于前期被误导/不理解——本以为完全没账单、或以为全额 retail 回购但实际只拿 avoided cost。但**连续看几个月后不应再有大惊吓**，因为是按月监控的。
- **早期采用者更懂账单**：5 年前的早期采用者很清楚账单；如今大问题是 **installer / developer 的不良销售实践**承诺过大节省，导致预期与实际严重不符。若用户事先联系 utility，理解通常较好；若依赖卖产品/安装的人，则充满 misinformation。

### 七、利用 AMI / 第三方取数的现实障碍（重要落地拦路点）

- **评估容易、拿到数据很难**：受访者认为 Casally 评估 AMI interval 数据不难，但**拿到手非常难**——没有自家监测设备就基本拿不到实时 AMI 数据。"getting your hands on it would be very different... not data I think you'd be able to really get your hands on without having your own monitoring device."
- **历史 vs 实时的差别**：用户可授权提供过去 12/24 个月账单数据用于建档；但"上月发生了什么、正在发生什么"这类实时数据是 **proprietary**，utility 出于财务、cyber security 等顾虑**不会共享**。"that's going to be tough to get."
- **→ 这是受访者眼中本产品最大限制**：见"产品方向建议"中的总评。
- **AMI 数据本身不延迟**：AMI 通过无线电/蜂窝信号（部分光纤硬连）+ 各处采集点，实时回传；utility 可近乎瞬时知道停电与恢复。延迟不是问题，"they get it pretty quickly."

### 八、住宅成本敞口排序（行业事实）

- **最大峰驱动 = 气候控制（AC / 制热）**，"almost always the main driver of peak"（加州部分地区不那么突出）。
- **第二 = 巧合性同时用电（coincidence）**：人们同一时间回家、开灯、做饭、洗衣等同时启动负荷。对策是把这些负荷错峰摊开。
- **EV 充电**是产品方提的主要敞口之一；受访者补充 AC/制热与回家巧合负荷是更主要峰驱动。
- **洗衣机/烘干机**：用户常以为洗衣很费电——受访者说"a lot is relative"，关键看 critical peak pricing 下的 delta；可对"典型洗衣机+烘干机"算通用数字提示"现在洗 vs 夜里洗"的差价，哪怕只是 critical peak 时段的一条提醒也有用。

### 九、C&I（商业/工业）差异

- 当前 demo 面向 residential 合理、计算"nothing crazy / pretty straightforward"。
- 若扩展到 commercial / industrial（C&I），**缺失的一大块是 peak demand charging（需量电费）**——但那会引入大量额外内容。residential 场景下不需要。

## 对产品方向的专业建议

- **锚定"过去账单 + 当前费率方案"设目标，合理、摩擦不大**：演示中以"过去三个月账单 + 当前 rate plan"给出推荐区间、不让用户填任意数字，受访者认为"very reasonable"——$200 账单的人不能选 $100（永远达不到）。
- **"容差边界 / 避免账单意外"而非"压到最低"的定位是好起点**："hitting a target I think is a great start."保持高层级、简单——避开 tariff/TOU 的复杂性正是其价值。"keeping it at that high level... helps a lot of people."
- **同时提供"优化"开关**：可让用户选择按纯财务/降能耗自动优化（两种都行：reduce energy consumption 或 reduce cost）。"you could almost have both."
- **强调"给选择、非全自动"**："it's not they push a button and the house automates itself. It's just giving them choice."并支持前置决策树/默认设置（如默认 EV 凌晨充电）。
- **2026 年用户期待自动化/AI**："I think there is some type of expectation of automation... even if you just make it up and say it's AI... I think that would be appreciated by consumers."→ 受访者建议至少呈现 AI 优化感。
- **执行建议中应包含潜在财务影响（potential financial impact）**，但别太复杂。示例："charge now = $3 vs charge at 9pm = $27"。**注意反面风险**：若只省几美分（"three cents"），可能让用户觉得不值、反而 discouraging。
- **执行建议层级保持简单**：三段式"what happened / what's matter / what to do next"很好；过深细节正是 tariff 困惑来源，连他这种专业人士作为个人用户也更想要简单格式。
- **明确分离"行为节省"与"账单官方核算"**：受访者强烈赞同（"Yes. Yeah."），因为这是当前计费的巨大困惑点；要把 fixed costs（如 minimum charge）讲清"永远不会消失"。
- **节省归因按系统类别拆分（EV/solar/powerwall）= 好**，避免黑箱、可解释。
- **generation 与 delivery 侧节省尽量分开**：delivery 用户"被绑定"，但 generation 在去管制空间可货比三家，分开有价值。
- **账单页按"固定项 vs 可变能源项"分组**：把 basic service charge、wildfire fund 等固定项归一组（用户无法改变），可变能源归一组，让用户清楚"哪些永远改不了"。逐年趋势展示是"very cool feature"。
- **学习各 utility 官网 sample bill / "how to read your bill"**：看它们重点解释哪些项，能获得洞见。设计 ledger 时也照此分层（fixed charge / energy charge，delivery 与 generation 分开）。
- **市场选择：先 California，再考虑 Texas**：聚焦一个区域（先西海岸，别先跳东海岸，做法差异大）。**California 是最大市场；Texas 机会与电力活动最多、平台最开放、发电选项多，但超级复杂、规则怪异**。"if you're starting in California and Texas, those are the two most exotic / different places... works there, it's going to work anywhere."其余州一旦建好，"上传 tariff 信息"即可套用。
- **建议引入有 utility billing / ratemaking 背景的人**：不必日常全职，但要在"前期、中期、后期"把方向想对（"are we thinking about this correctly before we go into it"）。实现本身一旦搞清公式"not crazy"。受访者提醒：**billing 结构全美大体相同，但每个州/utility 各有独特做法**；需要熟悉加州具体各 utility 计费的人（产品方此前请教的科罗拉多专家不懂加州体系）。

## 技术 / 政策 / 术语（简要解释，按原文）

- **interval data（间隔数据）**：按固定时间间隔记录的用电/功率数据；美国主流 15 分钟，AMI 可到 5 分钟。
- **AMI（Advanced Metering Infrastructure，智能电表基础设施）**：通过无线电/蜂窝/光纤 + 采集点实时回传 interval 数据，支撑 TOU 计费并实时感知停电。
- **TOU（Time of Use，分时电价）**：按时段定价，美国峰谷差大（峰时可达谷时 2–4 倍）；在美多落在 delivery 侧。
- **critical peak pricing（关键峰价）**：极端高峰时段的高电价；加州可达 50–75 cents/kWh。
- **NEM（Net Energy Metering，净计量）1/2/3**：加州太阳能并网回购的三代规则，含 true-up 结算；受 CPUC 监管的 IOU 须遵守，市政/公营（LADWP、SMUD 等）可自定。
- **true-up（净计量结算 / 年度对账）**：净计量用户的周期性结算；NEM 文件中规定（受访者不确定月度还是年度）。
- **avoided cost（避免成本）**：低于零售价的回购费率，常用于超额上网电量结算。
- **fixed service charge（固定服务费） vs variable energy charge（可变能源费）**：加州去年秋立法上调固定、下调可变，传统约 25/75 正反转。
- **HDD/CDD（heating/cooling degree days，制热/制冷度日数）**：以 65°F 为基准的气候归一化指标，用于天气归一化负荷与节省计算。
- **fuel adjustment / fuel adder（燃料调整附加费）**：随燃料价格浮动、无需走完整 tariff 审批的可变附加费，可达账单 5%–10%，是用户"为何账单更高"的常见困惑源（受访者不确定加州适用程度）。
- **bidirectional meter（双向表） vs separate import/export meters**：决定 import/export 是净计还是分别计量。
- **revenue-grade metering（计费级计量）**：容差严、带宽窄，精度远高于 API/太阳能板小监测器；账单争议中"以表为准"。

## 合规 / 认证路径

未涉及（FCC/NRTL/UL/DOE/Prop 65 等本访谈未触及）。受访者提及的更多是数据获取的 proprietary / cyber security / 财务顾虑，而非产品认证。

## 监管 / 门槛与成本

- **数据获取门槛（核心障碍）**：实时 AMI / 计费级数据为 utility 专有，出于财务与网络安全顾虑不对第三方共享；历史账单需用户授权获取。
- **加州固定费立法（去年秋）**：监管层面将成本回收从可变向固定迁移，受访者预期持续并扩散至更多州。
- **CPUC 管辖差异**：IOU 须遵守 NEM；市政/公营 utility 不必，规则各异。
- **认证/合规具体费用、周期、地区差异**：未涉及（未量化）。

## 风险 / 坑 / 现实障碍

- **最大限制：拿不到整户实时用电/AMI 数据**。无硬件则难知整户真实 consumption，而这是重建账单与算 counterfactual 节省的关键前提；这是受访者眼中本产品当前最大挑战。"how do you get that information without hardware of understanding how consumption is actually happening at the residence?"
- **installer/developer 不良销售**：夸大节省、"装太阳能就没电费"，造成预期落差——正是产品要解决的痛点，也是市场机会。
- **省太少反而 discouraging**：财务提示若金额过小（几美分）可能打击用户。
- **设备精度差异**：API/板级监测器精度远低于计费级电表，账单核对时易出现看似"不符"实则计量级差异；真异常通常"差异很大、容易看出"。
- **DST / true-up 月度还是年度 / tier 与 TOU 先后 / settlement 走 NEM 还是 net billing**：受访者明确不确定的点，落地前需另行确认权威来源。
- **硬件安装门槛**：开 panel 类设备出于保险考虑总建议请电工；受访者不知有无"免电工、用户自装"的消费级产品，建议作为一项 research。
- **C&I 扩展需补 peak demand charging**：residential 模型直接套商工会缺需量电费。

## 异常分级建议（受访者给出的具体阈值）

- 多数事物有几个百分点的容差；**>3% 标黄（yellow）、>5% 标橙（orange）、>10% 标红（red，"that's not right"）**。3% 常作为损耗等差异的默认值。

## 关键金句

- "you'd need the actual energy consumption of the premise." —— Mike
- "in today's world... everything has an app already, everything has an API, it's just use it if you have it." —— Mike
- "it's not they push a button and the house automates itself. It's just giving them choice." —— Mike
- "the critical peak pricing could be 50 cents, 75 cents. I mean, it can be very, very expensive." —— Mike
- "this is just what it is... your bill is never going to go below this." —— Mike（论固定费用）
- "it used to be like... 75% 25%... that's starting to flop on its head, like almost completely turning over." —— Mike（论加州固定/可变结构反转）
- "whatever the meter says is what it is... typically most of the time the utility is going to win if they say this is what the meter said." —— Mike
- "getting your hands on it would be very different... that's not data I think you'd be able to really get your hands on without having your own monitoring device." —— Mike
- "if you're starting in California and Texas, those are the two most exotic... places from a utility standpoint we've got. So works there, it's going to work anywhere." —— Mike
- "the utility industry is 5 to 10 years behind everybody else." —— Mike
- "Not this simple. And simple is not a negative in that context." —— Mike（评价产品）
- "if it's above 5% it's orange, if it's above 10%... yeah, that's not right." —— Mike（异常分级）
- "I'm always very open to that... looking for engineering support, tariff bill support, please don't hesitate to reach out." —— Mike（顾问意向）

## 行动项 / 机会点

- **解决整户用电数据缺口**：第一阶段靠设备 API + 用户授权的 12/24 个月历史账单可建档；实时整户 consumption 难，第二阶段硬件（CT clamp / collar meter / 整户套件）是关键 enabler。受访者认为这是产品能否"把账单串起来"的限制点。
- **取数策略**：放弃指望 utility 共享实时 AMI；走"用户授权历史账单 + 自有监测设备"路线。
- **counterfactual 引擎**：以 month-to-month + HDD/CDD 天气归一化为基线，纳入 tariff 变更，目标"defensible"；尽量取 ≥24 个月历史。
- **账单页设计**：固定项/可变项分组、generation/delivery 分开、对 fuel adder 等"为何变高"的项加一两句解释；参考各 utility sample bill。
- **异常提示**：对 export credit vs 账单不符用 3%/5%/10% 三级（黄/橙/红）阈值标记，并给"联系谁跟进"的引导。
- **市场顺序**：先 California，再评估 Texas；其余州靠上传 tariff 复用。
- **执行建议**：包含潜在财务影响、保持简单、对小额省钱谨慎呈现；提供"优化/AI"自动化感的开关。
- **团队**：引入熟悉加州各 utility 计费/ratemaking 的顾问，前/中/后期把方向把好。
- **待确认事项（受访者不确定，需另查权威来源）**：DST 在 TOU/计量中的处理、NEM true-up 月度还是年度、tier threshold 与 TOU 适用先后、settlement 走 NEM 还是 net billing、export retail/avoided-cost 块差异在加州是否出现。
- **顾问机会**：Michael 明确愿以私人咨询/advisor 形式（可走 Upwork）继续支持，提供工程、tariff、bill 支持——可推进为长期顾问关系。
