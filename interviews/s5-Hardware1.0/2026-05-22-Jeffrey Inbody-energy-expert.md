# Jeffrey Inbody · 专业咨询（合规认证：FCC / NRTL / 安规）· 2026-05-22

## 受访者画像
- Jeffrey Inbody（访谈中互称 Jeff），美国合规/认证专家，自称非"换电/能源"专家而是"certification expert"，长期处理把电子硬件合法引入美国市场的认证流程。
- 近年实操最多的两家 NRTL 是 **Intertek（原文转录为 "Intertech"）** 和 **Nemko（原文转录为 "NMCO" / "NEMCO" / "NEM KO"）**；早年也与 UL、CSA 合作过（近年没用过）。
- 受 Casally（采访者 Amber Fu）邀请，就一款"家庭用电监测 + 负载控制"硬件的赴美认证路径做咨询。访谈约 1 小时 40 分钟（计时至 01:42:33）。专家末尾主动表示后续可继续作顾问/合作，并答应邮件发 FCC Covered List 链接。
- 采访者一再声明自己"不是认证专家、来学习"，并主动透明告知制造地与产品形态，以便专家给准确判断。

### 被咨询的产品（Casally 设备，采访者反复强调"非常早期"）
- 采访者自述定位：帮助美国（尤其加州）有太阳能 / 电池 / EV、电价结构复杂（采访者口述为"California N3"，即加州 NEM 类电价；**原文只说 "N3"，未完整说出 NEM 3.0，此处不作展开**）的住宅理解并削减电费；已有 App，想从"可信建议"走向"自动执行"。
- 设备装在自家配电箱（electrical panel）附近，用 CT 电流钳（采访者口语反复说 "city clamp"，**应为 CT clamp / current transformer clamp，转录听错**）实时监测**全屋用电**，带 Wi-Fi 连 App + 云，并有控制功能，可基于可用容量与电价开关/限流 EV 充电器等大负载。采访者把它类比为"Emporia 能源监测器 + 充电控制器，但 Wi-Fi/App 控制"。
- 采访者明确：**不是**整屋智能配电盘（smart panel），**不是**太阳能/市电之间的转换开关（transfer switch），不在初期控制屋内一切，只做负载侧（load-side）需求管理；首版主要可控负载是 **EV 充电**。
- 系统设想为最多三件硬件：① 监测网关（gateway，含 PCB + Wi-Fi 模块 + 云/App 连接）；② CT 电流钳（有线接回网关，无独立 Wi-Fi/处理器，定位为网关的"配件/传感输入"）；③ EV 充电控制路径——采访者列出三种可能：(a) 纯软件/云 API 控充电器，(b) 装在充电器侧的第三方负载控制器（继电器/接触器类），(c) 用本就支持负载管理的智能充电器，由系统发指令。三选一尚未决定。
- 制造地大概率在亚洲（很可能中国，尚未定），目标市场为**美国本土（US-only）**。

## 主题判定
判定为**专业咨询（energy-expert / 合规认证）**，依据：
- 文件目录 `s5-Hardware1.0`（硬件）为初判，但**正文为准**：整场不是在描述某个硬件设备的型号/集成现状（hardware 维度），而是一位**外部认证专家**系统性输出 FCC 授权、NRTL 安规、测试地点政策、加州 Prop 65、DOE 能效、FCC Covered List 等**专业判断与建议**。
- 内容与 energy-expert.md 的"合规/认证路径""监管/门槛与成本""专业观点/建议""风险/坑"等维度高度吻合，故保留 `energy-expert` slug（本项目映射中"能源专家"泛指此类专业咨询）。

## 核心提炼

### 一、FCC 授权（FCC authorization）—— 法律强制
- **术语**：FCC authorization 即 FCC 授权该产品可在美国 import、sold、used。两条路径：**Certification**（正式认证）与 **SDOC**（Self-Declaration of Conformity，自我符合性声明）。
- **核心打法（专家强烈建议）**：采购**本身已带 FCC 认证的射频模组**（module-level certification）。例如 **Espressif（原文转录为 "ExpressF" / "Express if"）ESP32 系列**绝大多数已通过 FCC 认证。模组级认证意味着该模组已做过 EMC 测试 + 射频测试（功率、天线发射、频段都在允许范围内）。
  - 选模组时务必查 datasheet 或直接问销售："does it already have FCC certification?"
  - 好处：你只需对**最终整机（监测网关）做 EMC 测试**，不必重做射频部分。
