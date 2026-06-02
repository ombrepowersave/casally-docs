# Koos Erasmus · 专业咨询 · 2026-03-03

> 说明：本摘要基于语音转录逐字稿，对明显的转录错误做了内部还原并标注。常见转录错误对应关系：
> - "Sunrow"/"Sunun" → 太阳能板品牌（原文不一致，无法确定具体品牌，标注存疑）
> - "EM3"/"N2"/"NEM 3" → NEM 3 / NEM 2（净计量计划 Net Energy Metering）
> - "birectional" → bidirectional（双向）
> - "true up"/"true bill" → true-up（年度结算）
> - "OCP" → OCPP（开放充电点协议 Open Charge Point Protocol，专家口述为"open charge protocol"，标准缩写应为 OCPP；专家原话用 OCP，保留并标注）
> - "green button connect"/"GBC" → Green Button Connect（由技术负责人 Lingjie 提出，专家当场不了解，承诺会后查证）
> - "cracks"/"cracked"/"crack" → correct（正确，专家表达"账单是对的"之意，推断）
> - "PTO" → Permission To Operate（并网许可）

## 受访者画像
- 太阳能行业从业者，**自 2010 年入行**，主要在 **C&I（商业及工业）侧**，前 7-8 年在加州**专做商业太阳能项目**。
- 工作内容包括**为太阳能系统客户计算账单**。
- 熟悉的加州公用事业：**PG&E（最熟）**、SCE、LADWP（洛杉矶水电局）以及其他南加州公用事业（原文还提到 "SC and E" "L U"，疑为 SCE/SDGE 等的转录残缺）。
- 自述商业与住宅侧太阳能"差别不大"，认为能给出指导。
- **当前在 EV 充电业务**，是一家做"移动充电（mobile charging of EVs）"公司的成员，**面向 B 端商业市场，非消费者市场**。
- 自述**不住在加州**，因此对加州本地用户心态/政治敏感度不一定有把握（在被问账单组成项时主动声明）。

## 主题判定
判定为 **专业咨询**。依据：访谈核心是 Casally 团队（Amber、技术负责人 Lingjie）向具备太阳能账单计算经验的行业专家请教数据源、TOU/NEM 计费、储能配置、合规与硬件路径等专业问题，专家给出基于其从业经验的判断与建议，并非用户痛点访谈或 demo 满意度测评。

## 核心提炼

### 一、数据源与最小可用数据（专家反复强调的核心）
- **15 分钟间隔数据是计费分析的关键、最小必需项**。专家多次强调："is to ask for 15 minute data"。理由：住宅多为 **TOU（分时电价）**，费率随时段变化，**仅有月度账单汇总无法准确还原 TOU 成本、进出口（import/export）时序**。Amber 复述确认"只有月度汇总就无法重建 TOU 成本或进出口时序"，专家答 "Correct"。
- **加州公用事业电表是真正双向的（truly bidirectional）**：分别有用电（consumption/import）计数器和发电（generation/export）计数器，每个 15 分钟区间能同时给出该时段进口与出口的千瓦时数。专家特别区分：有些公用事业电表用同一计数器进口加、出口减；**加州电表是两个方向独立计数**。
- **TOU 同时适用于双向**（进口和出口）："A utility will give you both directions."
- **数据源重要性排序**（专家被直接要求排序时给出）：**公用事业数据最重要**。理由——电表数据"某种程度上也包含了你的太阳能和电池数据"，因为它在电表处显示任意时段的进出口。**即便没有 power wall / 太阳能数据，只要有 15 分钟公用事业数据，仍能做分析**。
- 仅有公用事业净负荷（net load）时，**无法精确看到电池何时充放电，但能得到大致判断（good idea / good assessment）**。"ultimately you need the data from all three sources"（公用事业 + 电池 + 太阳能），但单靠公用事业数据也能做不错的评估。
- **检测电池异常充放电所需信号**：需电池数据（充/放电数据）。专家提到太阳能监控系统（口述品牌转录为 Sunrow，存疑）通常也能给出 power wall 的数据。

