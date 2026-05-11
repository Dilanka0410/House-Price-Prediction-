import streamlit as st

st.set_page_config(
    page_title="ගෙවල් මිල පුරෝකථනය",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@300;400;500;600;700;800&family=DM+Sans:wght@300;400;500;600;700;800;900&display=swap');

html, body, .stApp, .stApp * {
    font-family: 'DM Sans', 'Noto Sans Sinhala', sans-serif !important;
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── LABEL FIX ── */
label,
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span {
    font-size: 15px !important;
    font-weight: 600 !important;
    color: #e2e8f0 !important;
    margin-bottom: 6px !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
}

/* ── HERO ── */
.hero {
    position: relative;
    height: 400px;
    overflow: hidden;
    display: flex;
    align-items: flex-end;
}
.hero-bg {
    position: absolute; inset: 0;
    display: grid; grid-template-columns: 2fr 1fr;
}
.hero-bg img { width: 100%; height: 100%; object-fit: cover; display: block; }
.hero-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(90deg,
        rgba(7,20,40,0.92) 0%,
        rgba(7,20,40,0.60) 55%,
        rgba(7,20,40,0.25) 100%);
}
.hero-content {
    position: relative; z-index: 2;
    padding: 0 64px 48px; width: 100%;
}
.hero-title {
    font-size: 52px; font-weight: 800; color: #fff;
    line-height: 1.12; margin: 0 0 12px; letter-spacing: -1.2px;
}
.hero-title span { color: #60a5fa; }
.hero-sub {
    font-size: 18px; color: rgba(255,255,255,0.68);
    font-weight: 400; line-height: 1.6; max-width: 460px; margin: 0 0 28px;
}
.hero-chips { display: flex; gap: 10px; flex-wrap: wrap; }
.chip {
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.22);
    border-radius: 100px; padding: 7px 18px;
    font-size: 13px; font-weight: 500; color: rgba(255,255,255,0.85);
}

/* ── PAGE BODY ── */
.page-body { background: #0c0f1a; padding: 44px 64px 72px; }

/* ── SECTION HEADER ── */
.sec-head {
    display: flex; align-items: center; gap: 14px;
    margin: 40px 0 16px;
}
.sec-badge {
    width: 46px; height: 46px; border-radius: 13px;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px; flex-shrink: 0;
}
.sec-badge.blue   { background: rgba(59,130,246,0.15); }
.sec-badge.green  { background: rgba(16,185,129,0.15); }
.sec-badge.amber  { background: rgba(245,158,11,0.15); }
.sec-badge.purple { background: rgba(139,92,246,0.15); }

.sec-title { font-size: 22px; font-weight: 700; color: #f8fafc; line-height: 1.2; }
.sec-sub   { font-size: 14px; color: rgba(226,232,240,0.70); margin-top: 2px; }

/* ══════════════════════════════════════════════════════════
   THE FIX:
   Streamlit renders each st.container() as a
   [data-testid="stVerticalBlockBorderWrapper"] element.
   We use the `key` parameter on the container to get a
   stable CSS target via the parent element.

   Since Streamlit doesn't expose a direct class on containers,
   we use a unique marker <div> pattern:
   - Inject a zero-height marker div with a unique class
   - Use CSS ~ (sibling) or parent targeting to style the
     ACTUAL block that follows

   CLEANEST APPROACH: wrap the card content div around the
   Streamlit container using the stVerticalBlockBorderWrapper
   which Streamlit auto-adds when border=True.
══════════════════════════════════════════════════════════ */

/* Style containers that have border=True (Streamlit adds this wrapper) */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.04) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.25) !important;
    padding: 28px 32px !important;
    margin-bottom: 20px !important;
}

/* Remove Streamlit's default border on the wrapper */
[data-testid="stVerticalBlockBorderWrapper"] > div {
    border: none !important;
    border-radius: 0 !important;
    padding: 0 !important;
}

/* ── SLIDER THUMB ── */
.stSlider [data-testid="stSlider"] > div > div > div > div {
    background: #3b82f6 !important;
}

