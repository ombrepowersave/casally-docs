# Dexter Luu · 专业咨询 · 2026-03-06

> 说明：本摘要基于语音转录逐字稿，对明显的转录错误做了内部还原并标注，**不修改原始 .txt**。常见转录错误对应关系：
> - "NEM 3"/"NE3"/"NE 3"/"M3"/"Numm Nem"/"NEM3" → NEM 3（净计量计划第三代 Net Energy Metering 3.0）
> - "N2"/"NE2"/"NEM2"/"name two"/"num too"/"them too" → NEM 2（净计量计划第二代）
> - "NEM 1"/"NE one"/"NEM one"/"num one" → NEM 1（净计量计划第一代）
> - "avoiding cost calculator"/"avoded cost calculator"/"avo margin cost"/"ACC" → Avoided Cost Calculator（避免成本计算器，NEM 3 出口积分依据，由咨询公司 E3 制定）
> - "tu"/"TLOU"/"TU"/"takeover" → TOU（Time-of-Use 分时电价；"takeover" 处实为 "peak hours"，推断）
> - "P Gen"/"PG Gene"/"P gen" → PG&E（太平洋燃气电力公司）
> - "SDG&"/"SDG&E" → SDG&E（圣地亚哥燃气电力）；"SE"/"SCE" → SCE（南加州爱迪生）
> - "chura bill"/"true bill"/"chew up"/"trip"/"job"/"true" → true-up（年度结算）
> - "Alura" → 专家所在 UCSF 使用的能源服务提供商公司名（转录存疑，无法确认确切拼写）
> - "non- bypassable"/"NPCs"/"non by possible" → non-bypassable charges（不可绕过费用 NBC）
> - "expat bill"/"bill price"/"surprise bill" → 账单意外/账单暴涨（surprise/spike bill，推断）
> - "kit/kitty glitch/KDH/KH/KW/kid of age" → kWh（千瓦时；专家口述常混用 KW 与 kWh，按语境还原）
> - "spam panel" 未出现；"Y status" → device status（设备状态，转录听错，推断）
> - "cracks/crack calculation" → correct calculation（正确的计算，推断）

## 受访者画像
- 加州能源专业人士，**位于 PG&E territory（服务区）**。
- 职业起点为**能源咨询（energy consulting）**，**做过加州全州的需求响应（demand response）**，与 **SDG&E 和 PG&E** 合作过。
- **现就职于 UCSF（加州大学旧金山分校），负责能源管理（energy management）**。
- 自述判断："I think California is probably the most complicated in the US."（加州大概是全美最复杂的）。
- 工作中常自己**建回归模型（regression based, 以时间/星期/温度为变量）**做基线，用于度量节能措施实施前后的差异——具备扎实的计量与建模背景。

## 主题判定
判定为 **专业咨询**。依据：访谈为 Casally 团队（Amber Fu 负责产品方向、Lingjie Jin 技术负责人）逐屏演示 demo，并就间隔数据、TOU/NEM 计费、储能调度、true-up 结算、出口积分、账单重建与数据获取等专业问题向具备加州能源管理与需求响应经验的专家请教，专家基于从业经验给出判断与建议，非用户痛点访谈或满意度测评。

## 核心提炼

### 一、间隔数据与设备字段（必需项）
- **进口（import）与出口（export）都需要间隔数据**："you would need interval data for both."
- **出口积分（export credits）的最小时间粒度大约是 1 小时**：专家称公用事业间隔数据通常是 15 分钟，**但出口积分是按小时（by the hour）结算的**——"the minimum for that is probably an hour... I know utility interval data is usually 15 minutes but I think they do the export credits by the hour."
- **间隔数据的必需字段**：时间戳（time stamp）+ 用电量（energy usage）。
- **设备状态（device status）的必需字段**（针对电池）：
  - **电池剩余电量（amount of charge left）**——明确点名"definitely the amount of charge the battery has left"。
  - **运行模式（operating modes）**：电池通常设多种运行模式，**有最低保留电量（minimum reserve）**；需了解剩余容量、当前用量/出口量，才能判断电池在触及最低阈值前"还能撑多久"。
  - **当前是否在出口（currently exporting）**、当前配置（current setup）。
