# 用户故事：Donald 受够了三个各管各的 App

> 改写自 Donald Rhesa 的三场访谈：[s1 用户痛点](../../interviews/s1-pain-point-interviews/Donald%20Rhesa-pain-point.md)、[s2 Demo 1.0（2026-01-20）](../../interviews/s2-demo-1.0/2026-01-20-Donald%20Rhesa-demo.md)、[s3 Demo 2.0](../../interviews/s3-demo-2.0/Donald%20Rhesa-demo.md)。
> ✅ **高质量验证场次（范围界定）**：跨三轮的回访用户，痛点具体、可量化、带强画面感（风暴预警手动 override 的故事是整个语料中最生动的之一）；Demo 反馈有真实的批判性（月度预算真卡壳、拒绝静音功能、坚持要 why + dollar impact），不是纯捧场。**两处需打折**：① s2/s3 整体有捧场倾向（几乎每个功能都说 nice/very good）；② 付费意愿仅到"愿意合理月订阅"，被问到具体金额时未作答（**WTP 价格点未验证**）。所有事实、原话均来自访谈，未作外推。

## 画像速览
- **谁**：Donald Rhesa，**数据分析师**，和妻子住在**南加州 Riverside** 的三居室独栋；家里还有一位**保姆**和两个儿子，**白天主要是保姆 + 两个儿子在家用电**。自我定位"愿意尝试但**不是早期采用者**"。
- **装备**：**Tesla Powerwall 2 + 一辆 Chevy Equinox EV（计划再添一辆）+ 太阳能**（现状与"还在规划"略有不一致）+ 智能电表 + 智能温控。
- **费率**：分时电价（TOU），峰时约晚 8–9 点起、9 点后转低。
- **账单**：装 Powerwall 前每月数百美元；装后**几乎减半、没有哪个月超过 $200**。

## 故事
Donald 是个数据分析师，和妻子带着两个儿子、还有一位保姆住在南加州 Riverside。他不是抱怨电费的人——装了 Powerwall 之后账单几乎砍半，他对"性价比"挺满意。真正折磨他的是另一件事：**家里的能源被三个互不通气的 App 各管各的。**

Tesla App 管 Powerwall，Chevy 的 App 管那辆 Equinox，PG&E 的 App 看账单和费率提醒——"它们各在各的筒仓里"。平时还能靠肌肉记忆凑合，可一遇到事就露馅。他讲了去年冬天最具体的一次：**收到风暴预警**，他既想把电池保持 100% 做备份，又得给车充好电准备一趟出行，于是只能**在两个 App 里分别手动覆盖日程，还在脑子里算峰时之前到底够不够电网的电**。他说："为什么这些东西就不能自己协调一下？电池知道风暴要来，就该告诉车去充电——这就是我发现的那个痛点。"

而且时机总对不上。系统提示晚上 8、9、10 点该充车，可那时他人不在家；等半夜到家发现今天没充，要么通宵补、要么自己估"还得多久充满"，第二天要早起就很赶。收到 PG&E 的 flex alert 时，他更是只能**满屋子跑着关电器**。

他想要的其实很清楚：**一个把家庭能耗、电池状态、EV 充电计划、还有任一公用事业的实时电价全汇到一处的面板**；能用大白话设目标——"把月账单控制在 $150""永远保 3 天备份电"——剩下的让系统自己跨设备去实现；来客人时还能临时把上限放宽到 $200–$250。收到 flex alert 时，温控、电池、EV 充电器能自动一起进省电模式，而不是他人肉去关。他不在家时，系统能察觉并自动平移充电窗口，或者把"现在最适合洗衣/洗碗"的提示**下发给保姆**。对失控他不担心——"就像有人牵着我的手指方向，反正最后命令是我来执行"。在"省钱 vs 减负"之间，他明确"**省钱第一**"。

到了 Casally Demo 2.0，最反复打动他的就是"**把一切汇到一个屋檐下**"带来的"心理安慰、减轻心理负担"。他也没有一味叫好——月度预算那块他真卡住、说了句"This doesn't make sense"，要团队解释半天才通；他还拒绝了"静音通知"功能，嫌是 overkill；并坚持每条提示都要有 why 和 dollar impact。但走查到最后，他给了一句整体评价：

