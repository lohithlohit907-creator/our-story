from flask import Flask, render_template
from flask import Flask, render_template, request
app = Flask(__name__)


# ==========================================
# PAGE 1 — AUTHENTICATION
# ==========================================

@app.route("/")
def home():
    return render_template("page1.html")


# ==========================================
# PAGE 2 — BIRTHDAY
# ==========================================

@app.route("/story")
def story():
    return render_template("page2.html")


# ==========================================
# PAGE 3 — STORY INTRODUCTION
# ==========================================

@app.route("/beginning")
def beginning():
    return render_template("page3.html")


# ==========================================
# CHAPTER 1 — THE EYE CONTACT
# ==========================================

@app.route("/chapter1")
def chapter1():
    return render_template(
        "chapter.html",
        chapter_number="01",
        chapter_title="The Eye Contact",
        images=["images/chapter1/chapter1.png"],
        story="❤️ Edella start agiddu four years back… adu 2021. ✨ Avaga nav ebru strangers — ninge nan yaru anta gothilla, nange nin yaru anta gothilla. 🥹❤️ Adre aa eye contact… nanu ninuna first time noddaga, noddidu bari ninna beautiful eyes aste. 👀❤️ Ade nanuna tumba attract madiddu. ✨ So nange ennu nenp ide kanda, nin avathu yellow color top hakidde and black mask hakidde. 🖤 Avagle nange nin mele crush agittu… adukella reason the eye contact. 👀❤️✨",
        next_chapter="/chapter2"
    )


# ==========================================
# CHAPTER 2 — THE DRAWING EXAM
# ==========================================

@app.route("/chapter2")
def chapter2():
    return render_template(
        "chapter.html",
        chapter_number="02",
        chapter_title="The Drawing Exam",
        images=["images/chapter2/chapter2.png"],
        story="❤️ Exam ondu doddu reason kanda nav ebru meet agoke… ✨ Life alli ninuna mt nodthini anta andkondirlilla nanu, but universe nam ebru nu mt meet madustu. 🌌❤️ Ade drawing exam alli again mt ade eye contact… 👀❤️ But ee sala first time nan nin face nodiddu, mt same crush. 🥹💕 Ninuna mathadusbeku  anta  esta ittu, adre dairya erlilla. 🙈❤️ Nan ninuna esta padthidini anta ninge gothagirbodu avaga… adre gothilla nin mansalli yen ittu anta… 🥺❤️✨",
        next_chapter="/chapter3"
    )


# ==========================================
# CHAPTER 3 — THE BREAK
# ==========================================

@app.route("/chapter3")
def chapter3():
    return render_template(
        "chapter.html",
        chapter_number="03",
        chapter_title="The Break",
        images=["images/chapter3/chapter3.png"],
        story="""❤️ Kanda, adu admele mt nan ninuna nodle ella… yko gothilla, tumba sala nin bagge yoachane madthidde. 🥹❤️

(Yar a hudgi astondu chanagi edlalla…?) ✨

(Yav uru erbodu alvdu…?) ❤️

Amele 10th standard alli drawing exam adaga ninuna hudkidde, adre ninu bande erlilla kanda… avathu tumba bejar agittu. 🥺💔

Amele nam school alli Prathiba Karanji agittu, avaga nim school hudgiru bandidru, ninu bandirlilla. Avruna kelidde, “Yk Bagyashree bandilva?” anta… 🥹❤️

Avru ninge idunna helidaro elvo gothilla kanda. 😅

Mt enna ivlu sigalla, bidu andkondidde… adre ade year sports alli ninuna mt nodde. 🥹❤️

Avathu navu sports sothidvi, tumba bejar agidde nanu. Amele manege hogthidde… ninge nenp ediyo elvo gothilla, adre avathu ninu mt nin friend stadium mele ninthidri. ❤️

Nanu manege hogbekadre ninuna nodde… 👀❤️ Ninu nanuna nothidde… mt avathu night, “Yk match sotvi?” anta yochane madodu bittu, “Ninu yk nanun nodthidde?” anta yochane madthidde kanda… 🥹❤️✨

Avaga ondu small hope bantu… ningu nan mele swalpa ista erbodu, adukke nan kade nodidiya anta. 🥹💕 Adre confirm agi yenu gothirlilla… ❤️‍🩹✨""",
        next_chapter="/chapter4"
    )

# ==========================================
# CHAPTER 4 — THE BUTTERFLY EFFECT
# ==========================================