- 电池配置通常由**房主与太阳能安装商一起编程设定**，"really depends on how they set it up"。

### 二、NEM 计划差异（专家反复、深入展开的核心）
专家把 NEM 1/2/3 的计费与 true-up 机制讲得很细，是本次访谈最有价值的部分。

**NEM 划线时间点**
- **NEM 2 在 2023 年 4 月结束**。2023 年 4 月**之前**装太阳能的用户多在 **NEM 2**；**之后**装的在 **NEM 3**。

**NEM 3（出口积分基于 ACC，不基于 TOU）**
- **出口积分基于 Avoided Cost Calculator（ACC，避免成本计算器）**，不再基于 TOU 零售费率。
- ACC 由一家咨询公司制定并公开，专家**推测公司名是 "E3"**（标注：专家原话 "might be their company name like E3 or I think um"，不确定）。只需输入若干参数即可得出出口积分。
- **NEM 3 下出口积分多数时候不高**，因此**激励用户用电池（incentivized to use batteries）**。
- **但夏季出口积分会很高**：专家点名 **8 月、9 月、10 月**天热时段出口积分"very high"，可在 ACC 中看到。
- **NEM 3 的年末调整（adjustment）机制**（专家讲得很细）：
  - NEM 3 的积分**年末不清零（don't get zeroed out）**。
  - 但若**全年净出口为正**（出口 > 进口），那部分净出口**拿不到基于 ACC 的积分**，而是由公用事业按**批发价（wholesale price，可能很低）**结算（加州政策要求）。
  - 机制是：你曾因出口拿到 ACC 积分，但净出口部分又必须按批发价支付给你，**不能两头拿（can't get credited twice）**，于是公用事业**收回（claw back）**其中一笔积分——表现为"看起来像被收了出口的费"，实则不是被收费，而是积分被回收后改按批发价结算。
  - 举例：出口 6000、进口 5000，对 1000 kWh 差额做调整，收回那部分小额积分，再按批发价（可能两三美分）付该 1000 kWh。
  - 专家明确："the NEM 3 is pretty confusing."

**NEM 2（基于 TOU 零售费率，年末清零 + 净出口批发结算）**
- **出口积分按 TOU 零售费率**（专家措辞："approximately the TOU retail rate"，不完全等于）。
- **积分按 TOU 时段分别累计**：peak、off-peak、super off-peak **各自分别净出口**，分别乘对应 TOU 费率转为积分——**不合并**。举例：1 月 off-peak 出口 10 kWh、peak 出口 5 kWh，分别按各自费率计入 1 月积分，**结转到 2 月账单**。
- 上月积分可抵下月电费，**但不可抵 non-bypassable charges（不可绕过费用）**。
- **年末 true-up**：若仍有剩余积分，**不现金兑付，直接清零（zero out）**；再取**全年净出口**按**批发价**结算。举例：全年净出口 500 kWh → 按 500 × 批发价（约两三美分）付。
- 专家："NEM 2 is not as complicated because they just zero it out and then they'll pay you on your net export."

**NEM 1**
- **通常只有单一费率值（one value），基本无 TOU**："NEM 1 is usually just one one value. I don't think there's any TOU for NEM 1."
- 是否有 true-up：专家**不确定**（"that's so long ago I don't even remember"），**推测有，且与 NEM 2 类似**。

**共性**
- 三种 NEM 的 true-up **各公用事业略有不同，但思路一致（the idea is still the same for all three）**。
- **delivery（配电）与 generation（发电）积分分两个独立的"银行（two separate banks）"**：delivery 的积分不能用于 generation，反之亦然；ACC 计算器里 delivery 与 generation 也分不同区块。出口积分**同时作用于 delivery 与 generation 两侧**，但分开记。
- **non-bypassable charges 只对进口 kWh 收取**，且无论净能量是否为零都要付。**因此用电池有利**——少进口就少付 NBC。

