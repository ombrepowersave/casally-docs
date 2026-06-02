# David Lodge · 硬件（hardware） · 2026-05-22

## 受访者画像
- David Lodge，加州持牌电工（CA Licensed electrician），自称**住宅领域专家**（"I'm definitely a residential specialist"），同时表示自己也做过不少商用工程（"while I know I have worked in commercial a lot"）。
- 爱尔兰口音（开场主动提醒访谈者可能听不清，让他重复）。
- 主要作业区域提到加州东湾 **Tri Valley**（Livermore、Pleasanton、Dublin 三城）——原文转录为 "Liverour"，按上下文几乎可确定为 Livermore（标"存疑"，下同）。
- 工作内容以住宅 EV 充电器安装为主（"the one that I do nine times out of 10"），也装过监控/控制类设备。
- 利益相关说明：本次为付费访谈（David 结尾感谢 "thank you for the payment on a on my last hour on a Friday"）。
- 访谈方：Amber Fu，公司名念作 "Cassie"/"Casally"（即 Casally）。

## 主题判定
判定为 **hardware（硬件）** 主题。
- 目录前缀 `s5-Hardware1.0` 初判为 hardware。
- 正文内容高度吻合：通篇围绕 EV 充电器安装流程、服务面板/子面板、智能面板（Span/Leviton/Schneider）、Emporia 能源监控与充电控制、charge controller、断路器（tandem/quad/double pole）、许可与检查、meter collar/转换开关、失效安全等硬件话题。以内容判定 hardware 无疑义。

## 核心提炼

> 说明：David 全程明确**只谈住宅（residential）**，多次声明商用/工业另当别论。

### 一、控制 vs 监控：智能面板能控什么、控不了什么
- 访谈方一开始就强调：他们**不只要监控，还要控制**大负载（EV、AC，甚至洗衣、热水器等）。David 据此引出智能面板路线。
- **智能面板可整盘换：**
  - **Span 面板**（原文转录为 "span panel"）——访谈方当场反应"that is really expensive"。
  - **Leviton** 出了"更便宜的版本"，但**功能相同**：用手机远程控制设备，本质是"你控制的是面板"。机制：设备保持开机状态，由面板上的断路器（breaker）按定时器开/合来启停（如到 9:00 定时器触发→面板把那路 breaker 合上→车开始充电）。
  - **Schneider 智能面板**（原文转录为 "Snider smart panel"，按品牌纠正为 Schneider，标"存疑"）——很新，安装量很少。
- **关键限制（能控什么、不能控什么）：**
  - 面板控制方式适用于"会自动启动"的设备：**AC、洗碗机（dishwasher）**这类——断电时它不动，来电（合 breaker）时它会自己启动。
  - **不适用烘干机（dryer）这类**：你能用 breaker 把烘干机**关掉**，也能远程把 breaker**合回去**，但**无法让烘干机重新启动**——除非烘干机本身接入了 App。David 反复澄清这点（"you can turn the breaker back on remotely but you would not be able to turn the dryer back on with this unless the dryer itself was connected to the app"）。
  - 所以面板能做的是：在面板处**开/关 breaker**，并在面板处**监控这些 breaker**（Span 或 Leviton 面板）。
- **采用现实（David 的一手观察）：**
  - 他亲手帮客户装智能面板**只有一次**（"One. One. Just one."）。
  - 谈过很多对智能面板感兴趣的人，**一听报价就不装了**（"when I would tell them how much it would cost, they would... stop"）。
  - 愿意装的**通常是科技圈的人**（tech people）——喜欢用手机看家里所有东西、监控用电与花销。
  - 多数人还不上智能面板，因为**仍然很贵**。

