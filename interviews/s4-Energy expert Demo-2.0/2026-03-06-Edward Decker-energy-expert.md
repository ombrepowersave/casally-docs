# Edward Decker · 专业咨询 · 2026-03-06

## 受访者画像
- 在"national team"工作约 13 年，做过全美乃至全球的楼宇级能效项目；专长在**需求侧（demand side）节能与节能改造**。
- 经验主要在**商业/联邦（commercial / federal）领域**，多次提到 ESPC 项目、联邦/军事设施、hyperscaler 资产选型工作；residential（住宅）经验相对较少，访谈中多处自述对住宅侧细节"不确定"。
- 太阳能与电费相关经验主要集中在 **California、Arizona、Texas**，其中 California 量最大、Arizona 次之、Texas 较少，另有一些各地 2 MW 量级的小项目。
- 自述近几年把工作重心转向了"this type of product development"（这类产品开发），表示对做 Casally 顾问很有兴趣。

## 主题判定
判定为 **专业咨询**。依据：通篇是 Casally 团队（Amber Fu + 技术同事 Ling Jet）逐屏演示 Demo 2.0，向 Edward 这位能源专家征询专业意见（电价/TOU、需求电费、NEM、停电预警、节省计算基线、账单重构、export credit 核对等），Edward 给出行业知识、产品建议与风险判断；非用户痛点访谈、非用户使用反馈。

## 核心提炼

### 专业观点 / 行业知识点

**能量(energy) vs 需求(demand) 的区分（Edward 反复强调，是其核心观点）**
- 很多人分不清"electricity（用电量）"和"electric demand（需求）"。Demand 是**瞬时**功率，electricity 是 demand 在时间上的积分（"demand is instantaneous where electricity use is the demand over time, the rate function"）。
- 任何用电设备同时贡献 demand 和 electricity。举例 60W 白炽灯：开着就是 60W demand；开一小时是 60W demand + 60 Wh electricity。
- 优化思路：保持 demand 低、demand 曲线平滑，从而 consumption 也低；不要大的 peaks and valleys。"whenever we look at optimizing buildings… that's typically what we're looking at"。

**TOU / 电价结构对行为的敏感度**
- 住宅账单对小的行为改变（如 EV 充电时段）**有多敏感取决于 tariff**；TOU 下可以非常敏感。
- 若存在显著的 **demand 分量且是 ratcheted（棘轮式）**，在 peak 期高费率充 EV，可能**把未来 12 个月的 demand 都设高**、全年为此付费（"setting your demand for the next 12 months"）。注：此为其商业侧经验，他明确表示不清楚 California 住宅 tariff 是否 ratchet/是否按 12 个月设峰值。
- TOU 边际成本差足以让行为转移有意义：举例把 EV 从晚上下班回家（4:00、25 美分/kWh）改到睡前（8:00 或更晚、12 美分/kWh），"a 50% difference on a significant load"。（数字是 Edward 的举例假设，他声明不知道具体 tariff。）

**TOU 是季节 + 时段的叠加结构**
- 既分季节又分时段，所以"hourly calculation is critical"，需在后台跑 **8760（全年逐小时）**。
- 典型结构：summer off-peak / summer on-peak / winter off-peak / winter on-peak 四个 block；有时更多（如 high / medium / low peak）；每个 block 内再叠加逐小时 TOU 费率。"you kind of have to layer them"。
- **夏季 block** 举例 March 1 – September（他举例，不确定边界）。
- **Daylight Saving（夏令时）**：Edward 认为**不影响 tariff 的时段映射**，但会让楼宇负荷曲线整体前移/后移一小时（因负荷高度依赖天气/时间），而负荷曲线只是个输入，所以"不会对你影响太大"。
- **节假日 override**：被问及时，Edward 只回答了 DST，未明确回答节假日是否覆盖 TOU 映射 → **未说明**。

**Interval data（区间数据）**
- 住宅是否能逐区间拿数据，Edward**不确定**。
- 商业/大 tariff：通常用 **15 分钟 interval data**，既用于 TOU 费率结构，也用于为各 block 设定 demand。