@app.route("/chapter4")
def chapter4():
    return render_template(
        "chapter.html",
        chapter_number="04",
        chapter_title="The Butterfly Effect",
        images=["images/chapter4/chapter4.png"],
        story="""❤️ Kanda, yen anusthidde ninge mt idunella nodtha edre sari… story continue madana. 🥹❤️

Kanda, adadmele mt nan ninuna nodidu clg gate munde, madhyana 2 gante ansutte… avathu ninuna nodi shock agidde kanda — “Evlu nam clg ye na?” 😳❤️

Amele tumba kushi agidde… yavthu nodalla andkondide, mt nam clg ge bandidale anta. 🥹✨

Mt ninge nenp elva… clg alli daily ninuna nodthidde. 👀❤️ Mt clg bitmelu yestond sala nin hinde nu bandidini. 🙈❤️

Amele 1st year last room alli window enda ninuna nodbeku antane barthidde… 🥹👀 Yestond sala ninu hinde tirgi nanuna nodli anta andkondidde. ❤️ Ninu nodthidde… 👀💕 Mt hange nin Insta ID eskonde… adu gottu ningu henge eskonde anta… 😅❤️

.................................................

Kanda… ivaga real story! ❤️‍🔥🥹✨
        """,
        next_chapter="/chapter5"
    )


# ==========================================
# CHAPTER 5 — THE HII
# ==========================================

@app.route("/chapter5")
def chapter5():
    return render_template(
        "chapter.html",
        chapter_number="05",
        chapter_title="The Hii",
        images=["images/chapter5/chapter5.png"],
        story="""
        Estu dina nan ninuna nodthidde, ninu nanuna nodthidde… adre ebru mathadirlilla. 👀❤️ July 19, 2024… avathu Saturday. 🗓️❤️

Nin ID siki tumba dina agidru ninge msg madirlilla. Yk andre, aa nam maga balegone… nin friend ninge obba hudga edane anta helidda. 😅❤️ Adike amele adru ondsala avaluna kelana anta tumba yochane madi… sanje 7:44 PM time ansutte, avaga nin ID ge request hakde. 🥹📱❤️

Amele within minutes ninu follow back madi, nan yella post ge like madde… ❤️ Avaga anustu “Avaligu nan mele interest ide antha…” 🥹💕

Amele “Hi” anta msg madde… ninu “Hello” anta. 😭❤️ Nanu “Nan yaru anta gotha nimge?” anta kelide… ninu “Huu, CS avnu thane ninu?” anta reply madidde kanda. 🥹❤️

Hange nam real story start aythu… ✨❤️

Amele nan nan bagge ninge helde, ninu nin bagge nange helde… hange navu friends advi. 🫶🏻❤️

Adre nam friendship tumba dina erlilla kanda…

Yk andre…? 👀❤️‍🔥
        """,
        next_chapter="/chapter6"
    )


# ==========================================
# CHAPTER 6 — THE BESTIES ERA
# ==========================================

@app.route("/chapter6")
def chapter6():
    return render_template(
        "chapter.html",
        chapter_number="06",
        chapter_title="The Besties Era",
        images=["images/chapter6/chapter6.png"],
        story="""❤️ Yk andre navu evaga bari friends alla, besties advi… 🥹❤️

Kanda, avthu nan hostel alli malkondu ninege msg madthidde… 🏠📱❤️ Amele ninu nange, “Yaradru bestie beku…” anta. Nanu “Nan nan bestie na tumba chennagi nodkothini” anta yen yeno helidde. 🥹😂❤️

Amele nanu, “Nan ok na?” anta helde… ninu, “Hwda? Nijvaglu nin nan bestie agthiya?” anta kelde. Nanu “Hmm… ninu madkondre agtini” anta helde. 🥹❤️

Ninu “Hmm sari… agu, enmelinda nav ebru besties” anta helde. 🫶🏻❤️

Avaginda nam Besties Era start aythu… ✨👫🏻❤️

Hogu baa anta mathadoru, hogo, baro, hoge, bare anta mathadoke start madudvi. 😂❤️ Kanda, nijvaglu adu best time kane… 🥹✨

Evaga navu jagala madodu swalpa kammi madidivi… 😭😂 Avaga week alli 3 sala pakka jagala adthivi. 😂💔❤️ Adru aa jagaladallu ondu special bond ittu. 🫶🏻

Adre innu ondu kammi ittu… nav ebru direct agi mathadirlilla. 🥹

Nange ninge mathadusbeku anta esta ettu… adre adukinta jasti baya ettu. 🙈❤️ Yk baya anta nanigu gothilla kanda… 🥺

Kanda… nam ebralli first time yar yarna mathadsiddu anta gotta? 👀❤️

Gothilla andre… next page nodu. 😏❤️‍🔥✨""",
        next_chapter="/chapter7"
    )