### 二、面板基础概念（David 给访谈方扫盲，挖透）
- **Service panel（服务面板）**：户外、带圆形电表（circular meter）的那个面板，电表由公用事业公司（utility，举例 PG&E）控制。澄清：**电表归 PG&E，面板本身归住户**（"the meter on that panel belongs to PG&E, the panel belongs to the house"）。访谈方理解为"类似 breaker box"，David 确认。
- **Sub panel（子面板）**：屋内的面板，通常在车库或壁橱里。**房子自带、已经在那里，不用额外花钱买。** Span 通常属于 sub panel（"the span would usually be a sub panel... it's not a service panel yet"）。
- **现有的智能 service panel**：现在有"作为 service panel 的智能面板"，可用手机控制，但**非常新、安装量很少**。
- 面板容量决定可装充电方案（见三）：100 / 125 / 200 amp 面板对应不同上限；面板大小一般取决于**房子大小**。

### 三、EV 充电器安装：三档方案 + 标准流程
**充电三档（取决于面板容量，从高到低）：**
1. **硬接线充电器（hardwired charger）**：占 **60 amp** 回路，直接接进充电器。**最高档**，约 **25 英里/小时** 充电速率。需 **200 amp 面板**才稳妥。
2. **50 amp 插座（receptacle）**：面板较小（如 **125 amp**）时用。装法：户外 service panel→钻孔进车库→屋内装 disconnect→disconnect 下方装插座→面板内装 **GFCI 断路器**（ground fault circuit interrupter，地故障保护，触电时 **300 毫秒**断电，"instead of being caught and cooked and killed"）。约 **20 英里/小时**。
3. **30 amp 插座**：面板更小（如 **100 amp**）时用，配 30 amp GFCI 断路器，约 **15 英里/小时**。

**最常用基础装法（hardwired，nine times out of 10）：**
- 用户外带电表的 service panel（前提是有空位放 breaker、能承载充电器）。
- 打开该面板→钻孔进车库→车库墙上装 **disconnect**（紧急切断装置，必须与充电器在**同一房间、可视线范围内**）→disconnect 旁边墙上装充电器→用**柔性导管（flexible conduit）**从充电器连到 disconnect→端接（terminate）。
- 安装本身**最多两小时**。

**许可（permit）与检查流程（David 讲得很细）：**
- EV 充电器**需要市政许可**，而且**许可比安装本身还贵**——常规接近两倍。
- 价格：靠近城市的地方，**许可约 $700–$900**，而**安装只要 $400**。许可贵的原因主要是"我的时间"（申报、提交材料、等待往返）。
- 流程：客户雇 David → David 向市政提交申请 → 约一周后市政要材料（**load calculation 负荷计算、site plan 现场图、充电器说明书**等，各市不同）→ 提交后约一周批准 → 与客户约施工/检查（检查通常在下午 12:00–3:00，各市不同）→ David 提前约两小时到（如 10:00 a.m.）做安装 → 等检查员来 → 出示许可、检查员查验签字 → 完工。

**"非法充电桩"现象（David 强调、带情绪的点）：**
- **多数电工和很多不懂行的杂工（handymen）不办许可**，直接 $400 装掉。结果各城市到处都是"基本上违法"的充电桩。
- 后果场景：两年后客户要 remodel，必须 pull permit，市政来查 remodel 时发现"有个没许可的充电桩"——**这种情况经常发生**（"that happens a lot of the time"）。
- 处置：市政**不是罚款**，而是强制客户补走许可流程、证明安装合规（up to code），按当初本该收的金额收（$700–$900）。
- David 的判断：客户往往**不知道这是违法的**，因为电气承包商为压成本没告诉他们。

### 四、轻量化控制方案（访谈方核心诉求："lighter way"）
访谈方明确：智能面板"太重"（要换面板、太新、太贵），想要只控**大负载**的轻量方案。David 给出路径：

- **Emporia 能源监控系统**（原文多处转录为 "Emporia/Empora/Emporium/imperial/in Pora"，明确品牌为 **Emporia**，并明确用 **CT 钳/clamps**）：
  - 易装在**任何老面板**上，但**只监控、不控制**（"it doesn't control anything... It simply tells you what's happening"）。
  - 借它的数据可向客户给建议（如"4:00–9:00 是高峰，你的 EV 充电器开着，不建议现在用"），但**它本身不能真正关掉充电器**。
