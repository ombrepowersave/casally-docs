# Simon Asenime · 硬件 · 2026-06-04

> 受访者：Simon Asenime；访谈人：Amber Fu。逐字稿正文标注的对话日期为 "Jun 3, 2026"，文件名日期为 2026-06-04。
> 转录纠错说明：本摘要在不改原始 `.txt` 的前提下，把明显的语音转录错误还原为受访者本意，关键术语首次出现处标注原文写法。

## 受访者画像
- 有太阳能行业从业经历（"back when I was working in solar"），做过 homeowner 上门安装，也接触过 utility scale（公用事业级）项目；目前已离开太阳能行业一段时间（"I've been out of solar for for like a minute now"）。
- 自己搭建有智能家居（"I actually have a smart home myself"），亲手试过 Matter 等协议。
- 工程背景偏 **Ethernet / Modbus**（原文 "Ethernet mode bus kind of guy"），自述对 CT 钳（CT clamps，原文转录为 "Cclamps / city clam / city claim"）的具体端口/协议没在技术层面深入做过。
- 关注行业动态与诉讼案例（"I do kind of follow the court cases in industry"）。
- 自述还年轻、仍在赚钱打拼，未必随时有空，但乐意持续提供建议（"I'm still young myself, so I may not always be available"）。

> Casally 当前方向（由 Amber 介绍，作为背景）：面向加州有太阳能 / 电池 / EV、或电费高的房主，做 App + **轻量小网关**（small gateway，可能带 CT 钳与电表用于全屋 sensing），不做重型 smart panel；目标是解释账单、识别高价行为（如 peak 时段充电）、审计账单错误，并最终推荐 / 自动化降本动作。典型用户痛点：家里有 Tesla、Sunrun、Enphase、Wallbox 充电器等多套系统，"hate juggling like five apps"（受不了在五个 App 之间切换）。

## 主题判定
判定为 **硬件（hardware）** 主题。依据：目录前缀 `s5-Hardware1.0`，且正文几乎全程围绕网关硬件形态、通信协议（Wi-Fi / Bluetooth / Zigbee / Thread / Matter）、设备 API 接入、CT 钳安装、电工 vs DIY、自动化在本地/云端的分层、安全攻击面、放置位置等硬件与集成议题展开。

## 核心提炼

### 1. 协议选型：Matter 不看好，Wi-Fi 必选
- **Matter（原文 "matter"）目前不受欢迎**（"matter is not very popular right now"）。受访者亲身多次尝试，常遇到：
  - 连接性问题，设备"几乎像不愿支持它一样"（"the devices kind of almost seem to not want to support it"）；
  - 拿不到完整 API / 完整控制权，很多时候**只能读数据（read only），不能控制任何东西**；
  - 他指出 Google 产品多数是这种情况；Amazon、Samsung 与 Google 差不多；Apple 没太多经验但推测类似。
- **他对 Matter 不普及的解读（个人观点）**：这些大公司真正的赚钱点是**采集用户数据**；Matter 作为可互操作协议，意味着它们无法在同等程度采集数据。用 Google Home / Apple HomeKit，厂商能拿到家里更多信息（智能温控的温度变化、智能扫地机甚至可能拿到户型图 floor plan）；Matter 更像"退一步的管理员总览"，给不了这种数据级别。所以"大家来统一生态"很大程度上"是做做样子"（"a lot of that is kind of just for show"）。
- **Thread 与 Zigbee（原文 "Thread and ziggp / Ziggb / Sigb"）相对更受欢迎**；但受访者认为 Tesla 没有与它们的集成。
- **大厂真正想要的是云集成（cloud integration）**：Tesla 和 Enphase（原文 "Nphase"）当前都提供 cloud API。

### 2. 各设备的接入现状（品牌/型号原文保留）
- **Enphase（"Nphase"）**：
  - 受访者用过，但主要是 **utility scale（公用事业级）**，且那边只支持 **cellular（蜂窝）**。
  - 家用侧有 **Enphase Envoy（"Nphase Envoy local"）** —— 专门的 home automation 本地 API；hobbyist 社区常用它配 **Home Assistant**。
  - 不确定 Enphase 在美国家用市场多大（"I'm not sure how big Nphase is in the US"）。