### 二、数据获取方式（专家给出的实操做法）
- 商业侧的常规做法：**让客户提供其 PG&E 在线账户访问权限（账号 + 密码）**，登录后**一次性拉取 15 分钟历史数据**。专家明确："you will need to do a one-time export from that bill for the last two three months data"——**不需要持续导出，只需一次性导出最近 2-3 个月数据**。
- 出于安全，客户可在你拉完数据后**自行改密码**，使你无法获得未来访问权。
- 替代方式：**让房主自己登录账户、把 15 分钟数据导成 Excel 表发给你**。专家指出房主"想法可能不同"，房主自己拉数据这点很重要，让房主知道这个选项。
- 对电池/太阳能监控系统同样需申请访问权限。
- 专家**强烈建议**：除了房主寄实体账单或邮件发 PDF 之外，作为更准确计算的必需信息，**应要求拿到公用事业账户的在线访问权**。
- **关于公用事业 API**（技术负责人 Lingjie 提问）：专家**不知道加州公用事业有可拉账单的 API**，至少其当年打交道时不知道；过去 2 年未直接接触。承诺**会后花 10-15 分钟查证是否有 API**。
- **关于 Green Button Connect / GBC**（Lingjie 提出的协议）：专家**当场不了解**，做了笔记，承诺会后查证。专家评论：若能用它优化/自动化数据拉取这步，"would save a lot of manual work on your site"，对 App 是很大帮助。请团队通过 Upwork 发邮箱以便后续沟通。

### 三、TOU / 计费引擎需处理的细节
- **季节性费率**：所有加州公用事业都有**冬季和夏季费率，通常不同**，必须做季节性调整。
- **费率计划更新频率**：专家称 **PG&E 大约每 2 到 6 个月更新一次费率计划**，变化通常很小，但有时确实影响账单——尤其近 4-5 年公用事业电价涨了不少。
- **费率表获取**：费率表发布在公用事业官网，通常以 **Excel 表**形式提供。要做准，**需每月去各公用事业站点下载最新费率表**，确保给客户套用了正确费率。专家强调这部分"会花你不少工夫"。
- **夏令时（Daylight Saving）必须处理**：峰时时段固定（专家说"4 到 10 PM 或 4 到 11 PM"，自述不确定具体），**若不应用夏令时会差 1 小时**，必须对账单应用夏令时。
- **NEM（净计量）演进**：NEM 1 → NEM 2 → **NEM 3**。**NEM 3 下太阳能发电的上网积分远低于此前协议**，"don't get full commercial credits anymore"，采用**避免成本费率（avoided cost rates）**。因此**配电池更有利**——要尽量减少太阳能回送电网。专家提到 Casally 目标客户在 NEM 3 下（Amber 提及目标是"NEM 3"，转录为 EM3）。

### 四、True-up（年度结算）建议
- 房主对 true-up 常感意外（Amber 转述其太阳能朋友常收到 true-up 账单很惊讶）。
- 专家建议：**有 15 分钟数据就已具备做 true-up 的信息**，做一个**逐月累加的 true-up 计算器**是好主意，让用户看到累计金额、预估年度 true-up 能拿多少。
- 逻辑：**若出口多于进口才有 true-up；若出口不多于进口，true-up 为零**。对超额发电的客户，逐月展示 true-up 累加金额"很有价值"。

### 五、对产品方向的专业建议
- **储蓄（Savings）vs 避免账单**：被问房主习惯按"省钱"还是"避免账单价格"思考，专家明确选 **savings（省钱）**。
- **认可 budget/savings/事件三层逻辑**：专家认为用安装前后账单对比来算月度预算、再算 savings 的逻辑"exactly what it should be"，"very good logic"。认可"savings 跟随 events"——修正事件后 savings 随时间增加，能体现 App 有效性。
- **认可把行为性 savings 与官方账单分离**："you have to separate the savings because that demonstrates the effectiveness of your app." 认可把行为节省与账单组成项（如 minimum charge）清楚分开。
- **反事实（counterfactual）savings 的可辩护基线**：专家说"取决于客户"。给出量化判断——**单户住宅房主，装太阳能前账单可能 $500-600，加电池前 $1000；安装后仍 $200-300，但安装商承诺过 $50-100**。**任何高于 $50 的节省在他看来是可辩护的（defensible）**。补充：savings 超过 $50 甚至 $100，客户会愿意付费/分成。注意有些客户根本不在乎一两百块（非理想客户）；**对预算敏感的有小孩家庭**更会看重。
- **发电侧 vs 配电侧 savings 拆分**：专家说是"很好的问题"，但需再想想；倾向认为**用户不会太在意这个拆分，nice to have 但非必需**——用户只会高兴你找到了节省和问题。
- **账单组成项（base/service charge/delivery/special funds）透明化**："不认为用户需要了解那种细节"，"good to show 但 probably not essential"。强调这涉及心态甚至政治，自己不住加州不好判断。
- **bottom sheet 计算逻辑透明度**（峰/谷费率、公式、估算 delta）：**认为足够支撑节省主张**，因为能让用户形成"回家别马上插车充电"的意识。

