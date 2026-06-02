# Amos Elberg · 用户痛点 · 日期未知

## 受访者画像
- 科技从业者，与妻子均为来自旧金山的 tech people；现住北加州（Northern California）。
- 今年（2025）买房，7 月买下、9 月入住；房屋约 3,100 平方英尺，住 4 个成年人 + 1 个婴儿（受访者夫妻 + 妻子的退休岳父母，岳父母全天在家带孩子）。受访者与妻子都在家办公，妻子每周去办公室 2 天（混合办公）。
- 设备：今年 11 月初安装太阳能、11 月 12 日并网启用（采访时刚启用约一个多月，尚未收到装太阳能后的第一张电费账单）；有家用电池 Power Wall；有一辆 EV（Volvo 电动车）并配 EV 充电桩；充电桩品牌为 Wallbox（原文转录为 "Warbucks/robot"，受访者明确说是 Wallbox）。
- 取暖为电踢脚线加热器（baseboard heater）；有一台智能恒温器（但功能弱，仅支持排程）；烘干机与洗衣机为电器；烤箱为电烤箱。**无空调（AC）**——房屋有大量遮荫且为西班牙陶土瓦屋顶（Spanish clay tile roof），自然凉爽，外面 90 华氏度时室内不超过 80 度。
- 装过 Home Assistant 但从未真正用起来：「We configured it but we never figured out how to get it to do anything useful.」
- 安装太阳能 + 电池的动机：(1) 想在年底前装上太阳能；(2) 所有接触过的太阳能公司都说，因为 NEM 3（原文 "NEM 3"），只有配电池太阳能在财务上才划算；(3) 想离网（off the grid），夫妻都在意；(4) 设想用太阳能给 EV 充电，让交通「effectively become free」。买 EV 的原因：不想要汽油车、认为 EV 更好开（妻子去年才拿驾照，Volvo EV 很好开）；买充电桩只是为了充得更快。

## 主题判定
判定为 **用户痛点（pain-point）**。依据：访谈由 Casally 联合创始人 Amber Fu 主导，围绕受访者家庭日常用电、电费、现有 app/设备的不足展开；受访者大量、具体地表达了「charge on solar 很难」「app 市场碎片化」「太阳能发电量远低于预期」等真实痛点与代价。所在目录 `s1-pain-point-interviews` 与内容一致。

## 核心提炼

### 具体痛点清单

**1. 没有好用的「太阳能给 EV 充电（charge on solar）」方案——最核心、反复强调的痛点。**
- 受访者明确说这是他被问到"想改两件事"中的第二件：「making it easy to charge on solar because charging on solar is really hard now.」
- 他想要的逻辑：白天正午太阳能发电多于自用时，应把多余电量优先用于给 EV 充电、停止上网售电，从而避免晚高峰电价高时从电网买电；若发电不够，至少要在电价便宜时给 EV 充电、避免晚上充。「Optimizing the consumption of the solar is all about charging the EV on solar because the EV is the largest consumer of electricity.」他估计 EV 大约占家庭用电的一半（probably half of our electricity use is the EV）。
- 卡点 1——非 Tesla 车的生态壁垒：Tesla 充电桩 + Tesla 车之间能互相通信、能做 charge on solar；但非 Tesla 车（他的是 Volvo）配 Tesla 充电桩就不做 charge on solar，必须换不同充电桩、用 app 控制一切，「it all gets very complicated, and the apps aren't very good.」
- 卡点 2——net zero 的 charge on solar 不好用：net zero 虽有 charge on solar 能力，但若发电多于 Power Wall 当前可接受的充电量，它会把多余电量上网售电，而**不会**把这部分分配给汽车充电。「it'll still export to the grid... it's going to export to the grid instead of allocating that to the car.」
- 卡点 3——专用充电 app 兼容性差：Optawatt（原文亦作 Octawatt/Opawatt，应为同一 app）只支持部分充电桩（如 ChargePoint、wall box），不支持他的充电桩；Charge HQ 只做 charge on solar 且要 $10/月。

**2. 太阳能实际发电量远低于预期（当下最具体的"代价"痛点）。**
- net zero 用 PV Watts 估算这个季节应日发约 26 kWh，但他家实际只发约 9 kWh/天（另一处提到很晴的天约 10 kWh）。
- 后果链条（他自述）：很晴的一天发 10 kWh → 5 kWh 白天直接供房屋自用 → 5 kWh 给 Power Wall 充到 50~60% → 日落后用 Power Wall 顶高电价时段 → 电池到晚上 8 点左右就耗尽。
- 怀疑原因：树木遮荫多；安装方把板子朝西而非朝南装了（he thinks they installed it facing west instead of south），正在追问为什么。已要求并收到了 shade study（遮荫研究），正与安装商持续沟通；尚不确定是系统设计错误、安装错误，还是几个月后会正常发电。
- 情绪/后悔：「if we knew how little power we're producing, we probably would not have done it... we're just not producing enough power to make it worthwhile.」EV 充电桩"做到了想要的一切"、Power Wall"在按预期工作"，唯独太阳能板发电不足是问题所在。

