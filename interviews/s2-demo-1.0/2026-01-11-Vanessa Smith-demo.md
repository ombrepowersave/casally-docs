# Vanessa Smith · Demo 反馈 · 2026-01-11

> 说明：逐字稿中受访者署名为 "Vanessa Smith"，原文件名为 "Vanessa Houston"；经确认为同一人，已统一命名为 **Vanessa Smith**（s1/s2/s3 三份为同一受访者）。访谈者为 Amber Fu，CTO Yi 与同事 Martin 在场旁听。

## 受访者画像
- 加州居民，与丈夫两人家庭（"we are a two[-person] household"）。
- 拥有太阳能、电动车（特斯拉，原文提到 "my Tesla app"）、Tesla Power Wall 电池（原文提到 "power wall switch to battery"）。
- 拥有智能冰箱（原文提到 "smart refrigerator" / "Samsung Family Hub"）；明确表示**没有**智能洗衣机/烘干机（"I don't have a smart washer and dryer"）。
- 用电公司为 PG&E（原文多次转录为 "PG&E"、"P Gen"、"Pione"、"PGE"，均指 PG&E，推断）。
- 最大痛点：**true-up（年终结算补缴）**，自述其 true-up "is over $1,000"。主因是电动车充电。
- 自称是"视觉型的人"（"I'm a visual person"），偏爱图表呈现。
- 这是与 Amber 的第二次访谈；上次已表达过核心诉求（见下）。

## 主题判定
判定为 **Demo 反馈**。依据：受访者全程通过共享屏幕，逐屏走查 Figma 原型（首页 banner、今日卡片、月度估算卡片、停电事件、EV 充电建议、事件页、savings 图表、设置/通知/权限/帮助页），逐功能给出喜欢/困惑/不喜欢及改进建议，并谈及付费意愿与推荐意愿。

## 核心提炼

### 上次访谈复述的核心诉求（Amber 开场复述，受访者确认）
- 不要能量图表本身，要"真正可操作的省钱方法来减少 true-up"。受访者确认："my biggest issue is the true up."
- 不要告诉她"哪里耗电（it's a pig）"，而要直接告诉她该怎么做并展示美元差额。受访者确认："Exactly."

### 逐功能反应

**顶部 banner："Something may require your attention"**
- 受访者认为这句话给人的感觉是"出事了、必须马上行动"（"something's wrong and you need to act now"）。但 Amber 澄清其本意只是"今天有些事可能影响成本，值得快速看一下"，非警报。
- 改进建议：加感叹号；文案更居中（建议 "attention" 放在 "may" 和 "require" 之间）；句号后留白让她觉得"是不是漏了什么"，建议用 bullet points 列出具体几条（如停电、用电过高、建议暂停 EV）。
- 最终（访谈结尾自评）她唯一想改的就是这条 banner 的红色："something may require your attention in red that shouldn't be in red."

**左侧卡片："Today vs. your usual / unusual pattern detected"（今日对比卡）**
- 强烈不喜欢用红色。红色=警戒/负面，看到 "unusual" 高亮红色会"担心、甚至有点慌、停下手里的事"（联想到银行的异常提醒）。她反复说"I just really don't like it"。
- 建议：非警报的内容用"友好的黄色"背景；文案改为"look what's changed"（因为这些都是"已改变"的项）。
- 强烈要求**图表**：作为视觉型用户，登录涉及金钱/储蓄类 app 时期待看到 graph（举例：Raken[球拍?，原文 "rackets"，疑为某 app 名，转录不确定]、健身步数 app 都有升降图）。"that's what people want to see... up, down, just to show me visually."
- Amber 澄清此卡用意是"今天是否偏离日常模式"（如太阳能平时这个点在发电、今天没发），受访者仍坚持要图表/百分比/大小标记来直观看差异。

**右侧卡片："Estimate for the month"（月度估算）**
- 困惑：不清楚这个数字（原文读到 "26880 to 280"，疑为占位符 / 转录错乱）代表什么——是按今天习惯能省的？是当前账单欠款？"does do my do I owe this much on my bill?... you're confused."
- Amber 解释：这不是账单，是"若本月持续此类情况，对成本大致的影响"。受访者要求把口径写清楚，如"based off your habits today / this week, you can save this much"。
- 兴趣度低："I would be less interested in the estimate for the month"，因为她平时根本不看这些数。但若该数字**直接累积进年终 true-up**，则"每次登录看到当前金额会不错，因为你看不到那些突袭式的（surprise）账单"。
- 建议把底部的"suggestion"上移到更靠近月度估算的位置，"because those two correlate very well together"。