> "UI 本身非常易用，即使是新手也能轻松上手。设计和用户体验也很棒——你只需要在不同标签页之间切换，就能轻松找到下一步所需的所有信息。所以，真的要给 Casally 点赞。"

## 一句话总结
> Donald 的核心痛点不是电费高，而是**三个互不通气的 App 把协调的活儿全压在他脑子里**——风暴时要手动 override、不在家时时机对不上、flex alert 来了只能满屋关电器。Casally 对他的价值，是当那个"把一切汇到一个屋檐下、替他协调、只要他确认"的决策层。产品方向与痛点验证质量高；但他对 Demo 偏捧场、付费只到"愿意订阅"未到价格，需复测。

## 拆成敏捷用户故事（验收视角）
- **作为**一个被 Tesla / Chevy / PG&E 三个 App 拖累的用户，**我想要**在一个面板里看到家庭能耗、电池状态、EV 充电计划和任一公用事业的实时电价，**以便**我不必在脑子里跨 App 协调。
- **作为**一个不想做脑算的房主，**我想要**用大白话设目标（"月账单控制在 $150""保 3 天备份电"）、并能临时调整，**以便**系统跨设备替我求解怎么实现。
- **作为**一个收到 flex alert 就满屋关电器的用户，**我想要**温控、电池、EV 充电器能自动一起进省电模式，**以便**我不必人工奔走。
- **作为**一个常不在家、充电时机总对不上的车主，**我想要**系统察觉我不在家并自动平移 EV 充电窗口，**以便**调度不再靠我记忆。
- **作为**一个家里有保姆/家人帮忙的房主，**我想要**把"现在最适合做家务/充电"的提示共享给家庭成员，**以便**不在家时也有人按最优时段执行。
- **作为**一个会被风暴打乱备份计划的电池用户，**我想要**至少提前一天收到风暴/停电预警并附行动建议，**以便**我从容把电池充满、安排好出行。
- **作为**一个有电池、想在高峰回售电网的用户，**我想要**回售过程自动化且收益清晰透明，**以便**这笔激励不再是一笔糊涂账。

## 关键金句
- "honestly at the beginning it was a mental load of having different apps that don't talk to each other... they are all in their own silos." —— Donald Rhesa（s1，核心痛点）
- "last winter during a storm alert... I had to manually override schedules in two different apps calculating in my head if I had enough grid power before peak rates." —— Donald Rhesa（s1，最生动的痛点场景）
- "If I get a text from PG&E about a flex alert I run around turning off things." —— Donald Rhesa（s1）
- "keep my goals in plain English like keep my bill under $150 a month... have the system figure out the most efficient way to make it happen across all my devices." —— Donald Rhesa（s1，核心诉求）
- "saving money is number one." —— Donald Rhesa（s1）
- "the synchronization itself now gives you a kind of that mental comfort. It takes a lot of mental load from the user." —— Donald Rhesa（s3，核心价值认知）
- "This This doesn't make sense." —— Donald Rhesa（s3，月度预算真实卡点——说明并非一味叫好）
- "the UI the user interface itself... actually very easy to use even for a first timer." —— Donald Rhesa（s3，UI 评价）
- "with all these features... I would think it is worth paying for maybe a certain subscription." —— Donald Rhesa（s3，付费意愿——金额未给）

## 数据强度备注
- **痛点（s1）：强**。多 App 各自为政、不在家时机对不上、缺风暴提醒、回售激励不透明——主动、具体、可量化（账单减半），且风暴 override 故事画面感极强。
- **产品方向验证（s2/s3）：强但需甄别**。给出大量有质量的设计取舍（要 why + dollar impact、拒绝静音、连续两次要真人帮助入口、统一时间表"只确认不决策"），但整体捧场倾向明显；月度预算概念**确有理解成本**（需大段解释）。
- **付费（s2/s3）：弱**。愿意"合理月订阅"，但被问具体金额时被打断/未答；价格敏感度未知。
- **代表的价值线**："多 App 整合到一个屋檐下的协调/决策层 + 大白话目标 + 自动需求响应"，以及"家庭多成员协作（保姆/house manager）"。
- **建议**：上线后纳入真实试用群体，用其真实账单补测**具体愿付价位**与是否真正替代现有 App。
