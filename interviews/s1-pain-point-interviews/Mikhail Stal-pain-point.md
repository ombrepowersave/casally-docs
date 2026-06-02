# Mikhail Stal · 用户痛点 · 日期未知

## 受访者画像
- 与妻子两人住，房屋约 1,200 平方英尺，位于加州圣地亚哥地区（电力公司 San Diego Gas & Electric，电价计划 TOU5）。
- 设备齐全（"full setup"）：太阳能 + Tesla Powerwall 家用电池 + 一辆电动车。访谈者指出这种"太阳能 + 电池 + EV"全套配置在受访人群中很少见。
- 电动车是现代（Hyundai）小型 SUV，电池约 77 kWh；另有一辆汽油车，开得不多。
- 充电桩是 Emporia 品牌（美国品牌），与车、电池都不同品牌；已用约 3 年。
- 太阳能通过 Tesla 电池的逆变器接入，太阳能 + 电池在同一个 App（Tesla App）里；EV 与充电桩各自独立。
- 还有：电热烘干机、热泵（供暖/制冷）、洗碗机、AC、Ecobee 智能温控器、智能冰箱等多种联网家电（无泳池）。
- 现处于 NEM3 电价政策下；之前住所是 NEM2、无电池，太阳能持续超额发电（"overproduced constantly"），几乎没有电费、还能拿退费（rebate）。
- 太阳能历史：2019 年在前一住所首次装太阳能（当时无电池），几年后加 EV；搬家后重新装太阳能并加电池（因为加州现在"基本必须有电池，否则回本不划算"）。
- 本人职业是用户体验（UX）相关，自述熟悉 App 开发；主动表示愿意做 beta 测试。
- 装太阳能/EV 的主要动机是省钱回本（打算住 5-7 年能回本），其次是 EV 便利（不用每周/两周加油），环保是加分项但财务考量"honestly 是最大的事"。

## 主题判定
判定为**用户痛点**访谈。访谈由 Casally 团队（Amber Fu 主问、技术负责人 Yongli Chen 在场）进行，围绕受访者家庭用电、太阳能/电池/EV 系统的实际使用体验、不便之处与期望展开。受访者就"系统不够智能/不互通""手动操作负担""订阅付费决策"等给出了多处具体、反复强调的痛点表达。

## 核心提炼

### 具体痛点清单

**痛点 1：Tesla Powerwall 无法自动调度备用电量（reserve），导致夜间充车后电池耗尽、白天高价时段无电可用**
- 现象/场景：夜间给 EV 充电会把 Powerwall 几乎抽干。受访者将 backup reserve 设为 10%，所以充电会用掉 90% 容量；Powerwall 只有 10–11 kW（受访者原话表述为 kilowatts，按上下文应指容量），而车是 77（kWh），"anytime I'm charging overnight ... it'll just draw the whole thing"。
- 后果：早上 6 点后电价变贵，但 Powerwall 已空。
- 他想要的自动化：午夜把备用容量调到一个较高值（举例 40% 或 50%）以保留电量，6 点后电价变贵时再调回 10%，从而在高价时段用电池剩余电量。NetZero App 能设这类"午夜 + 早 6 点"两段自动化，但 Tesla 自带 App "control is very limited"，做不到。
- 程度：明确称为 pain point（见金句）；"these systems are very very smart ... why doesn't it allow for that? Why doesn't it do it?"
- 注：他提到 Tesla Powerwall 有两种模式，其一是 time-based control，会基于用量在后台做预测，"something like that already exists there"。

**痛点 2：Emporia 充电桩与太阳能/Powerwall 不互通，无法用多余太阳能充车（excess solar charging）**
- 现象：Emporia 不支持 OCPP 协议（Open Charge Point Protocol，受访者口语先说 "O CC something"、后说 "OCP"，应为 OCPP / Open Charge Point Protocol），所以不像 Tesla 充电桩那样能识别并跟随多余太阳能充电。
- 受访者明确："I cannot do excess solar charging."
- 卡点：Emporia 提供一个装进电箱的配件（夹钳 clamp）来实现该功能，但他电箱里的标准夹钳太大装不下，需要另买更小的橡胶柔性夹钳，约 $100，他至今没买（"I just haven't really haven't bought it yet"）。
- 背景原因：充电桩是 3 年前买的，当时还没有 Tesla 系统，"didn't really think about it at the time"。他强调 Emporia 充电桩本身"is great"，只是不与其他设备通信。

