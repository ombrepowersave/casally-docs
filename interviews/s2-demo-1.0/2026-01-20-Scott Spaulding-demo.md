# Scott Spaulding · Demo 反馈 · 2026-01-20

## 受访者画像
- 拥有 Tesla Powerwall（电池）+ 太阳能 + 特斯拉电动车（EV）的家庭用户，是 Tesla App 的日常使用者。
- 电价方案为 NEM 2（原文转录为 "NEM 2"），所在地区没有动态买卖电价（dynamic buyback/sell price），他自述"我们没有动态买卖电价那种东西"。
- 太阳能系统此前用过微逆变器（micro inverters），现在没有了；他注意到烟囱在某块太阳能板上投下的一点小阴影几乎让整块板发电量归零（"a little tiny shadow from my chimney on the solar panels almost kills 100% of the production"），因为没有微逆变器。
- 拥有 Powerwall 的时间还不长——这是他第一次用 Powerwall 经历完整季节（"going through the season for the first time with my Power Wall"），访谈时正处冬季、日照短、发电量低。买 Powerwall 之前已用特斯拉一段时间。
- 最低电价时段是早上 8 点（"the lowest rate, which for me is 8 am"）。
- 自评对 Google Meet 不熟（"I don't have that much experience with Google Meet"）；本次看的是 Figma 早期版本 Demo，由访谈者 Amber Fu 引导。

## 主题判定
判定为 **Demo 反馈**：受访者在 Figma 早期 Demo 上逐页（主屏 / 事件页 / 节省页 / 电池切换 / 个人资料页）给出对功能、界面、文案的反应与改进建议，并反复与现用的 Tesla App 对比。目录前缀 s2-demo-1.0 与内容一致。

## 核心提炼

### 逐功能反应

**主屏（Home screen）**
- 打开 App 他第一件关心的是核心实时指标："电池电量状态（state of charge）、太阳能发电量、家庭用电量"——这是他平时打开 Tesla App 的习惯动作。
- 明确表示想要类似 Tesla App 主屏那种**动态能量流图示**：用代表性图像展示房子、Powerwall、太阳能板，且是动态的、显示能量流动和指标。"I would want to see something roughly similar... that's a good place to start." 他认为这是个好的起点。
- 对 Demo 主屏的"需要关注"红色横幅：他理解红色=需要触发动作（"when it's red... it would trigger action"），同时注意到还有黄色和蓝色。

**事件页（Event page，以 solar / Tesla power 为例）**
- 困惑点：电池上的红点不懂什么意思（"I don't know what that red dot means in the battery"）。
- 文案建议：如果这是 alert，就应该写"alert / needs attention"，而不是现在的样子。
- 按钮文案："remove" 应改成 "remove warning" 或 "remove alert"，更易懂、让用户清楚自己在做什么。
- 认为这个事件/设备拆解页更适合承载"系统需要你关注"这类提示，可以说明"发生了什么、为什么重要/影响"。
- 缺失项确认：他认同应加上**警报的解释（为什么触发）**，以及**下一步该怎么做的建议**——被问到时都答"会有帮助"。

**节省页（Savings）**
- 明确低优先级："savings is not a high priority"、"not something that I look at first"、不会经常去这个页面。
- 原因一：可能是 garbage in garbage out——结果依赖电价等输入参数是否准确。
- 原因二：节省数字**不会改变他的行为**，因为除了"别在高峰时段充电"之外能做的不多（"there's really not much you can do outside Don't charge during peak hour"）。
- 但他认为放在那里没错，是个好提醒（Tesla App 也有 savings tab）。对"预期 vs 实际发电、美元总额"这类呈现表示"fine、不关键也不坏"，并说"更多信息通常更好"。

**电池切换 bottom sheet / 数据源**
- 对"Powerwall 切换到电池"的说明 sheet：对他而言不是新信息——他和大多数人拿到电池就知道电池干嘛用（"this wouldn't be new information to me"）。
- 数据源页：同样归为 garbage in garbage out，且电池的用途在这里是隐含的，对他"不太有帮助"。