# ==========================================
# CHAPTER 7 — first talk and first touch 
# ==========================================

@app.route("/chapter7")
def chapter7():
    return render_template(
        "chapter.html",
        chapter_number="07",
        chapter_title="The First Talk & First Touch",
        images=["images/chapter7/chapter7-3.png",
               "images/chapter7/chapter7-2.png" ],
        story="""❤️ First mathdsiddu nine kanda... avathu namdu sports ittu, mt navu volleyball sotidvi. 🏐❤️

Avaga ninu mt nim friends nan opposite bandri... ninu, “Yen aythu match?” ande, nanu “Sotvi” ande. 🥹❤️ Ade first navu direct agi mathadiddu kanda... 👀❤️

Amele first touch... correct agi ivathige 730 days hinde, same nin birthday dina. 🎂❤️

Ninge direct agi wish madbeku anta Dairy Milk tagondu nim class munde ne wait madtha edde kanda. 🥹🍫

Kanda, nanu nijavaglu yavdadru hudgige yenadru kodsidini andre, adu ninge first... mt ninge last kane. ❤️🥹

Kanda, nija avathu yestu baya agittu gotta nange... yk anta gothilla, adre yeno ontara baya ninge direct agi wish madoke. 🙈❤️

Adru dairy madi wish madbidde... “Happy Birthday” anta heli, first handshake madudvalla... 🤝❤️ Ade nam first touch kanda. 🥹✨

Amele first small trip — Jenukal Betta. ⛰️❤️

Avaga nim appa, andre nam mava ge accident agbittu kanda... adike nanu, ninu mt nin friend Jenukal Betta ge hogidvi. 🥹❤️

Avathu date 19 November 2024. ❤️ Kanda, ee year kuda same ade date dina nav ebru same place ge hogana kane... yen antiya? 🥹❤️⛰️

Mt kanda, avathu ninu nanginta jasti bari nin friend jothe ne mathadthidde... nange swalpa bejar agittu. 🥺❤️

Adre navu Arsikere enda bartha iddaga nange nidde barthidde anta nanuna nin shoulders mele malguskondidalla... nenp ediya kanda? 🥹❤️

Adu nange tumba ista aythu kane... evaglu ond ondsala aduna nenuskondre yestu kushiyagutte gotta nange. 🥹❤️✨

Nanu yavthu yar shoulder melu aa tara malgilla kanda... adre avathu first time nin shoulder mele, nin kai hidkondu malgiddu. 🥹❤️

Aa moment na yavathu mariyoke agalla kane... ❤️‍🩹✨""",
        next_chapter="/chapter8"
    )
# ==========================================
# CHAPTER 8 — THE BAD BIRTHDAY
# ==========================================

@app.route("/chapter8")
def chapter8():
    return render_template(
        "chapter.html",
        chapter_number="08",
        chapter_title="The Bad Birthday",

        images=[
            "images/chapter8/chapter8.png",
            "images/chapter8/chapter8-2.png"
        ],

        story="""
        Kanda, edu yk Bad Birthday andre… ade first time ninu nangoskare athidde, mt nan enda athide. 🥹❤️ Adu nan birthday dina — 20 Dec 2024. 🎂✨

Avaga namge 2nd test nadita ettu. Avathu namge Maths test ettu kanda. 📝 Avathu test bardu nanu nan friends yella ache bandvi… ninu mt nin friend kaytha edri. Nange wish madoke… 🥹❤️

Mt ninu nange wish madi, “Amele call madthini, sigo” anta helde. Nanu “Hmm sari” anta helde. ❤️

Amele ninu call madi, “Railway station hatra baro, ninge yeno kodbeku” anta helde. Nanu “Baroke agalla” anta helde. Ninu yestond sala helde, “Ella baro, railway station hatra” anta… 😭❤️

Nanu, “Ella nan bike… henge barli?” anta helde. Ninu “Sari aythu, barbeda bidu” anta sit madkondu call cut madde. 🥺💔

Kanda, correct agi helthidinaa elva anta gothilla kane… yenadru mistake madidre adjust madkolavaa… 🥺❤️

Amele ninge bejar madbardu anta nan friend bike eskondu railway station hatra barta edde. 🥹❤️ Ninu Girls High School munde ne sikbitte… nenp ediyene ninge, avathu ninu henge adde anta? 🥺❤️

Yest mathadsudru mathe adthilla… astu sit madkondidde nan mele. 😭💔 Amele yestu anta mathadsana… nanigu swalpa sit bandu mt hostel ge hode. 🥺

Amele astondu sit madkondidru… mt nine call madde, “Yel ediyo?” anta helde. Ninu, “Yelo edini bidu, ninge yk?” ande… astuke call ye cut madbitte. 😭💔

Modle mathadsudru mathadilla anno sit ittu… adralli mt call cut madidukke ennu sittu jasti aythu. 😭😂 “Estondu kobba evlige!” anta sit alli nanu ninge enmele msg yenu madbeda, “Goodbye” anta block madbitte. 🥺💔

Mt ninu bere number enda call madidde kanda… avagle mt ontara madthidde, tumba bejar madkondu… mt athidde alva kanda… 🥹❤️

Nange avathe nin mele ediid love ennu jasti agbitu kane. ❤️‍🔥 Papa, nangoskara bere phone enda phone madidale… nangoskara athidale… 🥹❤️

Amele nanu mt nan friends bandvi railway station hatra. Ninu ennu bejar alle edde kanda… 🥺❤️

Amele nange wish madi, gift kotte. 🎁❤️

Adu ninu nange kothiro first gift… nan life alli obba hudgi nange kotta first gift. 🥹❤️🎁

Adu evaglu kuda daily aa photo na nodi, aa moment ella nenpuskothini kanda… 🥹❤️✨

Kandaa… avathe ondu decide madbitte kane… yen gotta……………………..! ❤️‍🔥🥹
        """,

        next_chapter="/chapter9"
    )

