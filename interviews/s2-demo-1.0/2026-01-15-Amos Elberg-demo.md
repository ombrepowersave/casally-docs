# Amos Elberg · Demo 反馈 · 2026-01-15

## 受访者画像
- 重度家庭能源/EV 用户，近期搬入新居，太阳能系统已运行满一个月。
- 设备：太阳能（屋顶阵列）、Tesla Powerwall（"power wall"）、EV（提到 Volvo 车与 Tesla 车，二者均出现，见下方纠错说明）、Wallbox 充电桩。
- 已在用的能源 App 多个：NetZero（"net zero" / "net0ero"，太阳能/EV 优化 App）、Wallbox App、ChargeHQ（"charge HQ"），以及车厂自带的 Volvo App、Tesla App。
- 现状痛点：太阳能实际发电量比安装商承诺的少约 20%，正准备发邮件质问安装商。EV 充电占其月度用电一半以上，是其最关心的优化点。
- 技术背景较强：熟悉 PVWatts、按小时发电预测；主动提到并使用过 Anthropic 的 Claude Code（"claw code" / "cloud code"，AI 编码代理），并用其交互模式类比理想产品体验。

## 主题判定
判定为 Demo 反馈。依据：访谈者发来 Figma 原型链接，请受访者边点边给"像平时一样"的真实反应（"What feel useful and feels wrong"），全程围绕原型各界面/功能的喜欢、困惑、缺失与付费意愿展开。

## 转录纠错说明
逐字稿为语音转录，以下为在 .md 中按本意还原的关键术语（**未改动原始 .txt**）：
- "net zero" / "net0ero" / "NetZero" → **NetZero**（一款太阳能/EV 优化 App）。
- "charge HQ" → **ChargeHQ**。
- "power wall" → **Powerwall**（Tesla 家用电池）。
- "claw code" / "cloud code" → **Claude Code**（受访者自己说明是 Anthropic 的 AI 编码代理，原文上下文已明确）。
- "PB W" / "PB wallet" / "PV watts" → **PVWatts**（NREL 太阳能发电估算工具；访谈者口误的 "PB wallet" 同指此物）。
- "Luna" / "luma" / "loop" → 受访者倾向认为是 **Luna**（一家电池厂商兼 App，原文称名字不确定，标"未确定"）。
- "Volvo app" 多次出现，但受访者也多次提到 Tesla 车/Tesla App，车型归属逐字稿未完全一致，**未做合并**，保留原文两种车厂表述。

## 核心提炼

### 逐功能反应
**首页"可能需要你关注"视图 / Estimated cost impact（成本影响条）**
- 困惑：进入时无上下文，不知自己在 App 中的位置、不知 App 还能做什么。
- 对 "estimated cost impact positive to negative" 不理解含义——分不清这是"太阳能带来的收益"还是"这个 App 带来的收益"，"I'm not sure what cost impact means"。

**Savings（储蓄）页 + Events（事件）页**
- 界面困惑：顶部叫 savings、是预期节省的条形图，底部却是 detected events；而单独的 Events 页里事件却不显示，反倒在 savings 页里有事件——位置错乱。
- 顶部提示 "Monthly aggregation detected of events, not a prediction of final bill" 被他读出，界面整体"a bit confusing"。
- 对事件内容本身评价正面：某条事件给出如何优化太阳能使用与充电的建议——"I like this event because this is giving me advice about how to optimize my use of solar and how to optimize my charging"，但觉得放错了地方（interface-wise in the wrong place）。

**通知 / Suggestions（黄色建议卡）**
- 喜欢：看到黄色建议卡说"That's a good I like that"。
- 喜欢事件卡的操作设计：有 mute、remove、remind me later。
- 关键缺失：卡片只讲了"发生了什么、为什么重要、影响是什么"，却没告诉他"我能做什么"——"it's bringing me a problem. It's not bringing me a solution"。主动提出应加第四项：我能调整什么设置（如为停电做准备 "what setting can I adjust that helps me prepare for power outages"）。

