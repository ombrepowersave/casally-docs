# Michael Cade · 专业咨询 · 2026-03-14

> 说明：本摘要基于语音转录逐字稿提炼。逐字稿日期标头为 "Mar 13, 2026"，派发指令的显示日期为 2026-03-14，以指令为准。转录中多处明显同音/听错词已在内部还原本意并按下方"转录纠错记录"标注，未改原始 .txt。

## 受访者画像
- 加州能源监管领域资深人士，自述"我与加州监管机构打交道差不多有近二十年"（"I've worked with uh California regulators uh the better part of the last two decades"）。
- 工作层级在**大型工商业（large commercial and industrial）**层面，而**非住宅层面**（"that hasn't been at the residential level. That has been at the large commercial and industrial level"）。他强调自己是"通才"（generalist），覆盖面"很广但相对薄"（"a vast... pool that's very wide and sort of necessarily thin"）。
- 现居俄勒冈州（Oregon），监管工作主要面向 **CPUC**（转录写 "CPU"，推断指 California Public Utilities Commission）及其辖下三大投资者所有制公用事业（IOU，转录写 "IUs/IUS"）：**Southern California Edison（SCE/Edison）、San Diego Gas and Electric（SDG&E）、PG&E**。具体工作内容为监管层面的"写作、监测、报告与分析"（"writing and monitoring and reporting and analysis"）。
- 自评：对净计量（NEM）相关决策"在远处饶有兴致地旁观"（"watched from afar"），有自己的判断；但承认在具体住宅 rate schedule 的细节上"我的专业有限"（"there's a a limit to my expertise on these particular rate schedules"）。
- 邮箱（受访者主动给出，用于后续联系）：mike@calregulatory.com。
- 身体状况：自述视力与听力均不如从前（"My my vision is not what it used to be"，"My hearing isn't the greatest"），访谈中数次请求放大屏幕、重复问题。

## 主题判定
判定为 **专业咨询**。依据：受访者作为加州能源监管资深从业者，全程围绕 Casally demo 的费率/计费建模问题给出行业知识与判断（费率变更机制、NEM/NBT、ACC、非旁路费用、PSPS、CCA 等），并就产品方向、团队配置、合规与数据获取给出建议。访谈不在于采集其个人作为"用户"的痛点，而在于借其监管专业为产品建模与方向把关。

## 核心提炼

### 一、专业观点 / 行业知识点

**1. 加州费率变更的频率与机制**
- 住宅费率每年"大约 2 到 3 次"在"重大层面"变更（"two to three times a year um on a major level for each of the three utilities"）。
- 最重要的一次是 **1 月 1 日**，即年度电费 true-up（"annual electric true up"），"大家都盯着这一次"。
- 此外今年三家公用事业还在 **3 月 1 日**做了更新；**10 月**也可预期会有更新。
- 费率变更通过向 CPUC 提交 **advice letter（建议函）** 这一程序载体实现（"the procedural vehicle that they file"）。

**2. General Rate Case（一般费率案）两阶段结构**
- 公用事业在一般费率案中申请一笔 **revenue requirement（收入需求）**，金额常常巨大，"比如 90 亿之类"（"like, you know, 9 billion or something"）。
- 两阶段：第一阶段委员会决定总盘子（批多少、disallow 多少百分比）；第二阶段决定如何在各 customer class（客户类别）间分摊，"有些被打得更重，有些过得轻松"。
- 流程"拖上数月、有时超过一年"，非常技术性；最终裁决后公用事业用 advice letter 落地 final decision 中的确切指令。

**3. 加州费率体系的极度碎片化（受访者反复强调的核心判断）**
- 加州"离谱"（"bonkers"）在于费率变更不止来自 general rate case。还有：**rate design proceedings（费率设计程序）**、**rulemakings（规则制定）**（举例 demand flexibility proceeding，含 income graduated fixed charge 收入分级固定费用构想）、**procurement proceedings**（称 energy resource recovery account proceedings，ERRA 采购程序）。
- 比喻："像一片小行星带，各种东西朝你飞来"（"it's like this asteroid field of things coming at you"）；因体量与复杂度，必须"非常密切地盯防"。
- 横向对比：他合作过的、在全美 50 州工作的经济学家说**加州是 50 州中最复杂（最 convoluted）的**；Missouri、Illinois 等地"基本上一份 filing 黑白分明，一年走完就定了"。Texas 也**不简单**（"Texas isn't super simple"），但他对德州市场不太熟，只知其有"海量的 solar 和 storage"。