**Solar 节省的两个组成**
- 不应把 solar 笼统当作"saving"看。应分两块展示：(1) 自用时的**直接 energy saving**；(2) 出口售电产生的 **revenue（export credit）**。建议在 solar PV 项下多加一条 line item。
- Edward 推测：自用那部分的每度省钱**通常比出口那部分高**，因为出口拿的是 net 费率、且出口时往往不在自己的 peak、费率更低。（标注：他明确说"that might just be me… I don't know"。）
- 住宅用户今天普遍**不理解**自用 vs 出口的区别——"but I think that's why they're using your app"。

**NEM（净计量）演变**
- NEM 1.0 / 2.0 时期，true-up 是**按月**结算，"really impactful"。
- **NEM 3.0**：Edward 自述"haven't done a whole lot with that yet / haven't seen one yet"，理解为**年度** true-up（不确定是 12 月/1 月还是按系统投运日起算）。
- NEM 3.0 出口 credit 不再是固定费率，而是 **net hourly time of use**（按时段、季节变化的净小时 TOU 价）。所以 bill proof 里不能用单一"rate"，建议改叫 "average rate"。
- 在年度（NEM 3.0）口径下，自用是否比出口 credit 更有价值：Edward 说 1.0/2.0 按月时很关键，年度下"might not be as important"，但明确"I'm not sure / something to think about"（推测，未确定）。

**Solar 销售乱象与"省不到全部"的真相（Edward 讲得很具体、判断明确）**
- 直言当前住宅 solar 销售"kind of snake oil salesmen"（卖蛇油的/忽悠）。
- 典型话术：你账单 $100、用 Y 度电、费率 20 美分/kWh，装这么大系统就给你每度省 20 美分。
- 真相：省不到全部 20 美分，因为账单里有**固定成本**——service fee 不受 solar 影响；某些 **demand charge 也不一定能被 solar 抵消**（因为可能在**阴天 solar 不发电时打出 peak demand**，demand charge 基本固定）。
- 举例：名义 20 美分里可能只有约 **11 美分**的 energy charge 能被影响。于是出现"说好省 \$100、实际只省 \$50"，查账单就知道为什么。

**哪些费用不能被 solar credit 抵消**
- **Service charge 一定不能**被 solar 抵消——它是"cost of doing business / cost of being able to purchase electricity when you need it"，是账单固定部分。
- **Demand charge**："你可能能影响、也可能不能"，高度 tariff dependent，取决于何时打出月度 peak demand。
- Public program charge / wildlife fund 等：归为 utility 运营成本类、通常不可抵（Amber 举例提问，Edward 以"Yep / those are utility charges for cost of doing business"确认；wildlife fund 他认为是 fixed rate，但说不确定是否变化）。
- **抵扣顺序**：utility 通常**先抵 energy charge**，因为你是按"net hourly cost of electricity"购电。Edward 推测抵的是 utility 的 net TOU 成本（不是零售 TOU 价），可能类似零售价的 ~80%（明确标注"haven't looked at it… going off memory… my guess"）。

**账单结构（reconstruct residential bill）**
- **没有固定的"正确顺序"**，取决于 utility tariff，utility 自己也会调换顺序。
- 建议把**固定/不可影响项（service charge、wildlife fund）放底部**——它们月月不变，app 的任何建议都改不了；把**可变、最有影响的项放顶部**。
- 提醒 Demo 的账单**可能缺了 consumption / demand charge**：现有 delivery charge 可能是 kWh，但缺 demand charge。Demand 和 consumption（electricity）是两大最有影响、也最可变的项，应当显眼。
- TOU 下可变项可能有四条、五六条甚至更多（不同 kW 费率段各一条）。
- 例子里提到 service charge 约 **\$24.60**（来自 Demo 截图），他指出这类是每月固定。

**Billing errors（账单错误）极其常见（Edward 强判断）**
- 他进新项目第一件事是做 utility analysis：拉两年账单、拆 cost/rate 结构、核对计费方式。
- **约 60% 的情况存在 billing error**。大型联邦系统的账单错误可达"in the millions"；住宅小得多，但同样存在。
- 多数人看不懂账单、为了有电就照付。

### 对产品方向的专业建议

1. **整楼负荷可视化**：Demo 顶部只显示 EV/solar/powerwall 等设备，Edward 主动问能否显示**整栋楼的 load**，把"generated vs consumed"拉平（levelize），看净负荷。Casally 解释当前阶段只有 API、靠多数据源（utility interval、solar 监控、battery、EV）估算 net load，有 main panel/CT 监测时可直读。

