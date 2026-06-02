# Harry Jackson · 硬件（hardware） · 2026-05-24

## 受访者画像
- 教育背景为机器人工程（robotics engineering），但职业多落在更动手的「生产工程 / 机械」类岗位；自述目前是技师（technician）角色，主动从管理岗退回到一线动手工作，因为「It's just what I like」。
- 自评工作内容更偏电气工程一侧，而非计算机工程或机械工程；用他自己的话形容，更像「a facilities manager who has electrical engineering experience」。
- 现就职于 SPAN（智能电气面板公司），入职约两年半（"two and a half years"）。SPAN 做家庭电子与能源行业相关产品。
- 居住在旧金山以南的半岛（peninsula），曾在加州经历过预防性停电；自述属于 PG&E 服务区域语境。
- 多次强调自己只讲非机密内容、不代表公司全貌：「I don't have the full picture right of everything that goes on in my company or in the like you know the manufacturing process」。SPAN 面板属公开销售产品，他认为相关信息「isn't confidential / isn't proprietary」。

## 主题判定
判定为 **hardware（硬件）** 主题。依据：来自 s5-Hardware1.0 系列，且正文通篇围绕硬件——SPAN 智能面板的结构（继电器替换铜母排）、实验室测试与安全失效、试验台搭建、火灾隐患合规、原型到量产周期、安装兼容性、智能断路器对比、以及硬件采用经济学。内容与目录主题高度吻合，slug 用 `hardware`。

## 核心提炼

### 一、技师日常 / 实验室职责（硬件需求与资源约束）
- 角色定位：听各工程师团队提需求，用有限资源同时满足大家。受限资源具体包括：建筑空间、预算、以及「整栋楼可用的安培数（amperage）」。
- 不同测试对供电需求差异大，有些需要从电网源（grid source）取到他们能拿到的「full capacity」。日常很大一块是「budgeting all that」——分配这些资源。
- 亲手搭建大量测试夹具 / 试验台（test fixtures）。
- 兼管物流：货运（freight shipping）、设备校准（calibration），自己做不了的就外送到别的车间。

### 二、最棘手 / 最有意思的事：消防合规与「移动化」绕法
- 不同设备受不同消防规则（fire marshall）约束；某些测试装置会被视为「fire risk」，不许放在楼内。
- 关键洞察（受访者亲历并主导）：同一套东西，**装在固定墙面（static wall）上**消防不乐意（尤其若非持证电工安装则被视为火灾隐患）；但**放到可移动的小车（cart）上**，「god forbid it catches on fire, you can just send that outside」，就突然合规了。
- 他主导的大事：找到一个经济的方案，把所有约 **800 磅**的电池（如 Tesla Power Walls、Franklin 电池等家用备份电池）装上小车，仍可接入测试装置，并通过消防检查（pass fire inspection）。
- 涉及品牌（受访者原文）：Tesla Power Walls、「Franklin batteries」（他不太确定确切叫法，"whatever they call them"）。

### 三、让实验室逼近真实家庭环境（硬件需求 / 供电搭建）
- 「There's ways you can do it cheaply. There's ways you can do it safely. There's ways you can do it quickly. ... sometimes you have to pick two of the three.」（便宜 / 安全 / 快，三选二）
- 美国家庭典型供电：240V，100A 或 200A。
- 楼宇侧供电为「483 phase and a transformer in the right place」——此处疑为转录有误：很可能是「480V 三相（480, 3-phase）」（原文转录为 "483 phase"，标注存疑）。从该楼宇供电造出家庭级 240V/100–200A 服务。
- 他亲自提供劳力：寻找变压器、必要时从总断路器（main breaker）拉新电路到变压器位置、把变压器用防振垫（anti-vibration pads，原文转录为 "antiibration"）固定进混凝土。
- 合规自律：自己不是持证电工（not a certified electrician），但做法要让「如果一个持证电工来做检查，他们挑不出毛病」。

### 四、被测设备：SPAN 智能面板的结构与测试场景（设备情况 / 集成）
- 产品定义（公开信息）：带「intelligence baked into it」的家用断路器面板（breaker panel），可远程开关电路、可监控每个所装断路器的能耗。
- 结构核心：整个面板背面是**计算机控制的继电器（computer controlled relays）**；把传统断路器（traditional breakers）插进去使用。即「我们把传统面板的铜母排（copper bus bars）换成计算机自动化继电器，再加上对每个 stab 通过电流的监控」。
- 他为工程师提供的是：放面板的位置 + 给到单户家庭可能拉取的全部电量（200A 至 240）。工程师再在不同场景下运行面板。
- 典型测试场景（他搭的辅助件）：
  - 模拟潜在停电——给一个按钮开关，一键切断 / 接通面板电流，而非物理剪线。
  - 电源切换——从电网源切到电池源（如 Tesla Power Wall 或当前市面其他电池），他提供计算机控制的继电器，让远程人员也能操作。