**4. 可信费率数据源 / 构建可靠 tariff engine 的方法**
- 最佳做法：安排人**监测所有变更的生效时点**，并查阅 advice letter filings 中附带的 rate schedules。
- 这些 filing 里有"巨大的费率表（massive rate tables）"，列出某日（如 3 月 1 日）生效的 illustrative rates。
- 过程"非常费力、枯燥"（"a very painstaking um dull process"）：要找出 app 用户各自所在的具体 rate schedule，再确保数据更新到位。

**5. 非旁路费用（Non-Bypassable Charges, NBC）—— 计费准确性的关键易漏项**
- 账单不只为能源（energy）付费，还有 **non-bypassable charge**：即便把 NEM 用量降到零也躲不掉（"even if you reduce your net energy metering usage to to nothing, you still can't escape this non-bypassable charge"）。
- 塞进 NBC 的项目包括：**grid hardening 与 wildfire（电网加固/野火）费用**；**Public Purpose Program 附加费（转录写 "PPP search charge / public purpose sir charge"，推断为 Public Purpose Program surcharge）**，其中含低收入项目、能效项目、研发；**nuclear decommissioning（核电退役）费用**。
- wildfire fund charge 另来自**立法（legislation）**。
- 核退役细节：加州除 **Diablo Canyon** 外已退役其核电站，含 **SONGS（San Onofre Nuclear Generating Station，转录写 "Sanafay/San Anifay"）**；其退役费用分摊进 NBC 出现在客户账单上。
- 受访者由此总结："你不只是在为电付费，你是在为体现在账单里的政策决定付费"（"you're not just paying for um electricity, you're paying for policy decisions that show up in your bill"）。
- 可行性判断：查清这些费用的确切构成与"全部范围"是**可做的（doable）**，可建立追踪。

**6. NEM → NBT（Solar Billing Plan）转变的监管动因**
- CPUC 官方说法：他们认为为这些"电子"付得太多（"they were paying too much for those electrons"），并主张造成 **cost shift（成本转移）**——未参与 NEM 的客户或低收入客户被不当加重负担。
- 受访者**个人观点（明确标注其自认为是 outlier / 非主流）**：他倾向认为成本转移"没那么严重"，认为加州的**根本问题是费率设计（rate design）本身**，多个程序里都存在成本转移，不止 NEM；因此他觉得 cost shift 有点像"red herring（转移视线的幌子）"。但他声明"我不是经济学家"，这是"从远处的解读"。
- 他进一步判断这本质是**政治性程序**："公民侧分布式发电（distributed generation）" 对阵 "大型公用事业 solar（large-scale utility solar）"，从集中式监管/公用事业视角看，"许多人会说大型 solar 和集中式力量赢了这场较量"。他重申这是 outlier 观点，"很多人确实相信成本转移很严重、NEM 客户拿得太多"。

**7. NEM 各代计费机制（受访者当场查阅自己笔记后给出）**
- **Legacy NEM（NEM 1.0 / 2.0）**：按月 **kWh netting（千瓦时净计量）** + **annual true-up（年度结算）**，出口按 **retail（零售）费率**补偿（retail export compensation）。
- **NBT（Net Billing Tariff，即 NEM 3.0）**：**无 netting**；出口 credit 以**美元（dollars）**计；基于 **avoided cost values（避免成本值）**。
- 出口补偿基于 ACC，为**逐时（hourly）避免成本费率**，做**月度平均（monthly averaging）**，并按**工作日/周末（weekday or weekend）区分**。
- 两者"我相信都有 annual true-up"（"I believe they both do"——受访者标注不完全确定）。
- 用户复述确认并获认可的结论：**在 Solar Billing Plan 下，出口 credit 由 ACC 信号驱动，而非零售 TOU 费率**（"Net billing tariff that that is guided by the avoided cost calculator. ... Previously they were compensated at retail uh rates"）。