**痛点 3：靠太阳能充电需手动记得插车、手动调整，没法自动跟随太阳能**
- 现象：因没有那个配件，充电桩"不会在有多余太阳能时自动开始充电"。
- 手动负担："I just have to remember to plug in the car in the morning"；可以手动改，但"I wish ... if it was automatic that would be much better"。
- 也提到天气因素：他所在地天气一般不错，但偶尔会变阴/下雨导致太阳能减少；希望充电桩能据此自动调整（理想是充电功率能随实时太阳能在如 6kW 到 2kW 间自动升降，他对此明确说 "Yes. Yes ... that's what I would expected to do"）。

**痛点 4：早上看到电池被抽干，感到没达到应有的效率**
- 情绪："I know that it's not being as efficient as it could be ... I wish I could automate it"；明确称"it's definitely like a pain point ... when it's totally drawn"。

**痛点 5：NEM3 下管理 EV 充电时机的心智负担（相比 NEM2 时期）**
- 现象：现在 NEM3 政策下"白天用多余太阳能充车最划算"，所以需要记得白天太阳出来时去插车；而以前在 NEM2 的旧房，可以"always plug it in at night and not worry about it"。
- 受访者答"哪部分最费心"时即指此：在 NEM3 下"知道我得在白天充车"是最需要操心的事。

**痛点 6：夜间的"决策/规划"负担**
- 场景：晚上需要判断当前车的电量、明天的安排（车是否在家、妻子是否开去上班、周末是否外出），从而决定是否过夜充电。"I have to know what the current state of the car is, but then I also have to like project into the future."
- 白天还要记得"下午太阳出来时去插车"。

**痛点 7：非智能家电无法自动调度**
- 现象：洗碗机等家电没接智能开关（smart switch），系统无从让它延后启动，只能手动设置（如把洗碗机设为午夜后启动）。"how does it know to start late? It really doesn't."

**痛点 8：多 App 分散，略显烦人**
- 现状：充电桩 Emporia 有 App、Tesla 有 App、车（Hyundai）有 App（订阅没续）、洗碗机、冰箱等也有 App；之前用 Enphase（原文转录为 "Nphase"，应为 Enphase）时也是独立 App。实际常用大约 3 个 App。
- 评价："it's definitely a little bit annoying ... but just kind of learn and deal with it."

**痛点 9：账单难读**
- 表达：账单行项多（不同时段用电、transmission charge、use charge 等），"not very easy to read / understand"；并提到 Reddit 上有人 $600 电费不知为何。注意：他本人对此"haven't been like unexpected"，更多是替"不太懂的人"指出。

### 痛的程度 / 紧迫性
- Powerwall 无法自动调 reserve：明确称 pain point，并多次反问"为什么不能/不做"。
- excess solar 不能用：被问"如果不用额外硬件就能做到会多大影响"时答 "That would be huge."
- 整体定性："it's some manual work ... it's not terrible ... it's inconvenient and it seems like it could be more efficient"——是不便、低效，但不至于让他不装太阳能/电池。属于"中等程度、持续存在的麻烦"，而非剧烈痛苦。
- 量化线索：Emporia 配件 $100；NetZero 订阅 $7/月（他做了试用但没订阅）；加州电费"可达数百美元"；San Diego TOU5 夏季 4–9pm 约 70 美分/kWh；"reduce your use" 日峰价约 $1/kWh（约为平时两倍）；Emporia App 每月通知曾显示"省了 $23"。

### 触发情境 / 规律
- 作息很规律：本人在家办公（约 8–4 或 9–5），妻子每周约 3 天开车去办公室（约 8 点走、4 点回，有时中午回）；家里大部分时间安静。
- 用电高峰：充车时一定最高；其次是热泵供暖/制冷、电热烘干机、洗碗机（按"花钱多少"排序：1 EV 充电、2 热泵、3 电烘干机、4 洗碗机）。
- 电价时段（SDG&E TOU5）：夏季 on-peak 4–9pm（约 70 美分/kWh）；冬季（约 11 月–3 月）低很多。受访者强调"4 to 9pm 是公认最糟时段，everyone knows"。
- 充电习惯：装电池前会用延时（dishwasher delay 到午夜后）、并固定在便宜时段充车——工作日午夜到早 6 点、周末午夜到下午 2 点。
- "Reduce your use day"（加州版需求侧响应，受访者据此回应访谈者问的 "demand charge"；他指出加州叫法不同）：通常夏季下午 2–6pm、约 $1/kWh，"只在有停电风险时才有，挺少见"。