### 六、执行建议 / 自动化的边界（重要风险判断）
- **强烈反对自动化执行（改用户系统）**："I would not automate it to that effect."、"I would not go as far as doing automatic updates to any system."
- 理由——**法律责任（liability）**：未经客户明确同意自动改其系统、且更新未达预期效果，会有责任问题；客户不满、差评（"this is customer-facing so you may get bad reviews"）。
- 推荐做法：**识别问题 + 推荐修复**。对 EV 充电这类（如"峰时在充电，停掉"），若你知道其充电器型号、知道怎么设置，可直接给出修复建议（如设为午夜后才充）。
- **对电池充放电时机错误**：房主自己通常改不了，**推荐动作应是"联系安装商重新编程电池"**。
- 认可"相对财务边界（而非纯优化）触发执行建议"的思路，但前提是不要做自动更改。

### 七、风险 / 坑 / 现实障碍（专家点名）
- **最常见问题：系统未正确配置**。尤其 **power wall 配置不当**——该充时不充、该（峰时）放时不放；这是"最重要需要识别的潜在故障点"。
- **第二常见：用户下班回家插车即充，正好撞上峰时**。需设置充电器仅在午夜后/低峰时段充电。
- **夏令时导致的事件**：公用事业账单会自动随夏令时调整；**但若 power wall 不遵循夏令时，其充放电时间会差 1 小时**（冬季对、夏季错），**这构成一个值得 surface 的"事件"**。注：被问"太阳能出口时序错配是否算事件"时，专家认为公用事业侧会自动随夏令时调整，所以不算；**电池/power wall 侧不随夏令时才算事件**。
- **事件排序/估值**：建议对事件做**基础排序系统**。指出 EV 峰时每天充电"could kill your budget one month"、抹掉 savings，值得高优先级。给每个事件都强行套上估算金额或排名较难，但应有基本排名。

### 八、"账单争议"的真相（专家强烈、明确的判断）
- **公用事业几乎从不算错**。专家称看过约 **1000 份公用事业账单，几乎没见过公用事业算错**；"the utility doing something wrong, that's 0.1% of the time"。
- 问题几乎总是**安装商/太阳能系统/电池配置错误**，而非公用事业。
- **房主拿你的系统去找公用事业证明账单错"不会有好结果"**（"That's not going to go down well for the homeowner"）——一旦公用事业把费率套到账单上，很难推翻其系统。
- **房主觉得账单不对，通常是误解了自己的费率计划（rate schedule）**。因此本产品的真正价值是**帮房主更好理解费率计划**，而非"证明公用事业错了"——专家明确认可这个重新定位（Amber 主动把定位改为"帮房主理解账单与系统行为是否一致"，专家赞同）。
- 即便公用事业总是对的，向房主展示导向结果的逻辑路径仍有价值：最坏情况下能让房主明白是自己算错或预期错了。

### 九、太阳能贷款 / PPA / 租赁 是否纳入"家庭能源账本"
- 专家**不主张默认纳入**（被问"应不应该包含 solar loan / PPA 义务"，先答 "no"），但若客户愿意分享这些信息，**有价值**——能让房主看到"我到底有没有省钱、从哪个阶段开始省钱、要还几年款才真正开始省"。
- 但纳入后数据采集复杂：何时开始还、还多久、**税收优惠是摊进月供还是一次性抵某年税**——"that calculation is not straightforward"。
- **租赁（lease）**：税收优惠通常归系统所有者而非付租金的人，是"另一层复杂度"；需查清是租赁、银行融资、谁拥有系统。
- 专家自己**只做过商业侧（全部是融资的）**，住宅侧 cash/loan/PPA/lease 占比**不知道**。
- **强调用户疲劳（user fatigue）风险**：问太多信息（租赁多少、是否融资、月供多少）用户会中途放弃，有些房主自己也不知道。**初期应尽量减少用户输入，用最少信息尽快出结果**。