- **Tesla Powerwall**：
  - Tesla 对其产品**不开放**（"not very open with their products"）。
  - 有面向房主的 API，且是 **Wi-Fi 集成**的（因为 Power Wall 需要 Wi-Fi）；这是多数房主走的路径。
  - 生态难搞，GitHub 上有大量第三方对接 Tesla Powerwall 的项目（"a lot of projects on GitHub ... for interfacing with Tesla power walls"）；受访者当年给一个有 Powerwall 的客户做过部署，"不是个容易打交道的生态"。
- **Smart panel / 智能电表 / CT 钳类电气组件**：
  - 受访者有"有限经验"。早年做太阳能上门安装时，房主要么装整套 smart panel，要么装监测电压电流的 clamps。
  - 这些**以 Wi-Fi 为主**，具体常走 **Ethernet**，因为电表/面板通常离家里网口近，会直接插网线。智能电表、smart panel 也多是 Wi-Fi 或 Bluetooth。
- **温控**：加州最大的是 **Google Nest thermostat**（"Nest thermostat is the biggest one there for ... thermostats"）。

### 3. 给 Casally 网关的协议建议
- **Wi-Fi 是刚需、必须有**（"Wi-Fi is definitely ... a must"）；**应支持 Wi-Fi 或 Ethernet**，因为无论如何都要和云 API 通信，"unavoidable"。
- **可选项分层建议**：
  - 可向客户提供**本地网关（local gateway over Wi-Fi）**，让他们甚至不必碰云端（是否做取决于商业定位，因人而异）。
  - **Bluetooth 是 nice to have，但不够安全**，不建议作为"控制整个家"的 hub 协议。风险举例：黑客侵入后可关掉全屋电子门锁、断电断灯、闯入屋内盗窃——"这确实发生在一些人身上"。Bluetooth 也能做安全，但对业务方是**额外工作量**。
  - **Zigbee / Thread / Bluetooth**：**保留这些能力用于对接家里的其它组件**（如某个温控可能走 Zigbee/Thread），但**不要把它们作为面向用户的主接口**。
  - **对用户只暴露 Wi-Fi**；像 Powerwall、电池系统、太阳能这类"重型"组件一般走 Wi-Fi 且需经厂商 API；更小、更便宜的组件才更可能用 Zigbee / Thread / Bluetooth。

### 4. 第一版要不要直接做控制 / 自动化：强烈建议"上来就做自动化"
- **Day one 就应带自动化与控制能力（"launch with automations 100% / day one"）**。
- 理由：市面上"上百万种"产品都能告诉你家里在发生什么（监测类已饱和）；**差异化在于能自动执行（automate），这才是当前的 gap（缺口）**。
- 不是做不到：有人用 Home Assistant 等能做，但前提是"all in 一个生态"——而多数人不是。Google / Apple / Amazon 都不齐组件；目前最接近全自动的是 **Samsung**，但 Samsung 没有太阳能 / 电池。
- **目标人群洞察**：纯监测只对 power user（主动盯账单、自己 game the system 的人）有价值；要触达更大众，得抓住"想降电费**但不想为此费劲**（don't want to work for it）"的人。

### 5. 云 API 不够用时，CT 钳数据能补多少
- **仅靠 CT 钳就能推断不少**：因为同一邮编 / 同一县内，用户间的家庭用电模式差异不大。
- 这可能不是 day one 功能，但**只要进了用户家就持续采集数据**，就能逐步建立每户的"预期用电画像（profile of expected energy usage）"。
- **不要让所有自动化都依赖 Enphase / Tesla 的 API**——它们可能随时撤销、或以"用太多"为由限制；让用户自己去申请 API key / 建 Google Cloud 项目都是 **friction（摩擦）**。
- **TOU（time of use，原文转录为 "toou / T O U / time of smoke"）**：建议用**第三方电网信息 API**。受访者记得做太阳能时用过一个能拿到 grid access 的付费服务，"相对便宜"，可按具体位置查，也可把多个邮编**批量打包查更便宜**；拿到后即可推断"此刻是否该降负载 / 关某设备"。
- **CT 钳数据的局限**：信息量不大，对电工更有用（他们更懂每路接的是什么）。但如果房主从太阳能 / 电池安装商那里被告知"太阳能 / 电池具体接在哪条 leg（相线/回路）、面板里的具体位置"，并把这些信息给到 Casally，就能精确判断电池与太阳能系统在任意时刻的行为，从而**更好地驱动自动化**。
- 但总体上："for the most part, you're probably going to get that from API"（多数情况还是从 API 拿）。