**个人资料页（Profile）**
- 总体评价正面："I think this is good"、信息量大；认同"功能越多、信息越多越好"。
- 主动提出的缺失/期望（见下）。

### 首次理解 / 价值认知
- 没有出现明显的整体"aha 时刻"；他主要把 Demo 各页与 Tesla App 逐项比对，判断"够不够用 / 有没有比现状更好"。
- 价值认知集中在：他真正想要的是**更聪明、可由用户下指令的自动化（if-then 规则）**，而不是被动看数字。Savings、数据源说明等被他判为"对我用处不大"。
- 对"对谁有用"：他认为 if-then 建议/规则"对很多人都会有帮助"，但强调每个人情况不同、需要可自定义。

### 可用性问题 / 卡点
- 主屏信息分组问题（重要）：他指出"something may require your attention"横幅与下方"你的 EV 正在高价时段充电"这条消息在 UI 上**没有被关联在一起**，中间隔着两个 tile。建议把 usage/saving 移到消息下方，或把告警与具体消息放进**同一个 tile** 让二者关联。"it took a little bit of effort to try to figure that out."——他费了点劲才看懂二者关系。
- 事件页红点语义不明（见上）。
- 引导环节本身有不少来回（找 Figma 链接、分辨"左侧/右侧/iPhone 内 vs 网页"），但这多为会议/操作沟通问题，非产品本身卡点。

### 功能请求 / 改进建议（受访者主动提出，强调充分）
- **核心诉求：if-then 规则 / 用户可自定义自动化。** 他多次、具体地强调，情绪明显（把 Tesla 现状称为"bad design"）。例子：
  - "if the battery is 60% then do X"
  - "if 用电高于 ~2 kW 就从电网取电、不从电池取"（任何时候）
  - "if 电池低于 50% 就从电网取电"
  - 更精细："家庭负载超过 X 就别从电池取 / 只从电池取 X、其余从电网"——他自己也说"会很快变复杂"。
- 规则的产品形态建议：
  - 理想是**用户能自己创建规则**；也可提供来自用户反馈的**通用规则**供选；可以是自然语言输入，App 据此给建议；也接受"原始方式"——给选项让用户勾选，而非纯自然语言。
  - 提到网站上可有"表单"，让用户提交 if-then 规则，使 App 比用户自己写得更能理解。
- 规则管理（很在意）：
  - 规则需考虑**季节性**，会随季节变（日照、驾驶、家庭用电变化）。
  - 可能有"相似但不同"的规则，需要"激活态 / 选哪条激活 / 优先级"。可用 checkbox 标记 active。
  - **强烈的负面要求**："不要出现我建一条规则、被另一条覆盖后回不去、还得重建的情况——那会非常烦人。"
- 主屏沿用 Tesla 式动态能量流图示（见上）。
- 事件/告警：加解释 + 下一步建议 + 改文案（见上）。
- **异常检测**（在 Profile 页提出，主动且具体）：希望 App 能监测系统、随时间学习正常用量，出现偏差时提醒。例如"夏天大晴天本该高发电，若没有就该告警——可能是故障，也可能只是阴天"。

### 与现状对比（Tesla App）
- 参照系几乎全是 Tesla App。正面：Tesla 主屏的动态能量流图示好，他想要类似的；savings tab"有挺好"。
- 负面（情绪强）：
  - **"babysit"（照看）**：系统技术上能跑，但他得一直盯着、还会忘记设置。上次访谈后情况变糟，因为入冬发电下降。"I've been doing that way more than I should be recently and I'll forget to do stuff." Amber 称 babysit 是个好词，他认同。
  - 冬季痛点具体：电池没满时，Tesla App 会**默认先从电池取电**，他不想这样；当前唯一办法是把电池预留阈值人为设到 80–90% 来"骗"系统（trick it）默认走电网——他直指这是"bad design on the Tesla app"。他更希望低价时段（早 8 点）从电网充。
  - Tesla 把充电计划从二级菜单挪到三级，他觉得烦——多一步。由此提出层级原则：第一级能进到"让你做想做的事"的入口、二级 OK，三/四级就烦人。
  - 实时发电诊断：他靠 Tesla 主屏图示发现"大晴天却只发 5%"，最终查出是单块板的小阴影——说明实时图示对诊断很有用。
