# Marc Jaffe · Demo 反馈 · 2026-02-05

## 受访者画像
- 居住地：San Diego，电力公司为 SDG&E（San Diego Gas & Electric）。
- 住房能源配置：家用太阳能 + EV + Level 2 壁挂充电器（wall charger）+ 智能家居。属于"自己已经把事情做对了"的高阶能源用户。
- 太阳能：已安装约 4 年（"I've had solar for I want to say four years"）。处于 NEM2（净计量 2.0），并"grandfathered for 20 years"（享 20 年祖父条款保护）。邻居上周才装，属于 NEM3。
  - 转录纠错：逐字稿多处出现 "MEM2 / EM2 / any3 / runner any3" 等，均为语音转录 NEM2 / NEM3（Net Energy Metering 2/3）的误转，已按本意理解。
- 电费极低：电费在 $0–$80 之间；目标是做到零账单（"ultimately I'd like to have a zero bill"）。
- 费率结构：EV 时段费率计划（time-of-use / EV plan）。电是真正关注点；燃气是 flat rate、固定不变，不关注。10 月起新增 $24/月的固定费（set fee）。
- 设备/费率细节：电费分三档费率、24 小时内四个时间窗（super off-peak / off-peak / on-peak），周末与节假日时段不同（周末 super off-peak 从 12:00 a.m. 一直到 2:00 p.m.）。EV 充电用壁挂充电器排程（只在 off-peak 充，除非手动），Tesla app 只用来设充电上限（80%）和电流（40A 电路设 32A）。
- 近况：几个月前买了第二辆电车，电费正处于变动期，尚不清楚最终影响；已向太阳能安装商询价加装更多面板，但因当前是冬天日照少，打算再观察几个月再决定。

## 主题判定
判定为 Demo 反馈。依据：访谈者 Amber 发来 demo 链接（"a fake mock"，无需登录），受访者全程共享屏幕、从顶部逐屏点击体验（monthly budget、实时条、usage 图表、event 页、saving/bill 页），并针对每个功能给出喜欢/困惑/改进意见，最后讨论付费意愿并自荐做 beta tester。

## 核心提炼

### 逐功能反应

**Monthly budget（月度预算）卡片**
- 理解到位：点开后看到"set a monthly budget limit, based on last three months bills and your rate plan"。自己推断"the more data I put in, the more accurate it's going to be"，把它理解为"target bill（目标账单）"。
- 主动提的关键困惑/需求：
  - 燃气是否计入？反复追问"is this electric only? Do I leave the gas out?"。Amber 答燃气不计入。Marc 强调要确保只录入电表信息、不混入燃气表。
  - 录入项：固定费 $24/月、每度电费率，以及是否要录入 time-of-use（因为用量在 peak/off-peak/super off-peak 三档间变化，"那这部分必须包含进去"）。

**自动/手动 设置（接 Tesla / 品牌 app）**
- 看到的是自己 Tesla app 的截图，明确表示困惑："I don't know what it wants me to do here"。
- 解释自己实际用法：Tesla app 只用来设充电上限（80%）和电流（32A），不用 app 排程充电；排程是用 Level 2 壁挂充电器做的。
- 功能请求（强）：希望 app 也能纳入并显示他的 **EV 壁挂充电器（wall charger）**，因为排程实际在那台设备上。希望能加自己的两辆 EV + 壁挂充电器，每个卡片显示同样的参数（活跃时间窗等）。
- 对"actionable moment"卡片结构（上=what's happening / 中=what to do / 下=time window，即 reason–action–time）理解并认可。

**其他家电（洗碗机、洗衣机、冰箱）**
- 主动问"How do I do anything with those? ... Those are all power-hungry devices."。Amber 答现在还不行、以后可以。
- Marc 自己补充：冰箱不可控（"the fridge goes on when it goes on"）；洗碗机有定时功能但通常手动开；洗衣机他尽量在非高峰时段用。

**实时条（real-time bar）**
- 明确确认是不是实时（"is this real time or not?"），得到肯定后表示这是他最看重的功能。
- 关键关切（上次也提过）：自家电表在发电多于用电时会倒转（"my reader runs backwards"），追问是否已纳入。"If I'm looking at real time, I want to make sure it's coming off my meter."
- 功能请求：希望能区分显示"正在送电回电网"——比如用电时绿、回送时红。但自评"I guess that's not necessarily crucial"。
- 价值点：实时数据会改变白天用电习惯（"it's noon, I'm producing all this power, now's a good time to run a washing machine"）。Amber 认可会加入。

