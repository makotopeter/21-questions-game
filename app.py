import random
import streamlit as st

st.set_page_config(
    page_title="21 Questions",
    page_icon="💬",
    layout="centered",
)

QUESTION_BANK = {
    "朋友": ['你做過最奇怪的一個夢是什麼？', '如果可以穿越時空回到過去，你最想去哪個年代？為什麼？', '如果可以改變自己的一件事，你會改變什麼？為什麼？', '一想到童年最快樂的回憶，第一個浮現在腦海的是什麼？', '如果可以擁有任何一位虛構角色的衣櫥，你會選誰？為什麼？', '小時候第一個夢想從事的職業是什麼？', '如果可以和一位名人共進晚餐（無論是否還在世），你會選誰？為什麼？', '你最喜歡一看再看的電影是哪一部？', '如果你是電玩遊戲的主角，你會選哪一款遊戲？為什麼？（也可以自己設計一款理想中的遊戲。）', '你最喜歡哪個季節？為什麼？', '你最不喜歡哪個季節？為什麼？', '如果可以創造一個全新的節日，它會叫什麼名字？大家會怎麼慶祝？', '你曾經在網路上買過最莫名其妙的東西是什麼？當初為什麼會買？', '如果可以發明一項科技產品，你會發明什麼？它有哪些功能？', '為了逃避麻煩，你做過最誇張的一件事是什麼？', '你最喜歡哪一間博物館？為什麼？', '你最大的恐懼是什麼？為什麼？', '人生中做過最冒險的一件事是什麼？', '你聽過最棒，以及最糟糕的一個建議分別是什麼？', '如果你突然獲得10萬美元創業基金，你會開什麼樣的公司？', '你成功戒掉過哪個壞習慣？又是怎麼做到的？', '如果可以安排一場夢想中的公路旅行，你會去哪裡？會帶誰一起？', '小時候最喜歡吃的食物是什麼？為什麼？', '你的人生願望清單中，有哪三件一定想完成的事？', '你人生中最大的遺憾是什麼？', '如果未來只能用電影台詞與人溝通，你會選哪一部電影？為什麼？', '你最喜歡哪個都市傳說？為什麼？', '你最喜歡自己哪一點？', '你的衣櫃裡最奇怪的一件衣服或配件是什麼？', '如果要猜大家最欣賞你的地方，你覺得會是什麼？', '你的夢想工作是什麼？', '你現在最喜歡的明星是誰？', '如果可以加入任何一部影集中的家庭，你最想成為哪一家人的一員？', '如果我可以問你任何私人問題，有哪一題是你最不想回答的？', '你最受不了社群媒體上的哪種行為？', '你最喜歡的虛構角色是誰？為什麼？（小說、電影、電玩、動漫都可以。）', '有什麼活動是你完全覺得不好玩的？為什麼？', '你做過最奇怪的一份工作是什麼？', '你最近一次搜尋紀錄是什麼？（必要的話，可以替自己解釋一下。）', '你手機裡最近一張截圖是什麼？', '你最喜歡穿什麼顏色？又有哪個顏色絕對不會穿？', '你最喜歡哪一種甜點？最不喜歡哪一種？', '小時候說過最嚴重的一個謊是什麼？當時為什麼要說？', '家人之中，你和誰最親近？那個人對你有什麼特別的意義？', '你最喜歡玩的運動是什麼？為什麼？', '如果世界爆發殭屍末日，你最希望哪三個人陪在你身邊？', '如果你是一種冰淇淋口味，會是哪一種？為什麼？（也可以自己發明新口味。）', '你洗澡時最愛唱哪一首歌？為什麼？', '有什麼事情是你的父母一直無法理解你的？', '如果未來有小孩，你會替他取什麼名字？為什麼？', '你的太陽、月亮、上升星座是什麼？', '你對占星有什麼看法？', '如果你現在走進一間購物中心，第一站會去哪裡？', '你最喜歡怎麼度過休假日？', '有什麼技能是你一直很想學會的？', '二選一：住在海邊，還是住在山裡？', '你希望自己的告別式會是什麼樣子？', '如果要刺青，你最想刺什麼？請說出第一個想到的圖案。', '打開手機設定看看，你花最多時間使用的是哪一個App？', '你認為朋友最重要的一項特質是什麼？', '有沒有哪個不受歡迎的觀點，是你非常堅持的？', '在友情或愛情中，你最大的地雷是什麼？', '你的家鄉最吸引你的地方是什麼？為什麼？', '你的家鄉最讓你受不了的地方是什麼？為什麼？', '你收到過最讓你感動的一句稱讚是什麼？', '你最喜歡怎麼慶祝自己的生日？', '你有任何恐懼症嗎？', '你人生看的第一場演唱會是哪一場？', '你第一位喜歡上的歌手是誰？', '如果只能體驗一天，你最想做什麼工作？為什麼？', '看電影時最喜歡吃什麼零食？', '你最喜歡的一個冷知識是什麼？只能選一個。', '你人生做過最正確的一個決定是什麼？', '你從一次失敗中學到最重要的一課是什麼？', '你有最喜歡的Podcast嗎？是哪一個？為什麼喜歡？', '你人生中最棒的一次旅行是哪一次？', '過去一年中，你最難忘的一段回憶是什麼？', '你最欣賞自己最好朋友的哪一點？', '你最喜歡用什麼方式做志工或公益服務？', '如果今天是專屬你的「犒賞自己日」，還可以實現三個願望，你會怎麼安排？', '最近學到的一件新知識或新技能是什麼？', '分享一次最糟糕的第一次約會，並用戲劇化的方式重新講一次。', '玩《瑪利歐賽車》時，你最喜歡使用哪個角色？為什麼？', '你做過最衝動的一件事是什麼？', '如果可以住進任何虛構世界，你會選哪一個？為什麼？', '你最喜歡哪一個陰謀論？為什麼？', '如果可以立刻精通一種樂器，你會選哪一種？', '你有什麼與眾不同的特殊才藝？', '你上過最有趣的一堂課是什麼？', '人生中發生過最不可思議的巧合是什麼？', '如果可以在任何一個國家住一年，你會選哪裡？為什麼？', '如果可以當一隻「牆上的蒼蠅」，偷偷旁觀任何場景，你最想去哪裡？為什麼？', '你曾經惡作劇別人最成功的一次是什麼？', '如果由你設計一座主題樂園，它會是什麼樣子？', '你做過最不像自己會做的一件事是什麼？為什麼？', '你家有哪些特別又有趣的傳統，希望能一直傳承下去？', '你收過最棒的一份禮物是什麼？為什麼那麼喜歡？', '你收過最糟糕的一份禮物是什麼？為什麼不喜歡？', '有沒有哪個迷信，你其實偷偷相信？', '哪一部電影讓你笑到停不下來？為什麼？', '哪一部電影讓你哭得最慘？為什麼？', '你最大的「Guilty Pleasure」（明知道不太好卻忍不住喜歡的事物）是什麼？是什麼時候開始的？', '如果可以立刻成為某個領域的專家，你會選哪一個？', '如果可以和任何虛構角色成為摯友，你會選誰？為什麼？', '假設你正在立遺囑，你會把什麼留給誰？', '如果可以重過人生中的某一天，你會選哪一天？為什麼？', '如果可以邀請任何已故或仍在世的藝人，在你下一次生日派對演出，你會選誰？', '小時候曾經相信過最好笑的一件事情是什麼？', '如果可以住進任何影集或電影中的房子，你會選哪一棟？', '如果家裡可以擁有一件價值連城的收藏品，你最想要什麼？', '如果可以和任何一位歷史人物交換人生，你會選誰？', '有什麼奇怪的食物搭配，是你私底下很愛吃的？', '你相信鬼嗎？請說明原因。', '你相信有來世嗎？請說明原因。', '分享一個你最喜歡的動物冷知識。', '如果可以變成一種動物，你想變成什麼？為什麼？', '如果今天中了樂透，你第一件事會做什麼？', '如果中了樂透，你最想寵愛、照顧哪些人？', '你相信魔法嗎？為什麼相信，或為什麼不相信？', '如果可以把任何興趣變成職業，你會選哪一個？', '如果可以創辦自己的Podcast，你會聊什麼主題？第一位來賓會邀請誰？', '現在有人送你一張單程機票，可以飛往任何地方。你會去哪裡？會帶誰一起？（也可以選擇獨自旅行。）', '你在跳蚤市場、古董店或二手市集撿到過最棒的寶物是什麼？', '有哪兩位名人，是你偷偷（或公開）一位超喜歡、一位超不喜歡？為什麼？', '如果這輩子只能吃一種食物，你會選什麼？為什麼？'],
    "感情": ['你相信一見鍾情嗎？', '你的初吻是什麼樣的體驗？', '你印象最深刻、最美好的一次接吻是什麼樣子？', '你對我的第一印象是什麼？', '如果有人約你第一次約會，你希望對方帶你去哪裡？如果換作是你，你又會帶對方去哪裡？', '你希望另一半具備哪三個特質？', '無論是優點還是生活習慣，另一半有哪些條件是你絕對不能妥協的？', '你曾經真正愛過一個人嗎？', '你曾經暗戀過哪位虛構角色？', '和喜歡的人傳訊息時，你最常使用哪些Emoji？', '為了吸引某個人的注意，你做過最瘋狂的一件事是什麼？', '在感情中，你最大的恐懼是什麼？', '在喜歡的人面前，你做過最糗的一件事是什麼？', '你覺得第一次約會是令人期待，還是讓人緊張？為什麼？', '你最喜歡哪一對電影情侶？為什麼？', '如果可以親身體驗一部浪漫喜劇，你會選哪一部？為什麼？', '你最喜歡帶另一半去哪裡約會？', '你最欣賞哪一對情侶或伴侶？為什麼？', '你認為一段感情發展到什麼階段，才適合在社群媒體公開？', '最容易讓你心動的特質是什麼？', '最容易讓你瞬間失去好感的是什麼？', '你最喜歡我的哪一點？', '你最近傳出的一則曖昧訊息是什麼內容？', '你覺得單身最大的缺點是什麼？', '你覺得單身最大的優點是什麼？', '你覺得自己是個浪漫至上的人嗎？為什麼？', '現階段的你，比較想談輕鬆自在的戀愛，還是認真穩定的感情？', '你認為長期交往最困難的地方是什麼？', '你認為長期交往最棒的地方是什麼？', '如果你明天就要結婚，而且婚禮一定要有主題，你會選擇什麼風格？', '回想過去的感情，你最大的遺憾是什麼？', '失戀後，你最喜歡用什麼方式療傷？', '如果要用一張迷因形容你現在的人生，會是哪一張？', '你寧願曾經深愛過卻失去，還是從來沒有愛過？', '和另一半發生爭執後，你通常會主動和好，還是等對方先開口？', '你曾經對幾個人說過「我愛你」？', '為了取消一次約會，你用過最荒唐的藉口是什麼？', '別人為你做過最浪漫的一件事是什麼？', '你為別人做過最浪漫的一件事是什麼？', '你心目中的完美約會，或夢幻約會是什麼樣子？', '如果現在可以帶我去世界任何一個地方，你會選哪裡？', '如果我們一起受困在無人島，你會帶哪一樣東西？', '你認為一個人最有魅力的特質是什麼？', '你通常會怎麼向喜歡的人示好或曖昧？', '你的「愛的表現」（Love Language）是什麼？', '你第一位迷戀過的明星是誰？', '你人生中最迷戀的一位明星是誰？', '你曾經在最大膽的什麼地方親吻過別人？', '你曾經夢到過我嗎？', '你的敏感帶有哪些？', '如果我們現在一起跳一支慢舞，你會選哪一首歌？', '有哪一件事是你很想和我一起完成的？', '有沒有什麼特質，明知道不該被吸引，卻還是忍不住覺得很有魅力？', '你心目中的第二次約會，最理想會是什麼樣子？', '你覺得認識多久之後接吻，才不算太快？'],
}