# ==========================================
# CHAPTER 9 — THE FIRST DATE
# ==========================================

@app.route("/chapter9")
def chapter9():
    return render_template(
        "chapter.html",
        chapter_number="09",
        chapter_title="The First Date",
        images=["images/chapter9/chapter9.png",
                "images/chapter9/chapter9-2.png",
                "images/chapter9/chapter9-3.png"],
        story="""❤️ The First Date 🌹

Edella agi 5 days nav ebre yelladru hogi barana ande decide madudvi… 🥹❤️

Yellige hogidvi helu? 👀❤️

Kanda, avathu Dec 25, 2024… 🎄❤️ I think around 9:15 AM ge ninu call madde — “Ready agidini, baro” anta. 🥹

Amele nanu 9:30 ge nim hostel hatra ninge call madi, “Bare, kelagade edini” anta helde. ❤️ Ninu bande… 🥹

Yes… common, let’s go! ❤️🏍️✨

Hange nam journey start madudvi… 🌹

Kanda, edu nam first date… mattu honestly, best date agittu alva kanda? 🥹❤️

Swalpa doora admele ninu bike odusde… nanu nin hinde kuthidde. 🏍️❤️ Ninnuna tapkondu kuthkondidde… aa moment na evaglu nenp madkothini. 🥹❤️

Amele first navu Namada Chilume ge hodvi. 🌿❤️ Alli nodo antadu yenu erlilla… statues, mt nin favourite monkey mt deers idvu. 🐒🦌❤️

Ninu Tirupathi ge hogbekadru same ede tara deers irtave anta helidde… 🥹❤️

Amele allinda Devarayanadurga ge hodvi. ⛰️❤️

Kanda, avathu monkey ondu problem agittu… yest hedrukondidde! 😭😂 Ninu hedrukondu nan kai na tight agi hidkondidde… nenp aytha kane? 🥹❤️

Amele metlu hathkondu mele hodvi… 🥵❤️ Mt alli nam first photo na teguskondvi. 📸🥹❤️

Next allinda Mandagiri Hills ge hodvi… adu matra sakat agittu alva kanda! 😭❤️

Nange avathu ade jasti ista agiddu. 🥹✨ Alli bere metlu hatoke agthirlilla… adru kasta pattu hatudvi. 😂❤️ Aamele allu photos tagondu, swalpa hottu alle kuthkondu mt kelage barthidvi. 📸❤️

Avathu papa yavdo hudga odogta acting madoke hogi bidbitidda… aa bejaru evathu nan mansalli hange ede kanda. 🥺❤️

Amele astralli sanje agittu… 🌅❤️ Return Tiptur ge journey start madudvi. Hange barta Zudio gu hogidvi alva kanda… 🥹❤️

Kanda… edella agi agle 2 years agbitu kane. 🥺❤️ Adre ennu nenne monne agiro tara ansutte nange. Time tumba fast agi hogbittu… ⏳❤️

Amele barta hotel alli ebru first lunch nu thindvi. 🍗❤️ Biryani and kebab… ninu first time nange avathu tinsidde, mt nanu ninge thinsidde. 🥹❤️

Astra alli agle sanje agittu… 🌆 Ninna safe agi nim hostel ge bittu, bejar madkondu manege hode. 🥺💔

Kanda… nange yar jothe nu hange agalla kane. Adre nin jothe full day time spend madi, mt manege hogbekadre tumba bejar agutte. 🥹❤️

Yavaglu hange irbeku… nin jothe ne irbeku ansutte. ❤️‍🩹🥹

Evaglu anusthidde… ❤️""",
        next_chapter="/chapter10"
    )