**8. Avoided Cost Calculator（ACC，避免成本计算器）**
- TOU 时段的时间变化信号由 CPUC 使用的工具 **ACC** 编排计算（"these time variance signals... are calculated using this avoided cost calculator"）。
- 更新频率：受访者"相信"约**每两年（every two years）**更新一次（多次自我标注不确定："I believe... I think"）；所以引用其数据的系统这一部分也需每两年刷新。
- CPUC 有一个页面公布历年（"回溯到他们开始使用以来"）各年的 ACC 值；受访者表示会发链接（"There's a link at the CPU that has the updated ACC values"）。
- 2022 年 CPUC 重新设计 NEM tariff 时，为三家 IOU 各**指定了三个特定 schedule**（"designated three specific schedules for the three IUS"）。

**9. ACC Plus Adders（ACC 加价补贴）**
- 重设计时为各家公用事业设了所谓 **ACC plus adders**，作为 NEM 客户向新 NBT/NEM 3.0 过渡的"缓冲奖励"（"a little um reward to soften the blow"）。
- 形如小额支付，"比如每千瓦两美分左右"（"like uh... two cents a kilowatt or something"——受访者用"or something"标注为约数），随年份**递减直至归零**。
- **例外：SDG&E 未获此 adder**。因为委员会认为圣地亚哥地区 solar 使用极重、电价高，经济上不需要为 SDG&E 创建这一"glide path（平滑过渡路径）"。

**10. Vintaging（"代次锁定"）—— 用户主动提出、受访者认可为关键但未给确切答案**
- 当 ACC 更新时，对现有客户是否立即生效：**"实施允许多快就多快地生效"**——公用事业提交 advice letter 纳入更新、CPUC 授权后费率生效；会有**提前预警（advanced warnings / heads up）**，不会"某晚一开关就变"。
- 客户是否被**锁定在安装时所处的 ACC 版本（vintaging）**：受访者**当场不记得 vintaging 具体如何运作**（"offhand I don't remember exactly how the vintaging works"），但确认"我知道存在一套 plan，特定 tariff 上的客户会处于特定 vintage"，并主动表示可查证回复。他评价此问题"会直接影响 app"。

**11. PSPS（Public Safety Power Shutoffs，公共安全断电）/ De-energization**
- 受访者认为这"又是个非常政治化的领域"，并给出**个人判断**：公用事业"在管理与平衡电网上做得不够高效"。
- 触发：野火威胁——若预判植被在干热条件下可能起火、对某区域某杆塔的植被管理有足够担忧，可能**主动预防性断电**。整体"从立法机构一路向下都是混乱的决策的下游产物"。
- **预警时长不一致**：用户提到有人提前 24–48 小时被通知、有人几乎无通知。受访者证实"我听过一模一样的说法"，称公用事业为此"在 CPUC 多个程序里被狠批"（messaging 不一致、有时完全无 messaging）；其股东因此**承受递增的处罚（penalties）**，"不只是打手腕"。监管层在认真对待，但"始终在追赶现实"，体系"非常不完善且混乱"。理论上有一套应遵循的"相对提前的预警"系统；他认为**并非三家 IOU 都做得好**，且**逐年表现不一**。
- PSPS/停电数据来源：受访者**不确定**告警具体由谁/从何处发布，但认为公用事业有此责任、"很容易查清"，且理论上三家公用事业网站上都应有 **outage maps 与 PSPS map 式架构**——但他坦言要"更仔细查"，"当下不记得"。他建议 Casally 可对接州监管的 de-energization 告警/公用事业的相关 messaging 存储处。
- 医疗脆弱人群：PSPS 把有医疗设备者置于危险境地；公用事业设有**针对 medically vulnerable 人群的强化流程**，尽力掌握谁属此类并予以照顾，这一点"常受审视（scrutiny）"。
- 无后备者的处境：若无 generator，"基本只能认栽"。受访者举自身在俄勒冈的经历——曾连续约 **10 天无电**，靠壁炉和保暖衣物度过。
- 趋势判断：因 PSPS 而装电池的 solar 客户"越来越多，是非常明智之举"——为了 **resiliency（韧性）**，"不管发生什么都能正常运转"。

