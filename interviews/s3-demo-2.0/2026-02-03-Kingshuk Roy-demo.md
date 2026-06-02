# Kingshuk Roy · Demo 反馈 · 2026-02-03

## 受访者画像
- 住宅自有太阳能 + EV，约 3 年前安装太阳能，**没有储能电池**（"I don't have a battery... I just have the solar setup and the EVs. I don't have the storage batteries."）。
- 处于较早期的太阳能补偿政策。访谈者问是 AM2 还是 AM3 政策（推断为 NEM 2.0 / NEM 3.0 的转录误读），受访者答"是较旧的那个"，并提到是在政策即将取消前几个月装的。（注：访谈者口述 "AM2/AM3"，本摘要按上下文判断指 NEM 太阳能净计量政策，受访者自己未明确说出政策名称。）
- 电费极低：每月给 PG&E（转录为 "PGNA"，按上下文应为 PG&E）约 $12 维护/接入费；年度 true-up 约 $60–$70/年。
- 用电习惯主动优化：装太阳能时先算好需要多少，且日常刻意把大部分电器安排在白天用，以直接消纳太阳能。EV 也尽量安排白天充电用太阳能。
- 季节性：夏天发电高、向电网回送多；冬天/雨天白天短、发电少，基本只够当天打平（break even），回送少。
- 家中有两辆特斯拉（"in my household also I have the same"，指多车场景）。
- 自述对 Google Meet 不太熟，需要摸索如何共享屏幕。

## 主题判定
判定为 Demo 反馈。依据：访谈者通过 Figma 原型分享屏幕，引导受访者逐屏浏览新版 home/event/saving/bill 等界面，受访者针对各功能给出理解、提问与改进建议。

## 核心提炼

### 首次理解 / 价值认知
- 浏览后能自行准确复述产品大意："you are like kind of monitoring like all the different kind of usage... suggesting like the charging schedule... showing the consumption and like kind of how much might be your expected bill"。
- 对账单成本溯源界面有明确正面反应（见可用性）。
- 但因自身电费极低（年 true-up 仅 $60–$70），对整体价值持保留：被问"对你的情况哪里有用"时，停顿思考后只能找出**一个**有用点——peak/off-peak 时段数据。（嘴上认可产品"覆盖了一切"，但落到自身实际收益时明显犹豫、勉强，价值与他低账单的现状不强匹配。）

### 逐功能反应
- **月度账单预算（budget / tolerance boundary）**：受访者主动质疑预算档位偏高——"if someone has a solar and the battery... this bill seems to be like kind of pretty high already like the 200 or 170"。访谈者解释档位会按用户真实账单动态生成（如月账单 $30 就给 $10/$15 档）。受访者表示理解（"Got it"）。点击 $170 时一度反馈"Nothing is happening"，存在一个交互无响应的瞬间。
- **建议卡 / 自动 vs 菜单（automatic / menu）**：理解两种模式（系统代操作 vs 跳转用户自己的 Tesla App 调整）。
- **EV 充电优化范围**：主动追问产品是否只看 EV 充电、不看其他高耗电老旧电器（"a very old dryer or old washing machine, old fridge... consuming a lot of electricity"）。访谈者答目前纯软件只能评估 EV，未来接入硬件后再扩展到冰箱/洗衣/AC 等。受访者确认"right now you're just like kind of starting with the EV car only"。
- **Event 页 / more detail（为什么这样建议）**：自行推断出逻辑——夜间（如 9 点）充电会更贵，因为没直接用太阳能。理解到位。
- **停电预警（power outage warning）**：理解"apply plan"= 系统自动代为执行（如停电前用太阳能先充 power wall 再充 EV 保家用）。
- **Usage（peak/off-peak）**：被问自己是否在分时电价（TOU，转录为 "till you rate plan"）计划下，受访者答记不清、需查证。
- **Saving / 风险账本（risk ledger）**：理解 saving 侧是基于行为与时序检测的"成本风险敞口"，bill 侧是账单实际显示；理解 $56 是当前计费周期检测到的总风险成本，重复同样模式则会变成额外成本。按 EV/solar/power wall 分类、每类显示发生次数（如 EV 充电出现 4 次）。
- **计算说明 / 可审计（auditable）**：明确表示喜欢——"this is really nice. I like this like kind of the explanation of this one"，并复述理解为"using this particular formula extra cost... makes sense"。这是访谈中最强的正面信号。
- **账单核对（bill proof / 账单行项匹配）**：理解 mismatch 不等于乱收费，而是"基于我们检测的数据，预期某行应约为 X，但账单显示 Y，值得复核"，回应"Right. Makes sense."
- **top cost driver**：访谈者带过，受访者只回"Okay"，无具体反应。

