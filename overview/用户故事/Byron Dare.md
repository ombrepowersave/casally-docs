# 用户故事：Byron 要一份能对峙 PG&E 的证据

> 改写自 Byron Dare 的三场访谈：[s1 用户痛点](../../interviews/s1-pain-point-interviews/Byron%20Dare-pain-point.md)、[s2 Demo 1.0（2026-01-21）](../../interviews/s2-demo-1.0/2026-01-21-Byron%20Dare-demo.md)、[s3 Demo 2.0（2026-02-04）](../../interviews/s3-demo-2.0/2026-02-04-Byron%20Dare-demo.md)。
> ✅ **高质量验证场次**：同一用户跨三轮（痛点 → Demo 1.0 → Demo 2.0）追踪，痛点具体、量化、带强情绪，付费意愿明确且言行一致——是证据强度最高的几个样本之一。所有事实、金额、原话均来自访谈，未作外推。

## 画像速览
- **谁**：Byron Dare，**律师，自认完全不懂电**（"I'm just a regular user lazy person... no electrical training"）。
- **房子**：北加州、靠近旧金山（San Bruno 一带），自 2013 年居住；属第二套房，**约半年空置、平时仅 1 人**，圣诞还会连续两周没人。约 2300 平方英尺。
- **装备**：**17 块太阳能板（含 9 块 Tesla Solar Roof）+ 2 块 Tesla 电池 + Tesla EV**；供电 PG&E，账单还涉及 Peninsula Clean Energy（CCA）。
- **账单**：从 8 块板时的近乎 $0/月，涨到 17 块板 + 2 电池后约 $200/月、一度超 $400；最近一张约 **$1,300，其中约 $1,100 是 true-up**。

## 故事
Byron 是个律师，但一碰到电费就彻底没辙——他反复强调自己"不是电工，就是个普通消费者"。

按理说，他该是最省电费的那种人：北加州一套 2300 平方英尺的房子，**一年有一半时间空着**，平时也只有他一个人住，圣诞还会连续两周没人。他先装了 8 块太阳能板，账单立刻降到"有时一个月 $0 或 $10"，每年还能拿一两百块回扣。

可后来他加建房子、把板子加到 **17 块、又上了 2 块 Tesla 电池**——**账单不降反升**，涨到一个月约 $200，一度超过 $400，最近一张干脆到了 $1,300，其中 $1,100 是年度 true-up。最让他想不通的是：**Tesla App 明明显示他几乎每天都在往电网送电，PG&E 的账单上却看不到对应的积分。** "Tesla 说我在往 PG&E 送电，但他们一点积分都不给我。"

而他完全无从招架。PG&E 的账单足足 8 页、满是缩写，"你简直得是个电工才看得懂"；两个客服直线电话和邮箱他打了、留言了、发了邮件，**没有一个人回他**；湾区连个营业厅都快没了；他投诉到 CPUC，对方问完 PG&E、听 PG&E 说一句"正常"，就结案了。他被卡死在"我知道有问题，却不知道该拿着数据去找谁"。

然后他看到了 Casally。打动他的不是省钱数字——而是**数据本身**。当画面把充电、太阳能发电、用电量摆出来时，他说：

> "我喜欢这个。这样我就能拿到充电、太阳能发电和用电这些数据了——**这些我在别的任何地方都拿不到**，真的很有帮助。"

到了 Demo 2.0，最戳中他的是 **Bill Proof（账单核对）**：把"设备侧该是多少"和"账单侧实际是多少"并排摆、标出对不上的地方。对一个正被"账单说我用电多于发电、却没人解释"困住的人，这给了他一个**起点**，更给了他梦寐以求的东西——一份**能拿出去给别人看、拿去和 PG&E 理论的证据**。"至少我能把这个拿给某个人看。"因为光是投诉，PG&E 只会甩一句"事情就是这样"。

他想要的最终形态很清楚：**接入 Tesla 数据 → 按每千瓦时费率反算"账单应该是多少" → 和实际账单逐项对账 → 生成一份可打印的证据**，让他能拿着它去 PG&E "揪住某个人"据理力争；而且因为术语他接不住，他还需要 App 在对话时**引导**他。他甚至愿意为此一次性付几百美元，在 Demo 2.0 里也明确说："这值得订阅——因为这些数据我别处拿不到。"

## 一句话总结
> Byron 的痛点不是"想省几块钱"，而是"我装得更多，账单反而更高，Tesla 说我在发电、PG&E 却不认账，而我看不懂账单、也找不到人"。Casally 对他的价值，是把分散在 Tesla 与 PG&E 两边、他自己永远对不上的数据，变成**一份看得懂、算得清、能拿去对峙的证据**。

## 拆成敏捷用户故事（验收视角）
- **作为**一个怀疑被错误计费的太阳能 + 电池用户，**我想要**把 Tesla 的上网发电数据和 PG&E 账单的积分逐项并排、标出对不上的地方，**以便**我拿到一个能 challenge PG&E 的起点。
- **作为**一个看不懂 8 页账单的非技术用户，**我想要**把 NEM、transmission charge 等术语翻译成人话、并用清晰的数学说明每一笔，**以便**我知道自己到底为什么被收这么多。
- **作为**一个客服永远联系不上的房主，**我想要**一份带数据来源、可打印的报告，**以便**我能拿着它去 PG&E / CPUC 据理力争，让对方没法一句"正常"敷衍我。
- **作为**一个在对话里接不住 kWh 等术语的人，**我想要**App 在我与 PG&E 沟通时给我引导/话术，**以便**对方一上专业名词时我不会被噎住。
- **作为**一个长期不在家、靠 Tesla 电池做停电备份的房主，**我想要**记录并告诉我停电时 Powerwall 到底有没有接管供电，**以便**我能拿这个去找 Tesla 修。
- **作为**一个"问题修好就不想再持续付费"的用户，**我想要**以一次性费用（约 $700 量级）解决问题，**以便**我不被当成又一个按月订阅。

## 关键金句
- "I went from like zero with eight panels to $200 with 17 panels and two batteries... I don't know what's really wrong." —— Byron Dare（s1）
- "Tesla says I am sending it back to [PG&E], but they're not giving me any credit." —— Byron Dare（s1）
- "my bill is like 12 pages long every month... you really have to be an electrician to understand it." —— Byron Dare（s2）
- "this would be worth subscribing to ... because I'm not getting the data from other places." —— Byron Dare（s3，付费意愿）
- "at least I could show that to somebody." —— Byron Dare（s3，Bill Proof 作为对外证据）
- "if I have the data then it's harder for PG&E to just say everything's okay." —— Byron Dare（s2）
- "I'd rather just pay a like a 700... couple hundred bucks then and solve the problem." —— Byron Dare（s1，偏好一次性付费）

## 数据强度备注
- **高**：跨三轮访谈、痛点高度一致且量化（$0→$200→$400+→$1,300）；付费意愿明确（一次性数百美元 / "worth subscribing"），言行与情绪一致。
- **需留意的偏差**：他的强需求**高度个人化**（怀疑被错误计费），不一定代表普通用户；其"喜欢"常是有条件的（每次正向评价后都会补一句"但不知道这会不会反映到账单上"）。把 Byron 当作 **"Bill Proof / 计费证据"这条价值线的代表用户**最贴切，而非通用省钱用户。