- **轻量控制组合：能源监控 + Wi-Fi 控制插头（Wi-Fi controlled plugs）**：插入 50 amp 插座或普通插座、连手机的 Wi-Fi 插头，用来控制单个大负载。
- **Charge controller（充电控制器）—— David 主推的真正可控方案：**
  - 用途：当客户想要 60 amp 硬接线充电器、但面板只有 100 amp，**市政不允许直接装**，除非加 charge controller。
  - 原理：带 clamps，监控进线功率（incoming power），只在确保面板不会过载时才允许那 60 amp 充电器开启。
  - **过载定义（David 讲透）**：100 amp 面板的 100 amp 断路器额定**连续负载 80%（即 80 amp）**——若超 80 amp 持续超 **3 小时**会发热跳闸；或瞬时超 100 amp（如 105 amp）也会跳。
  - **Emporia 充电器 + Emporia 监控系统**协同：监控全屋用电，只让充电器抽取 80% 内未被占用的电流。例：全屋用 40 amp，系统允许 Emporia 充电器抽 39 amp，加起来到 79 amp，不跳闸。
  - **David 的推荐与现状判断（一手）：**
    - **Emporia 的 charge controller 是他给每个客户推荐的，因为最便宜**。
    - 但他装过的 charge controller **都不是 Wi-Fi 控制的**——它们只是"看系统、监控、必要时关掉"。
    - 他认为 Casally**很有可能找到/做出一个 Wi-Fi 可控的 charge controller**用 App 控制。
- **市场结论（David 反复强调）**：就当前市场而言，控制 EV 充电器**最佳的轻量方案就是 Emporia**，他**没见过比这更好的**。Emporia 充电器与 Emporia 能源监控**成套配合**（买充电器+买能源监控，二者配对）。

### 五、失效安全 / 安全设计（访谈方"最大的担忧"）
- 访谈方问：若控制设备断网/崩溃/App 失效，怎么保证不让住户断电？
- David 主张**配手动开关（manual on/off）**：例如做一个插进 50 amp 插座的 50 amp 插头作为 charge controller，**既能 Wi-Fi 控制、也带物理开关按钮**；他指出这类设备"通常都有 on/off 按钮"。现在市面上的家用能源监控设备就有"既可手机控、也可设备侧按钮控"的。
- "安全地坏"应是什么状态？David 答：**就是把它关掉**（"obviously to just turn it off"）——"没有电就没有危险"（"If there's no power, there's no danger"）。
- **责任归属**：若装了控制设备出问题（误关断、损坏设备、或没能把东西重新打开），责任在谁？David：**他会把责任归到客户身上**——安装前他做推荐，但会说"请自行研究、看评价、确认满意"；建议 Casally 可以让客户**签免责声明（disclaimer）**，声明"这是他们的设备、是他们的责任"。

### 六、哪些设备愿意/不愿意装、踩过的坑
- David 说**电气类的我都装**（"I'll install anything electrical"）。
- **踩过的坑（重要、具体）**：几年前 EV 充电器刚出现时，电工们用 **Home Depot 的 50 amp 插座**——虽标称 50 amp，但**没人知道它们并不耐 6–8 小时的 50 amp 连续负载**，结果这些插座**开始熔化（melt）**。
  - 现在他**不再装那种**，必须用 **EV 级（EV rated）插座或工业级（industrial rated）50 amp 插座**，即为连续负载设计的。
  - **连续负载定义**：**3 小时或以上**即为连续负载。

### 七、自动控制的安全边界（住宅 vs 工业）
- 访谈方问：哪些家庭负载可安全自动控制、哪些绝不该控制？
- David（明确限定**住宅**）：**带监控的情况下，控制什么都行**（"it's okay to control anything with a monitor"），想不出住宅里有什么会因此变危险。
  - 唯一顾虑：**有小孩在场、设备意外启动**；但他随即说 dryer、EV 充电器、AC **都伤不到小孩**——这些设备都有内置防护，没人能伸手碰到电气部分；现代插座都有**防篡改（tamperproof / tamper-resistant）**设计，小孩插不进东西。
  - 住宅没问题，**工业/大型机械另说**：大型可自动启动的设备**必须有人工许可（manual permission）**，由现场负责该设备的人亲自许可。