**Power outage 停电提醒**
- 明确喜欢。"we all heavily rely on our things. So if they know ahead of time, I think that's great."
- 喜欢显示距离（"approximately 1.1 miles away"），因为即使没直接受影响，检修电线时也可能波及，便于提前准备。
- 喜欢其 who/what/when/where/why 结构；想看到开始时间、影响范围、预计恢复时间（"asking a lot but ideally that's what I would like to see"）。
- 条件：若只说"停电了"而不给上述细节，则"根本没理由放在那"。
- 喜欢 mute / remind me / remove 三个选项——因为提醒太多会让人静音甚至卸载 app，能自行处理很好。

**"Apply now" 建议按钮（暂停 EV 充电至非高峰）**
- 对"暂停 EV 充电至非高峰"这个建议本身很喜欢，但**强烈反对自动操作/绑定特斯拉**（详见隐私段）。她预期此功能只是"告诉她该做什么"，仍要自己进特斯拉 app 手动改设置；确认："I would have to manually go in this app to change it."
- "Apply now" 措辞让她警惕/有点害怕："what what information do they want now?"——一看到 apply now 第一反应是"他们又要我什么信息"。
- 不希望 apply now 每次都出现在屏幕上；无论她是否采纳过，都不想反复看到它。
- 偏好纯"建议（suggestion）"形态而非 apply：反复说"I really like the suggestion thing"。
- **关键诉求：建议必须带美元数字**。不要只说"pause EV charging until off peak"，要说"如果你充电到非高峰，今天能省 $6"（"If you charge... until offbeat[off-peak], you will save $6 today"）。Amber 给出假设：此建议今天省约 $6、长期可把年终 true-up 减少 $300–400，受访者回应："yeah, absolutely... that's a savings. $6 a day times 30/31 days... my true up is over $1,000. So if it can cut it down about 40%... That's amazing."

**事件页（Events / Needs attention）**
- 整体喜欢，认为很详细，满足她"总是问 why"的需求（"my question is always why... they tell you don't charge at five o'clock but why, so when should I charge"）。
- 排序建议：若同一天有多事件，**critical 应排在 unusual 之上**（按严重程度）。
- 逐事件价值排序（她主动评估哪些该留/可去）：
  - **EV charging during high price**：对她是 "a major"、"deal breaker"，必须保留。最想先看到的不是"会不会涨账单"（她说人人都知道会涨），而是**当前每千瓦电价**（如"54 kilowatts[此处应为 ¢/kWh，受访者口语混用]，凌晨 2 点只要 ~30 cents/kWh"），以及等几小时能省多少。还吐槽文案 "may increase cost exposure" 不该用 "may"，"it's going to increase"。
  - **Solar production unavailable**：喜欢，因为她现有太阳能 app **不会**提醒她这类情况。希望立即弹窗。
  - **Power outage**：保留。
  - **Power Wall switch to battery**：没那么重要（她假设自己的特斯拉 app 也会告知），但"有挺好"，倾向保留。
  - **Severe weather in your area**：**100% 可去掉**，"common sense，手机本来就会提醒，有没有这 app 都一样"，"doesn't need to be on the app at all"。
- 每个"needs attention / 事件"项都应**立即推送到手机**，不该让她进 app 才找得到。
- 希望事件带**图标**（如闪电图标），扫一眼就知道是停电，用久了能看图识意。
- 不要加太多内容："if you add too much, it just becomes too much"；现有信息量"good enough"，只需在底部补一句"现在该怎么做"。

**Savings 图表页**
- 非常喜欢，呼应她全程要的"graph"。喜欢标"estimate"而非"final bill"。喜欢既有整体又能按驱动项（如 EV、太阳能）拆解对比。
- 命名：认同叫 "Savings"，不需要改成 "true-up impact" 之类（"at the end of the day, we're just looking for our savings"）。建议把硬币图标改成钱袋图标。
- 偏好"全部展示 + 可拆解"而非只给 top 3：因为不是人人都有 EV，应"全都放上，何不全展示"。
- 喜欢底部 sheet 对电网/电价时段/太阳能等的解释，认为这些子分组都有用、清晰易读。
- 喜欢渐变紫色（ombre）配色。
- 数字过于夸张让她迟疑，Amber 说明是占位符。