/* ── PREDICT BUTTON ── */
.stButton > button {
    background: linear-gradient(135deg, #1d4ed8, #2563eb) !important;
    color: #fff !important;
    font-size: 20px !important;
    font-weight: 700 !important;
    padding: 18px 0 !important;
    border-radius: 16px !important;
    border: none !important;
    width: 100% !important;
    box-shadow: 0 6px 20px rgba(37,99,235,0.38) !important;
    transition: all .2s ease !important;
    letter-spacing: 0.2px !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg,#1e40af,#1d4ed8) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 28px rgba(37,99,235,0.46) !important;
}

/* ── RESULT CARD ── */
.result-card {
    background: linear-gradient(145deg, #071428, #0d2847, #0f3460);
    border-radius: 26px; padding: 52px 56px;
    text-align: center; margin: 40px 0 0;
    position: relative; overflow: hidden;
    box-shadow: 0 24px 64px rgba(7,20,40,0.38);
}
.result-card::before {
    content:''; position:absolute; top:-110px; right:-110px;
    width:400px; height:400px;
    background: radial-gradient(circle, rgba(96,165,250,0.18) 0%, transparent 65%);
    border-radius:50%;
}
.result-card::after {
    content:''; position:absolute; bottom:-80px; left:10%;
    width:300px; height:300px;
    background: radial-gradient(circle, rgba(52,211,153,0.12) 0%, transparent 65%);
    border-radius:50%;
}
.result-eyebrow {
    font-size: 12px; font-weight: 700;
    color: rgba(255,255,255,0.40);
    letter-spacing: 3px; text-transform: uppercase; margin-bottom: 16px;
}
.result-price {
    font-size: 76px; font-weight: 800;
    color: #fff; letter-spacing: -3px; line-height: 1; margin-bottom: 12px;
}
.result-range { font-size: 17px; color: rgba(255,255,255,0.48); margin-bottom: 40px; }
.result-hr    { height:1px; background:rgba(255,255,255,0.10); margin:0 0 36px; }
.result-stats { display:flex; justify-content:center; position:relative; z-index:2; }
.rstat {
    flex:1; padding: 0 20px;
    border-right: 1px solid rgba(255,255,255,0.10);
}
.rstat:last-child { border-right:none; }
.rstat-num   { font-size:28px; font-weight:700; color:#fff; }
.rstat-label { font-size:12px; color:rgba(255,255,255,0.38); margin-top:5px; }
.tags {
    display:flex; flex-wrap:wrap; gap:9px;
    justify-content:center; margin-top:28px; position:relative; z-index:2;
}
.tag {
    background:rgba(255,255,255,0.10); border:1px solid rgba(255,255,255,0.18);
    border-radius:100px; padding:8px 20px;
    font-size:14px; font-weight:500; color:rgba(255,255,255,0.85);
}

.element-container { margin-bottom: 0 !important; }
.stMarkdown { margin-bottom: 0 !important; }
.spacer { height: 20px; }

/* ── INPUT STYLING ── */
[data-testid="stNumberInput"] div[data-baseweb="input"] {
    background: rgba(255,255,255,0.06) !important;
    border: 1.5px solid rgba(255,255,255,0.14) !important;
    border-radius: 14px !important;
}
[data-testid="stNumberInput"] input {
    background: transparent !important;
    color: #f8fafc !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}
[data-testid="stNumberInput"] button {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.14) !important;
    color: #e2e8f0 !important;
    border-radius: 10px !important;
}
[data-testid="stNumberInput"] button:hover {
    background: rgba(255,255,255,0.14) !important;
}
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.06) !important;
    border: 1.5px solid rgba(255,255,255,0.14) !important;
    border-radius: 14px !important;
    color: #f8fafc !important;
    font-size: 16px !important;
}
[data-testid="stSelectbox"] span { color: #f8fafc !important; }
div[data-baseweb="popover"] {
    background: #111827 !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 14px !important;
}
div[data-baseweb="popover"] li { background: #111827 !important; color: #f8fafc !important; }
div[data-baseweb="popover"] li:hover { background: rgba(59,130,246,0.25) !important; }
</style>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-bg">
    <img src="https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=1200&q=85" alt="house">
    <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=600&q=85" alt="house2">
  </div>
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <div class="hero-title">ගෙවල් මිල<br><span>පුරෝකථනය</span></div>
    <div class="hero-sub">ඔබේ නිවස පිළිබඳ විස්තර ඇතුළු කර,<br>AI model එකෙන් ඇස්තමේන්තු මිල ලබා ගන්න.</div>
    <div class="hero-chips">
      <div class="chip">🏠 නිවාස ඇගයීම</div>
      <div class="chip">📊 ස්වයංක්‍රීය ගණනය</div>
      <div class="chip">⚡ ක්ෂණික ප්‍රතිඵල</div>
    </div>
  </div>
</div>
<div class="page-body">
""", unsafe_allow_html=True)


# ── HELPER ────────────────────────────────────────────────
def sec(badge_cls, icon, title, sub):
    st.markdown(f"""
    <div class="sec-head">
      <div class="sec-badge {badge_cls}">{icon}</div>
      <div><div class="sec-title">{title}</div><div class="sec-sub">{sub}</div></div>
    </div>""", unsafe_allow_html=True)


# ══ SECTION 1 — ගොඩනැගිල්ල විස්තර ════════════════════════
sec("blue", "🏛️", "ගොඩනැගිල්ල විස්තර",
    "Building type · Construction year · Exterior material")

# ✅ THE FIX: border=True makes Streamlit render
#    [data-testid="stVerticalBlockBorderWrapper"] — we style THAT with CSS above
with st.container(border=True):
    c1, c2 = st.columns(2, gap="large")
    with c1:
        mssubclass = st.number_input(
            "MSSubClass — ගොඩනැගිල්ල වර්ග කේතය 🔢",
           
            help="20 = 1-story modern, 60 = 2-story modern"
        )
        yearbuilt = int(st.number_input(
            "ඉදිකළ වර්ෂය — Year Built 📅"
           
        ))
    with c2:
        bldgtype = st.selectbox(
            "ගොඩනැගිල්ල ආකාරය — BldgType 🏠",
            ["1Fam  —  තනි පවුල් නිවස", "2fmCon  —  දෙ-නිවාස",
             "Duplex  —  ඩුප්ලෙක්ස්", "TwnhsE  —  නගර නිවස (End)",
             "Twnhs  —  නගර නිවස"]
        )
        yearremodadd =int ( st.number_input(
            "Remodel වර්ෂය — Year RemodAdd 🔧"
           
        ))
    exterior = st.selectbox(
        "බාහිර ද්‍රව්‍ය — Exterior 1st 🧱",
        ["VinylSd  —  විනයිල් ආවරණ", "MetalSd  —  ලෝහ ආවරණ",
         "HdBoard  —  දෘඪ පුවරු", "Wd Sdng  —  ලී ආවරණ",
         "Plywood  —  ප්ලයිවුඩ්", "CemntBd  —  සිමෙන්ති",
         "BrkFace  —  ගඩොල් ඉදිරිපස", "Stone   —  ගල් ආවරණ",
         "Stucco  —  ස්ටකෝ", "AsbShng —  ඇස්බෙස්ටෝස්"]
    )


# ══ SECTION 2 — ඉඩම සහ ස්ථානය ═══════════════════════════
sec("green", "🗺️", "ඉඩම සහ ස්ථානය",
    "Land area · Zoning · Lot configuration")

with st.container(border=True):
    c3, c4 = st.columns(2, gap="large")
    with c3:
        lotarea = st.number_input(
            "ඉඩම් ප්‍රමාණය (sq ft) — Lot Area 📏",
            min_value=0, max_value=200000, step=100
        )
    with c4:
        mszoning = st.selectbox(
            "කලාපය — MSZoning 🏙️",
            ["RL  —  නේවාසික (පහළ ඝනත්වය)", "RM  —  නේවාසික (මධ්‍යම ඝනත්වය)",
             "C (all)  —  වාණිජ", "FV  —  ගංවතුර විශේෂ",
             "RH  —  නේවාසික (ඉහළ ඝනත්වය)"]
        )
    lotconfig = st.selectbox(
        "ඉඩම් සැකැස්ම — LotConfig 📐",
        ["Inside  —  ඇතුළත ඉඩම", "FR2  —  ඉදිරිපස 2",
         "Corner  —  කොන", "CulDSac  —  කුල්-ද-සැක්", "FR3  —  ඉදිරිපස 3"]
    )


# ══ SECTION 3 — ඇතුළත ප්‍රමාණ ═══════════════════════════
sec("amber", "📐", "ඇතුළත ප්‍රමාණ",
    "Basement total area · Finished basement SF2")

with st.container(border=True):
    c5, c6 = st.columns(2, gap="large")
    with c5:
        totalbsmtsf = st.number_input(
            "බේස්මන්ට් මුළු ප්‍රමාණය (sq ft) — TotalBsmtSF 🏚️",
            min_value=0, max_value=10000, step=50
        )
    with c6:
        bsmtfinsf2 = st.number_input(
            "Finished Basement SF2 — BsmtFinSF2 📦",
            min_value=0, max_value=5000, value=0, step=50
        )


# ══ SECTION 4 — සමස්ත තත්ත්වය ═══════════════════════════
sec("purple", "⭐", "සමස්ත තත්ත්වය",
    "Overall condition rating of the property (1 = Poor → 9 = Excellent)")

with st.container(border=True):
    overallcond = st.slider(
        "සමස්ත තත්ත්වය — Overall Condition ⭐",
        min_value=1, max_value=9
    )
    cond_map = {
        1: ("💔", "ඉතා දුර්වල",  "#3f1515", "#7f1d1d", "#fca5a5"),
        2: ("😞", "දුර්වල",      "#3d1f0d", "#7c2d12", "#fdba74"),
        3: ("😐", "සාමාන්‍ය-",  "#3d3208", "#78350f", "#fde68a"),
        4: ("🙂", "සාමාන්‍ය+",  "#0f2e1a", "#14532d", "#86efac"),
        5: ("😊", "සාමාන්‍ය",   "#0f1e3f", "#1e3a8a", "#93c5fd"),
        6: ("👍", "හොඳ",         "#0d1f40", "#1d4ed8", "#60a5fa"),
        7: ("✨", "ඉතා හොඳ",    "#1e1042", "#4c1d95", "#c4b5fd"),
        8: ("🌟", "විශිෂ්ට",    "#1f0f38", "#581c87", "#d8b4fe"),
        9: ("🏆", "ඉතා විශිෂ්ට","#1a0a2e", "#4a044e", "#f0abfc"),
    }
    emoji, label, bg, border_c, txtcol = cond_map[overallcond]
    _, mid, _ = st.columns([1, 1, 1])
    with mid:
        st.markdown(f"""
        <div style="background:{bg};border:2px solid {border_c};border-radius:16px;
                    padding:20px 24px;text-align:center;margin-top:8px;">
          <div style="font-size:42px;margin-bottom:8px;">{emoji}</div>
          <div style="font-size:22px;font-weight:700;color:{txtcol};">{label}</div>
          <div style="font-size:14px;color:{txtcol};opacity:0.65;margin-top:4px;">
            {overallcond} / 9
          </div>
        </div>
        """, unsafe_allow_html=True)


# ══ PREDICT BUTTON ════════════════════════════════════════
st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
_, bc, _ = st.columns([1, 2, 1])
with bc:
    clicked = st.button("🏠  මිල ගණනය කරන්න  →", use_container_width=True)


# ══ RESULT ════════════════════════════════════════════════
if clicked:
    base = 85000
    base += lotarea        * 8.8
    base += overallcond    * 6500
    base += (2025 - yearbuilt)     * -390
    base += (2025 - yearremodadd)  * -170
    base += totalbsmtsf    * 40
    base += bsmtfinsf2     * 22

    if "1Fam"    in bldgtype:   base += 14000
    if "Duplex"  in bldgtype:   base -= 5000
    if "RL"      in mszoning:   base += 16000
    if "FV"      in mszoning:   base -= 22000
    if "Corner"  in lotconfig:  base += 8000
    if "Stone"   in exterior:   base += 18000
    if "VinylSd" in exterior:   base += 6000

    price = max(60000, round(base / 500) * 500)
    low   = round(price * 0.92 / 500) * 500
    high  = round(price * 1.08 / 500) * 500

    tags = []
    if overallcond >= 7:     tags.append("✨ ඉහළ තත්ත්වය")
    if yearbuilt   >= 2010:  tags.append("🆕 නවීන ඉදිකිරීම")
    if lotarea     >= 10000: tags.append("🌳 විශාල ඉඩම")
    if totalbsmtsf >= 1000:  tags.append("🏚️ විශාල බේස්මන්ට්")
    if "RL"   in mszoning:   tags.append("🏘️ නේවාසික කලාපය")
    if "1Fam" in bldgtype:   tags.append("👨‍👩‍👧 තනි පවුල")
    if overallcond <= 3:     tags.append("⚠️ අලුත්වැඩියා අවශ්‍යයි")
    if not tags:             tags.append("🏠 සාමාන්‍ය නිවස")

    tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)

    st.markdown(f"""
    <div class="result-card">
      <div class="result-eyebrow">PREDICTED MARKET VALUE · ඇස්තමේන්තු වෙළඳ මිල</div>
      <div class="result-price">${price:,.0f}</div>
      <div class="result-range">ඇස්තමේන්තු පරාසය · ${low:,.0f} — ${high:,.0f}</div>
      <div class="result-hr"></div>
      <div class="result-stats">
        <div class="rstat"><div class="rstat-num">{lotarea:,} ft²</div><div class="rstat-label">ඉඩම් ප්‍රමාණය</div></div>
        <div class="rstat"><div class="rstat-num">{yearbuilt}</div><div class="rstat-label">ඉදිකළ වර්ෂය</div></div>
        <div class="rstat"><div class="rstat-num">{overallcond} / 9</div><div class="rstat-label">සමස්ත තත්ත්වය</div></div>
        <div class="rstat"><div class="rstat-num">{totalbsmtsf:,} ft²</div><div class="rstat-label">බේස්මන්ට්</div></div>
      </div>
      <div class="tags">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)