### 三、True-up 的两层账本（专家确认 Amber 的模型）
- Amber 提出"两个账本：月度能量账本 + 年度 true-up 账本"，专家确认 "Yes."
- 月度逻辑：逐月结转积分（roll over credit）；年末按净出口做调整/结算。
- 专家举例讲解：全年滚存的积分（如 $100）"内含"那 1000 kWh 净出口的价值，但政策要求该净出口必须按批发价结算，故需对该部分做处理。

### 四、Solar Billing Engine 的最小输入与建模顺序（专家给出的实操清单）
- Amber 提出引擎分层顺序：**能量层（进/出 kWh）→ TOU 映射 → 费率引擎 → 积分计算 → 月度账本 → true-up 结算**。专家答**没有遗漏**（"No, I don't think so"），但提醒 **NEM 2 与 NEM 3 系统会不同**：NEM 3 出口积分不基于 TOU，必须**纳入 ACC（避免成本计算器）**。
- **被问"住宅 solar billing engine 必须正确建模的最小输入"，专家给出明确清单**：
  1. **NEM 协议类型**（NEM 1 / NEM 2 / NEM 3）——第一项输入。
  2. **净账单/间隔数据**：每个 15 分钟区间是进口还是出口。
  3. **TOU 费率**：NEM 2 需要 TOU 费率；NEM 1 通常单一费率、无 TOU。
  4. **NEM 3（仅 solar credits）**：只需**净出口** + **ACC 计算器**。

### 五、TOU 映射与基线（澄清了一个产品误区）
- **TOU 有季节性**：冬季与夏季费率不同；**冬季可能没有 off-peak / super off-peak**（专家不确定具体，但强调季节不同结构不同）。
- **TOU 映射通常对原始间隔数据直接计算，不需要基线（baseline）**：公用事业按 15 分钟区间（PG&E 如此）映射，"如果你在晚 7 点用 3 kW，就是 3 kW × 该时段费率"，**不基于任何 baseline**。
- **baseline 只在"建模/对比前后差异"时才需要**（如反事实节省、需求响应度量）。Amber 一度把"映射"和"基线"混淆，专家纠正：费率表本身已含各时段价格，套用即可。
- **TOU 对工作日/周末**：专家自家账单工作日/周末一致；有少数费率会区分，但"已整合进费率本身"，只要有各 tariff 的结构就已包含此信息。

### 六、反事实节省（Savings）基线建模
- **首选基线：去年同期（previous year）**。理由——**一整年才能覆盖完整温度区间（winter to summer）**；若只用 3-6 月数据建模，无法覆盖 7-10 月的温度范围。
- **模型应基于 kWh（用电量）而非成本（cost）**，因为去年费率可能不同；用反事实 kWh × 今年费率反推"本应花多少"。
- **专家本人需求响应做法**：用回归模型（时间/星期/温度），以实施前一年为基线，度量实施后差异。也可用"非事件日（event-like day that wasn't an event）"做对比，但**最简单的还是用去年同期**。
- **公用事业自己是否这样算**：专家答 "Yes"。
- 若天气相同，用上月也可，但**现实中专家更倾向用去年同期**。

### 七、行为对账单的敏感度
- **持续性的行为差异影响很大**："if you do it on a consistent basis it's going to be a big [difference]."
- **EV 峰时充电改到非峰时，估计可省至少 50%**："I would guess that they'll probably save at least like 50%."（专家标注为估计 "I would guess"）
- 加州夏季**峰时（4-9 PM）费率有时到 40 多、50 多美分/kWh**（视地区而定）。
- **最大成本暴露行为**：峰时用电；具体器具为 **AC（空调）与 EV 充电**。
- **专家判断 AC 是最大驱动**：因为多数人已知不该峰时充 EV、会避开最差时段；**而 AC 是"不能放弃的舒适（a comfort that people cannot give up）"**，所以 AC（及温度相关用电）通常是最大驱动。这也是账单随天气事件上升、强温度依赖的原因。