### 6. Tesla Powerwall 的最大集成风险
- **法律风险：基本不担心。** 个人未涉入，但跟进行业诉讼，没见 Tesla 为此告过谁；Tesla 的家庭业务不是其主要赚钱点（"现在主攻 humanoid robots"），不太在意。
- **技术性 / 存续性风险（existential risk technologically）：真正要防的。** 它们可能**随时关闭 API**（借口"看到滥用"或"不想再开放"）。
- **更值得防的另一风险：大厂抄袭（copycat behavior）。** 如果产品差异化不够、或暴露太多实现细节，对方可能"我们已经有这些客户，干脆卖个一样的小网关产品给他们"。
  - **Amazon 是最该警惕的抄袭者**；Google 偶尔但不常；Apple 基本不抄。
  - 特别提醒 **Tesla 现在也要当心**——"Musk 在 SpaceX IPO 之前什么都想抓"。
  - 但抄袭风险在**早期不大，做大后才显著**。
- 受访者明确：Tesla 和 Enphase **不存在非官方 API 支持（unofficial API support）**，只能走官方 API。

### 7. "只能先支持 5 个生态，选哪 5 个"（首发市场=加州）
按受访者建议的优先级（他强调具体仍需做市场调研）：
1. **Tesla Powerwall** —— 最该首要锁定；做太阳能 / 做 EV 都绕不开 Tesla；"everybody's on the Tesla power charging standard"；在加州（尤其硅谷一带）Powerwall 最普及。
2. **Google Home**。
3. **Apple HomeKit**。
4. **Enphase**（家用份额他不确定）。
5. 其余按市场调研"逐项打勾"：还点名了 **Fronius（原文 "Fonius"）**、**SMA**（确认其也进了家用市场）等太阳能厂商。
- EV 方面：Tesla 最大；**Rivian**、**Polestar（原文 "Pstar"）** 及一些豪华电动车在加州也很流行（充电系统细节他不清楚）。
- 还建议留意正在快速成长的 **"电池+公用事业打包即服务（battery+utility combo as a service）"** 类新公司，若在加州增长快，可考虑谈**合作（partnership）**把产品铺进更多家庭。

### 8. 市场调研方法（受访者主动分享的"打法"）
- AI deep research（Google / Claude）对技术信息他觉得一般，但**对市场调研很有用**，尤其在你"还不知道要找什么"时先拿初步结果再校准参数。
- 关键检索词："**publicly traded company disclosures（上市公司披露）**"——按州 / 按国别的市场规模披露很有帮助；还有"**product line sizes（产品线规模）**"，可据此估算某海岸 / 某地区的使用占比。
- **按财富分层（bisect by wealth）**：目标客户（有 Powerwall 等的人）有可支配收入。举例——加州一个年薪 ~120k 的软件开发者往往住公寓、不拥有住房、用不上这类产品（由公寓业主管理）。**要找有钱的房主（wealthy homeowners）**。
- 关注**有独栋住宅、而非以公寓为主的邮编**；**Google Maps 可用来看哪些人家装了太阳能**，再倒推其系统品牌。
- Casally 首发定位：**仅住宅（residential），暂不做商用**——受访者认同，并强调那就更要按财富分层。

### 9. 护城河 / 防抄袭策略
- 两条路：
  1. **退出（exit）**：大公司通常会先来收购而非自建（哪个更省时省钱就选哪个）；受访者判断 Casally 这种情况"它们可能会直接买，因为更省时间"。
  2. **若不想被收购 / 没人出价**：靠**功能 + 降低 friction** 领先。
