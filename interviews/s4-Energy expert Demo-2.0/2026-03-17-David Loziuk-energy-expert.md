# David Loziuk · 专业咨询 · 2026-03-17

## 受访者画像
- 能源工程从业者，主要做**联邦合同（federal contractor）**相关工作；自述"this is what I do for a living"。
- 地理：常驻**中西部（Midwest）**，主要在 Illinois 的 ComEd 区域（转录写作 "KMED"/"Kameed"，应为 **ComEd**）做过住宅光伏的费率评估（rate assessment）与光伏设计（solar design）；也提到 Ameren、Mid American（Illinois、Iowa）。
- 加州经验：在 Southern California 为联邦政府做过费率评估，但**只在商业侧（commercial）**，地点在 San Diego 区域靠边境的多个站点；明确说**未在加州做过住宅费率评估**（"I haven't done any residential rate assessment in Southern California, at least not recently"）。涉及的加州电力公司他提到 "S Southern California Electric"（应为 **SCE / Southern California Edison**）和 "DG gas and electric"（应为 **SDG&E / San Diego Gas & Electric**）。
- 自评：对全国各类项目"fairly familiar"。
- 在商业侧长期做建筑自动化系统（building automation systems）与能效改造项目的逐年节省核算（"that's what I do for a commercial customer … did an energy savings program … 8 years ago"）。
- 本人**没有 EV**（"I don't have an EV car"）、**没有太阳能**（自述不熟悉 true-up，"I don't have a solar so I never receive the true up"）。

注：访谈双方约 1:56:00。Casally 方为 Amber Fu（主持，主谈产品方向），并提及两位同事 Ling/Ivy（也念作 Lindia）做数据建模、以及一位 Jessica 负责对接邮件。

## 主题判定
判定为 **专业咨询**：Casally 向一位能源行业从业者逐屏演示 Demo 2.0，征询其对数据采集粒度、节省核算方法、TOU 费率映射、NEM 3.0 进出口计价、true-up 等的专业意见与建议。专家给出多条产品建议、若干行业事实与判断，并表示愿作为顾问长期协作。

## 核心提炼

### 专业观点 / 行业知识点

**数据采集粒度**
- 设备侧：电池最重要的是**荷电状态（state of charge, SOC）**；光伏最重要的是**发电量/产出（production）**。无需每秒拉数（"too much data"）；若要瞬时数据，每分钟即可。
- 拉数频率取决于要展示什么：若只给用户看**累计 KWH（一段时间产了多少）**，频率无所谓，让设备自己算能量即可；若要展示**瞬时功率 KW**，则需更短间隔。
- 对光伏发电，他倾向**更短间隔**，理由具体：一片云飘过约 5 分钟会造成功率下降（dip），15 分钟间隔会漏掉。
- 对 15 分钟间隔的判断：**"15 minutes is pretty standard … four points per hour … not that much data"**。他推荐 15 分钟（每小时 4 点）；若数据量太大，每小时也可接受，但他倾向 15 分钟一侧——理由是用户体验，"nobody's going to sit there for an hour for a new data point"。
- 关于"能否从电表拿到 15 分钟数据"：他的理解是加州都是**智能电表（smart meters）**，公用事业侧是"instantaneous"读数（具体多久一次他不确定）；因此"for you to get it every 15 minutes shouldn't be a problem"。但他**明确限定这是他在 ComEd 的经验**、不在加州，建议 Casally **直接登录某个加州住宅账户（如 PG&E）的电表在线系统去核实**实际能拉到什么间隔、有无延迟。
- 推断：他认为既然加州住宅光伏都上了 TOU、且必须在小时内展示分时定价（"they have to show pricing … throughout the hour"），那么导出/导入数据应该会以类似时间粒度提供。（**推断**，他用了 "I assume"）

**数据可信度 / 质量校验**
- 当被问"系统要呈现哪些信号才让用户觉得可信"，他理解为"how do you know the data is correct"。他的回答较弱、坦承不确定（"I don't know"）：你只是在读设备的数据，默认设备给的是对的。
- 给出的唯一可操作校验方式：让用户能**交叉比对**——若 app 显示电池 SOC 90%，但去看 Tesla pack 显示 80%，用户即可发现差异（discrepancy），判断数据不对。