import html
import streamlit.components.v1 as components

CATEGORY_CONFIG = {
    "朋友": {
        "icon": "♥",
        "label": "朋友題",
        "accent": "#c91f32",
    },
    "感情": {
        "icon": "◆",
        "label": "感情題",
        "accent": "#9f1d45",
    },
}


def initialize_state() -> None:
    defaults = {
        "category": "朋友",
        "current_question": None,
        "remaining_questions": [],
        "question_number": 0,
        "last_card_token": "",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_deck(category: str) -> None:
    """重新洗牌，整輪抽完前不重複。"""
    questions = QUESTION_BANK.get(category, []).copy()
    random.shuffle(questions)
    st.session_state.remaining_questions = questions


def draw_question() -> None:
    category = st.session_state.category

    if not st.session_state.remaining_questions:
        reset_deck(category)

    if not st.session_state.remaining_questions:
        st.session_state.current_question = "目前這個題型沒有題目。"
        return

    st.session_state.current_question = (
        st.session_state.remaining_questions.pop()
    )
    st.session_state.question_number += 1


def change_category() -> None:
    category = st.session_state.category_selector
    st.session_state.category = category
    st.session_state.current_question = None
    st.session_state.question_number = 0
    reset_deck(category)


def render_card() -> None:
    category = st.session_state.category
    config = CATEGORY_CONFIG[category]
    question = st.session_state.current_question

    is_flipped = question is not None
    safe_question = html.escape(question or "點一下牌面開始")
    safe_label = html.escape(config["label"])
    safe_icon = html.escape(config["icon"])
    state_class = "show-front" if is_flipped else "show-back"

    # 每一題使用不同 token，點牌面後整頁重新載入並觸發下一題。
    next_token = str(st.session_state.question_number + 1)
    card_url = f"?card_action=next&card_token={next_token}"

    card_html = f"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {{
    box-sizing: border-box;
}}