**12. CCA（Community Choice Aggregators，社区选择聚合商）与 PCIA**
- CCA **不在 CPUC 管辖内**，作为公用事业的某种"竞争者"，向客户承诺以可负担成本提供清洁/可再生电力，但仍由公用事业用其 poles and wires 输送。
- CCA 客户被收取 **PCIA（Power Charge Indifference Adjustment，电力费用无差别调整）**——受访者称这本质是离开系统者的 **"exit tax / exit fee（退出费）"**；离开 PG&E 或 SDG&E 系统的客户在账单上被评定此费，款项归 incumbent（在位）公用事业。
- 因此 **CCA 客户账单"看起来不同"**：多数公用事业客户是 bundled（捆绑，各项服务卷入公用事业账单），而 CCA 客户被单独处理并叠加 PCIA，在 tariff 中也体现不同——这是受访者会专门在 tariff 中留意的项。

**13. NEM 3.0 True-up（年度结算）**
- 太阳能家庭月度跟踪不够，需 true-up 做年度结算以确定真实年度结果（此为用户陈述，受访者认可方向）。
- 受访者理解：NEM 3.0 下大致**以美元结算（paid in dollars）**；先前安排下若符合条件则是**以 kWh 计的账单 credit**（受访者标注"That's my understanding of it"）。
- 滚动月度预测 true-up **是否可行**：受访者认为"可以得出一个或多或少准确的公式"，但"可能不会超级简单"；这是一门"imperfect science（不完美的科学）"，但**可建立有用的近似（a useful approximation could be built）**。

### 二、对产品方向的专业建议

- **总体评价积极但聚焦于"准确性 + 持续维护"**：多次称 demo "看起来很棒、设计优雅、已接近可用"（"It looks great"，"a beautiful elegant design"，"It's very close"），并称若自己在加州会愿意使用。核心建议是**保证准确性、持续刷新数据**——盯紧 rate cases、advice letter filings、ACC 更新，并留意各类 NBC。"这都是工程问题，可做，只是复杂。"
- **暴露计算逻辑 / 能源素养**：对 demo 中"展开计算逻辑的 bottom sheet"明确赞赏，称"非常促进能源素养（promoting energy literacy）"，会很有帮助。
- **行为归因的可行性**：把 avoided cost 归因到具体行为事件的设计，他认为"在加州会大受欢迎"、对人们既有用又"有趣"；现实上**可行（realistic）但不容易**，建议配 **2–3 名有能源经验的数据科学家**协助（不必是大团队）。
- **团队配置建议（受访者反复强调的最重要建议之一）**：团队技术/产品端"已就绪"，短板在 **tariff 侧（尤其加州）**。强烈建议引入懂"门道（knows the weeds）"的 **tariff specialist / 数据建模专家**，尤其精通 NEM 与 TOU 费率者。
  - 人才来源建议：在监管程序中**代表 intervening parties（介入方）的专家**是好猎场；点名 **TURN（The Utility Reform Network，转录写 "turn"）** 等 utility advocates/利益团体；并提到 **rooftop solar proceeding（屋顶光伏程序）** 是值得深挖、聚集很多聪明人的领域。
  - 受访者主动表示其有"很好的 network"，认识比他自己更适合此事的人（NEM 专家"相对充足"），并称下周正好要和一位符合该条件的人交谈，愿做引荐。他自我定位为可帮"定位 tariff 及其时点"，但不做具体 rate schedule 细节。
- **硬件方向（第二阶段构想）**：用户提出未来或加硬件（连接电盘/solar/smart meter）以提升数据准确性、做实时监控。受访者反应正面，类比为 **"virtual power plant（虚拟电厂）"**，喜欢 smart meter 这一点，称"让机器互相对话"。
- **数据获取/隐私的合规提示**：关于获取公用事业 meter/用电数据，受访者称"部分公开可得，部分可能要争取一下（may have to fight for it）"；明确存在公用事业/委员会**非常重视的 data privacy 问题**，会有一定限制，但他不确定限制有多大；表示需更深入研究。