- **住宅电气变化慢、可预测**（与商用相反）：原因是**基础电气系统通常不是电子化的**——电气面板"没有软件要升级"，不论是 1970、1998、2010 还是 2015 年的，"没有任何自动化成分"，就是**即插即用、开/关的设备**（"a plug and play on and off device"）。

### 八、第二电表 / Meter Collar / 转换开关
- "第二电表"：David 说他**只在有太阳能时见过住宅装第二个电表**，那是太阳能设备、不是控制设备。
- **Meter collar（电表环/套）—— 加州近期才批准**：把 service panel 上的电表取下→装上 collar→电表再装回 collar 上；collar 上有个插口（plug）接发电机（generator）。作用：**PG&E 停电时，可用发电机通过 collar 给整屋供电**。David 提示 Casally："你们也可以控制一个 collar"，或做一个**监控全屋进出功率**的新版本。
- 访谈方展示了一张图，是 **Enphase IQ Meter Collar**（原文转录为 "IQ meter caller"/"end phase"/"in phase"，按品牌纠正为 **Enphase**，标"存疑"）。David 看了说：那其实是**发电机用的电子转换开关（electronic transfer switch / generator attachment）**，**不是**太阳能客户专用。
- David 对 collar 路线的评价：**不如 Emporia**——因为 collar 只测"进屋有多少电"（如"这客户用了 60% 的电"），**看不到细节**（看不到 dryer 开着、cooker 开着等），不像 Emporia 能监控全屋每一项。

### 九、监控设备的许可问题（与 EV 充电器不同）
- 监控设备（如 Emporia 能源监控）**他做过几个、都没办许可**，因为**没有布线（no wiring）**——没有从面板拉线到别处，只是在面板里装监控器。
- 但他补充提醒：**有些城市可能要求给传感器/监控也办许可**，因市而异。**保险起见就当作需要许可**，监控许可大概 **$400**。
- 许可申请人：**电工或客户都可以申请**。加州（乃至全美各州）允许房主在自家做电气、自己 pull permit；市政之所以要来检查，是为防止房主做危险电活（"which they do... all the time"）。David 评论美国人常说"不想政府进我家、我自己来"，他会劝阻——电活不该自己做，"you could die"。

### 十、Emporia 安装成本（David 给的报价）
- 安装 Emporia（含硬接线充电器 + 监控系统）：约 **3 小时**，**$600**（先说"500 bucks maybe"，随即改口"let's call it 600 bucks and let's call it three hours"）。
- 加上 EV 充电器必需的许可 **$700–$900**（视地区）。
- 监控器本身若按需办许可约 **$400**。
- Emporia 与 David 之间**没有合作/返点**：客户自己买、David 负责装，他没见过厂家给安装费或硬件加成（"I haven't seen that. No."）。

## 关键金句
- "There's a panel called a span panel." —— David Lodge
- "Leviton does another version that's cheaper, but it is the same thing where you can remotely control devices with your phone. You're controlling the panel." —— David Lodge
- "You can turn the breaker back on remotely but you would not be able to turn the dryer back on with this... not unless the dryer itself was connected to the app." —— David Lodge
- "Most electricians and a lot of handymen who don't know what they're doing will not get a permit and will install it for $400. So, there's lots of chargers all over the cities that are basically illegal." —— David Lodge
- "There is an energy monitoring system provided by the company Emporia... that's easily installed on any old panel, but it doesn't control anything. It simply tells you what's happening." —— David Lodge
- "Only allows the customer to turn on that 60 amp charger when it makes sure that the panel is not going to be overloaded." —— David Lodge（讲 charge controller）
- "If your house is using 40 amps, the Emporia monitoring system will allow the Emporia charger to pull 39 amps up to 79 amps so it doesn't trip the breaker." —— David Lodge
- "It's very possible that you guys could find a Wi-Fi controlled charge controller that you can control with your app." —— David Lodge
- "Obviously to just turn it off. If there's no power, there's no danger." —— David Lodge（失效安全）
- "I have to make it the customer's responsibility... you guys could have a disclaimer to have them sign it that says this is their device. It's their responsibility." —— David Lodge
- "These receptacles, while they were rated at 50 amps, we didn't know that they weren't rated for 50 amps for six or eight hours... those devices started to melt." —— David Lodge
- "It's okay to control anything with a monitor... nothing comes to mind that could be dangerous." —— David Lodge（限住宅）
- "Basic electric systems are generally not electronic... There's nothing automated about it. It's a plug and play on and off device." —— David Lodge
- "The best way to control your EV charger right now is definitely the Emporia." —— David Lodge
- "Don't do electrics yourself. You need someone who knows what they're doing because you could die." —— David Lodge