- **EMC 两类测试**：
  - **Radiated（辐射）**：经空气散发多少不该有的能量。
  - **Conducted（传导）**：经连接线缆（如经外置电源回到 AC mains）传出多少不该有的能量。网关本体多为 DC 设备，但通过 AC-DC 外置电源接市电，FCC 要确保该线缆不外泄多余能量。
- **整机用 SDOC 自我认证**：射频模组**必须**有 FCC 许可才能在美销售/使用；**EMC 不需要 FCC 许可**，可走 SDOC。理论上自有设备/经验可自测，但实际几乎都外包第三方——公司即便有电气工程师，通常也没有 EMI 暗室和此类测试经验。
- **配件（CT 钳）须一起测**：钳子作为 accessory，FCC 测试时必须接上一起测。

> "you really want a module that already has FCC certification." —— Jeff
> "FCC authorization means just like the word implies, authorization. It means that the FCC is authorized it to be uh imported, sold, and used in the United States." —— Jeff

### 二、测试地点政策（中国测试实验室是否还能用）—— 反直觉重点
- 临近变化：FCC 有些**小改动约 6 月 1 日生效**；另有一批**更重大的拟议规则（proposed）**。但只要用**已认证射频模组**，对 Casally 基本无影响。
- **"China ban" 的真相**：拟议规则**条文里没有 "China" 字样，不是中国禁令**。其实质是 FCC 拟**不再允许在没有 MRA（Mutual Recognition Agreement，互认协议）的国家的实验室做测试**。
  - 历史：约 2015 年前 FCC 要求测试须在美国或有 MRA 的国家完成；2015 后放宽，只要实验室能证明自己 reputable，全球任何国家（专家举例 Sri Lanka、Uganda、Belize 等）都可获批。拟议规则是**退回旧标准**。
  - 有 MRA 的国家（专家凭记忆列举）：加拿大、欧盟及部分欧洲国家、一两个拉美国家，以及亚太的台湾、澳大利亚、新西兰、（专家"我想还有"）越南等。**中国不在 MRA 名单上**，故受影响最大。
- **关键缓冲**：该限制**只影响 radio certification（正式射频认证，更"formal"），不影响 EMC**。EMC 走 SDOC（很不正式、自我声明），**不受影响**——**只要用已认证模组，仍可在中国做 EMC 测试**。

> "a lot of people talk about it being a China ban. It's not. Um there's no language in the proposed rule that specifically says China." —— Jeff

### 三、EMC 测试成本（地点差异巨大）
- 用已认证模组、无需重测射频时，监测网关的 **EMC 测试在中国约 \$500–\$750 美元**。
- **同样测试在美国约 \$45,000 美元**。
- （注：采访者后文复述成本时口误为"five to 75 uh \$100"，专家原始报价为上面的 \$500–\$750；以专家原话为准。）

### 四、NRTL 安规认证（UL / Intertek 等）—— 法律不强制，但市场强制
- **法律上不强制**：制造商**无需** NRTL 即可合法 import/sell；美国海关不查 NRTL。但**客户和市场会要求**。
- **背后的监管逻辑（OSHA）**：OSHA（Occupational Safety and Health Administration，职业安全与健康管理局）只管**雇主/工作场所**（如电气公司、餐馆、仓库等有雇员的商业实体），**不管普通住宅消费者**（房主一般不是雇主）。OSHA 认定电气设备"安全"的方式就是要求有 **NRTL 认证（如 UL）**。
- **NRTL 机构**：UL、Intertek、**Bureau Veritas（原文转录为 "Bureau Veritoss" / "Veraritoss"）**、TÜV、Nemko、CSA 等，全美约 **12–13 家**。
  - **机构名 vs 认证标志（mark）名**常不同：UL 的标志叫 UL；Intertek 的标志叫 **ETL**；Eurofins（原文 "Euro Fins"，**存疑**）的标志专家记为 **"MEPS"（专家自述"我想是"，不确定，存疑）**。
  - 专家近年主用 **Intertek、Nemko**；UL 是 "gold standard"、最广为认可，但更贵、更不灵活；其他家价格更好、更灵活。