- 测试目标本质：让产品在「the most real conditions possible」下验证可靠性 / 行为 / 安全。

### 五、测试与验证 / 安全失效
- **浪涌 / 雷击模拟**：他做过一个模拟雷击（lightning strike）的试验台，要确保能承受「a surge of at least 3,000 volts very low current」（至少 3000V、极低电流的浪涌）；用高压测试仪（high pot tester，即 hipot tester）来模拟这种极高电压。
- 定位边界：SPAN 不是认证机构（"We are not a certification house ourselves"）。这些自测只是给产品「first basis」，确保送外部认证机构前一切正常，避免付费认证时间被浪费、避免遇到意外。
- **安全失效（safe failure）定义**（针对 SPAN 设备）：
  - 出现电源浪涌时，应「damage our device before it damaged any downstream loads」（先伤自己、不伤下游负载）。
  - 更理想的是：在损坏设备本体之前就先「trips our breakers」（跳闸保护）。
  - 保护层逻辑：SPAN 面板用传统断路器，断路器在面板实际铜体「之前和之后」都提供一层保护；他们只是把传统铜母排换成继电器加电流监控。

### 六、原型 → 量产周期
- 入职约 2.5 年间，亲眼见证一个产品从「absolutely nothing just an idea」走到「100 200 run manufacturing」（约 100–200 台的量产批次），用了两年半。
- 另有在研产品；从概念（concept）到首次量产（first manufacturing run）最快约 **6 个月**。取决于大家投入程度与协作程度。该在研产品是否公开发售 / 公开宣布尚不确定（他不便说）。
- 他借此点出品类难度：两年半的周期本身说明「this category is not easy」。

### 七、智能面板为何「重 / 笨重」——SPAN 的初衷（设备情况 / 集成）
- 公司使命：推动新建住宅的「electrification（电气化）」——把用气、用汽油的都换成用电。
- 痛点场景：家里厨房已用电、但供暖用气、车用汽油；若全面换成电热水器 / 电暖 + 电动车，不只是买设备的钱，还要**升级家庭基础设施**，把进户服务从 100A 升到更高。
- SPAN 面板的原始价值主张：升级进户服务比买 SPAN 面板更贵；SPAN 面板能在现有 100A 服务下**平衡各路负载**，让你「overload your panel」但仍能所有电器同时运行——面板替你做负载均衡。
- 他明确指出：**车队数据（fleet data）和户用能耗指标是「after the fact」后来才有的，原始意图就是让 100A 服务能超载运行并支撑全电器家庭。**

### 八、面板 vs. 智能断路器 vs. 更轻设备（硬件形态选择 / 个人观点）
- 替代形态：有公司做**智能断路器（smart breakers）**——把面板里所有断路器换成智能断路器，它们彼此通信、各自计量电流，可做负载优先级调度（如白天降权 EV 充电以保 AC、夜间反过来；峰时把总用电降低 20–30% 以少付费）。「Those exist.」他认为这是个好市场，只是不是 SPAN 选的路线。
- **个人观点（明确标注为 his opinion）**：
  - 他不认为智能面板是让公用事业看到全民能耗的「答案」，并直言「I do think it's a bit of an expensive toy」（尽管他靠这家公司谋生）。
  - 他个人更看好智能断路器是「a pretty good idea」。
  - 「The panel itself is just it's just copper... it's just a big wire basically. You don't need to bake intelligence into it.」想加智能可以叠在上面。
- 但他也给智能面板一个工程合理性辩护（个人推测）：把所有潜在故障点集中到一个设备里，可能比让一堆小设备协同工作「more engineering efficient」。
- 对「更轻设备能否替代整面板」：承认有价值——一个能帮你均衡所有负载、从而用满你付费购买的服务容量的设备是有价值的，因为「people aren't going to be keeping track of how much energy everything in their home uses」。