**Usage 图表（按时段的用量柱状图）**
- Amber 提到"a few users 看 usage 这部分会 confused"。
- 改进建议（受访者反复、强烈强调，是本场最深的一处）：在柱状图背景按时段着色（shaded background），把 24 小时的四个时间窗（super off-peak / off-peak / on-peak / off-peak）用不同底色画出来，这样一眼就能看出"我最高的柱子是不是落在 super off-peak"。现状下他"would have to guess"柱子落在哪个时段。
  - 强调这是"way it's presented so I can really kind of do a quick look and understand it"——是呈现方式问题，不是要更多数据（Amber 复述："isn't about show more data, it's about helping you answer"，Marc 认同）。
- "Curveball"（受访者自称抛出的难题）：时间窗在周末和节假日不同。周末 super off-peak 是 12:00 a.m.–2:00 p.m.（很大的窗口，"that's where I'm going to do my laundry"）。建议图表可点击在 weekday / weekend 间切换。他在自家车库就手画了 weekday / weekend 两张时段表当提醒。

**Event 页 / 详情**
- "This is really nice." 认可它能"pick up triggers"（如下午 3 点充 EV = 不好）。
- 类比为 ledger event（账本事件），让人知道发生了什么、影响如何。
- 功能联想：详情是否链接到电力公司（停电通知等）？建议警示用的感叹号能出现在别处提示用户去看警告页。
- **太阳能设备掉线监测 = 强 aha 点**：讲了真实痛点——安装商本应监控他的太阳能系统，但出过问题；若系统故障而安装商没及时反馈，他可能整整一周不发电都不知道，且安装商表示"会来修，但不赔你损失的电费"。他说这个功能"would totally fix something like that"，会提前预警，"that's very cool"。
- 认可严重天气预警（storm 前提醒准备）。

**Saving / Bill 页（Amber 说改动最大、想重点听）**
- 顶部分两类：Saving（己方侧，从行为/时机检测出的成本风险）与 Bill（utility 侧实际账单）。$56 被解释为"actual cost exposure / risk cost"（当前账单周期检测到的风险成本）。
- 追问"是不是算法生成的"，以及具体"what triggered that?"。
- Risk ledger 按 EV / Solar / Power wall 分类，每行显示该周期发生次数与累计额外成本暴露；可点进详情。
- 对"被点名羞愧"式反馈表示喜欢："While electricity prices were high, that's the stuff I want to be shamed about, right?" 喜欢同一页既告诉做错了什么、又给 what-to-do-next 建议（如"charge during super off-peak"）。"I like that. That's really cool."
- Bill 页：确认是从 utility 实时取数。看到 basic service charge、delivery、税费等明细。Amber 类比为"checking receipt at the grocery store"，逐条核对账单项是否与检测到的 solar/EV/battery 行为吻合。
- **重要数据准确性提醒（受访者主动）**：当前预测从近几个月外推，但太阳能用户冬夏差异巨大（"a huge difference between winter and summer"）。只回看冬季的几个月会低估夏季更多日照——提醒计算方式要考虑季节性。
- Bill 页底部三大成本归因：最大问题是 peak 时段 EV 充电（首要解决项）、solar unavailable（可能阴天、不可控）、power wall。

**真实世界对比（受访者自己 app 演示）**
- 受访者展示了自己现用的太阳能监控 app（推断为太阳能系统自带监控 app）：可看三天的实时发电曲线（中午为峰值的抛物线）。
- 痛点：现在只能看发电，看不到与实际用量的同步对比（"see how that syncs with my actual usage"）。两天前 10:15 有一个大凹陷（云遮挡）。希望有 app 能让他不用跑出去看天，就知道"现在有云，等一小时再用电"。

### 首次理解 / 价值认知
- 整体一眼能看懂各功能用途，多处自己就能推断出设计意图（卡片三段结构、预算即目标账单等）。
- 最强价值认知是**实时感知（real-time awareness）**：多次表示实时数据"will save me some money / really save me money"，因为能据当下日照/云况调整用电时机。
- 第二个 aha 是**太阳能掉线预警**（避免一周不发电不自知）。

### 可用性问题 / 卡点
- Tesla/品牌 app 设置那一屏不知道要他做什么（最明显卡点）。
- Usage 图表无时段着色，柱子落在哪个费率窗口只能猜。
- （Amber 转述）部分用户看 usage 部分会困惑。

### 功能请求 / 改进建议（受访者主动提出）
1. 纳入并显示 EV 壁挂充电器（排程实际在该设备）；支持添加两辆 EV + 壁挂充电器。
2. Usage 图表加按时段着色的背景，并支持 weekday/weekend（及节假日）切换。
3. 实时条区分"送电回电网"的显示（绿/红），但承认非必需。
4. 让发电与实际用量在实时视图中同步对比（来自他对自己现有 app 的不满）。
5. 计算预测时纳入季节性（冬夏日照差异），避免只外推近几月。
6. 把（其他大功率）家电也纳入管理——Amber 表示以后可以。