### 可用性问题 / 卡点
- 初始一度停留在旧版（"this is the old one / current one"），需访谈者引导到 "new home"。左侧 flow 中"new home 是新版、另外三个是旧版"的结构需口头解释才弄清。
- 点击月度账单预算的 $170 时"Nothing is happening"，随后才有响应——存在交互反馈延迟/不明显。

### 功能请求 / 改进建议（受访者主动提出）
1. **停电对账单的影响投影**：若是计划性停电（如 4–5 小时），希望给出该停电会如何影响账单/用电来源的预测（更多用电池或太阳能等），给一个"因为这次停电，你大概会产生这样的账单"的 projection。
2. **支持多辆车 / 多 EV**：很多家庭有多辆车（两辆 Tesla，或 Tesla + 其他电动车很常见，他自己家就是两辆 Tesla），希望能添加并分别展示多车的充电时间安排。
3. **工作日 / 周末 + 上班日程**：例如一周 3 天去办公室、2 天在家，去上班的日子（如 9am–5/6pm 不在家）无法享受白天太阳能，应据此调整充电安排——"this is the time frame... when I am at work... I can't really use the benefits of the solar"。他强调这是普适大参数（多数人每周回办公室几天）。
4. **休假 / 出差模式**：每月可能出差/旅行 3 天到一周，车闲置在车库不需充电，应能据此调整安排、进一步省钱。

### 与现状对比
- 目前**没有**用任何同类第三方 App。
- 现状是分用两个 App：PG&E App 看用量，太阳能 App 看发电/用量——"I don't have any integrated app like this... where I can see everything in a single place"。本产品的"单一整合视图"相对其现状是明确空白点。

### 购买 / 付费意愿信号
- **未涉及**付费意愿、价格敏感度、愿付金额等。访谈者未问，受访者未提。
- 间接信号：自身账单极低（年 true-up $60–$70），可省空间有限，落到自身价值时犹豫——对付费转化偏弱。
- 愿意在产品上线后参与试用（"I would love to like test that"），并认可补偿/激励；但也直言当前功能"things very limited / just few things"，建议补足更多场景与测试用例。

## 关键金句
- "I don't have a battery... I just have the solar setup and the EVs." —— Kingshuk Roy
- "if someone has a solar and the battery. So in that particular scenario like this bill seems to be like kind of pretty high already like the 200 or 170 or something." —— Kingshuk Roy
- "a user might have a like a very old like dryer or old washing machine, old fridge. So that might be consuming a lot of electricity. So you're just just looking at the EV vehicles only right now." —— Kingshuk Roy
- "this is really nice. I like this like kind of the explanation of this one." —— Kingshuk Roy
- "I don't have any integrated app like this like kind of where I can see everything in a single place." —— Kingshuk Roy
- "there are many houses households like there where there are multiple cars... two Teslas like in a particular household like that's pretty common cuz in my household also I have the same." —— Kingshuk Roy
- "if I have to go to work like weekly three days... this is the time frame... when I am at work... I can't really use the benefits of the solar thing." —— Kingshuk Roy
- "maybe one more thing you can add like some vacation thing also... your car might be just at home only like you don't need the charge for one week of a month." —— Kingshuk Roy
- "things very limited like just few things." —— Kingshuk Roy（对当前功能覆盖面的评价）

## 行动项 / 机会点
- 计算说明 / 可审计的成本溯源是最受欢迎的功能点，值得作为核心卖点强化。
- 强需求：支持多辆 EV（一户两车场景普遍，受访者自身即如此），当前单车假设是明显缺口。
- 强需求：把"用户日程"纳入充电优化——工作日/周末、上班日（不在家）、出差/休假（车闲置一周）等场景，会显著改变能否用上白天太阳能。这是受访者反复强调、讲得最具体的一点。
- 停电场景可扩展：从"如何应对停电"延伸到"计划性停电对账单的影响投影"。
- 价值-人群匹配风险：对已主动优化、账单极低、且无电池的太阳能老用户，本产品的省钱价值有限；这类用户更可能被"整合单一视图"和"成本可解释/可审计"吸引，而非省钱额度。建议在定位/付费设计时区分人群。
- 转录纠错记录（不改原始 .txt）：
  - "PGNA" → PG&E（电力公司）
  - "AM2 / AM3 policy" → 推断为 NEM 2.0 / NEM 3.0 净计量政策（访谈者口述，受访者本人未明确政策名）
  - "till you rate plan" → TOU（time-of-use / 分时电价）计划
  - "spam panel" 类术语本次未出现；"power wall" 保留（特斯拉 Powerwall）
- 不一致信号：受访者口头多次认可（"covers everything" / "really nice"），但落到自身实际收益与价值时明显犹豫、只能勉强找出一个有用点，且自评功能"very limited"——表态正面、实际价值匹配偏弱。
