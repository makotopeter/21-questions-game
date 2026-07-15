import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="21 Questions",
    page_icon="🃏",
    layout="centered",
)

QUESTION_BANK = {'朋友': ['你做過最奇怪的一個夢是什麼？', '如果可以穿越時空回到過去，你最想去哪個年代？為什麼？', '如果可以改變自己的一件事，你會改變什麼？為什麼？', '一想到童年最快樂的回憶，第一個浮現在腦海的是什麼？', '如果可以擁有任何一位虛構角色的衣櫥，你會選誰？為什麼？', '小時候第一個夢想從事的職業是什麼？', '如果可以和一位名人共進晚餐（無論是否還在世），你會選誰？為什麼？', '你最喜歡一看再看的電影是哪一部？', '如果你是電玩遊戲的主角，你會選哪一款遊戲？為什麼？（也可以自己設計一款理想中的遊戲。）', '你最喜歡哪個季節？為什麼？', '你最不喜歡哪個季節？為什麼？', '如果可以創造一個全新的節日，它會叫什麼名字？大家會怎麼慶祝？', '你曾經在網路上買過最莫名其妙的東西是什麼？當初為什麼會買？', '如果可以發明一項科技產品，你會發明什麼？它有哪些功能？', '為了逃避麻煩，你做過最誇張的一件事是什麼？', '你最喜歡哪一間博物館？為什麼？', '你最大的恐懼是什麼？為什麼？', '人生中做過最冒險的一件事是什麼？', '你聽過最棒，以及最糟糕的一個建議分別是什麼？', '如果你突然獲得10萬美元創業基金，你會開什麼樣的公司？', '你成功戒掉過哪個壞習慣？又是怎麼做到的？', '如果可以安排一場夢想中的公路旅行，你會去哪裡？會帶誰一起？', '小時候最喜歡吃的食物是什麼？為什麼？', '你的人生願望清單中，有哪三件一定想完成的事？', '你人生中最大的遺憾是什麼？', '如果未來只能用電影台詞與人溝通，你會選哪一部電影？為什麼？', '你最喜歡哪個都市傳說？為什麼？', '你最喜歡自己哪一點？', '你的衣櫃裡最奇怪的一件衣服或配件是什麼？', '如果要猜大家最欣賞你的地方，你覺得會是什麼？', '你的夢想工作是什麼？', '你現在最喜歡的明星是誰？', '如果可以加入任何一部影集中的家庭，你最想成為哪一家人的一員？', '如果我可以問你任何私人問題，有哪一題是你最不想回答的？', '你最受不了社群媒體上的哪種行為？', '你最喜歡的虛構角色是誰？為什麼？（小說、電影、電玩、動漫都可以。）', '有什麼活動是你完全覺得不好玩的？為什麼？', '你做過最奇怪的一份工作是什麼？', '你最近一次搜尋紀錄是什麼？（必要的話，可以替自己解釋一下。）', '你手機裡最近一張截圖是什麼？', '你最喜歡穿什麼顏色？又有哪個顏色絕對不會穿？', '你最喜歡哪一種甜點？最不喜歡哪一種？', '小時候說過最嚴重的一個謊是什麼？當時為什麼要說？', '家人之中，你和誰最親近？那個人對你有什麼特別的意義？', '你最喜歡玩的運動是什麼？為什麼？', '如果世界爆發殭屍末日，你最希望哪三個人陪在你身邊？', '如果你是一種冰淇淋口味，會是哪一種？為什麼？（也可以自己發明新口味。）', '你洗澡時最愛唱哪一首歌？為什麼？', '有什麼事情是你的父母一直無法理解你的？', '如果未來有小孩，你會替他取什麼名字？為什麼？', '你的太陽、月亮、上升星座是什麼？', '你對占星有什麼看法？', '如果你現在走進一間購物中心，第一站會去哪裡？', '你最喜歡怎麼度過休假日？', '有什麼技能是你一直很想學會的？', '二選一：住在海邊，還是住在山裡？', '你希望自己的告別式會是什麼樣子？', '如果要刺青，你最想刺什麼？請說出第一個想到的圖案。', '打開手機設定看看，你花最多時間使用的是哪一個App？', '你認為朋友最重要的一項特質是什麼？', '有沒有哪個不受歡迎的觀點，是你非常堅持的？', '在友情或愛情中，你最大的地雷是什麼？', '你的家鄉最吸引你的地方是什麼？為什麼？', '你的家鄉最讓你受不了的地方是什麼？為什麼？', '你收到過最讓你感動的一句稱讚是什麼？', '你最喜歡怎麼慶祝自己的生日？', '你有任何恐懼症嗎？', '你人生看的第一場演唱會是哪一場？', '你第一位喜歡上的歌手是誰？', '如果只能體驗一天，你最想做什麼工作？為什麼？', '看電影時最喜歡吃什麼零食？', '你最喜歡的一個冷知識是什麼？只能選一個。', '你人生做過最正確的一個決定是什麼？', '你從一次失敗中學到最重要的一課是什麼？', '你有最喜歡的Podcast嗎？是哪一個？為什麼喜歡？', '你人生中最棒的一次旅行是哪一次？', '過去一年中，你最難忘的一段回憶是什麼？', '你最欣賞自己最好朋友的哪一點？', '你最喜歡用什麼方式做志工或公益服務？', '如果今天是專屬你的「犒賞自己日」，還可以實現三個願望，你會怎麼安排？', '最近學到的一件新知識或新技能是什麼？', '分享一次最糟糕的第一次約會，並用戲劇化的方式重新講一次。', '玩《瑪利歐賽車》時，你最喜歡使用哪個角色？為什麼？', '你做過最衝動的一件事是什麼？', '如果可以住進任何虛構世界，你會選哪一個？為什麼？', '你最喜歡哪一個陰謀論？為什麼？', '如果可以立刻精通一種樂器，你會選哪一種？', '你有什麼與眾不同的特殊才藝？', '你上過最有趣的一堂課是什麼？', '人生中發生過最不可思議的巧合是什麼？', '如果可以在任何一個國家住一年，你會選哪裡？為什麼？', '如果可以當一隻「牆上的蒼蠅」，偷偷旁觀任何場景，你最想去哪裡？為什麼？', '你曾經惡作劇別人最成功的一次是什麼？', '如果由你設計一座主題樂園，它會是什麼樣子？', '你做過最不像自己會做的一件事是什麼？為什麼？', '你家有哪些特別又有趣的傳統，希望能一直傳承下去？', '你收過最棒的一份禮物是什麼？為什麼那麼喜歡？', '你收過最糟糕的一份禮物是什麼？為什麼不喜歡？', '有沒有哪個迷信，你其實偷偷相信？', '哪一部電影讓你笑到停不下來？為什麼？', '哪一部電影讓你哭得最慘？為什麼？', '你最大的「Guilty Pleasure」（明知道不太好卻忍不住喜歡的事物）是什麼？是什麼時候開始的？', '如果可以立刻成為某個領域的專家，你會選哪一個？', '如果可以和任何虛構角色成為摯友，你會選誰？為什麼？', '假設你正在立遺囑，你會把什麼留給誰？', '如果可以重過人生中的某一天，你會選哪一天？為什麼？', '如果可以邀請任何已故或仍在世的藝人，在你下一次生日派對演出，你會選誰？', '小時候曾經相信過最好笑的一件事情是什麼？', '如果可以住進任何影集或電影中的房子，你會選哪一棟？', '如果家裡可以擁有一件價值連城的收藏品，你最想要什麼？', '如果可以和任何一位歷史人物交換人生，你會選誰？', '有什麼奇怪的食物搭配，是你私底下很愛吃的？', '你相信鬼嗎？請說明原因。', '你相信有來世嗎？請說明原因。', '分享一個你最喜歡的動物冷知識。', '如果可以變成一種動物，你想變成什麼？為什麼？', '如果今天中了樂透，你第一件事會做什麼？', '如果中了樂透，你最想寵愛、照顧哪些人？', '你相信魔法嗎？為什麼相信，或為什麼不相信？', '如果可以把任何興趣變成職業，你會選哪一個？', '如果可以創辦自己的Podcast，你會聊什麼主題？第一位來賓會邀請誰？', '現在有人送你一張單程機票，可以飛往任何地方。你會去哪裡？會帶誰一起？（也可以選擇獨自旅行。）', '你在跳蚤市場、古董店或二手市集撿到過最棒的寶物是什麼？', '有哪兩位名人，是你偷偷（或公開）一位超喜歡、一位超不喜歡？為什麼？', '如果這輩子只能吃一種食物，你會選什麼？為什麼？'], '感情': ['你相信一見鍾情嗎？', '你的初吻是什麼樣的體驗？', '你印象最深刻、最美好的一次接吻是什麼樣子？', '你對我的第一印象是什麼？', '如果有人約你第一次約會，你希望對方帶你去哪裡？如果換作是你，你又會帶對方去哪裡？', '你希望另一半具備哪三個特質？', '無論是優點還是生活習慣，另一半有哪些條件是你絕對不能妥協的？', '你曾經真正愛過一個人嗎？', '你曾經暗戀過哪位虛構角色？', '和喜歡的人傳訊息時，你最常使用哪些Emoji？', '為了吸引某個人的注意，你做過最瘋狂的一件事是什麼？', '在感情中，你最大的恐懼是什麼？', '在喜歡的人面前，你做過最糗的一件事是什麼？', '你覺得第一次約會是令人期待，還是讓人緊張？為什麼？', '你最喜歡哪一對電影情侶？為什麼？', '如果可以親身體驗一部浪漫喜劇，你會選哪一部？為什麼？', '你最喜歡帶另一半去哪裡約會？', '你最欣賞哪一對情侶或伴侶？為什麼？', '你認為一段感情發展到什麼階段，才適合在社群媒體公開？', '最容易讓你心動的特質是什麼？', '最容易讓你瞬間失去好感的是什麼？', '你最喜歡我的哪一點？', '你最近傳出的一則曖昧訊息是什麼內容？', '你覺得單身最大的缺點是什麼？', '你覺得單身最大的優點是什麼？', '你覺得自己是個浪漫至上的人嗎？為什麼？', '現階段的你，比較想談輕鬆自在的戀愛，還是認真穩定的感情？', '你認為長期交往最困難的地方是什麼？', '你認為長期交往最棒的地方是什麼？', '如果你明天就要結婚，而且婚禮一定要有主題，你會選擇什麼風格？', '回想過去的感情，你最大的遺憾是什麼？', '失戀後，你最喜歡用什麼方式療傷？', '如果要用一張迷因形容你現在的人生，會是哪一張？', '你寧願曾經深愛過卻失去，還是從來沒有愛過？', '和另一半發生爭執後，你通常會主動和好，還是等對方先開口？', '你曾經對幾個人說過「我愛你」？', '為了取消一次約會，你用過最荒唐的藉口是什麼？', '別人為你做過最浪漫的一件事是什麼？', '你為別人做過最浪漫的一件事是什麼？', '你心目中的完美約會，或夢幻約會是什麼樣子？', '如果現在可以帶我去世界任何一個地方，你會選哪裡？', '如果我們一起受困在無人島，你會帶哪一樣東西？', '你認為一個人最有魅力的特質是什麼？', '你通常會怎麼向喜歡的人示好或曖昧？', '你的「愛的表現」（Love Language）是什麼？', '你第一位迷戀過的明星是誰？', '你人生中最迷戀的一位明星是誰？', '你曾經在最大膽的什麼地方親吻過別人？', '你曾經夢到過我嗎？', '你的敏感帶有哪些？', '如果我們現在一起跳一支慢舞，你會選哪一首歌？', '有哪一件事是你很想和我一起完成的？', '有沒有什麼特質，明知道不該被吸引，卻還是忍不住覺得很有魅力？', '你心目中的第二次約會，最理想會是什麼樣子？', '你覺得認識多久之後接吻，才不算太快？']}

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 50% 10%, #18202d 0, #0d1118 48%, #080b10 100%);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 760px;
        padding-top: 1.1rem;
        padding-bottom: 2rem;
    }

    h1 {
        color: #f7f7f8;
        text-align: center;
        letter-spacing: .04em;
        margin-bottom: .2rem;
    }

    .subtitle {
        color: #aab1bc;
        text-align: center;
        margin-bottom: .8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("21 Questions")
st.markdown(
    '<div class="subtitle">選擇題型，點選牌面翻牌；再次點擊可抽下一題。</div>',
    unsafe_allow_html=True,
)

bank_json = json.dumps(QUESTION_BANK, ensure_ascii=False)

html = r"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    overflow: hidden;
    background: transparent;
    color: #f5f7fa;
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        "Microsoft JhengHei",
        sans-serif;
}