**月度账单基准 / 行为预算**
- 用户对"惊吓账单（surprise bill）"普遍反感（"I don't think anybody likes the surprise bill"）；人们想对未来花费有大致预期。他个人会设预算并希望落在预算 ±10% 或合理方差内。
- "省钱"与"避免惊吓账单"两者他都认为重要。
- TOU 认知盲点：他认为人们**不知道**在 TOU 下某几小时电价会跳到很高（举例 "50 cents per kilowatt hour"）；若 app 能推送"现在 TOU 费率很高，尽量关掉负载"的通知，是"a very useful tool to have in your pocket"。
- 关于加州 TOU 适用范围，他**当场自我修正**：先说"time of use 可能只针对 export"，随即纠正为 **"No, I'm sorry. It's both."**（进口和出口都有 TOU）。但措辞含糊、明显不确定，应视为**专家个人推测**，非确证事实。

**节省的两类来源：系统自动化 vs 行为改变**
- 他把节省来源区分为两类：
  - **系统设计 / 自动化（system design / automation）**：如 EV 充电排程设在午夜~6am、恒温器排程、设备控制器，"the user doesn't think about it"。
  - **行为改变（behavior change）**：用户手动避开峰时洗衣、跑洗碗机、手动设定充电时间等。
- 关键判断："the savings are going to be calculated the same"——无论系统还是行为驱动，**节省的算法是一样的**，区别只在"是人决定还是电脑决定"。
- 若必须二选一聚焦，他**两者都做**，但补充："the automation's better because then the person doesn't have to think about it … both are useful"。

**节省归因（重要判断）**
- 关键观点：**若用户本来就已在做最优行为，就不应把这算作"节省"归功于 app**——"because they're not going to see any difference on their utility bill. I mean, they already have the savings"。
- 用户最终只认账单结果（"the end result is going to be the bill from the utility at the end of the month"）；若账单没降，用户会问"What did you do for me?"。
- 节省应从**用户自身的账单 baseline**推算：两个 baseline 高/低不同的用户，对高 baseline 者算节省、对已在执行优化策略者不抢功。

**最大负载排序（针对 Southern California）**
- 最大、且最易转移（easiest to shift）的是 **EV 充电**——大电池组，且大多数人夜里睡觉、夜间电价低。
- 第二是 **空调 / AC**——与室外气温绑定，热天用得多；他注意到 demo 里有"power outage"天气提醒，并提到"this week"加州严重高温（severe heat）。
- 第三是**电热水器（domestic water heater，若是电的）**——可加控制器只在午夜~6am 加热；手动做大多数人不会做。
- 较小：灯具（大家都用 LED）、其他家电。
- **加热（heating）/热泵/电阻加热在 Southern California 基本可忽略**（终年偏暖）。注意：他在 Illinois 才会建议用热泵或电阻加热在年底前消耗夏季过剩的光伏信用，避免 "use it or lose it"——但**这是中西部场景，他明确说南加州不必担心**。

**AC 负载转移的专家技巧（subcooling）**
- 他反复给出一个具体建议：**早晨预冷（subcooling）**——把房子先降到约 **67°F**，让白天升到 ~90°F 时空调可以"float"（尽量少开）；下午让室温在热舒适区间内"略微过热"（thermal comfort layer 约 **67–74°F**），从而避开一天最热时段的空调运行。前提是用户接受这种温度波动。
- AC 比 EV 难做行为改变；他认为**排程（scheduling on thermostat）是最佳**，尤其用户周一到周五上班、白天没人时设回温（setback / 把制冷设定点调高，如 76°F）很容易。但"come to the individual"——取决于个人预算与不适忍受度，"I can't answer for all people."

**EV 双向充电（bidirectional）机会点**
- 若用户有双向充电器，晚上不用 EV 的电时可在峰价时段**向电网出口**赚钱、夜间再充回。
- 他自己提出的权衡（**专家个人推测**）："if I'm charging discharging more, my batteries aren't going to last as long"——多充放可能缩短电池寿命，但车有潜力靠峰时放电为业主赚不少钱。