### 九、面板/设备级数据 vs. 智能电表数据（集成 / 数据价值）
- 现状：智能电表（smart meters）已给公用事业整户级数据。他点名：Silver Springs Networks、Itron（原文转录为 "Ittron"，标注纠正）的无线表；数据走 mesh Wi-Fi 网络上报；PG&E 很看重。
- 面板/设备级数据的增量价值：能看到**单个电路（individual circuits）**在做什么，而非整户总量。
- 具体可回答的问题（neighborhood 级）：某时段回家的人里有多少 EV？多少家用电空调 / 电热水器？停电时该限哪个邻里——一个全靠空调 / 全靠电的邻里，还是更依赖燃气、受停电影响小的邻里？是否有靠医疗设备用电的住户？这类决策需要电路级数据。

### 十、安装与兼容性
- SPAN 投入大量资金把设备做成传统面板的**「drop in replacement（直接替换件）」**。
- 关键洞察——**安装者（installer / home builder）是关键决策人**：他同时面对公用事业和业主、给出建议；如果安装者觉得这东西「difficult / tedious / I don't care about it」，就不会推荐给任何人。
- 因此 SPAN 刻意做到易装：「same shape, the same size, just a little bit heavier」（仅因含继电器等略重于普通面板）。
- 即便是已装面板的住宅做**retrofit（改造）**，也是直接替换件，技师无需额外培训（"No additional training required"）。

## 采用经济学与品类判断（受访者重点反复处）

### 采用为何慢
- 「things that aren't broke don't get fixed」——面板能用、无强创新需求，要在这个市场打出名气很难。
- 智能面板市场不止 SPAN 一家，各家提供不同东西。

### 价值在业主侧还是公用事业侧（受访者核心论点，多次重申，明确为个人观点）
- **业主侧价值有限**：纯监控对业主而言，多数人拿到「a little more information about what your habits are」后并不会真改习惯；只有「energy conscious / 想 future-proofing」的人才会自掏腰包。
- **真正大钱在公用事业侧**：足够多 SPAN 面板成网后，能让能源商看到整个邻里乃至城市随时间的**负荷曲线（load curve）**，更高效地调用调峰电厂（peaker plants）。
- 价值机制（他举的例子）：傍晚 5 点大家回家同时开烘干机，城市需多上「100 gawatts（疑为口误，单位存疑）」。若都有 SPAN 面板，通过手机 Wi-Fi 能「看见」人们正在回家、正做导致大负荷的事，公用事业就能**提早**（如早 5 分钟）启动调峰电厂——更早的预知 = 更多与电厂议价 / 谈判电价的时间。「that's where the real value is in a smart panel network.」
- 商业模式推断（受访者自述设想）：中间的软件层（software layer）由 SPAN 提供分析，「We sell the data to the utility.」装了 SPAN 面板的业主数据汇总到 SPAN，再卖给公用事业（如加州 PG&E）。

### 谁买单 / 定价
- 数字示例（他自报为举例）：智能面板假设 \$3,000，同等负载的非智能面板可能 \$30——这是「10 times」差。多数业主 / 新房买家不会为此买单。
- 临界点（个人估计）：若是「dumb panel」的 **5 倍**而非 10 倍成本，且差额由**公用事业补贴（utility subsidy）**补上，才更可能被接受。
- 广泛采用的路径：靠**公用事业激励 + 给新房建造商的激励**让其装入新房，需要「individual benefits」与「utility subsidies」两头同时具备。多为新建住宅作为 feature 装入，老房升级的很少。

### 数据价值的转变（受访者亲述认知变化）
- 「A year or two ago, I probably wouldn't have said that data was so valuable, but um my eyes have been opened a little bit. ... data is ridiculously valuable.」

## PSPS / 停电场景下的价值（应用场景）
- 他原先不了解 PSPS（公共安全断电，Public Safety Power Shutoff），由访谈者解释后回应。
- 价值设想：相比对整城 / 整区「一刀切」断电，若住户有与公用事业通信的智能面板 / 智能设备，可只关 50% 负载，或让每个用户预设优先级（如「I need my refrigerator to stay running」，其余在停电时可断）。公用事业可下指令把这些户压到只剩高优先级负载——「a much better outcome than just having an unexpected power outage for an entire region.」
- 他本人经历过停电：在了解智能设备 / 家用备份电池前，「it just felt like a fact of life. It's like a storm is coming and you didn't know umbrellas existed.」想不被影响就得提前备好（电池等），但他指出多数家庭不会为此升级，主要是新建房作为 feature 装入。
- **业主接受度 / 控制权焦虑（重要痛点）**：人们会有「you are not in full control of the electricity that comes into your home」的恐惧，可理解。但他指出这种失控其实已部分存在——公用事业本就能因火险自行 PSPS 断电、且业主什么补偿都得不到。若公用事业**免费**装设备、换来「更可预测的停电 / 保住关键设备的停电」，他认为这是很多人（甚至非新房业主）会接受的公平交换。