### 八、对产品方向的专业建议
- **省钱 vs 避免账单意外**：被问占比时专家答 **"honestly 100% for both"**——两者都重要且密切相关。**最重要的是账单符合预期（their bill is what they expect it to be）**；**"避免账单意外"应排在"省钱"之前**。但若给机会省钱，用户也会要。
- **自动化 vs 决策提示**：**若 App 能准确判断，自动化（automatic）更好**。但反复强调前提——**必须确保自动化做的是最优（optimal）的事**；若自动执行却没省钱、甚至多花钱，用户会不满。
- **执行卡触发逻辑（相对财务边界而非纯优化）**：专家认可 "this makes sense"——把它理解为"警告用户当前在做错的事（如峰时充 EV）并提示停止"。
- **执行建议是否附财务影响估算**：**"能准确做就做，但不是绝对必需"**；账单含很多非直接用电项（输电/配电费等），全量精确很难；**可简化为 kWh + 混合费率（blended rate）**，"usually that's enough for customers"。
- **事件检测灵敏度**：**应较高/重要**——峰时充 EV 这类"很大的事（pretty big thing）"，因为充电耗电量大。
- **账单展示——只显示三个核心数字即可**：被问"简化账单视图最重要的三个数字"，专家答 **kWh + 总成本（total cost）+ TOU 结构拆分（super off-peak / off-peak / peak 及对应成本）**。
- **混合费率（blended rate）建议**：把 wildfire fund charge（野火基金费）、CCA 费用、输配电费等"很多项"**合并进一个混合 TOU 费率**；对住宅客户，最关心的就是**用了多少电 + 每度有效电价**。
- **demand charge（需量费）对住宅**：住宅一般不收需量费；**专家本人不在意，多数住宅用户也不太在意**——不收就不必展示。（注：UCSF 等商业侧专家最关心的是 demand charge + 用电量 + 每度成本。）
- **发电侧 vs 配电侧节省拆分**：**对客户保持简单、合并展示即可**；但可设一个可单独查看的区块，供有疑问的用户深入（因为积分确实 generation/delivery 分开）——"95%、99% 的时候"合并就够。
- **at-risk exposure（风险暴露 / 忽略优化事件的成本）展示**：专家认为**对客户可能信息过载（"too much information for the customer"）**——"我不认为客户会看/在意这个"，建议弱化。
- **EV 充电事件成本归因（counterfactual）defensible 吗**：专家认可——估算"本会用多少电、归因一笔成本"是 fine 的；**前提是知道充电器的电力需求（demand）与充电时长**，则足够准确。
- **是否漏掉 tier threshold / minimum bill 步骤**：专家认为通常用户**本就会用到最低消费（minimum bill）**，且 minimum bill 是"无论是否用电都要付"的固定项，不影响该归因逻辑。
- **bottom sheet 透明度**：有费率、有计算过程、合理——**足以支撑可解释的节省主张**。
- **事件解释三层（what happened / why matters / what next）**：专家认可这个详细程度"fine / good"，能解释问题、为何重要、如何修复。

### 九、电池/储能调度判断
- **电池峰时充电是否一律标记（flag）**：**不一定**——**若用的是多余的太阳能（excess solar），峰时充电是 OK 的**。场景：峰时太阳能已覆盖全屋用电仍有富余，富余电应去充电池（除非想出口）。
- **NEM 3 下若预测出口积分很大，可考虑出口而非充电池**；**NEM 2 与 NEM 3 策略不同**。
- **真正重要的是"峰时不要进口（importing）"**：峰时段 4-9 PM 中，**4-7 PM 可能还有太阳能可充电池；7-9 PM 不要进口**——此时应靠电池放电，避免被高峰价计费。

### 十、数据获取与时延（专家点名的最大现实障碍）
- **数据延迟**：专家自己通过 PG&E 拿数据"**从来不是实时（never live / never current）**"，**通常滞后约 3 天（three-day lag）**——查 3 月 5 日的数据，往往只能拿到 3 月 2、3 日的。
- **15 分钟间隔仍非实时**："I can't get live 15 minute data, it's always like a three-day lag."
- **要实时数据就得装表**：需在系统上**装智能电表（smart meter）/能直接喂入自有系统的设备**。但专家认为**这类计费计算本就"事后（after the fact）"做即可**，不必实时。
- **数据获取是最大挑战**：专家明确 **"getting the data... is always a challenge"、"that's probably challenge number one"、"keeping that data flow working has been a huge issue for us"**。
- **PG&E 在加大难度**：UCSF 通过第三方拿 PG&E 数据，**SSL 证书原本一年续一次，现改为约每 45 天就要续一次**，"making it a lot harder"。
- **第三方接入路径**：专家建议——**作为第三方向加州公用事业申请，让客户直接把其间隔数据共享给你**。
- UCSF 当前用的能源服务提供商公司名转录为 **"Alura"**（拼写存疑，无法确认）。
- **数据源选择**：出口能量从间隔数据取；TOU 费率从账单或与 PG&E/SCE/SDG&E 的**互联协议（interconnection agreement）**取；NEM 3 出口积分需用电量 + ACC 计算器。