html, body {{
    margin: 0;
    overflow: hidden;
    background: transparent;
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        "Microsoft JhengHei",
        sans-serif;
}}

.scene {{
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 8px 6px 18px;
    perspective: 1300px;
}}

.card-link {{
    display: block;
    width: min(76vw, 330px);
    aspect-ratio: 0.70;
    position: relative;
    text-decoration: none;
    cursor: pointer;
    filter: drop-shadow(0 16px 22px rgba(0, 0, 0, .30));
    -webkit-tap-highlight-color: transparent;
}}

.face {{
    position: absolute;
    inset: 0;
    overflow: hidden;
    border: 6px solid #d9ad71;
    border-radius: 22px;
    transform-style: preserve-3d;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    box-shadow:
        inset 0 0 0 2px rgba(73, 31, 28, .45),
        inset 0 0 26px rgba(46, 17, 16, .18);
}}

/* 初始狀態：顯示牌背。 */
.back {{
    z-index: 2;
    transform: rotateY(0deg);
    opacity: 1;
}}

.front {{
    z-index: 1;
    transform: rotateY(-180deg);
    opacity: 0;
}}

/*
翻牌後不再旋轉整個容器。
牌背單獨轉走、正面單獨轉入，避免 Safari/Chrome
出現鏡像牌背或正反面堆疊錯誤。
*/
.show-front .back {{
    animation: back-out 720ms cubic-bezier(.2,.72,.22,1) forwards;
    pointer-events: none;
}}

