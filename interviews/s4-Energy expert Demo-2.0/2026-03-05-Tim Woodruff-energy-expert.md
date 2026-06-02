# Tim Woodruff · 专业咨询 · 2026-03-05

## 受访者画像
能源领域从业者，长期与公用事业账单/电价打交道，自述"每天都在跟能源打交道"。曾在 Utah、Colorado、New York 等多州工作，目前主要在东北部（northeast）各州工作；对 California 主要是通过大量阅读研究而非实操（"I've been doing a lot of reading about California""I haven't worked with California utilities"）。主要服务对象是商业客户、尤其小型商业客户（"I've mostly worked with commercial clients"）。本人现居 Colorado（推断：访谈中 Amber 称"you live in Colorado"，Tim 未否认）。

本次为 Casally 团队（Amber Fu 主持，技术同事 Ling 在场演示）就 Demo 2.0 的电价建模、账单重构、储蓄归因、True-Up 等逻辑做结构性验证的专家咨询。

## 主题判定
判定为 **专业咨询**。依据：Casally 明确目标是"validate whether our interpretation of the tariff structure and the billing logic is structurally correct"，全程由团队逐屏演示产品并就电价、净计量、True-Up、数据源、合规/数据留存等向专家求证，专家给出大量行业事实判断与产品建议，访谈尾声还邀请其担任顾问。

## 核心提炼

### 一、数据源与账单重构

- **三大关键设备数据源**：专家明确认为住宅侧最重要、最值得接入的是 **电池、汽车（EV）、太阳能** 三者的实时 API（"the three biggest ones are going to be batteries, cars, and solar"）。智能炉灶/灶台一类总用电量太小，不值得接（"their total use is so small that I don't think those are worth it"）。
- **不能直接拿电表数据**：第三方"很不幸"无法直接读取电表数据（meter data），而那本是最简单的方式（"the one thing you can't unfortunately do is access the meter data"）。
- **电表与计费的关系**：电表对公用事业是连续读数（continuous reading）的实时数据流；但在计费/给太阳能出口估值时，公用事业按 **15 分钟区间** 看（"they look at it in 15-minute intervals"）。公用事业内部对全年每一小时（8760 小时）都有各自预测的成本/avoided cost，按你那一小时的用电量计价，太阳能价值（EEC，能源出口信用）即由此而来，月底再聚合进 TOU 的各档（tier 1/2/3）桶里。
- **可用的实时数据替代方案**：
  - **智能电panel（smart panel）**，如 **Span**（原文转录 "span"），可连接，提供最稳健的 API；但安装成本约 **$3,000–$8,000**。（纠错：原文 "span" 指 Span 智能电panel。）
  - 提到一个 **TP-Link** 产品可配合使用（专家说记不太清名字）。
  - **Sense**：装在主线（mains）上的传感器，有 API，走蜂窝或家庭 Wi-Fi；约 **$250**，约需 **60 天** 学习每个设备的"电子签名"以识别"楼下冰箱开/关"等。但专家**不确定 Sense 是否还在经营**（"I'm not sure if they're still in business"）（推断：此为专家个人不确定，非已证实事实）。
  - 综合而言，最稳健的 API 来自 **智能电panel 厂商**。
- **Tesla**：若通过 Tesla 接入，能量都流经其电池，内部可实时掌握所有进/出/并网交换；**但不对第三方开放**，尤其住宅侧（"they don't open that up… not open to third party providers most of the time… at least not from a residential side"）。
- **实时洞察基本来自设备 API**：从公用事业拿实时 feed 很罕见，欧洲若公用事业有自家 app/系统更常见会开放 API feed，但美国一般不给。所以实时洞察主要来自太阳能/电池/EV 等设备 API。
- **整屋重构的概念逻辑**（专家给出的拆解思路）：自顶向下 = 总太阳能 + 总并网取电 − 出口到电网 − EV − 电池损耗（"battery losses are not insignificant"），再结合房子是电气化还是天然气、电热是电阻式还是热泵，可缩小假设范围。若总发电中约 **20%** 未被解释，可安全归为照明/电脑/风扇等；若有 **60%** 仍缺失，那就是更大的谜团（"that's a bigger mystery"）。

### 二、太阳能"省得不如预期"的常见原因

- **Phantom load（幽灵负载）** 是大头：老冰箱、错误布线（faulty wiring）会快速耗电。
- **老系统估算不准**：如 ~2016 年的系统是在"估算"发电量，精度不如公用事业的高频电表测量，源于当时的数据限制。
- **NEM 3.0 / NBT 下出口价值低**：太阳能出口已从其他成本中"解绑（unbundled）"，可能一月出口 400–600 kWh 却几乎拿不到价值——出口估值约 8 美分/kWh，而取电要付约 40 美分/kWh 还要付 delivery charges，时间错配（timing mismatch）让太阳能"看起来一文不值"，即便能量上确实发出了预期的电量。