- **安规测试标准**：网关本体测 **UL 62368-1**（专家称 UL/Intertek/Bureau Veritas 都会按 62368-1 测）。因有 CT 钳配件，**可能**还需额外标准，但专家明确**不愿凭空猜该额外标准编号**（"I don't even want to guess"）。

> "let me start by saying that legally you as a manufacturer um you don't have to have that... but your customers are going to demand it." —— Jeff

#### NRTL 费用结构（专家给的具体数字）
- **第一部分（测试 + 报告 + 证书）**：约 **\$14,000–\$15,000 美元**——提供样品到其实验室，出测试报告与官方证书。
- **第二部分（使用 mark 的年费）**：按年收（实际按季度开账单）。
  - 美国制造：约 **\$5,000–\$6,000/年**。
  - 中国制造：约 **\$8,000/年**（即约 \$2,000/季）。
- **标签/标志费（最多两项额外费）**：监管标签（regulatory label）须含公司名 / 品牌名 / 型号（型号要与测试报告一致，用于追溯）。
  - 自厂印刷 mark **vs** 向 NRTL 买标签，**盈亏平衡点约 2,000 台/年**：≲2,000 台/年买标签更划算（约 **\$1/张**）；≳2,000 台/年自印更划算（自印权利费约 **\$2,000/年**，即便自印 NRTL 仍收费）。
- **总体判断**：量小不可行（年产 50 台分摊不动约 \$20,000 成本，得每台加几百美元）；年产十万台时 \$20,000 不算什么；两三千台"manageable 但仍 expensive"。专家断言"I don't see any way around it for you"。

### 五、销售渠道 → 是否需要 NRTL（关键决策依赖）
- **认证流程本身不随"仅监测"还是"监测+控制"大变**；真正决定成本的是**有几件需独立认证的硬件**（两件 / 三件 / 更多）。
- **直接卖给现有房主（D2C）**：法律上可只先做 FCC、延后 NRTL，海关不查。**但专家强烈不建议**，两大风险：
  1. 房主若需专业维修，本地电气公司看不到 NRTL/安全标志，**可能拒绝施工**（"this thing doesn't have a marking that proves it's safe. We're not allowed to work on it."）。
  2. 你**无从证明产品安全**（是否按 UL 62368-1 测过、会不会起火烧房）→ 一旦起火即面临诉讼、口碑/社媒崩塌。
- **新建房 / 卖给开发商（home builder）**：开发商是雇主 → OSHA 介入；建房过程有政府电气验收（通常在 drywall 封板前、线缆/conduit 仍可见时），电工/验收员会找 NRTL mark，**必须有 NRTL**。
- **房主 DIY**：OSHA 不管房主，也不管作为制造商的你；但存在**建筑/许可/电气验收员**风险——既有住宅自住一般无人来验，**翻新或新建**时验收员可能在封板前看到钳子、因无 NRTL mark **判验收不通过**。
- **专家总论**：能否只做 FCC 先上？"Yes（法律上可）。" 是不是好主意？"No。"——最终**应当/必须拿 NRTL**。

> "can you do it? Yes. Is that a good idea? No." —— Jeff