2. **预警必须配优化策略**：对 Casally"不做优化、只在接近预算上限时预警"的定位，Edward 反复说"the two go hand in hand"——后台**必须理解优化策略**，否则只告诉用户"快超了"却不给降本办法没意义。Casally 澄清：优化逻辑在后台存在，产品层是 decision support（展示影响、让用户自己选），Edward 认可（"perfect"）。

3. **优先盯 thermostat（恒温器）set point**：他做需求削减时**第一个 target 的就是 thermostat 温度回调（setback）**；建议接入 smart thermostat。他注意到 Demo 的清单里没有 thermostat，建议加进去。

4. **大设备才是 demand 主因**：AC、heat、pool pump 等大设备最有影响；laundry 看机型——电烘干"maybe"，燃气烘干基本不影响负荷；洗衣机功率他要查 name plate 才能定，未下结论。

5. **停电/rolling brownout 预警用天气模型驱动**：
   - 公告型停电（utility 据其理解需提前 **24 小时**通知 brownout——Edward 说"I think… supposed to"，不确定）：给该区域用户推送"明天可能停电、请确保电池/EV 充满"。
   - **未公告/当天才知的 rolling brownout**：靠**天气模型**预测——非紧急（非雷击/大风刮断线）的限电通常**与高温 + peak 时段重合**；可用天气数据预测。建议做**绿/黄/红**三级提示可能性。
   - 停电本身**不会负面影响电费**（有时还更省，如下雨变凉、开窗）。

6. **天气数据源与字段**：建议直接用 **NOAA**（原文转录为"Noah"）的天气与预测数据——质量好、省内存、字段全、便于后续加功能。常引入 temperature、humidity、wind speed 等。

7. **告警字段克制（避免 alarm fatigue）**：商业侧楼宇 EMS 常见"alarm fatigue"——一天上百告警，监控员就什么都不处理了。做法是把告警做得 **actionable & impactful**，从 100 条砍到约 **3 条真告警**，其余降级为 warning。早期只用 **high temperature** 即可，其次可考虑 **high wind**；**不要超过这两个**。高风/大风预警往往是 microclimate 局部问题。

8. **真正可执行的住宅告警（Edward 以住宅消费者视角）**：
   - 高温 → 可能 brownout（要停电）：actionable。
   - **接近 high demand 点**时告警：会立刻影响账单，且 demand 高时 consumption 也高，可提前压下来。
   - 举了一个叠加场景：solar 不发电 + 电池耗尽全靠 grid + 刚插上 EV + pool pump 即将启动 + thermostat 没回调 → 多个大负荷同时"cooling power"叠加，这种时刻预警是 nice to have。

9. **节省计算基线（"energy savings 的艺术"）**：
   - 可信基线需**三者兼顾**：强 baseline + 天气归一化（weather normalization）+ 落到 tariff 里。
   - 简单可算的（如 EV 改时段）很直接、可测量；预测型（如"明天热、外出时把 thermostat 调高"）省的是温差 ΔT 对应的量。
   - 风险：预测落空（预报 103°F、实际 88°F）。建议**分开"predictive savings"与"realized savings"**，按实际天气各算一次（"calculate it twice"）。
   - Baseline 还可用于对标（如"你比邻居多花 20%"）提示用户。
   - 他明确说本次通话时间不够深入展开 energy savings 细节，建议下次再谈（Casally 同意）。

10. **越细越可信**：event 级 / 资产级的 saving 归因"the more granular… the better and more credible"。比喻"breadcrumbs → a slice of bread"（积少成多）。普通用户其实不太关心怎么算的，"as long as you show that it's calculated"，所以展示有计算依据即可。

11. **Bill proof 改成两页、能量优先**：把 export credit 核对拆成**两页**——先"energy（能量）"页（expected vs billed 的 kWh），再"cost/rate"页。
    - 能量对得上 = 绿旗；差异大 = 红旗，提示用户深挖、联系 utility。
    - **关键判断**：在 solar credit 核对这一页，**能量差异比金额差异更重要**（罕见地推翻了他一贯"先看 dollar"的原则）。示例：expected 412 kWh vs billed 200 kWh = 差 50%，"that to me is a big deal"；而 \$127 的年度 credit 金额差"not that big of a deal"，可能只是 TOU 时段取整/15 分钟区间归到下一小时的 rounding。但**能量是 finite number**，发了 1000 kWh、用 600、出口 400，若 utility 只 credit 200，"there's 200 kWh lost somewhere"→ 红旗。
    - 建议再按不同费率段/区间细分，定位差异在哪。
    - 命名（nomenclature）：rate 不能叫固定 rate，因 NEM 3.0 是 net hourly TOU，建议叫 "average rate"。