**逐年节省的归一化（normalization，很具体且强调）**
- 节省的 baseline 他推荐用**去年同月（same month last year）**，前提是能拿到客户 **12 个月账单**。
- 强烈强调：必须做**多重归一化**，否则"apples to oranges"：
  - **费率归一化（rate normalization）**：逐年费率会涨（举例涨 5%），不能只比美元金额；要把"用了多少 kWh"和"费率涨了多少"都算进去。
  - **负载/行为变化归一化**：若用户今年新增 EV 等负载，要么**调整 baseline**、要么把新增用量从今年用量里**扣除**再比（"you can put it on either side of the equation"），不能让用户改造原因导致的用量上升被算成超基线。
  - **天气归一化（weather normalization）**：举例去年 7 月很热要多开空调，今年凉（他随口说"El Nino"），不归一就没法精确对比。
- 他强调要把结果**拆开展示**给用户看：例如"你因为行为改变省了 $50，但因今年电价更贵要多付 $10，净省 $40"。"you have to break it out like that."
- 这正是他给商业客户做的：8 年前做了能效项目，每年展示节省时都**扣除逐年费率自然上涨**，使呈现的数字与客户当前账单对得上。

### 对产品方向的专业建议

1. **每个行动/事件都标"估算节省"美元值**（强烈、反复建议）。"my only suggestion would be try to quantify the the savings"。放在底部、标注 **"estimated savings"**，让用户自己判断值不值得。这是建筑自动化系统的标准做法（把故障/问题按可省的美元金额量化，帮设施经理决策）。
   - Casally 回应：两周前已计划给每个 action 加美元值。
2. **不要精确到分（penny）**。Demo 里出现 "$21.32" 这种精度，他认为这**暗示了不存在的计算精度**；应标"approximate / 近似"，按有效数字四舍五入到**整美元**，或给**区间**（如 "$20–$23"）。"Nobody cares about 30 cents really anyways."
3. **"at-risk cost"（不执行建议的潜在多花成本）框架是合适的、专业的**——"it's not unprofessional … people need to know a dollar amount"，且能激励行为改变；但同样应标注为近似。
4. **不必展示计算等式本身**；用户点进去看到一句解释（如"因为你在峰外充 EV，本月省了 $21"）即可。
5. **保持简单、别堆字**。事件明细页（给两个费率 off/on peak + 用量）他认为"simple enough"、"I don't think this is too much information"；目标是让不懂这些的普通业主不被淹没（"not overwhelmed"）。
6. **账单计算要尽量接近真实账单**：要把**固定费用（fixed / base service charge）**、**各类 riders / 附加费**（能效项目费等）、**税**都算进去，理想误差在 **$1 以内**，他认为应能做到 **5% 误差**以内。
7. 对"是否要加第二个智能电表/硬件"他**直接质疑**："Why would you add another smart meter?"——若公用事业已有电表、逆变器已有电表，他不理解为何再加一个主电表；除非是为**分项计量（submetering）家电**（洗衣、电视、冰箱等）才有意义。在听到 API 数据有 **1~3 天延迟**后，他才理解加硬件的动机。

### 技术 / 政策 / 术语