### 十、PTO / 互联 / 计费周期
- **PTO（并网许可）从签约到拿到，延迟主要在公用事业侧**：检查、大量文书；安装商需快速处理文书并交给公用事业；有时是等公用事业审批、上门重新编程电表，可能耗时。是"承包商 + 公用事业"组合因素。
- **互联/换表期间的计费周期混乱**：专家**不认为是大问题**——公用事业通常会通知，认真读账单就能看到；装这类系统的人通常会留意。

### 十一、硬件路径与合规（技术负责人 Lingjie 与 Amber 提问）
- **连接公用事业侧（含公用事业电表）"极其困难"**——专家明确告知。
- 但**控制 power wall、逆变器充电控制器、充电器都可行**：这些系统已存在，可建接口。
  - **EV 充电器**：若充电器符合 **OCPP（专家口述 "OCP / open charge protocol"，开放协议）**，可控制其何时开始/停止充电，可在 App 后台集成。
  - **逆变器**：多数大型逆变器厂商**有 API**，可远程接口控制太阳能向电池送电/取电时机。
- **自装电表（mimic 公用事业数据）**：可在公用事业电表旁**装一块电表来"复制/镜像"所需数据**，装了就不依赖公用事业。**合法、绝对允许**；太阳能安装商也常这么做（装在公用事业电表旁，用于控制电池充放电）。
- **责任/合规**：用现成（off-the-shelf）公用事业/能源电表，**多数本身符合安全要求**，**无需自建硬件**。只要电表有正确的安全协议/措施，**第三方设备装在主面板/电表附近无额外责任**（专家明确说 "no liabilities"）。这些是安全要求层面的事，符合即可。
- **关于具体认证**（Amber 提到 UL 916、FCC、NEC——转录 "NEC the 32 300" 疑为 NEC 文章号，存疑未明）：专家**未逐项回答这些认证**，而是把话题引向"用现成产品 + API 即可，不必自建硬件"。**注：专家未给出 UL 916/FCC/NEC 的具体要求、费用或流程**，此维度信息不足。
- **安装与成本**：自装电表**需找人安装**（涉及用电，普通房主不会自己开电箱装表，只有小部分会）。**最大障碍是价格而非客户意愿**——房主装过太阳能、已有部分组件，装表对他们不是问题；问题是你向他们收多少、他们愿付多少。专家未给出具体安装成本数字（被问及但未报价）。
- **软件 only 长期是否成立**：被问"若 OCPP 和逆变器 API 保持开放稳定，软件 only 是否长期可行"，专家答 "All right"（未展开明确表态，回答较模糊，不宜外推为肯定）。

### 十二、对产品整体与 GTM 的反馈
- **整体评价正面**："I like the app. It's a good app."、"very good app"、"a very good way to make something complex more understandable"。
- **最大未知数是 GTM（如何获客）**：典型美国用户信息过载、社媒过载，**如何有效把产品送到房主面前、如何说服房主付费/分成**是未知部分。"I'm not saying you cannot do it but... if you can effectively address that... very good app."
- 认可团队聚焦**小而高价值市场**（加州、有太阳能/电池 + EV 的单户房主）与**社区/安装商伙伴**而非大众营销的策略——"good idea"、"good app"。
- **教育价值**：很多人不知道回家即插车充电是错误时机，**App 能教育房主这点就"already be huge"**。
- 认可团队对市场规模有研究，但自己**不知道加州有多少户带太阳能+电池**（"Is it a million houses?"），认为是"significant target market"。
- **单一最该改的行为**：被问"房主只改一个行为最大化价值是什么"，专家答 **"EV charging habits"（EV 充电习惯），是最大的一项**。
- **合作意向**：表示愿做顾问/advisor（"Absolutely"），请团队通过 Upwork 发邮箱后续邮件沟通；并承诺会后查证公用事业 API 与 Green Button Connect。