# ==========================================
# CHAPTER 10 — THE END
# ==========================================

@app.route("/chapter10")
def chapter10():
    return render_template(
        "chapter.html",
        chapter_number="10",
        chapter_title="The End",
        images=["images/chapter10/chapter10.png"],
        story="""Kanda, yeno ondu decide madidde anta heludnalla… adu yen andre, ninge propose madbeku anta. 🥹❤️

Tumba dina yochne madidini — “Evathu helana… helana…” anta. Adre baya… 😭❤️ Yk andre, evaga besties agi adru idale… amele nanu propose madudmele adu ella andre yen madana anta tumba yochne madidde. 🥺

Kanda, nanu yav hudgir hatra nu astu close agi erlilla kane… nin harta ne astondu close agiddu nanu. ❤️

Nanu ninge avathu helidde… evathu helthidini kanda:

“Nan life hudgi andre nin oble erbku kane. ❤️ Nan just friend, best friend, bestie, lover, wife… yella nine agirbeku nange.” 🥹❤️

Amele nanu “Nin nanuna love madthiya?” anta kelide… ninu “No” anta helde. 💔🥺

Mt “Will you marry me?” antanu kelide… ninu “No” anta helde. 😭💔

Amele nange esta aglilla kanda… 🥺 Nanu “Bestie agi eroke nin jothe idre, nine yella agirbeku nange… ella andre erle bardu” anta ninge avathu helde. ❤️‍🩹

“Enmele nan nin bestie alla… nin nange msg, call yenu madbeda.” anta helde. 🥺💔

Ninu astukke chikka hudgi tara althidde… 🥹💔

Amele nanu ella prank madiddu anta yen yeno heli samadana madde. 😭❤️

Adru nange avaga bestie agi eroke ista erlilla kanda… 🥺

Bestie oblu… lover oblu… wife oblu… aa tara yella separate agi beda. Nange yella role-gu nine agirbeku kane. ❤️🥹

Nan lover, nan bestie, nan wife, nan maklu ge amma… yella nu nine agirbeku. ❤️‍🔥🥹

Yavaglu aste… ❤️

Kanda, ee time alli swalpa dina navu correct agi mathadirlilla alva… 🥺❤️ Adru ninu yk avathu nanuna reject madde anta ondu perfect reason hele kanda… nange nija evathu gothilla yk avathu “No” ande ninu anta. 🥺

Nanu yk anta nu kelilla… maybe aa moment alli nange adanna keloke aglilla. 💔

Kanda, nanu avathu tumba ne bejar agidde kane… 🥺💔 Ninu nambu… ella bidu, adre nange nane yav hudgi hinde nu hogilla kanda.

Adre ninnagi nane keludre reject madalla anta ankondidde… aduke tumba bejar agittu. 🥺❤️‍🩹

Adre… nam story alli “No” andre end alla alva kanda? ❤️‍🩹✨""",
        next_chapter="/chapter11"
    )


# ==========================================
# CHAPTER 11 — THE STORY
# ==========================================