- **TOU（Time of Use，分时电价）**：价格随**一天中的小时、星期几、一年中的月份**变化。他的理解：工作日 vs 周末不同（他**猜**周末更便宜，但自承"I forget which way it is"）；节假日同周末；夏季比冬季贵（供需+空调）。这些应视为一般行业常识，**具体加州数值他未给出、也声明不在加州做住宅**。
- **NEM 3.0（净计量 3.0 / 转录写作 "name 3.0"，应为 NEM 3.0）**：他熟悉这一较新法规，称**2023 年加州切换**（自述"three years old at this point"）。核心变化（他的理解）：**进口按固定费率、出口按市场/分时费率（time of use）**支付；此前 2.0 时进出口都是固定价、"easy"。政策意图（他的理解）：促使更多人**买电池做负载转移**，在高价时段出口。
  - 进/出口计价（他的描述）：导入电时按**固定费率**计费；导出电时按那一刻的**实时/市场价**给信用（"sometimes they might pay you 50 cents … other times only 5 cents"）。公用事业侧"instantaneously calculating it"。
  - **避免成本计算器 ACC（Avoided Cost Calculator）**：他点名**加州公用事业委员会（CPUC, California Public Utilities Commission）**推出的工具（"some type … on your computer"），用于帮（潜在）光伏用户测算 NEM 3.0 下的收益；有 workshop/培训研讨会，他刚开始研究、未深入。他一度以为 Casally 在做类似 ACC 的东西，后理解 Casally 是私营侧、面向账单解释。
  - **576 种费率结构**：他读到三家加州公用事业（PG&E、SDG&E、及另一家——指 SCE）之间住宅费率结构有 **576 种可能组合**（NEM 2.0→3.0 后）。用户仍可**选择**进口走 TOU 还是走固定零售费率，但**出口在新制度下一律 TOU**（他称公用事业把出口叫 **"deferred cost"**——按 .txt 原文；可能指 NEM 3.0 的 avoided-cost/ "deferred cost" 概念，原文如此，未进一步澄清）。
- **True-up（年度结算）**：他**坦承自己不熟悉**（"I'm not familiar with this true up"），由 Amber 解释后理解。他对"既然按月对账，为何年底会有巨大差异"反复表示**惊讶**（"I'm just surprised … there's that much of a discrepancy at the end of the year"），并推断可能是**月度只是近似/估算（approximating during the month），并非最终结算**。他用费率结构给出一个可能解释：若用户走**固定进口费率**，冬季电价本应低但仍按固定高价付，年底可能积累差异；若走 TOU 进口则冬季便宜、年底不应有大差异——所以差异大小取决于用户处在哪种费率结构。他表示要真正搞清楚需要"see one of these true up bills"。

> 注意：访谈中关于 true-up "为什么年底有大额账单 / $2,000、$1,000 很常见"、"月度只是 running balance 非最终结算"、"信用按不同价值结算、年底过期"等**绝大多数事实陈述是由 Casally 方（Amber）提出的**，David 多为接受/复述并表示理解。这些**不应记作 David 的专家确证**。

### 合规 / 认证路径
未涉及（本次未讨论 FCC/UL/NRTL/Prop 65 等）。

### 监管 / 门槛与成本
- 未直接涉及认证费用/周期。相关的"门槛/复杂度"点：NEM 3.0 把节省核算变复杂（576 种费率组合、进出口计价分离），他认为这正是此类应用**有价值**的原因，也可能是市场上类似产品稀少的原因（"it became a lot more complicated with the 3.0"）。

### 风险 / 坑 / 现实障碍（专家点名）
- **数据精度的虚假暗示**：精确到分会让用户误以为计算达到那种精度——应标近似/给区间。
- **节省归因陷阱**：给已经在做最优行为的用户算"节省"会失信，因为账单上看不到差异。
- **逐年对比的多重混淆变量**：不做费率/负载/天气归一化，去年 vs 今年就是"apples to oranges"，得出的节省不可信。
- **加州费率结构极度碎片化**：576 种住宅费率组合，进口可能 TOU 也可能固定、出口一律 TOU——计算真实账单/节省难度高，是账单匹配出现差异的潜在根源。
- **API 数据延迟**：他听到第三方 API 有 1~3 天延迟时明显意外（"Oh god"），认可这是引入本地硬件的合理动机。
- **真实账单匹配缺项**：固定费、riders、税未纳入会导致计算账单与实际账单不符（Casally 自承仍在解决）。
- 他对"加第二个智能电表"持保留——除非用于家电分项计量，否则不理解必要性。

