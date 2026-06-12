# 用户故事：Kael 不想再为太阳能掉线满屋子跑

> 改写自 Kael Williams 的三场访谈：[s1 用户痛点](../../interviews/s1-pain-point-interviews/Kael%20Williams-pain-point.md)、[s2 Demo 1.0（2026-01-21）](../../interviews/s2-demo-1.0/2026-01-21-Kael%20Williams-demo.md)、[s3 Demo 2.0](../../interviews/s3-demo-2.0/Kael%20Williams-demo.md)。
> ✅ **高质量验证场次**：跨三轮的深度回访用户，痛点具体、可量化、情绪分层清晰；Demo 反馈区分度高、带真实批判性（最强诉求是"把月预算移出首页"、反复反对依赖预测、被 Bill Proof 夸大差额绊住而动摇信任），不是一味叫好。**需谨慎**：s2 对自动化"认可中带多重前提与戒心"、付费表态以"先跑满 30 天周期、订阅价须低于实测节省"为前提（**绝对价格点未定**）。所有事实、原话均来自访谈，未作外推。

## 画像速览
- **谁**：Kael Williams，**加州**居家办公，作息固定、约 5:30 起床；2015 年购入独栋自住，**一家五口**（本人、妻子、3 个孩子）。
- **装备**：**太阳能（2016 年装，SolarEdge，非 Tesla）+ 一辆 Tesla Model 3 EV，无家用电池、无智能家居中枢**。日常用 **2 个 App：Tesla + SolarEdge**。供电 **Southern California Edison（SCE）**，走 TOU 费率。
- **账单**：装太阳能前约 $149/月；太阳能每年约省 $1,500；每月固定连接费约 $20；**装 EV 第一年 true-up 约 $1,200，现波动在 $800–900**。
- **认知**：访谈前**没听说过 NEM3**（Amber 现场科普），在考虑加装电池但尚未调研。

## 故事
Kael 在加州居家办公，一家五口，作息很规律。他 2016 年装了太阳能、后来又买了辆 Tesla Model 3，本以为能把电费大幅压下去，结果"neither here nor there"——不上不下。

真正折磨他的，是**太阳能逆变器三天两头掉线**。SolarEdge 的逆变器一断网，他就得走到装太阳能板的那一侧、扫 QR 码、再到房子各个角落反复确认有没有恢复——通常半小时，有时长达两小时。去年感恩节前后那次最惨，他正在工作。按客服给的步骤做，能不能修好"是个赌博"，而客服电话又极难打通。最让他难受的是这背后的代价：

> "我真的很想摆脱手动排障。你能想象我为此损失的陪家人时间——我得满屋子跑……可能孩子第一次走路那种时刻，我却在排查能源系统。"

除了排障，**两个 App 的割裂**也烦人：想给车充电，得先开 SolarEdge 看此刻有没有余电，确认了再去 Tesla App 调高充电上限，来回切；偏偏 SolarEdge 对他还有点太技术化。而每天下午 4 到 9 点电价最贵，他只能"go dark"——洗澡要么拖到晚上 11 点、看电影排到 9 点后，还得提醒老婆孩子那段时间少用电。等到年底，true-up 给他当头一棒：装 EV 第一年就是 $1,200，他低估了车的耗电，忍不住问自己——

> "既然账单还是这么贵，我环保图什么？"

他想要的很清楚：**一个覆盖全家能源、家人都能登录的统一看板**，首屏只放三件事——太阳能"生产 vs 消耗"、最佳充电时间、基于实时数据的省电提示，技术细节藏到二级页；最好还能像 Candy Crush 体力满了那样**主动推送**"现在可以充电了"；太阳能掉线能**自动检测、先自己重试两三次再通知**；通知同时发给他、妻子和大孩子，谁在家谁处理。但他坚持要**先确认再执行、不要全自动**（"这带来问责感"），也明确**不信任长程预测**——"我不喜欢依赖预测，我宁愿事情真发生时再实时告诉我"。

三轮看下来，他对 Casally 的认可是稳步建立的。到 Demo 2.0，他点击体验后给了实打实的评价——这版"进步很大、作为起点已经可以上线了"；尤其是事件明细页：

> "这很有用——你知道发生了什么事件、它带来多大影响、是怎么造成的，然后还给你一条下一步该怎么做的建议。所以我觉得它很完整。"