@app.route("/chapter11")
def chapter11():
    return render_template(
        "chapter.html",
        chapter_number="11",
        chapter_title="The Story",
        images=["images/chapter11/chapter11.png",
                "images/chapter11/chapter11-2.png"],
        
        story="""
        Kanda, edu nam story alli worst part kane… 🥺💔

Yk andre, ee time alli ninge tumba andre tumba bejar madidini kanda… tumba sala athidiya nan enda, nangoskara… 🥺💔

Adu admele tumba sala ninge arta madsi, ninuna bit hogoke try madidini kanda. Tumba sala block madidini… ninge hurt ago tara tumba mathadidini. 😔💔 Nijvaglu nin nange ista erlilla anta alla kanda… ninuna evaga yest ista padthidino, avaglu aste ista padthidde. ❤️ Adre nange bestie agi eroke ista erlilla, ninge nanuna bittu eroke ista erlilla. 🥺

Kanda, yest sala ninge arta madsoke try madudru ninu matra yenu kelthirlilla kane… 🥺 Nange “Ee tara yella yenu helbeda kano” antha ide ansutte… adre ninge yenu helde hange bittu hogoke nange ista erlilla kanda. ❤️‍🩹

Yest sala block madudru, mt mt bere phone enda call madthidde. 📱🥺 Yest bejar madidru, mt nane beku antide. ❤️

Kanda, ninu nanuna tumba achkondidde kane… 🥹❤️ Adru yk avathu nanu propose madidaga reject madde anta gothaglilla! 🥺

Ond sala alla, yerad sala alla… yest sala heludru ninu matra nanuna bit hogoke ready erlila. ❤️‍🩹 Adre nange yella nine agbeku… besties agi eroke ista erlilla. 🥺

Kanda, avathu same hinge nanu ninge helthidde… “Enmele navu ee tara besties agi erbardu, ninu arta madko… yk hing adthiya?” anta. 🥺 Ninu mt hata madthidde… ❤️

Amele avathu ninge ad yen anusto gothilla… ninu nange, “Nan nin jothe life purthi eroke ready… nin ready na?” anta kelde. 🥹❤️

Nange arta adru ella nange arta aglilla… “Ennod correct agi helu” anta helde.

Amele ninu, “Nan ninuna love madthidini… nan nin jothe eroke ready. Nin ready?” anta kelde. ❤️‍🔥🥹

Kanda… nange avaga yestu kushi agittu gotta! 🥹❤️ Ninge tumba kushi agittu kanda. ❤️

Avaga nanu “Nange time beku” anta helde. Ninu adukke, “Ella nin mansalli yen ide aduna ivagle helu” ande. ❤️ Aamele “Sari… enna 2 days alli helu” anta helde. 🥹

Kanda, nanu avthu night nidde ne madirlila kane… 🌙🥺 Adu ne yochne madthidde.

“Yen gotta? Ivlu evle propose madudlu… mt avathu yk nan propose madaga reject madudlu?” anta. 🥹

Amele yen ansittu gotta kanda… “Avlu nanuna tumba achkondidale… aduke nanu bit hogthini anta ee tara helthidale” andkonde. ❤️‍🩹

Amele ella real agi love ede evlige nan mele anta gothaytu… 🥹❤️

Kanda, adru ninu avathu reject yk madde anta helbeku nange… nanu kelalla, ninagi nine helbeku kanda. Kaytha erthini nanu… 🥺❤️

Kanda, avathinda navu lovers advi. ❤️‍🔥

Nange ninu nan ninuna nodidd dinudinda nu nin mele love ettu… ❤️ Adre ningu confirm agi love ede anta gothagiddu avathee kanda. 🥹❤️

Kanda, nijvaglu ninu nange sigoke punya maidde kane… 🥹❤️ Nanu mt ninu aste, nan ninge sigoke ninu punya madidde ansutte. ❤️‍🩹

Kanda, yest jagala adudru, yest kithadudru, yest math bitru… nange nine beku kane. Nin matra beku nange. ❤️🥹

Modlu ninuna bittu erodu easy andkondidde kane… adre evaga ninuna bittu heng erthini anta yochane nu madoke agalla kanda. 🥺❤️

Kanda… namdu 1st year anniversary kuda aythu… 🎂❤️

Amele… ❤️‍🩹✨
        """,
        next_chapter="/chapter12"
    )


# ==========================================
# CHAPTER 12 — THE BEST DAYS
# ==========================================