**3. 智能家居/温控无法被智能调度。**
- 取暖最大可控变量是何时开/关电踢脚线加热器（开时耗 1 kW/小时）。
- 现有智能恒温器只能设排程、不如 Nest 智能，虽（他认为）有 API，但"没有东西能去控制这个恒温器"。
- net zero 也"不够聪明"去连接踢脚线加热器、或告诉你何时关加热器/给加热器设排程。
- Home Assistant 配置了却没能用起来（见画像）。

**4. 电池充放电时机不够智能。**
- 反复提到 Lunar AI（原文 "lunar AI"）那帮人在"何时给 Power Wall/电池充电、何时放电"上比 Tesla 更聪明；net zero "not smart enough to optimize when to charge the battery and when to discharge the battery like the Lunar AI app."

**5. app 市场碎片化、没有一个"全能"产品（贯穿全程的元痛点）。**
- 「it's a really fragmented space」「none of them is really complete and none of them really does everything.」
- 各 app 短板：net zero 最全面但 charge on solar 差、不会优化电池充放电、连不了加热器；Charge HQ 只做 charge on solar 且 $10/月；Optawatt 不支持他的充电桩。
- 一个本地化痛点：他所在加州地区除 PG&E 收费外，社区电力（community electricity）还另收一笔附加费（"search charge"，疑为 surcharge 转录误写），而**除 Optawatt 外，没有 app 把这笔附加费算进去**。

### 痛的程度 / 紧迫性
- 电费："on the order of $300–$350 a month"（装太阳能前），他觉得高（"our electricity bill has been very high"）。注：装太阳能后第一张账单尚未到，省电效果未知，且因发电量低，他"不认为太阳能会有大效果"。
- 后悔情绪明确：早知发电这么少"probably would not have done it"。
- charge on solar 的诉求强烈到被列为"最想改的两件事之一"。
- 创业者自身也长期琢磨此事："I've thought a lot about this." 并曾上网请教别人该如何向太阳能公司交涉（被建议要 shade study）。

### 触发情境 / 规律
- 用电高峰/家庭最忙时段：傍晚 5:00–8:00——夫妻下班、要哄婴儿、岳父母做饭，"always a lot of activity"。
- 家几乎从不空：自入住以来只空过一次（送岳父母去某处时）；岳父母与婴儿全天在家。
- 太阳能日内曲线：清晨发电极少 → 正午发电多于自用（多余上网售电）→ 傍晚电价上涨、需从电网买电。
- 季节：采访发生在太阳能刚启用（11 月中旬）后的冬季初期，发电量低问题部分可能与季节/低日照相关（受访者自己也不确定是否几个月后会好转——推断其季节因素，原文未下定论）。

### 各大耗电设备（受访者排序时的犹豫与修正）
- 最大：EV（约占一半用电）。
- 第二大：他先说"踢脚线加热器或烤箱"，随即更正为**烘干机 + 洗衣机**——烘干机每次启动耗 6 kW（他能在 net zero app 上看到曲线跳到 6 kW）。
- 踢脚线加热器：开时 1 kW/小时。
- 电烤箱：约 4 kW，但很少用（"只有感恩节烤火鸡之类才用"）。
- 无 AC，故无空调用电痛点（他对此感到幸运，"one of the nice things about the house"）。

### 当前应对 / 替代方案
- 在用 app：**net zero**（订阅约 $7/月，他记为 "$6.99 或类似"）+ **Optawatt**。
- net zero 评价：很擅长估算太阳能发电、监控系统、设排程，"does a lot of things really, really well"；但不擅长 charge on solar、不会优化电池充放电、连不了加热器。
- 对订阅费态度："I'm not a fan of it. I prefer not to be spending money"，但认为 net zero 当前提供了足够价值（因为他是太阳能/EV 新手，想详细看各设备表现）。一年后预期："要么 net zero 变得能用来设排程/把 charge on solar 做好，要么我一年后不续订。"
- 土办法/手动调度：曾规定"只在晚上用烘干机"，后改为"只在白天有太阳能时用烘干机"，但因发电本就不够"so it doesn't matter"。
- 与太阳能安装商持续交涉发电量问题（已拿到 shade study）。
- Home Assistant：配了但没用起来。