### 六、CT 电流钳的安装现实 —— 专家反复强调的"最大问题"
- 美国单户住宅的**进户主馈线（service entrance cable）几乎都在墙内、藏在 drywall 后**：约两根粗热线（各约 120V、约 200A、约 3 号线径）、一根稍小中性线、一根更小地线，都走在 conduit（穿线管）里。
- 因此**普通房主几乎无法 DIY 装钳子**：要锯开 drywall 又不能锯到管内带电导线（误锯可致命），还要复原补墙（补 sheetrock、taping、mudding、floating）——多数房主会请人。采访者提到曾有电工说"有些美国家庭自己装、觉得请人太贵"，专家回应：若是 D2C 自购自装，房主自装不违法、OSHA 也不管，但现实中多数人不愿动墙，仍会请人。
- **装进配电箱（panel）里？**：理论可行但**风险大增**——普通住宅主箱**通常无法整体断电**，打开内盖即暴露带电主线；不建议引导房主开内盖；专家警告"somebody's going to get killed and you're going to get sued"。
- **两个"最大问题"（专家点名为收尾时的核心症结）**：
  1. **钳子到底装在哪**；
  2. 若装在 panel 内，**引线如何引出**——在钢制封闭 panel 上钻孔=给火灾留逃逸通道（panel 本应在内部短路/跳闸时封闭），且内盖/箱门还得合上，线根本出不来。
- **表前（meter 之前）一律不能动**：meter 之后归房主、meter 之前归电力公司；若在电力公司设备（如户外进线 conduit）上装钳子，可能被发现并**断电**。架空进线常经屋顶 conduit 进入，"几乎无法在那里装钳子"。

> "I don't see any way you're going to be able to get that on an area of the house that the homeowner owns, which again, that's everything behind the meter. And again, that that's almost always going to be in the wall." —— Jeff
> "when you start drilling a hole in the panel to bring a wire out, you know, that that's going to be a problem." —— Jeff

### 七、CT 钳的认证归属
- 钳子无独立 Wi-Fi/处理器、有线接回网关 → 专家认为**可作为网关的 "required accessory"**，归入网关那一套认证：FCC 测试需带它一起测；NRTL 也可作为必备配件捆进同一证书包。
- 因此当前从认证角度**只有一件产品**（网关 + 钳子配件）。未来若软件控不了 EV、需第三件硬件，则那件需**独立认证**。

### 八、第三件硬件（EV 负载控制）
- 若 EV 充电控制能纯软件实现（充电器自带云/API 联网）→ 不需第三件硬件，认证范围基本不变。
- 若必须加硬件（介于充电器与 AC mains 之间的限流装置，可能 240V）→ 该件**独立认证**：流程同网关，仍优先用已认证射频模组（多半是 Wi-Fi/蓝牙 IoT），只做 EMC；且因接 AC mains（≥120V），**务必做 NRTL**（否则可能致人伤亡或火灾）。
- 该限流硬件可**复用于其他大电流设备**；不同电压（120V/240V）可能需适配板（adapter plate）。

### 九、早期试点（20–40 户 beta）是否需要认证
- 内部原型/自测：不需 FCC（也无法在没有成品前拿 FCC/NRTL）。
- **向用户收费即必须先有 FCC**："If you're charging any money, you're going to have to have FCC certification."
- 若**完全不收费** + 有**书面协议**（写明：非卖品、尚未 FCC 认证、仍在开发、用户作为开发团队提供反馈）→ FCC 角度可豁免做 beta。
- **NRTL/安全仍应提前有**：理由是保险——若 beta 设备起火烧房，保险公司调查发现是"未做安全测试、接市电的 beta 设备"，**很可能拒赔**；房主转而追索制造商（在华则美国消费者起诉难，但仍会上社媒）。专家确认"听说过未经测试的电气设备烧房"的案例；并指出即便有 NRTL，房主仍可能来索赔，最终是制造商赔。

> "is your you know product going to burn down you know 500 houses or one house it really doesn't matter." —— Jeff

### 十、BOM 受控清单（FCC Covered List）
- FCC "Covered List"（原文转录为 "covery list" / "covered list"）上**仅约 10–14 家**亚洲公司（外加一两家俄罗斯公司）。专家举例提到"那家大型安防摄像头公司"（专家说成 "Huei"，**疑指华为 Huawei；但'大型安防摄像头公司'更贴近 Hikvision/Dahua，专家发音含糊，此处存疑、不当作确定事实**）。
- 关键判断：这些公司**多是成品制造商，不卖元器件**（不产射频模组、电容、电源、电阻）。只要你自研设计、由自己/代工厂采购零件组装，**基本不会踩雷**。可 Google "FCC covered list" 查实名单（专家不确定该清单是在 CFR/US Code 还是 FCC 其他文件中）；专家答应邮件发清单链接。