@app.route("/chapter12")
def chapter12():
    return render_template(
        "chapter.html",
        chapter_number="12",
        chapter_title="The Best Days",
        images=["images/chapter12/chapter12.png",
                "images/chapter12/chapter12-2.png",
                "images/chapter12/chapter12-3.png",
                "images/chapter12/chapter12-4.png",
                "images/chapter12/chapter12-5.png",
                "images/chapter12/chapter12-6.png",
                "images/chapter12/chapter12-7.png"],
        story="""
        amele mt dec 25 mt navu aa legacy na continue madbeku anta mt yelladru hogana anta deciede madudvi kanda ❤️🎄 navu besties agi edaga ninu nange ondu reel kalsi navu ellige hogbeku kano anta helidde kane 🥹❤️ nange adu nenp ettu aduke nanu sakleshpura ke karkondu hogbeku ninuna anta deceide madidde kanda ❤️⛰️ avathu nam love next level ge reach aythu kane ❤️‍🔥🥹 .. kanda avathu date 25 dec 2025 🎄❤️ navu adastu bega sakleshpura ke hogbeku anta 8:30 ge nim hostel hatra bandu ninuna karkondu journey start madudvi 🏍️❤️ yeppa yestuu chali ettu kanda 🥶❤️ avathu kai yella freeze agthittu yest tight agi hug madudru chali matra kammi agthane ella alva kanda 🥹❤️ adru swalpa doora admele nine bike odusde 🏍️❤️ amele navu ondu hotel hatra break tagondvi haasan alli ninu thindi thinebku anta kanda ❤️ a sorry kane 😭 a hotel hesru nange gothilla amele ninu bari 2 edli aste tindiddu kanda 😂❤️ amele allinda mt journey continue madudvi 🏍️✨ next navu reach agiddu manjarabad fort kanda 🏰❤️ adu love alli iconic place kane yk helu? 🥹❤️ ade place alli namduu first direct propose mt namdu first kiss agorodu kanda ❤️‍🔥🥹 kanda nange evaglu aduna nenuskondre mai yella jumm anuttte kane 🥹❤️ ............. kanda nanu yen plan madidide gotha modlu fort visit madodu amele falls visit madodu amele last ge navu ondu waste place ge hogidvalla aa place alli ninge propose madi kiss madbeku anta plan ediddu ❤️🥹 adre ykoo gothilla first place alle nange ansutu ede right time evagle helbkeu anta ... kanda nange yest baya agthittu gotta helbekadre 🥹❤️ nanu ninuna nan munde nilskondu imagine madko kanda mt aduna amele nan pocket enda brecelete tegdu i love you anta hele bitte ❤️‍🔥🥹 amele ninu 2 sec wait madi i love too kanda anta heli nanuna hug madde 🥹❤️ amele nanu heloke ontara agthidde kane nange amele nanu kiss madla anta kelde ninu sumne ninthidde amele mt kiss madla anta kelde ninu hmm ande amele kiss made bitte kanda ❤️🥹 adu matra yavathu mariyoke agalla kane alva ❤️‍🩹🥹 ........... first propose , first kiss yella tumba special ❤️‍🔥🥹 .........................kanda amele kiss madi admele ninu bejar madkondide hogo ninu yavaglu nange bejar madthiya anta amele nanu mt ninge kiss madi samadana madde ninge nenp ediyo elvo gothilla nange nenp edde 🥹❤️ amele ninu yen helde gotta "ninu nange yen bakadru madu adre bit hogthini anta matra helbeda nange promise madu nanuna yavathu bittu hogalla anta "anta helde 🥺❤️ amele nanu promise madde kanda 🤝❤️ ............adu adamele navu allinda next falls ge hodvi 🌊⛰️❤️ alli shoe yella bichi kai yelli hidkondu adventure madkondu hogdvi 😂❤️ henge ette kanda adu adventure 🥹❤️ amele alli swapa time spend madi photos tegondu mt ninu alli yen anta helde gotta 🥹❤️ "enn ond sala yenadru nanuna bit hodre , met met alle hodthini ninge bandu anta helidde kanda " 😂❤️ amele ella bide ninuna bittu yellu hogalla nanu anta helde kanda ❤️🥹 amele allilda  restarurent ge hodvi alli uta madkondu 🍽️❤️ navu next view point ge hoghidvi adu swalpa ettu mt bike alli petrol bere kammi ettu 😭😂 mt allige hogbekadre journey tumba boaring agittu alva kanda ninu nange bejar agthide kano antanu helde 🥹❤️ adru allige hodvi amele ali nodudru full bislu ☀️😭 ebru gu disappointment aythu aduna nodi alva kanda 😂❤️ . kanda yenadru nanu first plan tara alli ninge  propose madidre swalpa nu changi erthirlila alva kanda 🥹❤️ ........ amele last allinda tiptur ge journey start madudvi 🏍️❤️ amele barbekadre kithadudvi yk helu "nanu ninuna tapkondu sumne kuthidde amele nanu nin boobs na echukde ninu novutte kano sumne ero anta helde nanu ella anta mt hange ninu amele ninu sumne edde amele nanu mt ennu joragi echukbitte ninu aduke yeee tegiyo ninu kai na yest nov aythu gotta anta sit madkondu amele nanu kuda si madkondu ninuna touch maddange kuthidde alva kanda amele one 10 min admele nane papa hogli anta mt tapkondre ninu tegiyo kaina esta tanka kuthidalla hange kuhtko yk bande mt hogu anta helde amele nanu mt topkondu kiss madde ❤️ amele i love you anta helde ❤️ amele ninu samadana ade i love you too anta helde ❤️🥹 ......................................................... kanda next best days andre navu mantralaya ke hogiddu kanda ❤️🚆 adu life alle the best days kane 🥹❤️ 3 days and two nights kanda ❤️ adru bagge yenu helodu bekagilla ansutte adru  bagge nanginta gottu kanda ❤️‍🩹 matralaya dalli navu spend madiro ond ondu sec kuda nan tumba esta kane 🥹❤️ ........... mt navu a 2 night madiro kiss yeppa 2 night alli 2 years ge ago astu kiss madidivi ansutte ❤️‍🔥🥹 .................. aa tara nighe mt yavathu barutho anta wait madthidinin kane kanda nanu 🥹❤️ ............................ mt train alli avru nange nin yejmanru anta bere helidru kanda alva 😂❤️ .............. kanda navu munde yeste trip hodre mantralaya matra yavthu top 1 alle erutte kane 🥹❤️ nange aa 2 night mt 3 days tumba ne esta aythu kanda ❤️‍🩹🥹 ................ i love you ❤️ .............................. i love you so much kanda ❤️🥹

        """,
        next_chapter="/chapter13"
    )