### 三、技术 / 政策 / 术语（简要解释，依原文）
- **NEM（Net Energy Metering，净计量）**：分 1.0 / 2.0（legacy，零售费率补偿、kWh 月度净计量 + 年度 true-up）与 3.0。
- **NBT（Net Billing Tariff）= NEM 3.0**：无 netting，出口以美元 credit、基于 ACC 逐时避免成本、月度平均、按周末/工作日区分。
- **ACC（Avoided Cost Calculator）**：CPUC 用于编排 TOU 时间变化信号与出口补偿的工具；约每两年更新；历年值集中在 CPUC 一个网页公布。
- **ACC Plus Adders**：过渡缓冲小额补贴，逐年递减归零；SDG&E 无此项。
- **Advice Letter（建议函）**：公用事业落地 CPUC 裁决、实施费率变更的程序载体；含 illustrative rate tables。
- **General Rate Case（一般费率案）**：两阶段（定总盘子 → 客户类别分摊）确定 revenue requirement。
- **TOU（Time-of-Use，分时费率）**：三家 IOU 各有独特 TOU 费率；2022 重设计时为三家各指定特定 schedule。
- **NBC（Non-Bypassable Charges，非旁路费用）**：含 PPP surcharge（低收入/能效/研发）、核退役、grid hardening/wildfire 等，无法规避。
- **PCIA（Power Charge Indifference Adjustment）**：CCA 客户的"退出费"，归在位公用事业。
- **CCA（Community Choice Aggregators）**：非 CPUC 管辖的清洁电力聚合商，公用事业仍负责输送；账单形态与 bundled 客户不同。
- **PSPS（Public Safety Power Shutoffs）/ De-energization**：野火预防性断电。
- **Vintaging**：按安装/tariff 把客户锁定到特定 ACC 版本/代次的机制（具体规则受访者未明确，待查）。

### 四、合规 / 认证路径
- **未涉及**（FCC / NRTL / UL / DOE 能效 / Prop 65 等硬件安规认证本次未讨论）。本次合规相关内容仅限**数据隐私**层面（见上"数据获取/隐私的合规提示"）。

### 五、监管 / 门槛与成本
- 本次未讨论认证费用/周期/谁买单等硬件合规成本。
- 监管层面的"成本/门槛"体现为：加州费率体系的**极端复杂度与高维护成本**（需专人持续监测多类程序与 filing）、数据刷新节奏（费率 2–3 次/年、ACC 约 2 年/次）、以及对 tariff 专家人力的依赖。
- 地区差异：加州为全美最复杂；多数州简单（一份 filing、一年定案）；Texas 亦不简单。

### 六、风险 / 坑 / 现实障碍
- **数据管道刷新滞后（受访者最先点出的风险）**：第三方费率 API 的 rate data pipeline 可能"不会像现实中那样频繁更新"，需核实其刷新频率——"是一年一次，还是 2–3 次"，这会显著影响用户体验到的准确性（"could make a big difference in terms of accuracy"）。同理 ACC 数据需约每两年刷新。
- **遗漏非旁路费用**会导致账单重建不准；必须把 NBC 全量纳入第三方数据拉取。
- **费率体系碎片化**（"asteroid field"）导致需持续、密切盯防多类程序。
- **Vintaging 处理不当**会使 legacy NEM 客户账单形态判断出错——受访者明确这"会直接影响 app"。
- **加州落地难度**："可做但不容易"，反复强调需要懂行的 tariff 专家与工程化方案；缺此专家是当前团队最大现实障碍。
- **PSPS 数据源不确定**：告警发布渠道（utility API / 公共告警 / 邮件）受访者不确定；实时停电数据三家 IOU"能力水平不一"，理论上有 outage/PSPS 地图但需进一步核实。
- **数据隐私限制**：获取用户用电数据存在监管限制，部分数据"要争取"，限制范围未知。
- **受访者自身专业边界**：他是监管通才、非住宅 rate schedule 细节专家，多处明确"需查证后回复"（vintaging、TOU 映射具体做法、出口 credit 应用于 energy charge 还是 total bill、ACC 值发布位置等），不应把这些当作已确证事实。