### 十一、其他易被忽视的合规项（专家收尾主动补充）
- **加州 Proposition 65**：不禁用化学物质，但若用到清单上约 **1,000 种**化学品（或超过某限值）须加**警示标签**（如"含铅，加州认定致癌"）。重点是重金属（铅、铬、六价铬 hexavalent chromium）与**塑化剂（phthalates，塑料软化剂）**。**钳子很可能含铅/超限**——但非世界末日，**向客户披露即可**。清单公开可下载（CSV/Excel，约一千行）。化学检测在中国约 **\$400–\$500 美元**。
- **外置电源（AC-DC adapter）**：网关多用类似手机/笔记本的外置电源。采购时务必选**本身已带 NRTL 认证**的电源（市面成千上万款现成的，别自己花钱去认证）；并向电源厂索要：① FCC SDOC；② 加州 Prop 65 声明；③ NRTL 认证证明；④ **美国能源部 DOE Level VI 能效标志**（电源在美须至少 Level VI，电源上须印罗马数字 VI 标志）。

## 关键金句
- "you really want a module that already has FCC certification." —— Jeff（采购自带 FCC 认证的射频模组是降本关键）
- "if you do it in the United States, it's going to be $45,000." —— Jeff（同样 EMC，中国约 \$500–\$750，美国约 \$45,000）
- "a lot of people talk about it being a China ban. It's not. Um there's no language in the proposed rule that specifically says China." —— Jeff
- "legally you as a manufacturer um you don't have to have that... but your customers are going to demand it." —— Jeff（NRTL 法律不强制、市场强制）
- "can you do it? Yes. Is that a good idea? No." —— Jeff（只做 FCC 跳过 NRTL 先上市）
- "I don't see any way you're going to be able to get that on an area of the house that the homeowner owns." —— Jeff（钳子安装是最大现实障碍）
- "is your you know product going to burn down you know 500 houses or one house it really doesn't matter." —— Jeff（小规模 beta 同样需要安全保障）

## 行动项 / 机会点
- **优先决策钳子安装方案**：专家点名的两大死结之一。"全屋监测 + 绕主馈线"的钳子在美国住宅几乎无法 DIY、装箱内又有引线引出/钻孔/合盖三重难题——需重新评估传感方案（位置、是否专人安装、引线出箱方式）。
- **射频选型即合规策略**：BOM 锁定**已带 FCC 认证的射频模组**（如 Espressif ESP32 系列），把整机降级为只需 EMC + SDOC，并使中国 EMC 测试在 MRA 新政下仍可行。
- **EMC 测试放中国**：约 \$500–\$750 vs 美国 \$45,000；SDOC/EMC 不受 MRA 新政影响（前提：用已认证模组）。
- **NRTL 不可省**：尽早规划 UL 62368-1 测试，预算第一部分约 \$14k–15k + 中国制造年费约 \$8k + 标签费；机构可优先评估 Intertek / Nemko（性价比/灵活），UL 作高认可度备选；CT 钳大概率可作配件捆进同一证书包，但可能另需一项尚不确定的额外标准。
- **渠道与认证绑定**：若坚持 D2C 现有房主可"先 FCC 后 NRTL"过渡，但须接受维修受阻 / 安全无背书 / 翻新验收风险；任何涉及新建房 / 开发商渠道则 NRTL 前置硬性必备。
- **beta 试点合规**：免费 + 书面协议可暂缓 FCC；一旦收费必须先 FCC；NRTL/安全因保险拒赔风险建议仍提前具备。
- **采购合规清单**：外置电源须自带 NRTL + DOE Level VI + FCC SDOC + Prop 65 声明；BOM 比对 FCC Covered List（约 10–14 家，多为成品商，风险低）；做 Prop 65 化学检测（钳子大概率含铅，披露即可，中国测约 \$400–\$500）。
- **顾问关系**：专家明确表示后续可继续作认证顾问，并将邮件发送 FCC Covered List 链接（已确认采访者 Gmail 邮箱）。建议建立长期咨询合作。