12. **差异根因取决于数据来源**：
    - 若用 **utility interval / 直接读电表** 的数据还出现 expected vs billed 差异 → **最可能是 billing error（utility 端）**，需与 utility 交涉。
    - 若用 **模型数据（如 PV Watts）** → 八成是**没做天气归一化**，应先查这个。
    - Casally 澄清：当前主要用 meter/inverter/battery/utility interval 等**实测能量数据**，而非 PV 产量模型。

13. **年度 solar true-up 的展示顺序**：一般他主张"先 show dollar saving"，但 solar 年度 net true-up 是例外——因 app 端算的和 utility 算的很可能略有出入，若每月都先 show 金额差异**会损害 app 公信力**；先证明能量 expected 与 billed 一致、再呈现金额误差更"palpable"。补充：若模型做对了其实不会有差异，但这些 tariff 一年下来很复杂。

### 技术 / 政策 / 术语（依原文）
- **Demand vs Energy**：见上，demand=瞬时功率，energy=功率×时间。
- **TOU（time of use）**：季节 + 时段叠加；可能含 demand 分量；可 ratcheted（按月峰值棘轮，影响后续 12 个月）。
- **8760**：全年逐小时（24×365）计算口径。
- **15-minute interval data**：商业/大 tariff 计费与定 demand 的数据粒度。
- **NEM 1.0/2.0/3.0**：1.0/2.0 月度 true-up；3.0 年度 true-up、出口按 net hourly TOU 计价。
- **PSPS / rolling brownout**：California 计划性/滚动限电；Edward 理解可"fairly regular"，公告型据其理解需提前 24h（不确定）。
- **PV Watts**：太阳能产量估算工具（Casally 当前不主要依赖）。
- **NOAA（转录为 "Noah"）**：天气与预测数据源。
- **ESPC**：能源节约绩效合同（Edward 联邦市场经验来源之一）。
- **Commodity power / electric choice states**：部分州住宅可单独购买电力商品、再由本地 utility 配送；Edward 认为 California **不是** electric choice 州（但不确定），建议未来跨州时把 "commodity purchasing" 也列为账单 line item。

### 合规 / 认证路径
未涉及（本访谈未谈 FCC/UL/NRTL/DOE/Prop 65 等认证）。

### 监管 / 门槛与成本
- **核心门槛 = 每个 utility 都不同**。所有后台计算与逻辑都要为**每一个 utility、每一套 rate 结构、多套 tariff** 单独开发，"it's a lot of data"——这是这类产品此前没人做出来的根本原因。
- 建议路径：**先做 California、先做某一个 utility**，build out、跑通、alpha/beta 测，再向其他 utility 扩展。
- **SDG&E（San Diego Gas & Electric）**特殊性：San Diego 没有选择、只有一家公司；账单很长（Amber 称约 17 页），还要对接一个 servo 公司；电价**很贵**，Edward 认同（"very expensive"），半开玩笑说"I wouldn't start in San Diego… 因为很痛苦"，但也承认正因痛点大，"maybe it is a good one to"做。San Diego 很多联邦/军事设施其实不用 SDG&E，而用 Imperial（小型本地 co-op，变动费率约 **4 美分/kWh**，极低）。

### 风险 / 坑 / 现实障碍
- **最大风险 = 规模化铺开（critical mass）**：能源本身搞懂了"pretty straightforward"，不下保证、不会给出让用户花钱的建议，所以技术风险不大；真正的挑战是 utility/tariff 数量巨大、能否扩展。只做好 SDG&E 但铺不开、拿不到 critical mass，就是风险。
- **Solar 销售误导**导致用户对"能省多少"预期失真（见上）。
- **固定费用不可抵**导致实际省钱低于宣传（service charge、部分 demand charge）。
- **预测型节省落空**（天气未如预报）→ 须区分 predictive vs realized。
- **Billing error 高发**（约 60% 项目有）→ bill proof 的现实价值，但也意味着 app 计算与 utility 口径差异需谨慎呈现，否则伤公信力。
- **Alarm fatigue**：告警过多则全失效。
- 注：Edward 多处强调自己住宅侧、NEM 3.0、California 住宅 tariff 经验有限，相关结论需另行核实。