### 与现状对比
- 现状：他脑子里记着费率时段、车库手画 weekday/weekend 时段表、用壁挂充电器排程、用太阳能自带 app 看发电曲线。他自评"已经知道怎么省钱、系统已搭好、整体很高效"。
- 本 app 的增量价值：更多数据、更易读的呈现、实时可见——尤其实时电表/发电，能帮他根据当下天气调整，省下他现在靠肉眼看天判断的部分。
- 对账单可读性的核心痛点：现状电费账单 12 页"impossible to read / completely impossible"，credits 如何抵扣"doesn't make sense to me"——正因看不懂，他无法判断是否值得加装更多面板。这是他寻求帮助的根本动机：不是要更省，而是要看懂系统的财务真相、并判断"加装面板是否划算"。

### 购买 / 付费意愿信号
- 主动问"how much you going to charge for it?"——价格敏感、关心定价。
- 明确价格锚点：$20/月"would scare me"，因为订阅太多（流媒体、音乐等）在累加；$5/月可接受。Amber 提 $5.99–$6.99，他表示这价位"I jump in and see"。
- 付费条件（行为/语气一致但有保留）：会先试，"if it's saving me over $6 a month then worth"——把付费与可见省钱挂钩。
- 不一致 / 犹豫信号：他反复强调"自己已经知道怎么省钱、系统已搭好"，本 app 对他更多是"added aspect / more readable / real-time"，省钱判断用了"I think will save me / which I think will save me some money"（推断式、留余地）。即口头积极、但价值定位偏"锦上添花"而非刚需，付费门槛压得很低（必须省过 $6 才值）。借特斯拉自动驾驶突然要收 $50/月的事表达对订阅疲劳的强烈反感（"I'm mad ... they gave me something and they just took it away"）。
- 强正向信号：主动自荐做 beta tester，愿用真实账单和充电习惯试用，并要求 ready 后通知下载。

## 关键金句
- "It's impossible to read. Completely impossible." —— Marc（指 12 页电费账单）
- "That's why I can't really make this determination about adding extra panels or not ... It's just so unclear about how credits are applied." —— Marc
- "If I'm looking at real time, I want to make sure it's coming off my meter." —— Marc
- "It's noon, I'm producing all this power. Now's a good time to run a washing machine." —— Marc
- "Super off peak on the weekends between midnight and 2 p.m. is a huge window. That's where I'm going to do my laundry." —— Marc
- "It'd just be easier to read at a glance." —— Marc（指 usage 图表加时段着色）
- "I could go for a week without generating power and I wouldn't even know ... This would totally fix something like that." —— Marc（太阳能掉线痛点）
- "While electricity prices were high, that's the stuff I want to be shamed about, right?" —— Marc
- "There's a huge difference between winter and summer ... just to keep that in mind in terms of how you calculate that." —— Marc
- "Something like $20 a month would scare me ... but like $5 a month, you know?" —— Marc
- "If it's saving me over $6 a month then [it's] worth [it]." —— Marc
- "Maybe I can be one of your beta testers or something." —— Marc
- "The real time aspect of it, I think, really save[s] me money." —— Marc

## 行动项 / 机会点
- Usage 图表加按费率时段着色的背景，并支持 weekday/weekend（含节假日）切换；Amber 已承诺会上传新版并回发链接请 Marc 评审格式。
- 支持纳入/显示 EV 壁挂充电器与多辆 EV，作为可排程设备。
- 实时视图把发电与实际用量并列对比（对标用户现用的太阳能监控 app 的缺口）。
- 实时条考虑区分"送电回电网"显示（非必需，可后置）。
- 预测/账单计算引入季节性（冬夏日照差异），勿仅外推近几月。
- 太阳能掉线/故障预警是高价值卖点，对依赖安装商监控的太阳能用户尤其打动人——值得作为差异化功能强化。
- 明确 Tesla/品牌 app 设置屏要用户做什么（当前文案让人不知所措）。
- 定价：对此类高阶、订阅疲劳用户，$5–$6.99/月是可接受区间，$20/月会吓退；价值主张需绑定"可见的、超过订阅费的省钱"。
- 转化机会：Marc 已自荐 beta tester，愿用真实账单试用——可纳入 beta 名单，ready 后通知。
- 注意：Marc 属"已做对一切"的用户，本 app 对他是锦上添花而非刚需；其付费意愿绑定在实时可视化与账单可读性上，而非省钱本身。