但他也没放过该挑的地方，而且挑得很准。**月度预算他认可概念，却反复、明确地要求把它从首页拿走**——"这是每月只设一次的东西，没必要每次打开 App 都提醒我"，被问"30 天只改一件事改哪个"时他的答案正是这个。Bill Proof 页里 demo 故意放大的差额（费率 0.31 vs 0.83、差近三倍）直接动摇了他的信任——"这差距太大了，难以接受"，即便 Amber 解释是演示数据也没完全消解。他还敏锐点破多成员通知的漏洞：收到通知的人若没有 Tesla 权限，就执行不了更改。

## 一句话总结
> Kael 的核心痛点是**太阳能掉线后只能满屋子手动排障**（最想消除、代价是陪家人的时间）+ 双 App 割裂 + true-up 冲击。他要的是一个**全家共享、自动检测/自动重试、主动提醒、但保留人工确认**的统一能源大脑。他对 Casally 高度认可且区分度高——但同样用力地划清边界：月预算别放首页、别依赖长程预测、别用夸大的示例数据，付费要看跑满一个完整账单周期的真实 ROI。

## 拆成敏捷用户故事（验收视角）
- **作为**一个被太阳能逆变器频繁掉线折磨的房主，**我想要**系统自动检测离线、先自己重试两三次、仍失败再通知我，**以便**我不必满屋子跑着扫 QR 码、打难打的客服。
- **作为**一个在 Tesla 和 SolarEdge 之间来回切的用户，**我想要**一个全家都能登录的统一看板，首屏只放"生产 vs 消耗 + 最佳充电时间 + 实时省电提示"，**以便**我一眼看懂、技术细节藏到二级页。
- **作为**一个充电前要反复查"太阳能够不够"的人，**我想要**像游戏体力恢复那样主动推送"现在适合充电了"（并附实际产出依据），**以便**我不必手动判断和调上限。
- **作为**一个常不在家的家庭决策者，**我想要**关键通知同时发给妻子和大孩子、并能分派小任务，**以便**离设备最近的人能处理——前提是执行者要有 Tesla 权限。
- **作为**一个担心自动化出岔子的用户，**我想要**系统排好计划后由我确认再执行，而不是全自动，**以便**我保留问责感与掌控。
- **作为**一个不信任长程预测的人，**我想要**实时/每日滚动的信号，而不是 24–72 小时的天气预测，**以便**我据实况而非猜测行动。
- **作为**一个每月只设一次预算的用户，**我想要**把月度预算放到设置页、首页只留每次都在变的实时信号，**以便**首页不被冗余提醒占据。

## 关键金句
- "I would want to definitely move away from manually troubleshooting stuff... the time lost with my family... maybe the kids first steps... because I'm trying to troubleshoot the energy grid." —— Kael（s1，最想消除的痛点）
- "why am I going green if my bill is still the same?" —— Kael（s1，true-up 挫败）
- "It's a gamble... they've given you the prescribed steps... but you don't know whether that would happen." —— Kael（s1，排障不确定）
- "I normally wish that we'd have an app that covers my entire home in terms of energy." —— Kael（s1，统一看板诉求）
- "I don't like relying on predictions... I prefer going with the things as they are... informed when it actually happens, in real time." —— Kael（s2，反对长程预测）
- "this is useful because you know the event and the impact it brought and how it brought it. Then you're also given a suggestion on what to do. So I think it is complete." —— Kael（s3，对事件明细页的认可）
- "being that it is something that you said once a month... it is not necessary on the home screen." —— Kael（s3，最强改进诉求：月预算移出首页）
- "this number seems quite big... we should not be expecting such a big discrepancy." —— Kael（s3，被 Bill Proof 夸大差额绊住）
- "let's say you save 50 and the application wants you to pay 60 per month... there will be no need because you will be spending more than what you save." —— Kael（s3，付费 ROI 阈值）

## 数据强度备注
- **痛点（s1）：强**。手动排障（情绪最强、代价具体）、双 App 割裂、true-up 冲击、TOU 牵制家庭生活，均主动、具体、可量化。
- **产品方向验证（s2/s3）：强且区分度高**。给出大量有质量的批判（月预算移出首页、反对长程预测、点破 Bill Proof 夸大差额与多成员通知权限漏洞），证明不是捧场式肯定。
- **自动化/付费：偏审慎**。自动化"认可但带多重前提"，坚持"询问—批准"；付费需先跑满 30 天周期、订阅价须低于实测节省（绝对价格点未定）。
- **代表的价值线**："太阳能离线自动检测/自动排障 + 全家共享的统一看板 + 实时优先于预测"，以及"保留人工确认的半自动充电"。
- **建议**：纳入早期共创/真实试用名单（他明确愿意），用真实账单跑满一个周期来验证省钱效果与愿付价位。