**设置 / 数据连接 / 通知 / 权限 / 帮助页**
- 数据连接舒适度：**PG&E（utility）可以、Solar 可以**；**特斯拉 EV 绝不连**（详见隐私段）。地址：既然愿连 PG&E 账单、对方本就有地址，可接受。
- 电力套餐：愿意提供当前套餐；若 app 能据日常用电建议更省钱的套餐（如从 plan A 换 plan B），很想要，"because P Gen won't do that"。
- 通知设置 + toggle：非常喜欢，反复强调要可自定义看/不看什么，"notifications can drive you crazy"。
- 添加家人：喜欢，可加丈夫一起省钱（"household effort"）；认为**孩子不该加进来**，看到像是暗示可加小孩，她觉得没必要。
- 权限页（先征求许可的 toggle）：100% 重要，给人安心感，类比手机系统会先问。
- 电量百分比/千瓦阈值提醒 + toggle：正是她想要的（"these are all things that I wanted to see and I'm actually seeing"）。
- 帮助与支持：必备；建议用 **FAQ 页 + 聊天按钮（chat）+ 电话/邮箱**，不喜欢只能"发消息等邮件来回"。不喜欢页面放头像照片，觉得连同邮箱/地址/账单一起很奇怪、隐私感不适。喜欢带红点的消息中心。

### 首次理解 / 价值认知
- 一眼能 get 红色 banner 与 unusual 是"要她注意"——但理解成了"出事/警报"，与产品本意（温和提示）有偏差，是个理解落差。
- aha 点集中在：**带美元数字的可执行建议**、**停电提醒（尤其距离与提前量）**、**solar production unavailable 提醒（现有 app 没有）**、**savings 图表**。
- 始终没 get / 不买账：月度估算数字（口径不清、平时不看），除非明确它直接滚入 true-up。

### 可用性问题 / 卡点
- 原型多处点不动（"I don't think it's letting me click anything"），部分页面加载慢、读不清（"I can't read it"），属原型限制。
- 红色误导（banner 与今日卡）。
- "Apply now" 措辞引发戒备与困惑。
- 月度估算数字（26880→280 等）含义不明，疑占位符导致更难理解。

### 功能请求 / 改进建议（受访者主动提出）
- 所有建议/事件都要带**具体美元金额**和**每千瓦电价**。
- 首页要**升降图/百分比**直观对比。
- 可设**储蓄阈值提醒 toggle**："能省 $X 时才提醒我"（她个人门槛≈$5，但应可让别人设到 $0.25 甚至 $0.10）。
- 想看停电的开始/影响范围/预计恢复时间。
- 建议接入**智能电器**（智能冰箱/洗烘，Samsung Family Hub），给出如"调高冰箱温度一年省 $25"之类建议。
- 套餐切换建议（plan A→plan B 更省）。
- FAQ + 实时 chat 客服。
- 钱袋图标替代硬币图标。
- 所有建议都要**基于她个人习惯**而非泛泛通用建议（结尾反复强调："based off my habits, not general"）。

### 与现状对比
- 现有太阳能 app **不会**提醒 solar production unavailable，本产品能补这块。
- 现有特斯拉 app 已能告知 Power Wall 切电池，本产品该项重要性因此打折。
- 对比给 PG&E 打电话：常被长时间挂起、双方都 frustrated，"to just get the answer at your fingertips is great"——这是她认可的核心价值。

### 购买 / 付费意愿信号
- 有意愿但**强价格/价值敏感**。明确的盈亏算式："if you guys are charging annual $100 a month... if I'm only saving $200, I... wouldn't continue."（注：原文 "annual $100 a month" 口径自相矛盾，推断她想表达"按月/按年收费"且省额需显著高于费用，具体未说清）。
- 高费用下："eventually you're going to learn these habits on your own"——担心学会习惯后就不再需要订阅。
- 期望**激励机制**留存：如坚持一年省 20% 给 10% 折扣，或积分换免费月。
- **试用 → 留存的硬门槛**：积极改变习惯后，若**第一个月（至少 60 天内）看不到任何变化/省钱**，就会停用——这是她说的"unacceptable / deal breaker"级别的失败。
- 推荐意愿：会推荐给**有 EV 和太阳能的邻居/社区里人**，但不会随口泛泛安利。
- 结尾情绪积极："I'm actually looking forward to seeing some of this app... I'm going to be very excited"，愿做真实版本的测试与反馈。