### 十一、账单错误与 Bill Proof（账单核对）
- **公用事业算错的概率：约 5%**（"maybe 5% of the time"）——比此前另一位专家（约 0.1%）的估计高，记录差异。
- **常见错误原因**：多收费、归到你名下的 kWh 数量不对（associating too much kWh）、CCA 等"随机费用"略有偏差。专家在 UCSF 也偶尔遇到账单金额不对。
- **追踪方法**：账单意外暴涨时就该去查"发生了什么"。专家看 demo 示例点评："expected 412 kWh 出口、实际只 200 kWh，that's a big difference"——认可这种偏差检测。
- **Expected 与 Bill 出口积分不一致的最常见原因**：**数据不匹配（data mismatch）**（而非间隔时序差异）。
- **Bill Proof 部分的改进建议**：当前只覆盖 solar 出口，**应同时显示从公用事业进口了多少（how much they imported）**。

### 十二、硬件（Lingjie 提问）
- **可在客户家公用事业电表旁加装自有硬件/电表来模拟（simulate）电力数据**：**只要客户同意即可（"if they agree to it, you could do it, but you have to get them to agree"）**——专家未展开技术/合规细节，仅强调需客户同意。

### 十三、对产品整体与市场的反馈
- **整体正面**："I think this app is cool"、"looks useful"、"if everything is accurate, then yes, it would be useful"、**"a lot more helpful than just PG&E portal"**。
- **市场上是否有类似 App**：专家说**没见过这样一体化的**——市面上功能多是**分散在不同 App**（公用事业的"换费率能省多少"工具、太阳能/Tesla 充电 App 等）；**把所有东西整合到一个 App 很好（central energy manager for a residential customer）**。
- **最大风险/挑战 = 数据获取**（见第十节）：尤其用第三方拿数据、维持数据流稳定。
- **合作意向**：愿做 **advisor**（"I could be open to it"、"I wouldn't mind helping"），尤其团队对 true-up 困惑、愿提供帮助。**主动提出会后发送 ACC 计算器（Avoided Cost Calculator）的链接（一个 Excel 表）**，并通过 chat 留邮箱。

## 关键金句
- "I think California is probably the most complicated in the US." —— Dexter Luu
- "I think the minimum for that is probably an hour... I know utility interval data is usually 15 minutes but I think they do the export credits by the hour." —— Dexter Luu
- "customers under NEM 3 they're incentivized to use batteries because the export credit is not very good most of the time." —— Dexter Luu
- "honestly 100% for for both... they don't want surprise bills... I would put the avoiding surprise bills probably ahead of saving money." —— Dexter Luu
- "if it's correct, then automatic would be better... you guys just need to make sure that it is doing what is optimal." —— Dexter Luu（自动化的前提）
- "AC is a comfort that people cannot give up. So... usually AC is probably the biggest driver." —— Dexter Luu
- "I would just include all that as like a blended rate as with the time of use." —— Dexter Luu（混合费率建议）
- "I think that might be actually too much information for the customer." —— Dexter Luu（论 at-risk exposure 展示）
- "the NEM 3 is pretty confusing." —— Dexter Luu
- "NEM 2 is not as complicated because they just zero it out and then they'll pay you on your net export." —— Dexter Luu
- "the export credit isn't based off the TOU, it's going to be based off of the ACC. So you need to incorporate the avoided cost calculator too for NEM 3." —— Dexter Luu
- "usually you don't... do these calculations at the bill level. You would do this after the fact." —— Dexter Luu
- "even when I get it from PG&E, I never get it... it's always... three days after." —— Dexter Luu（约 3 天数据时延）
- "they're making it so the SSL certificate needs to be renewed every like 45 days now. It used to be one year." —— Dexter Luu（PG&E 加大第三方接入难度）
- "getting the data... is always a challenge... keeping that data flow working has been a huge issue for us. So... that's probably challenge number one." —— Dexter Luu
- "having everything in one place is nice. It's kind of like a central energy manager for a residential customer." —— Dexter Luu
- "the first input is you need to know their NEM agreement... NEM 1, NEM 2, NEM 3." —— Dexter Luu（建模最小输入）

