# Christina Di Stefano · Demo 反馈 · 2026-01-15

## 受访者画像
- 拥有完整的特斯拉能源生态：电动车（Tesla Model 3，访谈中出现的车型）、Powerwall 储能电池、太阳能板（连接设备页列出 cars / power walls / solar panels）。
- 日常通过特斯拉自家 App 监控这些设备；提到丈夫比她更多地处理这些设置（"my husband does so much of that stuff more than I do"）。
- 自认对太阳能系统的运维很不了解：不知道太阳能板该多久清洁、不知道如何开关太阳能（"I still don't even know how to turn the solar off and back on"），整体感觉"有点不知所措"（overwhelming）。
- 曾经历一次电费异常偏高，打电话给（推断为电力公司/特斯拉，原文未明确）询问原因，等待很久（on hold forever），最后发现是高峰时段给车充电导致；此后把车改回夜间充电。
- 家庭：提到希望"add family members"功能不错、其他家人也能看到，可推断为多人家庭，但具体人数未说明。地区/住房类型未说明。

> 转录纠错说明：逐字稿多处把人名 "Christina" 转成 "Christie"、"Tessa"、"Tesla"（如 "like Tessa said""like Tesla said, like, okay, we've partnered"），从上下文看指的是品牌/合作背书可信度，统一理解为"特斯拉（或某可信品牌）背书"。"test lab"（"takes me to my test lab"）应为 "Tesla app"。"this firewall switch to battery""This firewall"应为 "Powerwall switched to battery"。这些为明显同音/听错，已在理解中还原，未改原始 .txt。

## 主题判定
判定为 **Demo 反馈**。依据：访谈者 Amber Fu 发送 Figma demo 链接，请受访者共享屏幕、逐屏逐功能（首页 home、事件 event/yellow-suggestion 页、saving 月度页、profile 页）走查并给出第一印象与反应，全程围绕"对这个 demo 的理解、喜欢/困惑、想要的功能、是否愿用"，符合 Demo 反馈维度。

## 核心提炼

### 逐功能反应

**首页 / 顶部横幅（"something may require your attention"）**
- 红色横幅理解准确："it's red... I should be pay attention to it"；读出"something may require your attention"与"power outage"，推断是在提示当前正停电。
- 对警示强度的判断：感觉更像"值得看一眼、让你知晓"，而非"必须立刻行动"——"more of just it's something to look at... you may or may not need to act on it"。

**"今天 vs 平时"用量卡片（Today versus usual）**
- 注意到文案说有 bar chart 但当前没看到图（"I don't see a bar chart, but I'm assuming that there will be one below"）——可用性观察：图表缺失/未渲染。
- 价值感偏低：相比"power outage"提醒，"今天 vs 平时"不是她会真正关注的（"the today versus usual wouldn't be something I'd really focus... as much as something may require your attention"）。

**右上"本月预估"卡片（made for the month，$268.81 → $280.12 类金额）**
- 理解为"大约要付的电费金额"（"the price you're going to pay approximately"）。转录金额含糊（"$28012"），理解为月度账单预估区间，具体数字以 demo 为准。

**EV 充电高价提醒（红色，attention）**
- 读出"your electric vehicle is currently charging during a high price period... suggestion pause EV charging till off peak"，评价"that would be super helpful"，作为高峰提醒很有用。

**颜色语义反馈（重要、反复强调）**
- 红色（attention）很完美，能抓注意力（"red I think was perfect because it brings it to my attention"）。
- 黄色（suggestion / "All good. No action needed"）让她困惑：黄色在她认知里是"caution 谨慎"，与"无需行动"矛盾——"yellow's caution... if you're saying no action needed, then maybe that's more useful [in green]"。建议改用绿色表示"go / 一切正常"。不过当看到黄色卡片实际内容"High solar output available. We recommend charging your vehicle now"后，她又认可黄色适合这种"提示性可选动作"（"the yellow works for that"）。→ 存在前后微妙不一致，核心诉求是"颜色要与动作强度匹配"。
- 蓝色（normal，"all systems normal"）可接受，但也提了绿色或许更合适（"blue is fine, but maybe even green might be an option"）。

**事件页（event，可点开看详情：EV 高价充电 / 太阳能白天不可用 / Powerwall 切换电池）**
- 整体认为有用："helpful to have someone watch over that"——价值在于"有人替你盯着"。
- 对"太阳能白天不可用"类：信息有用但属于她无法控制的事（"kind of out of my control if solar is not working properly"），所以优先级低于行为类。
- 主动指出最有价值的两类（=最省钱）：① EV 高价时段充电（明确排第一，"the EV charging is probably the number one"）；② Powerwall 高价时段充电（可并列第二）。
- 也提到重视"恶劣天气"提醒，并说特斯拉已提供此类（"the Tesla says severe weather is in area"），希望此 App 也能告知电池在恶劣天气会多留电、不放电。