## 关键金句
- "my biggest issue is the true up." —— Vanessa
- "I want to see it and make it worth it." —— Vanessa
- "I think it comes off as something's wrong and you need to act now." —— Vanessa（评 banner 文案）
- "Maybe that would be a friendly yellow in the background instead. But the red doesn't make sense." —— Vanessa（评今日卡红色）
- "Don't just tell me pause EV charging until off peak. If you charge... until off[-]peak, you will save $6 today." —— Vanessa
- "My true up is over $1,000. So if it can cut it down about 40%... That's amazing." —— Vanessa
- "EV charging during high price... that's a deal breaker for me." —— Vanessa
- "The severe weather in your area... I could live without it. It doesn't need to be on the app at all." —— Vanessa
- "I don't want to connect my app... there's cameras in there... I 100% would not do it. I wouldn't even connect my Ring camera to it." —— Vanessa（拒绝连特斯拉）
- "Instead of EV on here, [if] it said your smart refrigerator, your smart washer dryer, I would [connect]." —— Vanessa
- "If I'm changing my habits and don't see anything in the first month... I'm not going to use the app anymore." —— Vanessa
- "I want it based off my habits. I want to see the graphs. I want to see the numbers. I want to see the percentages." —— Vanessa
- "When I call P[G&E]... I'm frustrated. They're frustrated. I've been on holds forever. So to just get the answer at your fingertips is great." —— Vanessa
- "It kind of hit everything... spot on for me." —— Vanessa（总评）

## 行动项 / 机会点
- **去掉/弱化首页红色**：banner 与今日对比卡不是警报就别用红；用黄色等"友好"色，文案改"look what's changed"。这是她唯一坚持要改的视觉问题。
- **每条建议/事件都挂美元数字 + 每千瓦电价**，且强调"省多少"而非"会涨多少"；建议靠近月度估算放置。
- **首页加升降图/百分比**满足视觉型用户对比直觉。
- **重做 "Apply now"**：改为纯建议口吻、可一键完成或明确"只是告诉你该做什么"；避免每次重复出现；消除"又要我什么信息"的戒备。
- **明确月度估算口径**：写清"based off your habits today/this week"，并明确它如何滚入年终 true-up；否则该卡价值感低。
- **EV 永不强制绑定**：提供"只读 / 不连 app 也能展示"的方案；隐私（摄像头、定位、开锁）是她的硬红线。把"连接设备"叙事从 EV 扩到智能家电（冰箱/洗烘、Samsung Family Hub）更易获得授权。
- **储蓄阈值提醒做成 toggle**（可设 $0.10 / $0.25 / $5…），并全局强化通知可自定义，避免提醒疲劳导致卸载。
- **停电事件补全**：开始时间、影响范围、预计恢复时间、距离。
- **事件默认推送到手机**并配图标；severe weather 默认可关/不做。
- **savings 页**：保留 estimate 字样、整体+拆解、全展示而非只 top3；钱袋图标。
- **留存设计**：必须在 60 天内让用户看到可量化的省钱效果，否则流失；考虑积分/折扣等激励。
- **个性化优先**：所有建议基于个人用电习惯，而非通用建议。
- **套餐切换建议**与**FAQ + 实时 chat 客服**是受认可的增值点。

## 一致性 / 信号备注
- 嘴上说喜欢但行为/语气犹豫的点：对"月度估算"卡反复说"sounds great / 很好"，但同时坦言"我平时根本不看这些数""兴趣不大"——属典型口头认可、实际低使用意愿，价值要靠"直连 true-up"才成立。
- 隐私态度坚决一致：多处明确拒连特斯拉/Ring，可信度高，不是随口。
- 付费表态存在口径矛盾（"annual $100 a month"），具体价格点未说清，仅能确认"省额需远高于费用、且需快速见效"。

## 转录纠错标注（不改原始 .txt）
- "P Gen" / "Pione" / "PGE" / "PG&E" → 均指 **PG&E**（Pacific Gas & Electric，加州电力公司）（推断）。
- "EB charging" / "EV like a $10" 等 → **EV charging**（电动车充电）。
- "offbeat" / "off beat" → **off-peak**（非高峰时段）。
- "Eevee" → **EV**（电动车，转录把 EV 听成宝可梦 Eevee）。
- "54 kilowatts... 30 cents per kilowatt" → 语境是电价，**应为 ¢/kWh（每千瓦时电价）**，受访者口语把功率(kW)与电价单位混用（推断）。
- "rackets" → 疑为某 app 名（如 "Rakuten"？转录不确定），**保留原样存疑**，未据此新增事实。
- "26880 to 280" / savings 页"drastic number" → Amber 确认为**占位符**，非真实金额。
- 受访者署名 "Vanessa Smith" vs 原文件名 "Vanessa Houston" → 经确认为同一人，已统一为 Vanessa Smith。