### 当前应对 / 替代方案
- 装电池后大部分负载调度问题被电池"吸收"：现在不太需要刻意错峰跑烘干机/洗碗机，因为电池容量够（除非当晚要充车）。
- EV 充电桩固定设在 24 安培（"中间值，不多不少"），属于"有点 babysitting"。
- reserve 调度只能手动，但"太麻烦，就一直让它自己跑"（"too much work ... I've just been letting it run"）。
- 试用过 NetZero（$7/月）：能设他想要的自动化，但因看不到明确的省钱证据/图表，没订阅（"I need some evidence before I blindly commit"）。
- 旧房用 Ecobee 做预冷（pre-cool）：在 1–4pm 较便宜时段提前制冷，以应对 4–9pm。

### 未被满足的需求 / 期望
- **跨品牌打通**：让充电桩、Powerwall、太阳能、温控器互通；只要"integrations 能用、能登录链接凭证"，这样的系统会很有用——他说现在没见到真正做到这点的产品。
- **Powerwall reserve 自动调度**：被问"若只能自动化一件事"时，首选 reserve shifting；若能用多余太阳能充车，则首选 excess solar 充电。被问"最想从大脑里移除、再也不想管的一件事"时答：backup reserve 设置。
- **无需额外硬件即可做太阳能跟随充电**：若 App 能在不加硬件下实现，"would be huge"（但会算 $100 配件 vs. 订阅费的回本）。
- **充电优先级（理想行为）**：1）优先用多余太阳能充；2）其次夜间充；3）再次是他说的电池负载调度（battery load shifting）。
- **预测 + 提前规划/提醒**：希望系统能前瞻——如"明天阴天，充不了太阳能，建议过夜充够通勤里程"；"这周后面要下雨，过夜充车"；夏季下午会热则提前预冷。
- **学习用量做决策**：举例"知道你早上用 3kW 取暖，所以今晚让电池放电 80%；夏天早上不开空调就放到底"。
- **推荐 + 审批模式**：偏好系统给建议、由他批准（"make recommendations and let me approve"）；但同时强调易于手动调整也很重要，因为"AI 不总是完美"。
- **透明、可审计、可量化的省钱报告**：要能看到"本周/本月做了什么、省了 $X"这类与自身用量挂钩的指标，才会信任并放心交给自动化（"gives the end user confidence ... I trust this, it's looking out for me"）。Emporia 式月度"省了 $23"通知是他认可的范本。
- **理想完美的一天**：早 6:30–7 起床想要屋里暖和→此时无阳光，用电池供暖；车若插着就到合适时间自动开始充、自动调充电速率；预测午后热则夏天提前制冷；并给天气/规划提醒。核心是"把心智负担拿走"。

### 自动化的顾虑 / 信任条件
- **不能犯的致命错误**：在 on-peak（最贵）时段用电——"I don't see a reason for it to use on peak energy"，若发生会让他质疑。
- 担心自动化做错决定："In theory, it's possible"，但只要透明、可理解其行为，就更信任。
- 价值定性：自动化主要价值是省钱，但"省钱本身要花心智，解决一个就同时解决两个"——自动化本质是"把心智负担拿走"。

### 付费意愿（明确且反复）
- 倾向避免订阅；偏好一次性付费的硬件（如 breaker monitor 一次性买断）胜过多年订阅。对装 breaker monitor 没意见，唯一负面是可能需请电工安装（而 NetZero 不需上门）。
- 订阅的前提：要有试用（理想 30 天），并能持续证明每月省的钱高于订阅费。"If the app costs $5 and I'm saving $5 ... I think I need a little bit more help there."
- 对 NetZero $7/月："I'm not sure if I'm going to save more than $7 on it"，没看到针对"按你的用法能省 $9/$10"的具体指标/图表前不会盲订。

