# Byron Dare · Demo 反馈 · 2026-01-21

## 受访者画像
- 居住在北加州（住宅区，PG&E 服务区）。提到自己另有一处"北边的房子"，并非全职居住——常会离开一周、两周，尤其圣诞节期间会连续数周不在家（亲戚不在旧金山）。
- 设备：装有太阳能板 + Tesla Powerwall 电池。当前为 17 块面板 + 2 块电池；早先曾是 8 块面板、无电池。也有 EV（访谈中提到 EV 充电）。
- 用 Tesla App 查看能源数据；自述用电账单走 PG&E，可能涉及 NEM、CCA（Peninsula Clean Energy）等多种费率。
- 核心痛点（沿用上次访谈）：他不是想优化用电、省几美元，而是怀疑 **PG&E 计费/太阳能出口抵扣有问题**——装了更多面板和电池后账单反而比早年（8 块面板、无电池）更高，PG&E 无法解释，他想要证据去challenge。

## 主题判定
判定为 **Demo 反馈**。依据：Amber Fu 发送 Figma 早期 demo 链接（"our early demo version app"），引导 Byron 共享屏幕、自由探索并逐屏（首页 / 用量 / 节省 / 事件 / 数据来源）给出反应，全程围绕产品功能的理解、价值与改进展开。

## 核心提炼

### 首次理解 / 价值认知
- 整体第一印象正面："it looks pretty good and the color codes look good"，并能自行推断颜色编码是用来提示"是否该做点什么"（红色=Something may require your attention）。
- 对"用量(usage)"屏：理解它能告诉他用得比平时多/少，但**不知道原因**。"It says I'm using less, but I wouldn't know why." 他自己举例推断：开烘干机时用电多、没开时少（推断，属他自己的解读）。
- 对"节省(saving)"金额：觉得"that would be good"，但**立刻质疑这个数字是否会反映到 PG&E 账单上**——因为 Tesla App 也显示他在向电网回送电量，"but apparently PGE doesn't agree with me"。即看到节省数字时，信任与价值认知被他的核心痛点（PG&E 不认账）直接打断。

### 逐功能反应
- **首页"建议(suggestion)"卡（黄色，中间）**："that's good"，能理解是好建议。
- **首页"停电警告 / 给 Powerwall 和 EV 充电(charge your power wall and EV)"卡**：明显困惑。
  - 第一处困惑：以为是让他当场操作，"if you have a power outage... I'm not sure how you could do that"——Amber 解释是停电前 24–48h 预警提醒提前充电后他才理解。
  - 第二处（更关键）困惑：这个"power outage warning"措辞让他联想到**计划性滚动停电(planned rolling blackout)**，而他强调北加州**他从没见过计划停电**，遇到的都是大风/大雨/事故导致的**突发停电(sudden/unplanned blackout)，没有预警**。"this is a little confusing cuz this sounds like a plan rolling blackout when you say power outage warning." → 该功能的前提假设（提前预警）与他的真实场景不符。
- **"节省"明细页 / EV 高价时段充电 / 数据来源(data & source)**：反应平淡正向（"that's good"）。对 EV 高峰时段他自评"people sort of know that... between 4pm and 9pm"（注：原文 "400 p.m." 应为 4 p.m./下午4点，转录数字误写），认为对不知道的人有用。但他反复把话题拉回到"需要可打印的日志/明细"。
- **"事件(event)"页（底部 tab，靠近 home）**：他立刻问"this one what happened? You could access my data and tell me?"——把事件理解为可回溯解释发生了什么的记录，很感兴趣。最关心的事件：**停电时 Powerwall 是否真的接管供电**（见下）。

### 可用性问题 / 卡点
- 屏幕共享环节卡了很久（约 5:34–13:13），Byron 不熟悉如何共享屏幕、误把 Figma 里的 iPhone mockup 当成要操作的对象。属会议工具/被试操作熟练度问题，但也反映**他对"这是个原型"不够清楚**。
- 多次 Amber 指引"左侧 flows / 某个 tab"时 Byron 找不到对应位置（"Did you see it?" → "No"）。
- 核心认知卡点："power outage warning"措辞触发对计划停电的误解（见上）。

### 功能请求 / 改进建议（受访者主动提出）
1. **可打印的明细/日志（PDF）**——反复强调（多次）。希望有 daily/monthly 的 printout/log，能拿去给 PG&E、PUC 或第三方顾问看。理由：PG&E 账单"12 pages long"且满是术语，"you really have to be an electrician to understand it"。明确偏好"带数字和数据的可打印 PDF"，因为 PG&E/Tesla 沟通多靠 email。
2. **并排对比 + 高亮不匹配**——对 Amber 提出的"应付金额(基于 Tesla 出口) vs 实付金额(PG&E 账单) + 差额高亮"明确认可（"Yeah... Right"）。希望像"detail receipt"，精确到日期区间（如 6/1–6/5 的 Tesla 出口数 vs PG&E 抵扣行项）。
3. **接入 Tesla 数据**——主动问"if you tie your app into Tesla, is there some way you could do that?" Tesla 说有记录但他不知如何访问、客服差。
4. **第三方顾问/专家资源**——希望 App 内提供能解读数据的协会/个人联系方式，"even if it cost me a couple hundred... I would be willing to pay that"。
5. **Powerwall 接管状态追踪**——希望 App 记录停电时 Powerwall 是否在充电/是否接管供电。"if your app could tell me if the power wall is being charged or not"，这样可拿去找 Tesla 修。他不确定自己的 Powerwall 在停电时是否正常工作（他不在家，无从得知）。
6. **突发停电通知 + 应急联系人**——希望 App 能监听 PG&E 的停电推送（如风灾断电、预计X小时恢复），尤其他不在家时能收到，进而联系有钥匙的邻居/家人去处理冰箱食物、医疗设备等需持续供电的东西。Amber 称这是"really good question"。