## 行动项 / 机会点
- **会后跟进（专家承诺）**：接收专家发来的 **Avoided Cost Calculator（ACC）Excel 表链接**——这是 NEM 3 出口积分建模的关键依据，务必索取并研究。
- **Solar billing engine 最小输入（按专家清单实现）**：① NEM 协议类型（1/2/3）；② 每 15 分钟区间的进/出口；③ TOU 费率（NEM 2 必需，NEM 1 单一费率）；④ NEM 3 仅需净出口 + ACC 计算器。NEM 2 与 NEM 3 引擎分支必须分开建。
- **出口积分时间粒度**：按**小时**结算出口积分（间隔数据虽 15 分钟）。
- **NEM 计费分支**：NEM 3 出口积分用 ACC（夏季 8/9/10 月积分高）；NEM 2 用 TOU 零售费率、按 peak/off-peak/super off-peak 分别净出口结转、年末清零 + 净出口批发结算；区分 delivery 与 generation 两个独立积分银行；non-bypassable charges 仅对进口 kWh。
- **TOU 映射**：直接对原始间隔数据套费率，不需 baseline；处理季节性（冬季可能无 off-peak/super off-peak）。
- **节省（counterfactual）模型**：基线用**去年同期**、基于 **kWh**（非成本），覆盖完整温度区间；用反事实 kWh × 今年费率反推。
- **账单展示简化**：突出 **kWh + 总成本 + TOU 时段拆分**三项；把 wildfire/CCA/输配电等合并为 blended TOU 费率；住宅不展示 demand charge。
- **弱化 at-risk exposure 展示**：专家认为对客户信息过载，考虑收起或降权。
- **执行/自动化**：自动化以"确保最优"为前提；执行建议可附简化财务影响（kWh + blended rate），不必全量精确；事件检测灵敏度偏高（峰时 EV/AC 优先）。
- **电池调度规则**：峰时用 excess solar 充电池 OK；重点是 7-9 PM 不进口；NEM 3 下若预测出口积分大可考虑出口而非充电池。
- **数据策略（最大现实障碍）**：作为第三方申请、由客户直接共享间隔数据；接受约 3 天时延、按"事后"做计费计算；注意 PG&E 把第三方 SSL 证书续期从 1 年缩短到约 45 天，需为数据流稳定性做工程保障；要真正实时则需在客户处装智能电表（需客户同意）。
- **Bill Proof**：补充展示"从公用事业进口了多少"；不一致的最常见原因是数据不匹配；公用事业算错率约 5%。
- **定位**："避免账单意外"优先于"省钱"，但两者都做；强调账单符合预期。
- **顾问关系**：专家愿做 advisor，尤其在 true-up 上提供帮助；通过 chat 取得其邮箱后续跟进。

## 待澄清 / 信息不足（如实标注）
- ACC 制定咨询公司名——专家**推测为 "E3"** 但不确定（"might be... like E3 or I think um"）。
- NEM 1 是否有 true-up——专家不确定，**推测有且类似 NEM 2**。
- 冬季 TOU 是否有 off-peak/super off-peak——专家不确定。
- UCSF 所用能源服务提供商公司名——转录为 "Alura"，拼写存疑。
- 公用事业算错率 5% 为专家个人估计（与同批另一位专家约 0.1% 的估计存在差异，记录备查）。
- EV 改非峰充电省 50% 为专家估计（"I would guess"），非实测。
- 硬件加装的合规/认证（FCC/UL/NRTL/安规等）——本访谈**未涉及**，专家仅就"需客户同意"作答。