- **产品理想形态：隐形产品（invisible product）**——"设了就一直好用、对账单有可衡量影响（measurable impact on their bills）"。从硬件到 App UI 都要**尽可能零摩擦**；用户越要"跳火圈"才能让产品工作，越可能留在大厂（大厂已有生态优势，小厂留客天然要多翻几道坎）。
- **最重要的是让客户爱你（make sure your customers love you）**：维系 goodwill 与 customer loyalty；用户真心喜欢，就会在别人问"该买什么"时替你站台——**口碑 / 自然增长（organic marketing）**。

### 10. 安装：电工 vs 用户自装（DIY 安全边界）
- 受访者从电工朋友处学到的判定法："**客户能否在不挪动电（without moving electricity around）的前提下完成？**"
- **判定规则：是否 non-destructive（非破坏性）**：
  - 只是**把 clamps 卡在断路器上**——任何人都能做，不是问题。
  - 一旦需要**换面板、做新的电气连接、换线**——叫电工。
  - 只要不需要做任何物理改造、只是"加装上去"，客户就能自己做。

### 11. 自动化的本地 / 云分层（三类）
- **第一类：纯本地、无需 API/网络。** 基于基本规则：如"过了下午 5 点、多数人下班→大概率进入用电高峰"；"早上大家都走了、家里关着→非高峰、可随意用电"（即 TOU 逻辑，可**预置 preload**，不需 Wi-Fi）。也可**学习并本地存储用户习惯**（如"这个时间他们喜欢这个温度→开温控"；"现在没人→可以削减"）。
- **第二类：需要云端。** 如"此刻确切电价是多少（以降本）""此刻确切用量""屋外温度 / 体感冷热"。
- **第三类：来自客户自身的自动化。** 让用户自定义/设置自己的规则；这类**不需要云或 API**，因为指令直接来自客户（"我要在某时做某事"）。

### 12. 安全措施与攻击面
- **Zigbee / Thread**：受访者不太熟其安全机制，相信是常规加密通信，但需再确认。
- **Wi-Fi / 账户**：最重要是认证。几种模式：
  - **纯云（pure cloud）**：不向任何人暴露本地接口，用户只能经云 API 控制。攻击面只剩后端——**客户账户被黑→其家被黑**。
  - **提供本地接口（local interface）**：最干净的做法是遵循**行业标准认证**，要求用户持有从你这里 / 其账户获取的 key 才能本地访问。虽不便，但多数客户能接受，因为这保护其家庭安全。
  - **反例警示**：若仅凭"在同一 Wi-Fi 网络上"就放行本地控制，攻击者可**伪造 Wi-Fi 凭据上网、冒充设备**，从而拿到一切控制权。
  - **纯本地（full local only）**：经 Wi-Fi / Bluetooth 通信，用户首次拿到设备时获得 key 用于通信；**重置须物理操作（如实体按钮）**，使攻击者**无法远程重置、走默认凭据夺权**。
- 本地接口在 Wi-Fi 不可用等情况下能提供更多 goodwill；但若不想花时间 / 钱，也可只做云端。

### 13. 硬件形态、CT 钳端口与放置（量产/工程化）
- **形态：就做一个盒子（box）。** "每个客户都预期是个盒子"，不是盒子会让人觉得怪。也可做圆形 / 球形等更抢眼的造型，但**更难找代工生产**。
- **CT 钳端口**：受访者没在技术层面做过，不确定具体协议；感觉可能是 **RJ12**（不确定），也可能就是普通线接头；"没什么太离谱的"。建议网关上**留好供 CT 钳读数的端口**。
- **放置位置**：每家布局不同。一般电气面板离 **router（路由器）** 不远——因为建房时把网线（同轴 / 光纤）和接入电网的电线就近走线能少挖少开沟。
  - **经验法则：优先放在 router 旁；不行就放在面板（panel）旁。**
  - **若要用 CT 钳，应优先靠近面板**，并配**更强的 Wi-Fi 网卡 / 更强天线**以覆盖更远距离。
  - 例外：房主把路由器搬到楼上、或面板在户外离得远时，就不一定靠得近。