## 关键金句
- "I think they're kind of snake oil salesmen to be perfectly honest with you a bit." —— Edward Decker（评当前住宅 solar 销售）
- "Of that 20 cents, you might only be able to impact 11 cents of energy charges on your utility bill." —— Edward Decker
- "You could hit your peak demand on a cloudy day when your solar system is not generating, so your demand charges are going to stay sort of fixed." —— Edward Decker
- "Demand is instantaneous where electricity use is the demand over time, the rate function." —— Edward Decker
- "If the utility is only crediting me with 200 kW, there's 200 kW that's lost somewhere. That to me is more of a red flag." —— Edward Decker
- "With this, when it comes to credits from the utility, the energy would override the dollar, in my opinion." —— Edward Decker
- "Probably 60% of the time there are billing errors… when you're talking large federal systems, those billing errors can be in the millions." —— Edward Decker
- "You're saving a little bit here, a little bit here… you get enough breadcrumbs, you have a slice of bread." —— Edward Decker
- "The reason it hasn't been done is because every utility is different… all the logic needs to be developed for every single utility." —— Edward Decker
- "I would put the service charges at the bottom… you're not going to impact those." —— Edward Decker
- "I wouldn't start in San Diego… I was kind of joking, just because it's painful." —— Edward Decker
- "The average homeowner doesn't really care how it's calculated as long as you show that it's calculated." —— Edward Decker

## 行动项 / 机会点
- 在主屏顶部增加**整楼 net load 可视化**（generated vs consumed 拉平），优先利用 main panel / CT 监测，缺硬件时多源估算。
- 在事件/告警清单里**加入 smart thermostat（温度 setback）**，作为需求削减的首要抓手。
- 后台构建**优化策略引擎**（即使产品层只做 decision support）——预警必须能配套给出降本动作。
- TOU 引擎按**季节 block + 逐小时（8760）叠加**实现；明确 California 住宅 tariff 是否含 ratcheted demand、是否按 12 个月设峰、节假日是否 override（本访谈未定论，需核实）。
- **告警分级、克制**：早期只用 high temperature（必要时加 high wind）；目标从"上百"砍到约 3 条真告警，其余降级 warning，避免 alarm fatigue。
- **停电预警**：公告型推 24h 提醒；未公告型用 NOAA 天气模型做绿/黄/红 rolling-brownout 概率提示（高温 + peak 时段为主信号）。
- **Solar 节省分两条 line item**：自用直接 saving + 出口 export credit revenue。
- **节省计算**采用 强 baseline + 天气归一化 + tariff 三要素；分别记录 predictive 与 realized savings。
- **账单重构**：固定项（service charge、wildlife fund）置底、可变项（energy/consumption、demand）置顶；补齐缺失的 consumption / demand charge；定义跨 utility 通用费用类别（electricity、demand、service charge、commodity purchasing 等）；标注哪些类别不可被 solar 抵（service charge 必不可抵、demand 视情况）。
- **Bill proof 改两页**：energy 页（expected vs billed kWh，能量优先判红/绿旗）+ rate/cost 页；rate 命名改为 "average rate"（NEM 3.0 net hourly TOU）；按费率段细分定位差异。
- 用**数据来源**判定差异根因：实测/interval 数据差异 → 大概率 billing error（找 utility）；模型数据差异 → 先查天气归一化。
- **落地路径**：先 California、先单一 utility（SDG&E 痛点大但可考虑）跑通再扩；把"每个 utility 都不同 → 规模化铺开"列为头号风险，尽快建立 critical mass。
- 把 Edward 发展为**长期顾问**（他已明确有兴趣），下次专门深入 energy savings 计算方法与 NEM 3.0 net true-up 细节。

---
*转录纠错说明：原文 "Noah" 还原为天气数据源机构 **NOAA**；"NEM3.0" 即 California 净计量 3.0。其余术语（demand、TOU、8760、ESPC、PV Watts、SDG&E、Imperial 等）按原文保留。Edward 多次声明对住宅 tariff、NEM 3.0、California 住宅细节"不确定/没深入研究"，相关数字与结论（如 11/20 美分、4:00→8:00 的 25→12 美分、夏季 block 日期、~80% net 价、24h 通知等）多为其举例或记忆推测，已就近标注，不应作为既成事实引用。*