## 关键金句
- "15 minutes is pretty standard … it's four points per hour. It's not that much for the …" —— David Loziuk
- "for the solar production, you're going to want it short because … a cloud can come overhead … for a five minute period. you're not going to see that dip if you're pulling every 15 minutes." —— David Loziuk
- "I don't think anybody likes the surprise bill." —— David Loziuk
- "the savings are going to be calculated the same … one you're calling a system, the other one is the behavior." —— David Loziuk
- "the automation's better because then the person doesn't have to think about it … But both are useful." —— David Loziuk
- "if somebody's already doing that strategy without your app, then I don't think your app is going to be able to take credit for it." —— David Loziuk
- "the user is going to want to see end results and the end result is going to be the bill from the utility at the end of the month." —— David Loziuk
- "my only suggestion would be try to quantify the savings … I would put estimated savings at the bottom so that somebody can then judge well is this worth it or not." —— David Loziuk
- "I wouldn't do it to the penny like this because that implies that you've calculated to that level of accuracy … Nobody cares about 30 cents really anyways." —— David Loziuk
- "I subcool in the morning … bring it down to 67° … then in the afternoon you let the house overheat a little … 67 to say 74 degrees Fahrenheit." —— David Loziuk
- "I would think the EV is the largest. And that one just seems the easiest to shift because most people sleep at night time." —— David Loziuk
- "you'd have to rate normalize … you got to consider both how the rate increases year to year and how the energy use varies for the same month each year." —— David Loziuk
- "there's like 576 different rate structures … between the three utilities." —— David Loziuk
- "you import at a fixed rate and then the new rules say you can export at the time of use rate." —— David Loziuk (NEM 3.0)
- "Why would you add another smart meter?" —— David Loziuk
- "it seems like it's useful because of the complexity now." —— David Loziuk（论 NEM 3.0 后此类产品的价值）
- "I can provide my industry expertise as you guys are developing this app further … I'm available for that." —— David Loziuk（愿作顾问）

## 行动项 / 机会点
- **每个 action/事件加"estimated savings"美元值**，标"approximate"，**精度到整美元或给区间，不到分**。（Casally 已计划）
- 保留并打磨 **"at-risk cost"（不行动的潜在多花）框架**——专家认可其专业性与激励作用，但同样标近似。
- 节省核算采用**去年同月 baseline + 12 个月账单**，并必做 **费率、负载/行为、天气** 三重归一化，结果**拆项展示**（行为省了多少 / 费率涨了多少 / 净省多少）。
- **不要把已在执行最优行为的用户的"节省"归功于 app**，避免账单对不上时失信。
- 节省/账单计算需纳入**固定费、riders、税**，目标误差 ≤5%（理想 ≤$1）。
- **自动化与行为建议两者都做**；自动化更优（恒温器排程、EV 充电排程、热水器控制器）。
- AC 难做行为改变 → 优先**排程/setback**；可纳入"早晨预冷（subcool 到 ~67°F）+ 午后在 67–74°F 舒适区内 float"的专家技巧作为建议内容。
- 关注 **EV 双向充电**峰时出口赚钱的机会点（提示电池寿命权衡）。
- **去核实加州住宅电表实际可拉的数据间隔与延迟**（建议直接登录一个 PG&E 等住宅账户在线系统验证）。
- 研究 **CPUC 的 Avoided Cost Calculator (ACC)** 作为 NEM 3.0 收益测算的参考/对标。
- **质疑"第二个智能电表"的必要性**：除非做家电分项计量（submetering），否则重新评估硬件方案。
- **建立顾问关系**：David 明确愿作为行业顾问，按问题/计算方法提供持续意见；对接人为 Casally 的 Jessica，邮箱 info@（Ombre, Pasadena，原文 "Ombre Pasadena"）。

---
### 转录纠错说明（不改原始 .txt，仅在此标注）
- "name 3.0" / "name" → **NEM 3.0 / NEM**（净计量，Net Energy Metering）。
- "KMED" / "Kameed" → 几乎确定为 **ComEd**（Commonwealth Edison，Illinois 电力公司）。
- "S Southern California Electric" → **SCE / Southern California Edison**。
- "DG gas and electric" → **SDG&E / San Diego Gas & Electric**（推断，依上下文"San Diego area"）。
- "Amaran" → **Ameren**（中西部电力公司，推断）。
- 数字"576 different rate structures"、"50 cents / 5 cents"出口价、"\$2,000 / \$1,000 年底账单"等均按原文保留；其中年底大额账单与 true-up 机制的事实陈述**主要由 Casally 方提出**，非 David 确证，已在正文标注。