## 关键金句
- "the Tesla app is very limited in the control that you can have with it." —— Mikhail Stal
- "if I charge my car overnight, it's going to drain my Tesla power wall completely ... after 6 a.m. the electricity is expensive, but my power wall is empty" —— Mikhail Stal
- "the power wall is only 10 or 11 kilowatts and my car is 77. So ... I've just been letting it run because it's too much work." —— Mikhail Stal
- "it's definitely like a a pain point. I would say that when it's totally drawn." —— Mikhail Stal
- "these systems are very very smart, you know. So, it's just like why why doesn't it allow for that? Why doesn't it do it?" —— Mikhail Stal
- "I cannot do excess solar charging." —— Mikhail Stal
- "That would be hu that would be huge. If I didn't need extra hardware, then I wouldn't need to buy a $100 item" —— Mikhail Stal
- "I just have to remember to plug in the car in the morning ... if it was automatic that would be much better." —— Mikhail Stal
- "I need some evidence before I blindly commit." —— Mikhail Stal
- "the reserve shifting it that should be very easy for Tesla to set up on their app, but they just don't have it." —— Mikhail Stal
- "if it's using uh on peak energy which is the most expensive ... I don't see a reason for it to use on peak energy so that would make me raise some questions" —— Mikhail Stal
- "as long as there's like a ... you're able to audit it or just understand and look deeper to see what it's doing, I think that is important for building trust" —— Mikhail Stal
- "I think it takes mental energy to save the money. So, by solving one problem, you kind of solve both problems. The automation is basically taking the mental workload away from you." —— Mikhail Stal
- "I try to avoid subscriptions if I can ... I would want a trial maybe 30 days ... It has to give me more value than the app costs." —— Mikhail Stal
- "if I could just buy the breaker monitor and there's like a onetime fee, I would probably prefer that more than subscription for however many years." —— Mikhail Stal
- "this is very insightful. Thank you." —— Yongli Chen（技术负责人）
- "I do user experience as my job, so I'm like pretty familiar with like that app development." —— Mikhail Stal
- "I wish I could just uh hit a big button, charge car, but I have to go through multiple menus now. So, it's not as good as it used to be." —— Mikhail Stal（评 Emporia App 变难用）

## 行动项 / 机会点
- **跨品牌整合是核心机会**：受访者有 Tesla（太阳能+电池）+ Hyundai EV + Emporia 充电桩 + Ecobee + 多家电，各自为政；他明确说没见过真正打通这些的产品，且只要"能登录链接凭证、集成可用"就愿意用。这是 Casally 的高价值切入点。
- **Powerwall reserve 自动调度（午夜抬高 / 早 6 点回落）**：他最想自动化的功能之一，且认为 Tesla 本可轻松做但没做——可作为软件层补足点（NetZero 已证明此自动化通过 Tesla cloud API 可行）。
- **无需额外硬件的太阳能跟随充电**：若能在不让用户买 $100 配件、不依赖 OCPP 的前提下实现 excess-solar 充电（或动态调充电功率随实时太阳能升降），价值 "huge"。需注意 Emporia 不支持 OCPP，技术可行性待评估。
- **前瞻式规划与提醒**：基于天气/电价/用量的预测建议（如"明天阴天→过夜充够通勤""午后会热→提前预冷"），并支持"建议+用户审批"模式，同时保留易用的手动覆盖。
- **可量化、可审计的省钱报告**是建立信任与付费转化的关键：需展示"本周/本月省了 $X、做了什么"，对标 Emporia 月度"省 $23"通知；这是他不订阅 NetZero 的直接原因。
- **定价策略**：提供 30 天试用并用数据证明月省 > 月费；他偏好一次性买断硬件胜过长期订阅——可考虑一次性/硬件买断或明确 ROI 的订阅。
- **明确的红线**：自动化绝不能在 on-peak 时段（4–9pm）用电，否则立即丧失信任。
- **潜在 beta 测试者 + UX 专业人士**：主动表示愿意 beta 测试，且本职做 UX，是高质量反馈来源（"feel free to email me"）。
- 用户认可的产品体验范本可参考：Ecobee（基础体验好、预冷功能）、Emporia App（旧版的"一键充车"被新版多层菜单取代是反面教训——简单直接的主操作很重要）。

---
### 转录纠错 / 不一致信号说明
- 协议名：原文先转录为 "O CC something"、后写 "OCP"、全称 "Open Charge Point Protocol"，应为 **OCPP**（Open Charge Point Protocol）。
- "Nphase" 应为 **Enphase**（太阳能微逆变器品牌）。
- "EM3 / EM2 / NM2 / any M3 / M3" 等口语均指加州净计量政策 **NEM3 / NEM2**（Net Energy Metering）。
- "EcoB" 指 **Ecobee** 智能温控器。
- "eBay charging" 系语音转录错误，应为 **EV charging**。
- "demand charge"：访谈者问加州是否有 demand charge，受访者澄清加州对应叫法是 **"reduce your use day"**（需求侧响应/高峰预警），并非典型工商业 demand charge；他将 Arizona 的住宅 demand charge 与加州做了区分（此处为受访者个人表述，非经核实事实）。
- 容量单位不一致：受访者称 Powerwall "only 10 or 11 kilowatts"、车 "77"——按上下文 77 为 kWh（电池容量），Powerwall 应指约 10–11 kWh 容量；原文用词为 kilowatts，此处按上下文标注（推断）。
- 日期未在逐字稿中出现，标为"日期未知"。