- 会不会换：**未明确表态**会从 Tesla 切换到本产品。他愿意继续参与（愿意再看改版、愿意随时邮件反馈想法），但没有给出迁移/替换意向。

### 购买 / 付费意愿信号
- **未涉及**：全程未谈价格、付费意愿、愿付多少或购买条件。

### 不一致 / 犹豫信号
- 对多个功能"嘴上说 fine / 不坏"但**态度明显冷淡**：savings、数据源说明、电池用途 sheet 被反复归为"对我用处不大 / 不是新信息 / garbage in garbage out / 不影响我行为"。即"说可以接受"≠"看重"。
- 真正有热度、讲得最细、情绪最强的只有 **if-then 自定义规则** 和**摆脱 babysit**；这是他对本 Demo 的核心价值落点，其余多为礼貌性认可。

## 关键金句
- "myself wanting a smarter app that would operate with like if then statements... something like if the battery is 60% then do X." —— Scott Spaulding
- "that's just bad design on the Tesla app." —— Scott Spaulding（指 Tesla 默认先从电池取电、只能靠设高阈值来"骗"它走电网）
- "if the user would somehow have the ability to set their own rules, that would make it super powerful because... everyone's different." —— Scott Spaulding
- "I wouldn't want a situation where I create a rule and then I override it with another rule and I can't go back to the other one or I'd have to recreate it. That would be super annoying." —— Scott Spaulding
- "savings is not a high priority... it's not something that would affect my behavior because there's really not much you can do outside Don't charge during peak hour." —— Scott Spaulding
- "it took a little bit of effort to try to figure that out."（主屏告警横幅与"EV 高价充电"消息没关联在一起）—— Scott Spaulding
- "one thing that would be good would be if the app could monitor the system... learn how it's used and then if there's an aberration from that, that would be notable." —— Scott Spaulding
- "a little tiny shadow from my chimney on the solar panels almost kills 100% of the production." —— Scott Spaulding
- "instead of remove... 'remove warning' or 'remove alert' would be easier to understand." —— Scott Spaulding

## 行动项 / 机会点
- **优先做用户可自定义的 if-then 规则引擎**：支持电池 SoC、家庭负载、电网/电池取电源、时段等条件；同时提供基于用户反馈的通用规则模板供选。这是受访者最强的需求点，也直击其"换不换"的决策核心。
- 规则管理需支持：多规则共存、激活/优先级（checkbox active）、随季节切换、可逆（不被覆盖丢失）。把"切换不丢、可回退"作为明确设计约束。
- 主屏：1) 提供 Tesla 式动态能量流图示作为起点；2) 修复信息分组——把"需要关注"告警与对应消息放进同一 tile / 紧邻，避免用户费力关联。
- 事件/告警页：红点等图标需明确语义；统一文案（"alert/needs attention"、"remove warning/alert"）；为每个告警加"为什么触发（含是否由用户规则引起）+ 影响 + 下一步建议"。
- 异常检测机会：基于历史用量学习"正常基线"，对偏差（如晴天却低发电）主动告警，并区分"可能故障 vs 阴天"。
- 信息层级原则：常用操作入口控制在一/二级，避免三、四级深埋。
- 降低 savings/数据源说明等页面的展示权重（对该类深度用户非决策驱动）；但保留作为提醒，并确保输入参数准确（否则被视为 garbage in garbage out）。
- 关系维护：受访者愿意复看改版、愿意随时邮件反馈，可纳入持续反馈名单。
- 待补：本次未触及付费/价格，下次需探查付费意愿与切换 Tesla 的门槛。