## 品类未来 / 「Ring 时刻」（受访者重点处）
- 谁先用「足够便宜、足够好装」的设备进入市场、靠口碑（word of mouth）铺开，谁就可能赢。
- 类比：安防摄像头早就有，但「Ring cameras」靠普及度 + 口碑变成了这类东西的代名词。「I think that's what's going to happen to energy monitoring devices for most homes.」
- 当前没有任何一家（包括 SPAN）做到「Ring of energy monitoring」——「there's nothing that's really made itself a name as like the best thing yet... Like not even my company.」
- SPAN 现状：在美国不少家庭已装，但远未遍地；只做美国市场（拿美国市场的资格已经够难），世界还很大。
- 「Ring 时刻」的钩子：业主向朋友安利 App——「I got this span panel and I really like it. Here, check out this app.」他评价 SPAN 的 App「pretty decent... pretty clean looking」。并指出：若不是为了业主侧的好处，他们本可只做纯面向公用事业的数据设备、根本不会做这个 App。

## 与 Casally 方向的交流（受访者对访谈者方案的反馈）
访谈者介绍 Casally 现仅有 App，想加「更轻的硬件层」而非整面板，先在软件侧帮业主理解 / 管理用能。受访者反馈（均为其个人意见 / 设想）：
- 认可有空白市场：「there's not like a Ring camera of energy monitoring yet」，谁先搞清人们最在意什么并满足，谁就能成。
- 给软件先行的「该先证明什么」：他最看好——把**邻里 / 城市的负荷模式**结合假期、人口结构、重大事件，做出**有精度的区域用能预测**，这对公用事业「extremely valuable... ready to pay big bucks」。
  - 例 1：世界杯期间某以拉美裔为主的邻里，会在 4 小时内集体打开约「200 watt smart TVs」——可预测负荷。跨全州累加即可观，用于谈判调峰电厂电价。
  - 例 2：总统大选之夜大家看电视；旧金山看 Giants 比赛前，有人提前给 EV 充电、有人离家把家里全关。
  - 他强调这是他「just made this idea up right now」，SPAN 并不真做此事。
- 起步数据源（无自有硬件时）：加州智能电表数据（走 mesh Wi-Fi），虽非公开，但「maybe PG&E would be willing to share it for some price」；用电表整户数据 + 用户自报信息 + 人口/事件数据可拼出某种负荷预测。「AI can figure out some crazy things these days.」
- 业主 App 是否仍必要：「if we could succeed as a company with only being a utility facing tool, we would have done it.」业主侧体验是「necessary」让两边都买账、把设备价格做得值；若公用事业能完全补贴则是「best case scenario」。若纯走业主路线，更合理的可能是**智能插座（smart outlets）/ 智能电源**这类更小、只覆盖你最在意设备的形态。
- 公用事业最在意：**全州层面的需求预测（demand prediction）**，以便在正确时机调用调峰电厂——「that's their business」。

## 太阳能 / EV / V2X / NEM 3.0（设备与集成）
- EV / 太阳能趋势：当下热点是「not paying for gasoline」，大家会买 EV；太阳能板逐年更高效、更便宜、更合理。
- 面板作为桥接：能接入太阳能来电、作为「电动车与既有电网之间」或「充电桩与既有电网之间」的桥。
- **V2X**（原文说「a thing called V2」，应指 V2H/V2G 之类用 EV 电池给家庭做备份电池，标注：原文仅说 "V2"）——他认为是个不错的主意，但不清楚谁在做、是否已可用。SPAN 面板能让这类（及加 EV 充电器、太阳能逆变器）比改造既有面板更易加入家庭，「just a matter of software」。
- **NEM 3.0**（原文转录为 "NAM3 / NAM 3"，标注纠正为 NEM 3.0）：访谈者解释为加州政策，使太阳能业主把电卖回电网的价值大幅降低，更多人转向家用电池。受访者此前不了解（"What is this?"）。他个人态度：「I don't know how I feel about that」——他认为太阳能和电池本质都是「低价时取能、峰时自用、避免高价买电」；若是他自家，本就不太会被「把太阳能卖回电网」驱动，那不是他装太阳能的初衷。但无论哪种，仍需对用能有洞察 / 监控来判断买太阳能或电池是否划算。