# ==========================================
# CHAPTER 13 — THE BEGINNING
# ==========================================

@app.route("/chapter13")
def chapter13():
    return render_template(
        "chapter.html",
        chapter_number="13",
        chapter_title="The Beginning",
        images=["images/chapter13/chapter13.png"],
        story="""
        Kanda, hinde nanu ninge yeste bejar madirbodu kane… 🥺❤️ Yestond sala ninuna bittu hogoke try madirbodu… adre evaga yar jothe edini helu kanda. ❤️

Kanda, nange navu yest jagala adi, kithadudru dooora matra agbardu kane. 🥺❤️

Kanda, nange gottu… nan ee tara yella heludre evaga yenu value ella anta. 🥺

Adre nijavaglu… nan ninuna tumba andre tumba love madthini kane. ❤️‍🔥

Ennu 1000 janma bandru nanu nine beku anta keltini kane… nin tara alla, nine beku nange. ❤️🥹

Kanda, nanu ninge ondu promise madidde kane — yavathu ninuna bittu hogalla anta. 🤝❤️

Adre evathu innondu promise madthini kanda:

“Bagyashree, ninge edu vargu yest bejar madidinoo, ninuna yest alsidinoo… adu yelladukinta jasti ninuna chanagi nodkothini kanda.” ❤️🥹

Edu nan promise kanda. 🤞❤️
Ninuna nan yede mele etkondu nodkothini kane. 🥹❤️

Kanda, edu nam love journey. ❤️
Adre edu end alla… edu new beginning. 🌅❤️

Nam journey ellige end agalla kanda… elli nam journey enda start agthidde. ❤️‍🔥

Navu ee website na 13 pages enda nam memories na collect madta madta… one day full life journey na collect madbeku kanda. 🥹❤️📖

Kanda, avathu nanu ninge yen helidde nenp ediya?

Mantralaya enda train alli barbekadre… 🚆❤️

“Kanda, nam photos ella Polaroids madi, aduna book alli paste alli nam journey na collect madbeku.” anta helidde. 🥹📸❤️

Adre book safe eralla kanda… kaldu hogbodu, bere yaradru nodbodu… safe eralla. 🥺

Adre edu yaru nodoke agalla… nanuna mt ninuna bittu mt kaldu hogalla kanda. ❤️‍🩹🔐

Kanda, edu nin 18th birthday ge nan small gift. 🎂🎁❤️

Ee website nam love journey na carry madutte. ❤️

Enmele… nam love alli yene adru, aduna ee website alli update madta irthini. 🥹❤️

Future alli ond dina… ebru gu full age agi, life alli busy agi, yeno ondu dina bore agthirbekadre… 😂❤️

Ee website na open madi nam memories na nodi… nam journey na matte recall madkolona. 🥹❤️📖

Aaga ee memories yella nodi, “Nodu… nam story illinda start agittu.” anta ibru smile madona. ❤️🥹

❤️ Once Again, Happy Birthday Kanda 🎂

I love you so much. ❤️

I love you more than anything in the world. 🌎❤️

I love you until my last breathe. ❤️‍🩹

Really… I love you, Bagyashree. 🥹❤️‍🔥

This isn't the end of our story…
This is just the beginning. 🌅❤️
        """,
        next_chapter="/final"
    )


# ==========================================
# FINAL PAGE — REVIEW
# ==========================================

@app.route("/final")
def final():

    try:
        with open("reviews.txt", "r", encoding="utf-8") as file:
            review = file.read()

    except FileNotFoundError:
        review = ""

    return render_template(
        "final.html",
        review=review
    )


@app.route("/save-review", methods=["POST"])
def save_review():

    review = request.form.get("review", "").strip()

    if review:

        with open("reviews.txt", "w", encoding="utf-8") as file:
            file.write(review)

    return render_template(
        "final.html",
        review=review
    )


# ---------------------------------------------
# THE REVIEW PAGE
# ---------------------------------------------

@app.route("/review")
def review():
    return render_template("review.html")


# ==========================================
# RUN FLASK
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)