### 三、TOU 电价与行为敏感度（产品"月度账单预算"逻辑验证）

- **峰谷价差巨大**：超低谷/隔夜充电约 **5–7 美分/kWh**，峰段约 **35 美分/kWh**；峰段用电可达 4–10 倍贵，且部分 benefits charges / 税在更高费率上计算。delivery charges 不分时（"not time of use"）、不可避免。举例 SDG&E（原文转录 "SDG&"）夏季峰段约 **80 美分/kWh**，超低谷约 **12 美分**。（纠错：原文 "SDG&" 指 SDG&E。）
- **敏感时段**：约 **晚 7–9 点（7 to 9 p.m.）** 最敏感，kWh 费率可高至约 1 美元；高峰窗口通常很短，一般 **早 5–9 点、晚 7–10 点**。夏季尤甚。把约 100 kWh 移出峰段可较快省下约 **$30–$50+**。
- **行为可节省的占比（专家估计，个体差异大）**：
  - 在峰价激进（aggressive）的公用事业区：账单可从约 **$300 降到 $180**（不到 50%，但显著）。
  - 在没有激进 TOU 的地区：约从 **$250 降到 $180**，约 **25%** 降幅。
  - 强调"非常因人而异"，有人本就习惯好、可调整空间小，有人空间大。
- **最大成本暴露行为 = EV 充电**：估计 **不到 10%** 的人做分时充电；装了太阳能的房子会被自动放到很激进的 TOU 电价上（白天用电几乎免费，傍晚回家开空调+插车则很贵）。举例：往返 60 英里通勤 → 需充 **15–20 kWh**，在 80 美分下"突然就是七八美元"再加各项费用；一周五次累积可观；若移到隔夜，"突然就是一两美元"（至少冬天，夏天不然）。
- **电池**是第二大杠杆：白天充、傍晚 5–8 点高峰时作为主力供电，每天能省几美元、累月可观。核心是"尽量自给自足或避开高费时段"。
- **空调（AC/HVAC）的告诫**：若峰段高用电只在夏季而非冬季出现，多半是空调——这是大得多、也难改的行为（"they're probably not going to want to turn off their AC at six o'clock"）；若全年都高，则更可能是车充等可调项。
- **用历史账单估上限**：TOU 账单已按分时段拆开，看历史峰段用电量即可判断行为转移的"天花板"——若峰段只有 $60，那最多省 $60；若有 $200，则可移空间大得多。

### 四、储蓄归因与反事实建模（产品"Saving"逻辑验证）

- **能源部分占比小、需解耦**：住宅账单中能源（energy）部分仅约 **25–30%**，用户容易误以为 $170 全是用电。应把不受行为影响的 base charges 与 delivery charges 解耦出来。
- **反事实基线（counterfactual baseline）**：
  - 若用户在同一住址住了一段时间，用 **去年同月** 作基线通常可接受。
  - 更可信的做法：当用户**承诺了某项行动**（如"我会隔夜充车"），就用车的数据 feed 拿到实际 kWh，反事实即"假设在更高费时段充"。
- **天气归一化**：可拉城市/州的 **采暖度日/制冷度日（heating/cooling degree days）** 做年对年季节调整；若某夏季制冷度日多 30%，可把去年用量中 HVAC 部分上调 30%。专家不确定 California 是否按城市级别追踪度日。
- **储蓄可信度（关键经验）**：
  - 先把"这个行为改变可能为你省多少"呈现出来，再在下期账单上让用户**看到实际兑现**（如"你的超峰 kWh 下降了 X，我们预测会降这么多"），展示已实现的省钱比例——比实际多或少都不那么重要，关键是让用户感到"我做的事真的有影响"。专家在商业客户上用 **三年行为均值** 作基准来证明干预带来的节省，能增强客户对"省钱是真的"的信心。
  - **保守估计、后续超额兑现（underpromise, overdeliver）** 永远比乐观估计后跑不到、令用户失望更好。