## 关键金句
- "matter is not very popular right now. Uh, unfortunately, matter is not very popular." —— Simon Asenime
- "a lot of that is kind of just for show because a lot of the money makers for these for these companies is the data that they're able to collect." —— Simon Asenime
- "you're really not going to get more than Wi-Fi." —— Simon Asenime（谈 Tesla/家庭组件接入）
- "you should definitely launch with automations 100%. You should launch with the ability to control the home." —— Simon Asenime
- "there are a lot of products right now that are just for monitoring ... what's going to make you a differentiator in the market is being able to automate that ... that's more of a gap." —— Simon Asenime
- "there are people who are like, I want to lower my electricity bill, but I don't want to work for it. That's who you need to reach." —— Simon Asenime
- "home usage between users does not vary very much. Say within ... a zip code or even ... a county." —— Simon Asenime
- "I would recommend that you're not necessarily dependent on them for all of your automations just because they may revoke them at any time." —— Simon Asenime
- "I would worry a little bit more about technological risk to your business ... unofficial API support I believe does not exist for Tesla and Nphase." —— Simon Asenime
- "the way to stay ahead is features and reducing friction ... you want the kind of invisible product. You want the product that people just set and it just works always and has a very measurable impact on their bills." —— Simon Asenime
- "the most important thing is making sure that your customers love you ... If people love you, they'll go out to bat for you online." —— Simon Asenime
- "can the customer do it without moving electricity around? ... If it's non-destructive ... the customer can do it." —— Simon Asenime
- "just get a box like what everybody else does cuz every customer expects a box. If you do something that's not a box, they're going to feel a little weird about it." —— Simon Asenime
- "a good rule of thumb is next to the router. Ideally, if you can't do next to the router, then do next to the panel." —— Simon Asenime
- "Tesla is definitely going to be your biggest one to target ... everybody's on the Tesla power charging standard." —— Simon Asenime

## 行动项 / 机会点
- **网关协议**：Day-one 支持 **Wi-Fi（必选）/ Ethernet**；将 **Zigbee / Thread / Bluetooth** 仅作为对接家内第三方组件（如温控）的能力，**不作为面向用户的主接口**；不押注 Matter。
- **产品定位**：首发即带**控制 / 自动化**能力（不止监测），把"自动降本、隐形无感"作为差异化卖点。
- **降低对厂商 API 依赖**：用 **CT 钳 + 同邮编/同县用电画像**做兜底推断；引入**第三方电网/TOU API**（可按邮编批量打包降本）；尝试让用户提供"太阳能/电池接在哪条 leg、面板位置"以提升自动化精度。
- **生态优先级（加州）**：Tesla Powerwall → Google Home → Apple HomeKit → Enphase → 其余按调研补（Fronius、SMA 等）；EV 关注 Tesla、Rivian、Polestar。
- **市场调研**：用 AI deep research 做市调；检索"publicly traded company disclosures""product line sizes"；按财富分层、按独栋住宅邮编锁定富裕房主；用 Google Maps 反查太阳能装机。
- **防抄袭/护城河**：早期不必过虑大厂抄袭，重点放在**功能 + 零摩擦 + 客户口碑**；警惕 Amazon、Tesla；明确 exit 也是一条路。
- **安全设计**：明确选纯云 / 本地接口 / 纯本地三种模式之一；本地接口走行业标准认证 + key；**重置须物理操作**防远程夺权；勿凭"同一 Wi-Fi"放行。
- **硬件形态**：先做标准**盒子**形态，预留 CT 钳读数端口（端口/协议待与代工确认，疑似 RJ12）；放置优先 router 旁、其次面板旁，靠面板时配强 Wi-Fi 网卡/天线。
- **安装策略**：以"non-destructive / 不挪动电"为界划分 DIY vs 持牌电工——卡 clamps 可自装，换面板/改线需电工。
- **关系维护**：受访者愿意持续顾问式参与，硬件方案更清晰后可再约其评估可行性，并探索与"电池+公用事业即服务"类成长型公司谈合作。

## 待澄清 / 存疑（转录不确定项）
- 用户设备清单中的 "imperial miners"（00:01）含义不确定，**疑为某能源监测品牌（推断可能是 Emporia 能源监测仪）**，原文未明说，未作定论。
- CT 钳端口"RJ12"为受访者**不确定的猜测**（"I might be wrong"）。
- "Tesla sunron in phase"（00:01）推断为 **Tesla、Sunrun、Enphase** 三个品牌的连读转录。