**saving 月度页（逐日列出事件、可下钻明细）**
- 明确表示这是"in the nitty-gritty / in the weeds"，是给"真正想细看的人"，她本人不会经常看、不会坐下来逐数字分析（"for me to sit and analyze it, I doubt that I would"）。
- 不需要逐日看 EV 高价充电（因为她打算直接把车改到夜间充）；不需要知道 Powerwall 每次切电池的时刻（"I don't need to know when the power wall switched to battery"）。
- 觉得太阳能多次不可用这类聚合信号才有用（"helpful if there's multiple times where the solar production is unavailable... maybe you want to have your solar panels cleaned"）。
- 月度图表（1月–12月那种）：当前形式"挺好"，不需要改成"按月 true-up 风险等级"之类（"I think this is fine"）。

**profile 页（数据连接 / 连接设备 / 通知设置 / 添加家人 / 隐私权限 / 阈值 / 帮助）**
- 连接设备列表（车、Powerwall、太阳能板、家庭地址）："that's great"。
- 通知设置（EV / 设备 / 太阳能产出 / 系统信息可开关）：理解为按需开关，认可。
- 添加家人："That's great. So other family members can see."
- 阈值（battery / home load exceeds、电池预留比例）：理解为用太多会触发；再次强调希望恶劣天气能自动多留电。
- 帮助：吐槽现在"找不到真人客服"让她抓狂（"no one seems to have a person you can call anymore which kind of drives me crazy"），听到会有客服后认可。
- 总评 profile："all good stuff... all important stuff"。

### 首次理解 / 价值认知
- 基本一眼看懂各屏在干嘛，理解准确度高（红色提醒、月度金额、EV/太阳能事件均自行读懂）。
- 自行提炼出产品定位（接近 aha）："you're trying to make it more concise and more user friendly"（相对特斯拉 App 更简洁友好）；后被访谈者点明"特斯拉告诉你系统做了什么，我们告诉你这是否让你走上花更多钱的风险路径"，她回应"I get it. This is basically like help get you in a pinch spending extra money"。
- 最打动她的价值是"有人替我盯着、不用我费劲"（"someone else is monitoring it because I really don't [know] how to monitor it... it's just kind of done for you"）。

### 可用性问题 / 卡点
- "Today versus usual"卡片说有 bar chart 但没显示（缺图）。
- 黄色色彩语义与"no action needed"冲突，造成理解迟疑（见颜色反馈）。
- 走查中多次需访谈者指引点哪个 tab（部分因 demo 不完整，部分因导航不直观），但未表达强烈挫败。
- 注：本次有大量音频/麦克风技术故障（反复掉线、静音），属环境问题，非产品可用性问题。

### 功能请求 / 改进建议（受访者主动提出）
- 电网恢复通知："your power has been restored"——她现在每次停电都得手动开 App 查。
- 恶劣天气时电池行为告知 + 自动多留电（不放电）。
- "忘记插充电"提醒：发现往常会充电、今天没充则提醒（"hey, you forgot to plug in your car"）。访谈者称"会有"。
- 太阳能健康/产出反馈：是否需要清洁、产出是否低于应有水平（"is it not producing enough?... there's no feedback with that"）——这是她反复提、最在意的痛点之一。
- 账单异常的主动归因/预警：把"本月账单偏高 + 原因（如高峰充电、太阳能板可能需清洁）"前置到"需关注"首页，而非埋在明细里。
- profile 的设备阈值页可加"下一步建议"类目：给出本地电力公司高峰/非高峰时段，并建议把充电改到非高峰（尤其对特斯拉新车主友好，免去自己查询夏冬不同时段）。
- 充电计划变更时告知"改了什么、大致省多少"——她说不一定需要精确金额，但要知道"已不在高峰时段"。

### 与现状对比（特斯拉 App）
- 优点：特斯拉**不会合并电力公司账单**，导致"在那块抓瞎"（"you're kind of in the dark there"），本 App 能把两者合并是亮点。
- 缺点/冗余：很多内容与特斯拉 App 重复（"a lot of that's redundant"）；特斯拉细节比她需要的多、有些她看不懂（"I don't even know what it's telling me"）。
- 对本 demo 的评价：用户友好、易看（"pretty user friendly... easy to look at"），喜欢"简洁 + 可点击下钻、自选深度"的层级设计（"you can kind of choose how deep dive... I like that"）。
- 她明确希望本 App 提供特斯拉没有的"added value"，特别是那次账单异常时若有主动提醒就好了。