**EV 充电建议 + "Apply now"**
- 一开始没注意到 "apply now" 按钮（"I didn't see that before… I don't know how I missed that"）——可用性卡点：该操作入口不够显眼。
- 发现后评价 "That's useful… I like that"。
- 这是他认可的核心交互：App 给建议 + 一键 apply now 让系统替他执行，他明确说"that would be useful to me / something that I would want"。

**Profile / 设置 / Connect device（数据连接）**
- 对连接太阳能、Powerwall、EV、充电桩等设备完全没有隐私顾虑："I'm very comfortable… readon or it doesn't even have to be readon"（即接受只读，甚至接受写/控制权限）。理由：他现在已经在让 NetZero 连这些设备做控制了。

**Add family member（添加家庭成员）**
- "yes and no"：理论上有用，但实际在他家行不通——他试过邀请妻子用各类 App，妻子全部无视邀请，宁可打电话让他代操作（如开扫地机器人）。属于"对他个人价值有限"的诚实反馈。

**Automations（自动化）页（注：此为他展示的现有 NetZero 界面，非本 Demo）**
- "extremely confusing"，他自己从没用过任何自动化。
- 可设 backup reserve、time-based control、energy exports、按时间/充电量/EV 起停等触发条件，但"功能很多却不知道自己到底要哪个自动化"——"what automation do I want?"，要弄懂得"sit down for like an afternoon or a day"。
- 举例自己设的 "grid rises above 3 kW start charging"，但担心没有清晰的停止条件（太阳能停产后充电会不会继续）——规则配置难以覆盖动态情况，"it would probably be really complicated"。

### 首次理解 / 价值认知
- 逐步 get 到核心功能："the app is giving me advice. It's monitoring my usage and it's telling me ways that I could be using electricity more efficiently."
- aha 点出现在理解"建议 + apply now 执行"这一组合，以及访谈者点明"我们不是再做一个看数据的地方，而是直接给你推荐/替你判断"之后，他认同 Claude Code 式"给计划→可编辑→执行"的交互"that's the interaction that works"。

### 可用性问题 / 卡点
- 进入即缺上下文、不知所处位置。
- "cost impact" 术语不可解。
- savings/events 信息架构错位（事件分散在两处、events 页空）。
- "apply now" 按钮第一次没被注意到。

### 功能请求 / 改进建议（受访者主动）
- 每条问题卡补"我能做什么/该调哪个设置"的解决方案项。
- 真正接管控制：自动控制充电、控制 Powerwall 充放与预留电量、控制 EV 何时充电（这是他认为值得付费的门槛）。
- 提供可媲美 NetZero 的统计图表（display statistics, charts and graphs）。
- 接入智能恒温器（Nest），帮恒温器"更聪明"——但他不确定那些恒温器 API 是否支持（推断为他对技术可行性的保留意见）。
- 提供类似 NetGero 的 PVWatts 按小时发电预测曲线（预期 vs 实际，黄色面积图 + 红点），并认为本 Demo "could do better than this"。
- 交互模式：希望 App 说"明天我们打算这么做"，并允许他 override 计划（"I want to be able to override the plan"）——非无条件全自动。

### 与现状对比
- 当前同时装着 NetZero、Wallbox、ChargeHQ 三个充电优化 App，"None of them solve the problem"——彼此设置不一致、在不同时间各自启停、互不协作。
- 现实做法：已关闭 charge-on-solar（冬季发电不足），改用 Volvo App 只在便宜时段充电；坦言"冬天可行，夏天不行"，夏天再研究 charge-on-solar。
- 提及竞品 Luna（电池厂商+App，用机器学习看天气/纬度/阵列预测发电、决定电池预留与并网时机，"does a better job than the Tesla app"），但因 Luna 只配自家昂贵电池、他没买，故未实际用过其 App。
- 还提到 Tesla Reddit 频道上有人新推一款对标 NetZero、同样做机器学习的 App（名字记不清）。