- **按设备分项归因更可信**：分系统组件（individual system components）归因比系统级（system level）更 defensible，因为对 EV 用电掌握更准。建议 onboarding 问行为问题（"你下班回家就充车吗？几点到家？"），快速判断高价值干预并喂进电价算反事实；系统级笼统估计"可能显得过于雄心勃勃（overly ambitious）"。
- **可减部分（reducible portion）**：建议先估"不可减部分"（HVAC 等 non-reducible），需要设备清单 + 行为问题；联邦政府有通用估算、部分按区域细分，California 很可能有住户级/设备级能耗估算（或分南北），通常区分电气化 vs 非电气化家庭。先估可减部分、再算该范围内的潜在节省更合理，但需要一定历史数据提供用量背景。

### 五、计费细节与电价模型（产品"计算逻辑"验证）

- **账单不止 kWh 费**：还有 delivery charge、system benefit charges（可能按用量计），需逐项 double-check。
- **California 是否对住宅能源征销售税**：专家不确定（"I'm not positive… whether California charges sales tax on residential energy"，"most states don't"）（明确未确定，勿当事实）。
- **必须高度动态**：费率随工作日/周末、节假日、季节变化；且每个公用事业处理不同（如 PG&E 节假日可能按周末费率，SDG&E（原文 "SDce/ce"）可能不）。（纠错：原文转录含糊的 "ce"/"SDce" 推断指 SDG&E；标注"推断"。）
- **TOU 是预定义计划而非实时市场**：即便有小时数据，也只是喂进工作日或周末的 TOU 价；不像 Texas 那种 live market。是固定的分时价，"但每年都会可靠地上涨"。
- **电价数据可得性差**：大多数 tariff 埋在"很老的网站上的旧 PDF"里，"truly not meant to be accessible"，且全是**段落形式（paragraph form）**而非表格。公用事业每年要把更新的电价拿到 **public utilities commission（公用事业委员会）** 批准；通常约 **10 月（October）** 公布次年电价（专家不确定每家具体生效月）。
- **rate schedule 数量庞大**：某公用事业（原文转录 "likece" 含糊，推断指某加州公用事业，可能 SDG&E）有 **30–40 个** 不同 rate schedule，按房屋面积、是否有电池及电池 kWh、是否有 EV、太阳能是 5–10 还是 10+ kW 等划分到不同 tariff。
- **最小可行电价模型（minimum defensible model）**：让用户输入其 **off-peak 成本 + 所在公用事业 + 峰/谷比 + 时段小时**，因为峰谷通常约 **4–5 倍** 比例，即可近似建模。

### 六、True-Up 与 NEM/NBT（产品"账单/True-Up"验证）

- **NEM 演进**：
  - **NEM 1**：一度电就是一度电（"a kilowatt hour is a kilowatt hour"），等值。
  - **NEM 2**：出口到电网价值更低但非完全无价值；通常出口约为所用 kWh 价值的 **75%**，年底信用过期或欠费补差，"就这么简单"。
  - **NBT（Net Billing Tariff，新的，2023 年）**：对每一度出口电，按全年**逐小时 avoided cost** 定值，给 **能源出口信用（EEC/energy export credits）**，年底过期；分开 generation 与 delivery credits 等多项。
- **California True-Up 是"噩梦（a nightmare）"，全美最复杂**。Utah 也有 True-Up（专家做过大量阅读）。
- **滚动 vs 日历年**：专家倾向**实打实的日历年（solid calendar）**而非滚动 12 个月，因为很多信用年底过期，日历年能让用户知道年底会损失多少价值。
- **正确建模 NBT True-Up 的难度（点名的坑）**：需要从 California 拉取政府允许公用事业使用的 **avoided cost 计算模型**，且按 **locational（按地点/zone）** 区分——同一公用事业内不同 zone 都不同；还需全年 **8760 小时** 的发电与进口数据，以及每家公用事业每个 line item 的算法。"It is a monster"，可做但需 locational 模型并在本地自行运行。NEM 1/2 则"fine"。
- **行业现状**：大多数太阳能 app **不复刻完整 True-Up**，只估 **趋势与方向（trend & direction）**、用 kWh；Tesla Powerwall、SolarEdge 会基于地点用 TOU 价估出口价值，但不做逐小时实际核算。
- **用户可接受精度**：若年总额约 $1,000–$2,000，年底误差需在 **±$50** 内才被认为"够好"；总账单 $2,200 却显示 $2,000 或 $2,400 就"偏太远"。难点在公用事业间、zone 间差异（solar-saturated zone 估值完全不同）。

### 七、账单核对 / 出错排查（产品"Bill Proof"验证）