.show-front .front {{
    z-index: 3;
    animation: front-in 720ms cubic-bezier(.2,.72,.22,1) forwards;
}}

@keyframes back-out {{
    0% {{
        transform: rotateY(0deg) scale(1);
        opacity: 1;
        visibility: visible;
    }}
    49% {{
        opacity: 1;
    }}
    50% {{
        opacity: 0;
    }}
    100% {{
        transform: rotateY(180deg) scale(.98);
        opacity: 0;
        visibility: hidden;
    }}
}}

@keyframes front-in {{
    0% {{
        transform: rotateY(-180deg) scale(.98);
        opacity: 0;
    }}
    49% {{
        opacity: 0;
    }}
    50% {{
        opacity: 1;
    }}
    100% {{
        transform: rotateY(0deg) scale(1);
        opacity: 1;
        visibility: visible;
    }}
}}

.back {{
    display: grid;
    place-items: center;
    color: #f4cf8e;
    background:
        radial-gradient(circle at 50% 50%,
            rgba(108, 20, 25, .22) 0 16%,
            transparent 16.5%),
        repeating-radial-gradient(
            circle at 52% 48%,
            rgba(255,255,255,.025) 0 1px,
            transparent 1px 4px
        ),
        linear-gradient(145deg, #9f2027, #71131b 58%, #8f2026);
}}

.back::before {{
    content: "";
    position: absolute;
    inset: 15px;
    border: 2px solid rgba(241, 198, 119, .85);
    border-radius: 15px;
    box-shadow:
        inset 0 0 0 6px rgba(128, 31, 35, .78),
        inset 0 0 0 8px rgba(240, 196, 116, .42);
}}

.corner {{
    position: absolute;
    width: 42px;
    height: 42px;
    color: #edc47c;
    font-size: 32px;
    line-height: 1;
}}

.corner.tl {{ top: 20px; left: 22px; }}
.corner.tr {{ top: 20px; right: 22px; transform: rotate(90deg); }}
.corner.bl {{ bottom: 20px; left: 22px; transform: rotate(-90deg); }}
.corner.br {{ bottom: 20px; right: 22px; transform: rotate(180deg); }}

.sigil {{
    position: relative;
    width: 62%;
    aspect-ratio: 1;
    display: grid;
    place-items: center;
    border: 2px solid rgba(239, 193, 113, .78);
    border-radius: 50%;
    box-shadow:
        0 0 0 15px rgba(235, 185, 99, .08),
        0 0 0 2px rgba(93, 19, 24, .9) inset;
}}

.sigil::before,
.sigil::after {{
    content: "";
    position: absolute;
    inset: 14%;
    border: 1px solid rgba(239, 193, 113, .68);
    transform: rotate(45deg);
}}

.sigil::after {{
    inset: 27%;
    border-radius: 50%;
    transform: none;
}}

.question-mark {{
    position: relative;
    z-index: 2;
    font-family: Georgia, serif;
    font-size: clamp(78px, 18vw, 118px);
    font-weight: 700;
    text-shadow: 0 6px 12px rgba(38, 6, 9, .55);
}}

.front {{
    color: #221d1a;
    background:
        radial-gradient(circle at 25% 12%,
            rgba(255,255,255,.96), transparent 38%),
        repeating-linear-gradient(
            15deg,
            rgba(120, 74, 41, .018) 0 1px,
            transparent 1px 5px
        ),
        linear-gradient(145deg, #fffaf0, #f5ead8);
}}

.front::before {{
    content: "";
    position: absolute;
    inset: 16px;
    border: 2px solid {config["accent"]};
    border-radius: 14px;
    opacity: .72;
}}

.front::after {{
    content: "✦";
    position: absolute;
    left: 50%;
    bottom: 27px;
    transform: translateX(-50%);
    color: {config["accent"]};
    font-size: 21px;
}}

.front-content {{
    position: absolute;
    inset: 0;
    z-index: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 38px 27px 43px;
    text-align: center;
}}

.category {{
    display: flex;
    align-items: center;
    gap: 8px;
    color: {config["accent"]};
    font-size: 19px;
    font-weight: 800;
    letter-spacing: .03em;
}}

.divider {{
    width: 58%;
    height: 1px;
    margin-top: 17px;
    background: linear-gradient(
        90deg,
        transparent,
        {config["accent"]},
        transparent
    );
    opacity: .65;
}}

.question {{
    flex: 1;
    width: 100%;
    display: grid;
    place-items: center;
    color: #211d1a;
    font-size: clamp(20px, 3vw, 27px);
    font-weight: 700;
    line-height: 1.55;
    letter-spacing: .015em;
    overflow-wrap: anywhere;
}}

.number {{
    color: rgba(68, 45, 35, .62);
    font-size: 13px;
    letter-spacing: .08em;
}}

.click-hint {{
    position: absolute;
    left: 50%;
    bottom: -31px;
    transform: translateX(-50%);
    width: 100%;
    color: #aeb5c0;
    font-size: 13px;
    text-align: center;
}}

@media (max-width: 520px) {{
    .card-link {{
        width: min(70vw, 280px);
    }}

    .face {{
        border-width: 5px;
        border-radius: 19px;
    }}

    .front-content {{
        padding: 32px 22px 38px;
    }}

    .question {{
        font-size: clamp(18px, 5.4vw, 23px);
    }}

    .category {{
        font-size: 17px;
    }}
}}

@media (prefers-reduced-motion: reduce) {{
    .show-front .back,
    .show-front .front {{
        animation-duration: 1ms;
    }}
}}
</style>
</head>
<body>
<div class="scene">
    <a
        class="card-link {state_class}"
        href="{card_url}"
        target="_top"
        aria-label="翻開下一張牌"
    >
        <div class="face back">
            <div class="corner tl">⌜</div>
            <div class="corner tr">⌜</div>
            <div class="corner bl">⌜</div>
            <div class="corner br">⌜</div>
            <div class="sigil">
                <div class="question-mark">?</div>
            </div>
        </div>

        <div class="face front">
            <div class="front-content">
                <div class="category">
                    <span>{safe_icon}</span>
                    <span>{safe_label}</span>
                </div>
                <div class="divider"></div>
                <div class="question">{safe_question}</div>
                <div class="number">
                    第 {st.session_state.question_number} 題
                </div>
            </div>
        </div>

        <div class="click-hint">
            點選牌面可翻開下一張牌
        </div>
    </a>
</div>
</body>
</html>
"""

    components.html(
        card_html,
        height=525,
        scrolling=False,
    )

initialize_state()

# 處理 iframe 牌面點擊。使用遞增 token 避免重新整理時重複抽題。
card_action = st.query_params.get("card_action", "")
card_token = st.query_params.get("card_token", "")

if (
    card_action == "next"
    and card_token
    and card_token != st.session_state.last_card_token
):
    st.session_state.last_card_token = card_token
    draw_question()
    st.query_params.clear()
    st.rerun()

st.markdown(
    """
<style>
    .stApp {
        background:
            radial-gradient(circle at 50% 15%, #18202d 0, #0d1118 48%, #080b10 100%);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 760px;
        padding-top: 1.6rem;
        padding-bottom: 3rem;
    }

    h1 {
        color: #f7f7f8;
        text-align: center;
        letter-spacing: .04em;
    }

    .app-subtitle {
        margin: -5px 0 22px;
        color: #aab1bc;
        text-align: center;
    }

    div[role="radiogroup"] {
        justify-content: center;
        gap: 12px;
        padding: 8px;
        border: 1px solid rgba(255,255,255,.08);
        border-radius: 17px;
        background: rgba(36, 43, 54, .88);
    }

    div[role="radiogroup"] label {
        min-width: 150px;
        justify-content: center;
        padding: 11px 20px;
        border-radius: 12px;
        color: #e9ecf1 !important;
    }

    div[role="radiogroup"] label:has(input:checked) {
        background: linear-gradient(135deg, #d51d36, #b61328);
        box-shadow: 0 8px 18px rgba(178, 21, 42, .28);
    }

    div[role="radiogroup"] label > div:first-child {
        display: none;
    }

    .stats {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin: 18px 0 0;
        color: #c1c6cf;
        font-size: 17px;
    }

    .stats strong {
        color: #ffffff;
    }

    .stButton > button {
        min-height: 58px;
        border: 0;
        border-radius: 14px;
        background: linear-gradient(135deg, #e21d35, #be1028);
        color: white;
        font-size: 19px;
        font-weight: 800;
        box-shadow: 0 12px 24px rgba(190, 16, 40, .22);
    }

    .stButton > button:hover {
        border: 0;
        background: linear-gradient(135deg, #ee2941, #ca1730);
        color: white;
    }

    .stButton > button:focus {
        box-shadow: 0 0 0 3px rgba(238, 41, 65, .25);
        color: white;
    }

    [data-testid="stProgress"] > div > div {
        background: #d51d36;
    }

    details {
        color: #d9dde4;
    }

    @media (max-width: 560px) {
        .block-container {
            padding-left: 14px;
            padding-right: 14px;
        }

        div[role="radiogroup"] label {
            min-width: 120px;
        }

        .stats {
            gap: 15px;
            font-size: 14px;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("21 Questions")
st.markdown(
    '<p class="app-subtitle">選擇題型，翻開一張屬於你們的問題卡。</p>',
    unsafe_allow_html=True,
)

st.radio(
    "選擇題型",
    options=["朋友", "感情"],
    horizontal=True,
    key="category_selector",
    on_change=change_category,
    label_visibility="collapsed",
)

if not st.session_state.remaining_questions:
    reset_deck(st.session_state.category)

total = len(QUESTION_BANK[st.session_state.category])
remaining = len(st.session_state.remaining_questions)
drawn = st.session_state.question_number

st.markdown(
    f"""
    <div class="stats">
        <span>▱ 題目進度：<strong>{drawn} / {total}</strong></span>
        <span>↻ 未抽題：<strong>{remaining}</strong></span>
    </div>
    """,
    unsafe_allow_html=True,
)

render_card()

button_label = (
    "▱ 翻開第一張牌"
    if st.session_state.current_question is None
    else "▱ 翻開下一張牌"
)

if st.button(
    button_label,
    use_container_width=True,
    type="primary",
):
    draw_question()
    st.rerun()

if st.session_state.current_question:
    st.progress((total - remaining) / total)

with st.expander("重新洗牌與題庫資訊"):
    st.write(f"朋友題：{len(QUESTION_BANK['朋友'])} 題")
    st.write(f"感情題：{len(QUESTION_BANK['感情'])} 題")

    if st.button("重新洗牌", use_container_width=True):
        st.session_state.current_question = None
        st.session_state.question_number = 0
        reset_deck(st.session_state.category)
        st.rerun()