## 关键金句
- "I've worked with uh California regulators uh the better part of the last two decades." —— Michael Cade
- "that hasn't been at the residential level. That has been at the large commercial and industrial level." —— Michael Cade
- "it's like this asteroid field of things coming at you and so it definitely needs um to be watched over very closely because of its complexity and because of the sheer volume" —— Michael Cade（论加州费率体系碎片化）
- "even if you reduce your net energy metering usage to to nothing, you still can't escape this non-bypassable charge." —— Michael Cade
- "you're not just paying for um electricity, you're paying for policy decisions that show up in your bill." —— Michael Cade
- "I tend not to believe that the cost shift was that severe. I think the overarching problem in the state is the rate design itself. ... for me, the cost shift I thought was a little bit of a red herring, but I'm not an economist." —— Michael Cade（明确为其个人 outlier 观点）
- "citizen generated distributed generation uh was pitted against large scale utility solar ... many would argue large scale solar and centralized uh forces won that battle." —— Michael Cade（个人观点）
- "Net billing tariff that that is guided by the avoided cost calculator. ... Previously they were compensated at retail uh rates." —— Michael Cade
- "by far California is the most convoluted of all 50 states." —— Michael Cade（转述其在 50 州工作的经济学家朋友）
- "It's it's doable just not easy." / "It's very close. It's a great idea. It just it needs some tweaking." —— Michael Cade
- "you've nailed the technology side. ... It's just that that's the complicating thing, the tariff side." —— Michael Cade
- "that's really promoting energy literacy." —— Michael Cade（评 demo 暴露计算逻辑）
- "most importantly, I'd like to help you guys find someone who's uh you know, a a tariff specialist, especially with these NEM rates and time of use rates." —— Michael Cade
- "Almost like a virtual power plant or something, you know? I like that." —— Michael Cade（评硬件构想）

## 行动项 / 机会点
- **核实第三方费率 API 的刷新频率**：是否覆盖每年 2–3 次（1/1、3/1、10 月）的更新；若仅 1 月一次则准确性存疑。
- **确保 API 拉取全部 NBC**（PPP surcharge、核退役、grid hardening/wildfire 等）及 ACC 值，并建立按生效时点的追踪。
- **ACC 数据约每两年刷新**一次；向受访者索取 CPUC 历年 ACC 值汇总页链接（受访者已承诺发送）。
- **招募/对接 tariff specialist + 数据建模专家**（尤精 NEM/TOU、加州）：受访者主动提供 network 引荐，并称下周与一位符合条件者交谈；可顺其引荐，并探索 TURN 等 utility advocate、rooftop solar proceeding 圈子。
- **待受访者回复确认的开放问题**（当前不可当作事实）：① vintaging 具体如何把客户锁定到特定 ACC 版本；② TOU 费率对 interval data 的具体映射方式（直接映射还是聚合后）；③ 出口 credit 在 NBT 下是应用于 energy charge 还是全部费用后的 total bill；④ PSPS 告警/实时停电数据的官方来源与 API 可得性；⑤ 获取用户用电数据的数据隐私边界。
- **保持联系渠道**：受访者邮箱 mike@calregulatory.com，明确表示有 bandwidth、愿持续参与并就 advice letter 检索等随时答疑；用户已表达希望其深度参与产品共建。
- **市场拓展启示**：先攻最难的加州，受访者认为之后其他州"会显得很轻松"；Texas 亦不简单但 solar/storage 体量大，是好市场（受访者对德州不熟，此为其大致印象）。

---

### 转录纠错记录（仅在正确词几乎无歧义时内部还原，未改原始 .txt）
- "CPU" → **CPUC**（California Public Utilities Commission，上下文为加州监管委员会）。
- "spam panel" 未出现；"name three / M3 / NM" → **NEM 3.0**；"N3" → **NEM 3.0**。
- "ICE / SGE" → **SCE（Southern California Edison）/ SDG&E（San Diego Gas and Electric）**（上下文为加州三大 IOU）。
- "avoided cost calculator" 多处被转录为 "world cost / volt cost / avault cost / bold cause / a cost calculator" → 统一为 **Avoided Cost Calculator（ACC）**。
- "NBT" 多处保留；"net billing tariff" 即 NBT = NEM 3.0。
- "Sanafay / San Anifay generation station" → **SONGS（San Onofre Nuclear Generating Station）**。
- "turn / the utility reform network" → **TURN（The Utility Reform Network）**。
- "PPP search charge / public purpose sir charge" → **Public Purpose Program surcharge（推断）**。
- "TRUA / true up" → **true-up（年度结算）**；"HTOU / HTU / visa HTU period" → **TOU period（分时段）**。
- "PCIA"（power charge indifference adjustment）、"CCA"（community choice aggregators）、"PSPS"（public safety power shutoffs）按上下文规范化。
- 涉及数字均按原文保留并标注约数：revenue requirement "9 billion or something"、ACC adder "two cents a kilowatt or something"、ACC 更新 "every two years"（受访者自标不确定）、断电 "10 days"、预警 "24 48 hour"。
- 受访者多次明确表示对若干细节"不确定/需查证"，相应内容已在正文标注，未当作既成事实。