- **出口信用与账单不符的常见原因**：专家自述"见得不多"，若有，多为设备故障——通常是 **逆变器（inverter）**，有时是电表；但更常见的其实是 **公用事业的计费/账单系统出错**（"more often it's going to be… the utilities' accounting and billing system"），他发现过很多此类错误，公用事业查后承认"长期多收/少收"，与设备无关。
- **驳斥"公用事业账单几乎从不出错"**：专家明确反对——"I've seen a lot of mistakes in my time… By no means are they not making mistakes."（注：他声明未做过 California 公用事业。）错误常见形态：把人放错 tariff/rate schedule、把数字 2 倍、把别人账户加进来——通常**很明显**（"it's like double"，不是 5%–15% 的小误差）。
- **争议/审计流程**：**没有正式流程（not a formal process）**。多见于商业账户：得自己收集所有账单 + 第三方数据 + 你认为发生了什么（尤其用量无故跳升时），交给公用事业，对方可能派人查或做 inspection，但全靠客服和大量 leg work。
- **有意义的差异门槛**：必须**相当大**（如 $200 量级）**且持续（consistent）**，否则公用事业不会理会，且通常会让你先去检测设备。
- **"在家没用电账单还很高"的解释**：很大程度是**教育性**问题——能源用量只占账单一小部分，transmission/distribution/delivery 与 benefits charges 占大头，"真的整月不在家也可能还有 $140 账单"，这并不一定代表算错。要真正回溯，需要电表日级用量或家庭能耗 API（这也正解释了 Casally 为何想拿实时 API）。

### 八、行业趋势与产品判断

- **电价会越来越动态/复杂**："utilities love complex formulas because it makes it really easy to charge more money." NBT 的 TOU 价已定到 **9 年**（约 **2032** 到期，可随燃料成本上涨），到期后 California 很可能转向类似 **Texas 的更实时市场**（推断/专家个人预测，非近期）。复杂化的根因：在 California 能源大多数时候其实接近免费，大家付的是**可靠性（reliability）**。
- **实时定价的行为效应**：以 UK 的 **Octopus Energy** 为例，实时电价下人们确实会改变行为（"是不是现在烘衣服划算"），但需要丰富的实时数据 feed + 实时响应 + 用户理解复杂市场——正是 Casally 在做的方向。
- **对产品的整体评价（正面）**：多数能源 app 是给"energy nerds"（追求 passive house/net-zero、整天盯太阳能板）做的重数据可视化层；Casally 提供"中间层"——教用户看懂账单又不用整天琢磨，"unique"、"accessible and empowering"，不强制绑定 Tesla 整套生态。最接近的对标是 **Octopus**（但 Octopus 是公用事业本身、且在 UK）。
- **小型商业客户也适用**：家族企业等"低于会配能源/设施经理那一档"的小商业很合适；且**商业电价其实比住宅简单**；很多人不想雇能源 CFO/审计，这是理解账单的好"第一步"。
- **地理与扩张**：Colorado 偏便宜；东北部很贵但太阳能远不如 California 普及。一切按州/公用事业划分；建议 **California → Texas → New York** 的逐州打法合理——Texas 自由能源市场某些方面更易切入，New York 监管又与两者都不同、学习曲线和进入门槛高。

### 九、专家主动提的产品建议

- **"反事实成本提醒"**：若拿到充电数据，除了正向省钱，也可呈现"你在高价时段充了车，本可更便宜——你的账单本可低这么多"，不是惩罚而是教育（"not to punish them"），但别堆一堆大红数字。Amber 评价"brilliant idea"。
- **onboarding 行为问卷**：用设备清单 + 行为问题（何时充车、几点到家）来锚定高价值干预与可减比例。
- **on-ramp 观察期**（专家发问，团队回应当前以模型为主、后续收集行为细化）：可考虑前一两个月先观察用户真实用电峰值再做建议。

## 风险 / 坑 / 现实障碍（专家点名）
- **每个公用事业、甚至同一公用事业内的不同 zone 规则完全不同**，成本计算"在每个 territory 都完全不一样"，是实现上的大障碍。
- **NBT True-Up 的精确复刻是"monster"**：需 locational avoided-cost 模型 + 8760 小时数据 + 逐 line item 算法。
- **电价数据可得性极差**：旧 PDF、段落形式、非表格、30–40 个 rate schedule。
- **拿不到电表实时数据**；设备级 API 多不对第三方开放（Tesla 等）。
- **数据留存（data retention）是主要合规风险**：尤其若做"拍账单照片 OCR 上传"，涉及姓名、地址等 PII。
- **不要承诺具体省钱金额**：必须讲清"不是承诺、是行动的最大可能影响"，否则用户会回头找你和公用事业理论（underpromise overdeliver）。
- **空调相关的峰段用电**难改，行为干预效果有限。