## 行动项 / 机会点
- **产品方向（David 直接点出）**：现成最优轻量控制方案是 **Emporia 充电器 + Emporia 监控**成套；Casally 的差异化机会是做一个**Wi-Fi/App 可控的 charge controller**（目前市面 charge controller 普遍非 Wi-Fi 控制）。
- **失效安全设计**：控制设备应**带物理 on/off 按钮**，失效时**默认关断**（"没电=没危险"）；可考虑做成插进 50 amp 插座的 50 amp 智能插头形态。
- **责任/合规**：为控制类设备准备**用户签署的免责声明**，把设备责任落到客户。
- **许可策略**：EV 充电器许可必办（$700–$900，比安装贵）；监控/传感器许可**因市而异，保守起见按需要办（约 $400）**；许可可由电工或房主申请。
- **硬件选型红线**：50 amp 插座必须用 **EV 级或工业级**（耐 3 小时以上连续负载），杜绝 Home Depot 普通 50 amp 插座（会熔化）。
- **面板容量适配**：方案需按面板容量分档（200→60A 硬接线 / 125→50A / 100→30A），并考虑面板满位时的 tandem/quad breaker 或加 sub panel（详见下"补充"）。
- **可探索的新硬件形态**：可监控全屋进出功率的 **meter collar** 变体（但 David 认为颗粒度不如 Emporia，看不到单设备）。
- **可持续合作**：David 表示愿意作为顾问继续帮 Casally 评估方案是否合理（"Of course... Anytime"）。

## 补充：面板满位时的扩容做法（David 现场演示讲解）
- 打开住宅面板时，空位被占满**偶尔**会遇到（David 自我纠正：不说 "often"，应说 "occasionally"，但也说"often 打开面板各位都满了"——口语前后略矛盾，照实记录）。
- 标准家用车库面板有 **12 个位（spaces）**，装 12 个标准断路器。
- **Tandem breaker（连体断路器）**：一个位放两个断路器→12 位面板可做到 **24 路**。比标准断路器贵。
- **Quad breaker（四联断路器）**：占**两个位**，同样用于扩容到 24 路。
- 若已经被人做过扩容、再无空间：在旧 sub panel 旁/下方加一个**新 sub panel**，把部分回路从旧面板**改接（reroute）**到新面板，旧面板里装一个**双极断路器（double pole breaker）**给新面板供电。
  - David 解释 double pole breaker：用于 **240V**，占两个位、但属一个回路；两路 110V 进、出来 240V。

---
### 转录纠错与存疑标注（汇总）
- **Span 面板**：原文 "span panel"，按品牌确认为 Span。
- **Emporia**：原文多处转录为 "Emporia / Empora / Emporium / imperial / imperia / in Pora"，统一纠正为品牌 **Emporia**。
- **Schneider 智能面板**：原文 "Snider smart panel"，按品牌纠正为 Schneider（**存疑**，依发音推断）。
- **Enphase IQ Meter Collar**：原文 "in phase / end phase / IQ meter caller"，纠正为 **Enphase IQ Meter Collar**（**存疑**，依发音与产品名推断）。
- **Livermore**：原文 "Liverour"，按 Tri Valley 地名纠正为 Livermore（**存疑**）。"Tri Valley = Pleasanton + Dublin + Livermore" 为原文所述三城。
- **PG&E**：原文 "PG / PG&"，按上下文为公用事业公司 PG&E。
- 其余口语含糊/未说清处（如个别成本数字 David 自己也用 "maybe / let's call it" 估算）已照实标注为估算，未补全。