## 关键金句
- "the way I understand the billing is um it will be beneficial for you to get 15 minute data... if you just get a monthly summary, you're not going to be able to accurately tell the customer when he's exporting, when he's importing, and at what time of the day." —— Koos Erasmus
- "the utility data is probably your most important data... because the utility data in a way captures your solar and your battery data as well because it shows at the meter what's been exported and what's been imported at any time of the day." —— Koos Erasmus
- "I would not automate it to that effect. I think if you do that you may be opening yourself to liabilities." —— Koos Erasmus（论自动化执行的法律责任）
- "I do not know of any instances in probably... a thousand utility bills I've looked at over the years where the utility was wrong... that's 0.1% of the time." —— Koos Erasmus
- "It's usually the solar system installer or the battery that's configured wrong." —— Koos Erasmus
- "if it's different to what the homeowner expects, it's because they misunderstood their rate schedule." —— Koos Erasmus
- "the biggest... most important thing that you need to try and identify as a potential trouble spot is a power wall that's not configured properly." —— Koos Erasmus
- "you have to separate the savings because that demonstrates the effectiveness of your app." —— Koos Erasmus
- "anything... any saving probably above \$50 would be something that's defensible in my mind." —— Koos Erasmus
- "you really need to be careful about user fatigue... get as minimal as possible information from the customer to produce the results as quickly as possible." —— Koos Erasmus
- "it's going to be extremely difficult to connect to anything on the utility side including the utility meter." —— Koos Erasmus
- "you can install a meter right next to the utility meter and it can mimic the data you need... If you install that meter, you don't need the utility." —— Koos Erasmus
- "no liabilities... if your meter has the correct safety protocols... you're fine there." —— Koos Erasmus
- "your biggest barrier there would be price and not the willingness of the customer." —— Koos Erasmus
- "I would probably say EV charging habits. That's probably the largest one." —— Koos Erasmus（单一最该改的行为）
- "how are you going to get this in front of effectively in front of a homeowner... how you going to convince a homeowner to pay or to share in their savings with you. So to me that is the unknown part." —— Koos Erasmus（GTM 未知数）

## 行动项 / 机会点
- **数据策略**：把"获取 15 分钟间隔数据"作为产品的硬性要求；月度账单汇总不足以做 TOU/进出口/true-up 计算。优先级：公用事业 15 分钟数据 > 太阳能/电池监控数据。
- **数据接入流程**：初期可采用"一次性导出最近 2-3 个月历史数据"模式（房主授权登录或房主自导 Excel）；不必持续导出。
- **会后跟进（专家承诺）**：(1) 查证加州公用事业是否有可拉账单的 API；(2) 查证 Green Button Connect / GBC 协议——若可用可大幅自动化数据拉取。团队需通过 Upwork 把邮箱发给专家以建立邮件沟通。
- **计费引擎必做项**：季节性（冬/夏）费率调整；夏令时对账单与 power wall 时序的处理；每月从各公用事业官网下载最新费率表（Excel）以保持费率准确。
- **风险定位调整**：不要把产品定位成"证明公用事业算错"（公用事业几乎从不错，房主拿去维权会碰壁）；定位为"帮房主理解费率计划、判断账单与系统行为是否一致"。
- **自动化边界**：不做自动改用户系统（责任/差评风险）；采用"识别问题 + 推荐修复（含'联系安装商重新编程电池'）"模式。
- **事件系统**：建立基础事件排名；重点监测 power wall 配置错误、EV 峰时充电、夏令时导致的 power wall 时序漂移。
- **Savings 模型**：保持行为性 savings 与官方账单分离；反事实基线可辩护门槛参考 >\$50；发电/配电侧拆分列为 nice-to-have。
- **True-up**：做逐月累加的 true-up 计算器（仅对出口>进口的客户有意义）。
- **硬件路线（长期）**：优先用现成电表 + API（OCPP 充电器、逆变器 API）；自装镜像电表合法且无额外责任，但需专业安装，最大障碍是价格；连接公用事业侧极难，避免。
- **GTM（专家点名的最大未知）**：需想清楚如何在信息过载环境中触达房主、如何说服付费/分成；可借力 EV 角度与教育（教房主避开峰时充电）。
- **顾问关系**：专家表示愿做 advisor，后续通过邮件推进。

## 待澄清 / 信息不足（如实标注）
- 专家口述的太阳能板品牌转录不一致（Sunrow/Sunun），具体品牌未能确认。
- UL 916 / FCC / NEC 具体认证的要求、费用、流程——专家未逐项回答，本维度信息不足。
- 自装电表的具体安装成本——被问及但专家未给出数字。
- "软件 only 是否长期可行"——专家回答模糊（"All right"），未明确表态，不宜外推。
- 加州带太阳能+电池的住宅总量——专家明确表示不知道。
- 住宅侧 cash/loan/PPA/lease 占比——专家只做过商业侧，不知道。