## 关键金句
- "I I do think the three biggest ones are going to be batteries, cars, and solar." —— Tim Woodruff
- "the one thing you can't unfortunately do is access the meter data which would be the easiest way." —— Tim Woodruff
- "you might actually be exporting like four, five, 600 kilowatt hours a month and not really getting any value for it… a big part of it is just the mismatch in timing that is making the solar system seem so worthless." —— Tim Woodruff
- "the energy portion of a utility bill, especially for residential, is like 25 to 30% of the total bill." —— Tim Woodruff
- "I think conservatively estimating savings upfront and then overachieving later always goes over better." —— Tim Woodruff
- "It's more defensible to actually do individual system components than system level." —— Tim Woodruff
- "most of the tariffs are buried in old PDFs on very old websites. They are they're truly not meant to be accessible." —— Tim Woodruff
- "California has by far the most complicated true up." —— Tim Woodruff
- "I've seen a lot of mistakes in my time… By no means are they not making mistakes." —— Tim Woodruff
- "utilities love complex formulas because it makes it really easy to charge more money." —— Tim Woodruff
- "they could be gone for a month truly and still have a $140 bill. And that doesn't mean that it's necessarily wrong." —— Tim Woodruff
- "most apps… in energy are just for like energy nerds… you're doing the good job… of giving that middle layer of teaching someone about their bill, but not making them think about it all day." —— Tim Woodruff
- "it needs to be clear that it's not a promise. It's like here's the maximum impact of your action so that they're not then yelling at you and their utility." —— Tim Woodruff

## 行动项 / 机会点
- **优先接入 电池 / EV / 太阳能 三类设备 API**；放弃小负载设备；明确电表实时数据不可得，规划用 smart panel（Span 等）/Sense 等作替代时考虑其成本（$3k–$8k / $250）与可用性。
- **储蓄展示遵循 underpromise–overdeliver**：先保守估计、再在下期账单显示已兑现比例；商业经验用三年均值基准建立可信度。
- **按设备分项做储蓄归因**，配 onboarding 行为问卷锚定高价值干预；避免系统级笼统估计。
- **解耦能源部分（约 25–30%）与 base/delivery charges**；先估不可减部分（借联邦/加州住户级能耗估算）再算可减范围。
- **反事实基线**用去年同月 + 度日（HDD/CDD）天气归一化，或对已承诺行动用设备实际 kWh 算反事实。
- **最小电价模型**：用户输入 off-peak 成本 + 公用事业 + 峰谷比 + 时段即可近似；计费需覆盖 delivery、system benefit charges、工作日/周末/节假日/季节动态、（待核实）销售税。
- **True-Up**：NEM 1/2 可做；NBT 先做趋势/方向估计（对标 Tesla/SolarEdge），完整逐小时复刻需 California locational avoided-cost 模型 + 8760 小时数据，门槛高；目标精度 ±$50/年。日历年优于滚动 12 月（应对信用过期）。
- **Bill Proof**：差异需"大且持续"（~$200 量级）才有申诉意义；公用事业无正式争议流程，需自备账单+第三方数据；常见错因更多是计费系统而非设备；"在家也高账单"多为教育性解释。
- **合规重点放在 data retention**；做账单 OCR 时注意 PII。
- **扩张路径** California → Texas → New York 合理（逐州/逐公用事业适配）。
- **拓展机会**：小型/家族商业客户（商业电价反而更简单）。
- **顾问关系**：Tim 口头表示有兴趣以轻量方式担任 Casally 顾问（"Yeah, absolutely. This is cool."）。

## 转录纠错说明
本逐字稿为语音转录，存在术语/机构名同音误写。.md 中已在相应处标注，未改动原始 .txt：
- "span" → **Span**（智能电panel品牌）。
- "SDG&" / "SDce" / "ce" → **SDG&E**（San Diego Gas & Electric）；上下文谈加州公用事业费率。
- "likece"（"likece I think has 30 or 40 different rate schedules"）→ 推断指某加州公用事业（可能 SDG&E），含糊，标注"推断"。
- "EEC's" / "energy export credits" → **EEC（能源出口信用）**，NBT 下的出口估值机制。
- "NBT" / "net billing tariff" → **NBT（Net Billing Tariff，即 NEM 3.0）**。
- "dur market"（"if at any point California had a dur market"）→ 推断指 **DR（需求响应）市场**，存疑，标注。
- "dematic"（"more dematic over time" / "pricing will become more dematic"）→ 推断指 **dynamic（动态）**。
- 文中数字（5–7¢、35¢、80¢、12¢、$3k–$8k、$250、25–30%、75%、8760、±$50、9 年/2032 等）均为专家原话，按原文保留。