### 购买 / 付费意愿信号
- 价格/付费意愿：访谈**未直接问价**，未涉及具体付费金额或价格敏感度——此项**未涉及**。
- 使用意愿：偏正向但有条件。"I think it would be helpful... great"，愿意试用、也答应产品完善后在自己家里试一段并反馈。
- 关键顾虑/犹豫信号（嘴上认可但行为保留）：
  - 数据接入授权反复纠结。对特斯拉账户接入尤其谨慎，担心引入故障："the Tesla app runs pretty smoothly... I don't really need more glitches"；倾向自己在特斯拉 App 里操作，而非让本 App 控制设备。
  - 对控制类动作（apply now 直接控制充电）犹豫：若可能引发故障则拒绝（"if it does cause glitches then I would say no"），更愿意"apply now 跳转到我自己的特斯拉 App 去做"。
  - 信任依赖第三方背书：反复说若特斯拉表态支持/合作、报告准确，她才更愿意接入（"if Tesla was like... we support it, then I probably be more inclined"）。
  - 多次说"还不清楚要披露多少特斯拉/电费数据"，把最终意愿挂在隐私边界上（"how much I want to share and how much I don't"）。
- 终极取舍题（更便宜电费但不确定 vs 即使省得少但有信心走在安全路径）：她选**省钱/降本**，理由是装太阳能的初衷就是降本、尽量利用自然（"the whole idea to have solar is to decrease your cost and utilize nature"）。

## 关键金句
- "red I think was perfect because it brings it to my attention, but yellow's caution. So... if you're saying no action needed, then maybe that's [green] more useful." —— Christina
- "I think the two most important are the EV charging during [high] price... the EV charging is probably the number one in my opinion." —— Christina
- "This is where it gets kind of like in the nitty-gritty in the weeds... probably more for like the person that really wants to look at this in more detail. I probably wouldn't be looking at this as much." —— Christina
- "Tesla also doesn't merge your utility bill in with it. So you're kind of in the dark there. So that's kind of nice that you're able to do that. But to me, a lot of that's redundant." —— Christina
- "It's almost like you don't have to put too much effort into it... it's just kind of done for you and someone else is monitoring it because I really don't [know] how to monitor it." —— Christina
- "I still don't even know how to turn the solar off and back on... it's a little overwhelming." —— Christina
- "I don't even know how often to clean it. I don't know like will it tell me when it's not getting the amount that it should be getting. There's no feedback with that." —— Christina
- "The Tesla app runs pretty smoothly... I don't really need more glitches." —— Christina（解释为何犹豫接入特斯拉控制权）
- "If I'm going to utilize your services, I would think I'm going to be fine with both of them [utility + solar data]." —— Christina（接入授权上的有条件接受）
- "The whole idea to have solar is to decrease your cost and utilize nature as best you can." —— Christina（在"省钱 vs 安心"中选省钱）

## 行动项 / 机会点
- **修复首页 "Today vs usual" 缺失的 bar chart**（demo 已声称有图但未显示）。
- **重审颜色语义**：黄色=caution 与"无需行动"冲突；考虑"绿色=正常/可选优化、红色=需关注、保留黄色仅用于提示性可选动作"，确保颜色与动作强度一致。
- **把"价值排序"映射到信息架构**：用户自评最值钱的是 EV/Powerwall 高价时段充电（可控行为），太阳能不可用属不可控、优先级低；月度逐日明细对她属"杂草区"，应弱化、改为聚合异常信号（如"太阳能多次不可用→建议清洁/联系太阳能公司"）。
- **太阳能健康反馈**是强未满足痛点：产出是否偏低、是否该清洁——市场上明显缺口，可作差异化卖点。
- **新增主动通知**：电网恢复、忘插充电、账单异常归因（高峰充电/太阳能异常）、恶劣天气电池策略。
- **降低接入门槛与信任成本**：提供只读（read-only）接入选项；明确各数据源的最小披露范围；争取特斯拉/品牌背书以打消"会引入故障"和"准确性"顾虑。
- **profile 阈值页加"下一步建议"**：自动给出本地高峰/非高峰时段并建议改充电时段（对新车主尤其有价值，免去夏冬时段自查）。
- **强化核心定位话术**：相对特斯拉 App 的差异是"合并电费账单 + 告诉你是否走在花更多钱的风险路径 + 简洁可下钻"；规避与特斯拉 App 的功能冗余。
- 待跟进：邀请其完成版后在家实测；付费意愿/价格未问，下一轮需补问。