.app {
    width: 100%;
    max-width: 620px;
    margin: 0 auto;
    padding: 4px 12px 18px;
}

.tabs {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    padding: 7px;
    border: 1px solid rgba(255, 255, 255, .09);
    border-radius: 16px;
    background: rgba(36, 43, 54, .92);
}

.tab {
    border: 0;
    border-radius: 11px;
    padding: 12px 14px;
    background: transparent;
    color: #d7dbe2;
    font-size: 16px;
    font-weight: 800;
    cursor: pointer;
}

.tab.active {
    background: linear-gradient(135deg, #d51d36, #b61328);
    color: #fff;
    box-shadow: 0 8px 18px rgba(178, 21, 42, .28);
}

.stats {
    display: flex;
    justify-content: center;
    gap: 24px;
    margin: 15px 0 11px;
    color: #b9c0ca;
    font-size: 14px;
}

.stats strong {
    color: #fff;
}

.scene {
    display: flex;
    justify-content: center;
    padding: 3px 0 9px;
}

/*
不再使用 rotateY 或 backface-visibility。
卡片只做 scaleX，縮到 0 時由 JavaScript 切換正反面內容。
因此 Chrome、Safari、手機瀏覽器都不會顯示鏡像牌背。
*/
.card {
    position: relative;
    width: min(72vw, 310px);
    aspect-ratio: .70;
    overflow: hidden;
    border: 6px solid #d9ad71;
    border-radius: 22px;
    cursor: pointer;
    transform: scaleX(1);
    transform-origin: center;
    filter: drop-shadow(0 16px 22px rgba(0, 0, 0, .30));
    box-shadow:
        inset 0 0 0 2px rgba(73, 31, 28, .45),
        inset 0 0 26px rgba(46, 17, 16, .18);
    -webkit-tap-highlight-color: transparent;
    user-select: none;
}

.card.closing {
    animation: close-card 300ms ease-in forwards;
}

.card.opening {
    animation: open-card 360ms cubic-bezier(.2, .78, .2, 1) forwards;
}

@keyframes close-card {
    from {
        transform: scaleX(1);
    }
    to {
        transform: scaleX(.015);
    }
}

@keyframes open-card {
    from {
        transform: scaleX(.015);
    }
    72% {
        transform: scaleX(1.035);
    }
    to {
        transform: scaleX(1);
    }
}

.card-back,
.card-front {
    position: absolute;
    inset: 0;
}

.card-back {
    display: grid;
    place-items: center;
    color: #f4cf8e;
    background:
        radial-gradient(
            circle at 50% 50%,
            rgba(108, 20, 25, .22) 0 16%,
            transparent 16.5%
        ),
        repeating-radial-gradient(
            circle at 52% 48%,
            rgba(255, 255, 255, .025) 0 1px,
            transparent 1px 4px
        ),
        linear-gradient(145deg, #9f2027, #71131b 58%, #8f2026);
}

.card-back::before {
    content: "";
    position: absolute;
    inset: 15px;
    border: 2px solid rgba(241, 198, 119, .85);
    border-radius: 15px;
    box-shadow:
        inset 0 0 0 6px rgba(128, 31, 35, .78),
        inset 0 0 0 8px rgba(240, 196, 116, .42);
}

.sigil {
    position: relative;
    width: 62%;
    aspect-ratio: 1;
    display: grid;
    place-items: center;
    border: 2px solid rgba(239, 193, 113, .78);
    border-radius: 50%;
    box-shadow:
        0 0 0 15px rgba(235, 185, 99, .08),
        0 0 0 2px rgba(93, 19, 24, .90) inset;
}

.sigil::before,
.sigil::after {
    content: "";
    position: absolute;
    inset: 14%;
    border: 1px solid rgba(239, 193, 113, .68);
    transform: rotate(45deg);
}

.sigil::after {
    inset: 27%;
    border-radius: 50%;
    transform: none;
}

.question-mark {
    position: relative;
    z-index: 2;
    font-family: Georgia, serif;
    font-size: clamp(78px, 18vw, 116px);
    font-weight: 700;
}

.card-front {
    display: none;
    color: #211d1a;
    background:
        radial-gradient(
            circle at 25% 12%,
            rgba(255, 255, 255, .96),
            transparent 38%
        ),
        repeating-linear-gradient(
            15deg,
            rgba(120, 74, 41, .018) 0 1px,
            transparent 1px 5px
        ),
        linear-gradient(145deg, #fffaf0, #f5ead8);
}

.card-front::before {
    content: "";
    position: absolute;
    inset: 16px;
    border: 2px solid #c91f32;
    border-radius: 14px;
    opacity: .72;
}

.front-content {
    position: absolute;
    inset: 0;
    z-index: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 36px 25px 40px;
    text-align: center;
}

.category {
    color: #c91f32;
    font-size: 18px;
    font-weight: 800;
}

.divider {
    width: 58%;
    height: 1px;
    margin-top: 16px;
    background: linear-gradient(90deg, transparent, #c91f32, transparent);
}

.question {
    flex: 1;
    width: 100%;
    display: grid;
    place-items: center;
    color: #211d1a;
    font-size: clamp(19px, 3vw, 26px);
    font-weight: 700;
    line-height: 1.55;
    overflow-wrap: anywhere;
}

.number {
    color: rgba(68, 45, 35, .62);
    font-size: 13px;
}

.hint {
    margin: 8px 0 12px;
    color: #aeb5c0;
    font-size: 13px;
    text-align: center;
}

.next {
    width: 100%;
    min-height: 54px;
    border: 0;
    border-radius: 13px;
    background: linear-gradient(135deg, #e21d35, #be1028);
    color: white;
    font-size: 18px;
    font-weight: 800;
    cursor: pointer;
}

.secondary {
    width: 100%;
    min-height: 45px;
    margin-top: 9px;
    border: 1px solid rgba(255, 255, 255, .14);
    border-radius: 12px;
    background: rgba(255, 255, 255, .03);
    color: #d6dbe3;
    font-size: 15px;
    cursor: pointer;
}

@media (max-width: 520px) {
    .card {
        width: min(68vw, 270px);
        border-width: 5px;
        border-radius: 19px;
    }

    .front-content {
        padding: 31px 21px 36px;
    }

    .question {
        font-size: clamp(18px, 5.2vw, 22px);
    }

    .stats {
        gap: 14px;
        font-size: 13px;
    }
}

@media (prefers-reduced-motion: reduce) {
    .card.closing,
    .card.opening {
        animation-duration: 1ms;
    }
}
</style>
</head>

<body>
<div class="app">
    <div class="tabs">
        <button class="tab active" data-category="朋友">● 朋友</button>
        <button class="tab" data-category="感情">● 感情</button>
    </div>

    <div class="stats">
        <span>題目進度：<strong id="progress">0 / 0</strong></span>
        <span>未抽題：<strong id="remaining">0</strong></span>
    </div>

    <div class="scene">
        <div
            id="card"
            class="card"
            role="button"
            tabindex="0"
            aria-label="翻牌或抽下一題"
        >
            <div id="cardBack" class="card-back">
                <div class="sigil">
                    <div class="question-mark">?</div>
                </div>
            </div>

            <div id="cardFront" class="card-front">
                <div class="front-content">
                    <div id="categoryLabel" class="category">♥ 朋友題</div>
                    <div class="divider"></div>
                    <div id="question" class="question">點一下牌面開始</div>
                    <div id="number" class="number">第 0 題</div>
                </div>
            </div>
        </div>
    </div>

    <div class="hint">
        點選牌面可翻牌；顯示題目後再點一次可抽下一題
    </div>

    <button id="nextButton" class="next">翻開第一張牌</button>
    <button id="shuffleButton" class="secondary">重新洗牌</button>
</div>

<script>
const questionBank = __BANK_JSON__;

let category = "朋友";
let deck = [];
let drawn = 0;
let showingFront = false;
let busy = false;

const card = document.getElementById("card");
const cardBack = document.getElementById("cardBack");
const cardFront = document.getElementById("cardFront");
const questionEl = document.getElementById("question");
const categoryLabel = document.getElementById("categoryLabel");
const numberEl = document.getElementById("number");
const progressEl = document.getElementById("progress");
const remainingEl = document.getElementById("remaining");
const nextButton = document.getElementById("nextButton");
const shuffleButton = document.getElementById("shuffleButton");
const tabs = [...document.querySelectorAll(".tab")];

function shuffle(items) {
    const result = [...items];

    for (let index = result.length - 1; index > 0; index -= 1) {
        const randomIndex = Math.floor(Math.random() * (index + 1));
        [result[index], result[randomIndex]] =
            [result[randomIndex], result[index]];
    }

    return result;
}

function showBackImmediately() {
    cardFront.style.display = "none";
    cardBack.style.display = "grid";
    showingFront = false;
}

function showFrontImmediately() {
    cardBack.style.display = "none";
    cardFront.style.display = "block";
    showingFront = true;
}

function updateStats() {
    const total = (questionBank[category] || []).length;
    progressEl.textContent = `${drawn} / ${total}`;
    remainingEl.textContent = deck.length;
}

function resetDeck() {
    deck = shuffle(questionBank[category] || []);
    drawn = 0;
    busy = false;

    card.classList.remove("closing", "opening");
    showBackImmediately();

    questionEl.textContent = "點一下牌面開始";
    numberEl.textContent = "第 0 題";
    nextButton.textContent = "翻開第一張牌";

    updateStats();
}

function setCategory(nextCategory) {
    category = nextCategory;

    tabs.forEach(tab => {
        tab.classList.toggle(
            "active",
            tab.dataset.category === category
        );
    });

    categoryLabel.textContent =
        category === "朋友" ? "♥ 朋友題" : "◆ 感情題";

    resetDeck();
}

function getNextQuestion() {
    if (deck.length === 0) {
        deck = shuffle(questionBank[category] || []);
        drawn = 0;
    }

    return deck.pop() || null;
}

function animateToFront(nextQuestion) {
    if (busy || !nextQuestion) {
        return;
    }

    busy = true;
    card.classList.remove("opening");
    void card.offsetWidth;
    card.classList.add("closing");

    window.setTimeout(() => {
        questionEl.textContent = nextQuestion;
        drawn += 1;
        numberEl.textContent = `第 ${drawn} 題`;
        nextButton.textContent = "下一張牌";
        updateStats();

        showFrontImmediately();

        card.classList.remove("closing");
        void card.offsetWidth;
        card.classList.add("opening");

        window.setTimeout(() => {
            card.classList.remove("opening");
            busy = false;
        }, 380);
    }, 305);
}

function drawNext() {
    if (busy) {
        return;
    }

    const nextQuestion = getNextQuestion();

    if (!showingFront) {
        animateToFront(nextQuestion);
        return;
    }

    /*
    已顯示題目時，先縮牌、切換到牌背、展開；
    再縮一次、換新題目、展開正面。
    */
    busy = true;
    card.classList.remove("opening");
    void card.offsetWidth;
    card.classList.add("closing");

    window.setTimeout(() => {
        showBackImmediately();

        card.classList.remove("closing");
        void card.offsetWidth;
        card.classList.add("opening");

        window.setTimeout(() => {
            card.classList.remove("opening");
            busy = false;

            window.setTimeout(() => {
                animateToFront(nextQuestion);
            }, 90);
        }, 380);
    }, 305);
}

card.addEventListener("click", drawNext);
nextButton.addEventListener("click", drawNext);
shuffleButton.addEventListener("click", resetDeck);

card.addEventListener("keydown", event => {
    if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        drawNext();
    }
});

tabs.forEach(tab => {
    tab.addEventListener("click", () => {
        setCategory(tab.dataset.category);
    });
});

resetDeck();
</script>
</body>
</html>
"""

html = html.replace("__BANK_JSON__", bank_json)

components.html(
    html,
    height=700,
    scrolling=False,)