### 购买 / 付费意愿信号（重点，存在明显不一致）
- 安装意愿明确：只要给出好建议 + 可 apply now，"I would install the app and I would set it up"、"I would use the app"。
- **付费意愿犹豫**：反复说"but I wouldn't pay for it" / "the question is would I pay a subscription fee… that's where I'm not so sure"。
- 不愿付费的核心逻辑：若 App 只是给建议，"after a few weeks I'm going to remember the advice and I'm not going to need the app anymore"——学会就退订。
- 付费门槛：必须真正接管系统控制（充电、Powerwall、EV 充电时机），并提供 NetGero 级图表。
- **不一致信号**：当访谈者强力引导"建议其实每天/每分钟随天气、发电、电池、昨日用车等变化而变，你付费买的是'不必自己时刻判断建议是否仍适用'"，他被说服后态度从"not so sure"软化为"Maybe"、"I might be willing to pay a subscription fee for it"。但紧接着对访谈者的 Claude Code 类比表达保留——"I don't know if the claw code analogy stretches that far"，随后又含糊地"yeah… I might be willing to pay"。整体属"被引导后口头松动、但本心仍存疑"的弱信号，付费意愿不应被记为肯定。
- 试用承诺明确：愿意在产品就绪后于真实生活中试用——"absolutely, I'll give it a try"。

## 关键金句
- "If it's going to give me advice, I would install the app, but I wouldn't pay for it. If I'm going to pay for it, it needs to do more than give me advice." —— Amos Elberg
- "Right now, I have three apps. None of them solve the problem." —— Amos Elberg
- "It's bringing me a problem. It's not bringing me a solution." —— Amos Elberg（评事件卡缺"我能做什么"）
- "I think for me to pay the subscription fee… it would have to actually take control of the system, take control of the charging, take control of the power wall… take control of when to charge the EV." —— Amos Elberg
- "After a few weeks, I'm going to remember the advice and I'm not going to need the app anymore." —— Amos Elberg
- "I would rather the system figure that out for me." —— Amos Elberg（相对自己看曲线决策）
- "I want to be able to override the plan… I would like it to say 'Here's what we're going to do tomorrow' and then I'd like to be able to make changes to that." —— Amos Elberg
- "I'm very comfortable letting an app control the power wall and the solar and the charging and all of that. I'm already doing that. It's just that the app isn't very good." —— Amos Elberg
- "That's great, but what automation do I want?" —— Amos Elberg（评 NetGero 自动化过于复杂）
- "I don't know if the claw code analogy stretches that far." —— Amos Elberg（对付费类比的保留）

## 行动项 / 机会点
- 首页/事件卡补"下一步行动/可调设置"——把"problem"变"solution"，是其最强烈、最具体的诉求。
- 提升 "apply now" 入口可发现性（首次被漏看）。
- 重做 savings 与 events 的信息架构，消除事件分散两处、events 页为空的错位。
- 明确并解释 "estimated cost impact" 的含义与来源。
- 核心定价策略验证点：纯建议型产品付费意愿弱（"学会即退订"），需向"代为接管控制 + 持续随条件变化重规划"演进，才可能支撑订阅——"付费买的是不必自己时刻判断建议是否仍适用"这一价值主张值得继续验证（目前仅获其弱认同）。
- 控制权设计需保留用户 override（"明天的计划"可见可改），契合其 Claude Code 式"提案→编辑→执行"心智。
- 补齐 NetGero 级数据可视化（含 PVWatts 按小时预期 vs 实际发电曲线）作为留存/竞争要素。
- 探索智能恒温器（Nest）接入（需先评估 API 可行性）。
- 已确认愿意在产品就绪后参与真实环境试用，可纳入 beta 名单。