### 未被满足的需求 / 期望
- 一个能"全包"的系统：自动处理时机调度，优先用太阳能、再用便宜时段电价，自动安排 EV 充电、洗碗机、烘干机等，让用户"不用思考"就省钱。被问到是否愿意试，答："absolutely. Absolutely."
- 把发电量提上去（"最想改的两件事"之一）——若真能日发 26 kWh，"除了 EV 我们几乎完全离网"。
- 真正好用、跨品牌（不限 Tesla 生态）的 charge on solar，能把多余太阳能优先给车充电而非上网。
- 像 Lunar AI 那样聪明的电池充放电优化。
- 能连接并智能控制踢脚线加热器/恒温器，告诉/执行何时开关。
- 把社区电力附加费等本地费率算进优化逻辑。
- **控制权与隐私边界（明确表达）**：对 app 控制 Power Wall / Tesla 这种写权限有顾虑；他只会给**读权限（read access）**、不给**写权限（write access）**；若要 app 控制 Power Wall，他希望 app 先**提议一个排程让他确认（yes/no）**、并能随时查看 app 在做什么。

### 付费意愿
- 若产品真能每月省约 $100，他认为 $10–$15/月合理（"if it was really that effective, I would think 10 or $15 a month would be reasonable."）。
- 若有东西能优化用电（做到 Lunar AI 做的事或把 charge on solar 优化好），他愿意从 net zero **切换过去**："I would switch to that thing."
- 愿意当 beta 测试者（"Absolutely."），并表示想支持创业者。

## 关键金句
- "probably half of our electricity use is the EV." —— Amos Elberg
- "what we really want is to be able to charge on solar... but you haven't charged your power wall sufficiently... it's going to export to the grid instead of allocating that to the car." —— Amos Elberg
- "Everybody who we talked to told us that because of NEM 3, the only way to make solar have financial sense was to buy a battery." —— Amos Elberg
- "if we knew how little power we're producing, we probably would not have done it... we're just not producing enough power to make it worthwhile." —— Amos Elberg
- "making it easy to charge on solar because charging on solar is really hard now." —— Amos Elberg
- "Optimizing the consumption of the solar is all about charging the EV on solar because the EV is the largest consumer of electricity." —— Amos Elberg
- "if you have a car that isn't a Tesla, it won't do charge on solar with the Tesla charger. You have to use an app to control everything... and it all gets very complicated, and the apps aren't very good." —— Amos Elberg
- "it's a really fragmented space." —— Amos Elberg
- "none of them is really complete and none of them really does everything." —— Amos Elberg
- "We got Home Assistant... but we never figured out how to get it to do anything useful." —— Amos Elberg
- "I would have given read access... but I wouldn't have given write access... have it propose a schedule and say yes or... I would want to be able to check what it is." —— Amos Elberg
- "if it was really that effective, I would think 10 or $15 a month would be reasonable." —— Amos Elberg
- "if there was something that... optimized the charge on solar, I would switch to that thing." —— Amos Elberg

## 行动项 / 机会点
- **核心机会：做"跨品牌、真正好用的 charge on solar"**——把多余太阳能优先分配给 EV 充电（而非默认上网售电），不依赖 Tesla 闭环生态，覆盖 Wallbox 等非 Tesla 充电桩。这是受访者最强、最具体的诉求。
- **做"全能整合"产品**填补碎片化空白：在一个产品里同时覆盖发电监控 + 电池充放电优化（对标 Lunar AI）+ EV 充电调度 + 可控负载（踢脚线加热器/恒温器、烘干机、洗碗机）调度，让用户"无需思考"。受访者愿为此从 net zero 切换。
- **费率精度是差异点**：把本地社区电力附加费（surcharge，原文 "search charge"）等纳入优化，多数竞品做不到。
- **权限设计要点**：默认只读、写操作走"先提议排程 → 用户确认 → 可随时查看"的人在回路模式，直接对应受访者对隐私/失控的顾虑。
- **定价锚点**：若可证明月省 ~$100，$10–$15/月可接受。
- 受访者明确愿意当 beta 测试者，可纳入早期内测名单。

## 纠错与不一致信号
- 转录纠错（已在正文标注）：充电桩品牌 **Wallbox**（原文 "Warbucks/robot/wall box"）；**NEM 3**（净计量政策，转录正确）；**Lunar AI**（原文 "lunar AI"）；**Optawatt** app（原文出现 "octawatt/Opawatt/Optawatt" 三种写法，应为同一产品）；社区电力的 **surcharge** 附加费（原文转录为 "search charge"，按语义推断为 surcharge）；**PG&E**（原文 "PG&"）。
- 数据不一致（保留原文、未替受访者裁定）：太阳能实际发电量他先说 "9 kilowatt hours a day"，后在举例时说 "10 kilowatt hours"；二者都保留。
- 日期未知：逐字稿无明确日期，仅可知太阳能 11 月初安装、11 月 12 日并网，且采访在并网约一个多月后（推断为 2025 年底，原文未明示年份）。
- 关键留白：装太阳能后第一张电费账单尚未到，省电实效未知；发电量偏低的根因（设计/安装/季节）仍在与安装商核实中，未有定论。