## 关键金句
- "It's just what I like." —— Harry Jackson（论为何从管理岗退回一线技师）
- "There's ways you can do it cheaply. There's ways you can do it safely. There's ways you can do it quickly. ... sometimes you have to pick two of the three." —— Harry Jackson
- "it would damage our device before it damaged any downstream loads ... it actually trips our breakers before it damages the device itself." —— Harry Jackson（安全失效）
- "The panel itself is just it's just copper ... it's just a big wire basically. You don't need to bake intelligence into it." —— Harry Jackson
- "I do think it's a bit of an expensive toy." —— Harry Jackson（论智能面板，个人观点）
- "data is ridiculously valuable." —— Harry Jackson
- "We sell the data to the utility. That's how it would be." —— Harry Jackson
- "it just felt like a fact of life. It's like a storm is coming and you didn't know umbrellas existed." —— Harry Jackson（停电前未知备份电池的存在）
- "you are not in full control of the electricity that comes into your home ... that's a fear that people would have to get over." —— Harry Jackson
- "there's nothing that's really made itself a name as like the best thing yet. ... Like not even my company." —— Harry Jackson
- "more power to whoever actually figures it out and finds like what people care about the most and then gives it to them and then become successful because of it." —— Harry Jackson
- "if we could succeed as a company with only being a utility facing tool, we would have done it." —— Harry Jackson
- "if you're making something and it's good for the world ... I don't really care. I'm not the business owner here. ... Just do it. I hope you do well." —— Harry Jackson
- "hardware is necessary and then just enough software to keep your hardware working." —— Harry Jackson（被问若重头开始会否先做软件）

## 行动项 / 机会点
- **市场空白确认**：尚无「能源监控界的 Ring」，连 SPAN 都没占住——存在以「足够便宜 + 足够好装 + 口碑」抢先的机会窗。
- **价值锚定在公用事业侧**：业主侧纯监控难驱动行为改变；真正可货币化的是把多户行为聚合成邻里/区域级**负荷预测**卖给公用事业（调峰电厂议价、PSPS 分级断电）。Casally 若软件先行，应优先验证「区域负荷预测的精度与公用事业付费意愿」。
- **软件先行的最小起点**：从智能电表整户数据（加州 mesh Wi-Fi，或向 PG&E 付费获取）+ 用户自报信息 + 人口/日历事件数据，拼负荷预测原型；先验证是否需要设备级数据才足够。
- **轻硬件形态**：若走业主侧，考虑智能插座 / 智能电源等更小形态，只覆盖用户最在意的负载；负载均衡（让 100A 服务用满）是有真实价值的功能点。
- **安装是关键决策人**：任何硬件都要做成 drop-in、易装、无需额外培训，否则安装者不推荐就难铺开。
- **业主控制权焦虑要正面设计**：以「业主预设规则、公用事业在规则内调控、业主可 override」的形式换取「更可预测的停电 / 保住关键负载」，并辅以免费/补贴安装，是更易被接受的交换。
- **可保持联系**：受访者愿意在 Casally 有清晰原型/方向后查看并反馈，邮件（必要时电话）联系即可。

---
### 转录纠错与存疑标注汇总
- "Ittron" → **Itron**（智能电表厂商，纠正）。
- "NAM3 / NAM 3" → **NEM 3.0**（加州净计量政策，纠正）。
- "antiibration pads" → **anti-vibration pads**（防振垫，纠正）。
- "high pot tester" → **hipot tester**（耐压/高电位测试仪，规范化）。
- "483 phase" → 疑为 **480V 三相**（标注存疑，原文转录为 "483 phase"，未确证故仅标注）。
- "100 gawatts" → 单位疑为口误（傍晚高峰增量，原文如此，标注存疑）。
- "V2" → 指 **V2H/V2G 类（EV 作家庭备份电池）**（原文仅说 "a thing called V2"，标注）。
- "Franklin batteries" → 受访者本人即不确定确切叫法（"whatever they call them"），保留原文。
- 「band/fan/spam panel」等处的口音/转录变体，统一按上下文理解为 **SPAN 面板**（原文偶现 "fan panel"、"spam of these span panels" 等，按 SPAN 处理）。