### 与现状对比
- **Tesla App**：能看到发电/向电网送电，但与 PG&E 口径冲突；无法导出打印件（"I don't think Tesla offers that, at least as far as I know"，他不确定）；客服差、人在 Arizona/Nevada、只能 email 沟通。
- **PG&E**：提供月度 PDF 账单（网站可下），也提供用量图表，但解释不了他的疑问；无线下办公室、两个客服直线电话+email 都不回；他认为本产品对日常监控有用（"the website's good for everyday monitoring"），但**出问题时需要更多数据/生成的证据**。
- **PUC（公共事业委员会）**：他投诉过，PUC 联系 PG&E、PG&E 说"normal"后就结案。他相信**有了数据/证据后，PG&E 和 PUC 更难再敷衍**。

### 购买 / 付费意愿信号
- 明确愿意为"能解读数据、指出问题的第三方顾问"付费："even if it cost me you know couple hundred or whatever. Uh I would be willing to pay that"。
- 愿意完成 onboarding 四步（连接 Tesla 数据、上传 PG&E 账单 PDF、确认 PTO 日期、确认是否在 CCA/清洁能源项目）："sure. I could do that... you just tell me what I need to do"。也愿意提供电表号/PG&E 账户号、授权访问数据。
- **不一致/犹豫信号**：他对产品本身的"喜欢"始终是**有条件的**——几乎每次正向评价后都立刻补一句"but I'm not sure if that shows up on my utility bill"之类的疑虑。其付费意愿主要指向"顾问/解读服务"而非产品订阅本身；对 App 当前展示的节省/用量数字，他的价值认同较弱（因为不解决他的"PG&E 不认账"核心问题）。需注意：他的强需求高度个人化（怀疑被错误计费），不一定代表普通用户。

## 关键金句
- "my bill is higher than it was like five years ago... Now my bills higher than when I just had eight panels and no batteries. And PG&E can't explain it to me." —— Byron Dare
- "I get the same thing from the Tesla app... I'm sending all this energy back to the grid. But apparently PGE doesn't agree with me." —— Byron Dare
- "if there was some sort of consultant... outside [PG&E] who could tell me what's happening... I would be willing to pay that." —— Byron Dare
- "my bill is like 12 pages long every month and it has all these technical terms in it and I think you really have to be an electrician to understand it." —— Byron Dare
- "this is a little confusing cuz this sounds like a plan rolling blackout when you say power outage warning." —— Byron Dare
- "if your app could tell me if the power wall is being charged or not... then I could probably go to Tesla and say... can you fix it?" —— Byron Dare
- "if I have the data then it's harder for PG&E to just say everything's okay." —— Byron Dare
- "the website's good for everyday monitoring but when there's a problem like I have there's more data... it needs to be generated." —— Byron Dare

## 行动项 / 机会点
- **核心价值主张应从"省钱/监控"转向"计费证据"**：Byron 的强需求是可信、可打印、可对峙 PG&E/PUC 的证据，而非节省数字。考虑把节省页的主数字/叙事可选切换为"本月疑似缺失的出口抵扣(estimate missing export credit)"。
- **构建"案卷(case file)"流程**：导入 PG&E 账单 + 拉取 Tesla 出口数据 → 高亮 mismatch → 生成可打印 PDF 套件 + 配套通话脚本（call scripts）。Amber 已将此定为下一步。
- **修正"power outage warning"措辞**：区分"计划停电(planned/有预警，可提前充电)"与"突发停电(unplanned/无预警)"两类场景，避免误导北加州这类几乎只遇突发停电的用户。
- **Powerwall 接管状态可视化**：记录并展示停电时电池是否应接管、是否实际接管，作为高价值"事件"。
- **突发停电通知 + 应急联系人**：监听 PG&E 停电 feed，在用户外出时推送，并提供联系邻居/家人（有钥匙者）处理冰箱/医疗设备的路径。
- **数据来源信任**：他最信任电表数据（meter），但又被告知电表数据流向 Tesla、自己不知如何导出 → onboarding 中明确"接电表/utility 账户"路径，降低他对 Tesla 单一来源的不信任。
- **第三方顾问对接**：探索在 App 内提供付费专家/协会资源，存在明确付费意愿。

## 转录纠错说明（不改原始 .txt）
- "P Gen / P Genie / Peny / Pen / PG" 多处指 **PG&E**（Pacific Gas & Electric），语音转录变体。
- "PC / PUC" 指 **CPUC / 公共事业委员会**（California Public Utilities Commission）。
- "NEMS rate" 应为 **NEM**（Net Energy Metering，净计量）相关费率。
- "peninsula clean energy" = **Peninsula Clean Energy**（CCA，社区选择聚合商）。
- "PTO" = **Permission To Operate**（并网运行许可）。
- "XPro detected" / "PJ credit"（Amber 话术）疑为 **export detected / PG&E credit** 的转录误写。
- "400 p.m." 应为 **4 p.m.（下午4点）**；高价时段 Byron 自述为下午 4–9 点。
- "corn check" 应为 **core check**（核心检查，Amber 话术）。
- 注：Byron 关于"账单变高""8 块面板→17 块面板+2 电池""停电时长 48 小时""无人时账单超 $200"等数字与事实均为其本人陈述，未经独立核实，按原文记录。
