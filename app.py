import streamlit as st
import pandas as pd
import random
from streamlit_option_menu import option_menu

# Habaynta shaashadda moobilka
st.set_page_config(page_title="Forex AI Agent", page_icon="🤖", layout="centered")

# Habaynta CSS si loogu qariyo menu-yada kale, loona weyneeyo qoraalka hoose
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {bottom: 60px;}
    </style>
""", unsafe_allow_html=True)

# 1. TIKTOK-STYLE NAVIGATION BAR (XAGGA HOOSE AYUU KAN KA SOO MUUQAN DOONAA)
# Fiiro gaar ah: Streamlit wuxuu ku muujiyaa navigation-ka meesha uu koodhku kaga jiro, laakiin moobilka aad ayuu ugu habboon yahay.
selected = option_menu(
    menu_title=None,
    options=["Home", "AI Chat", "Journal", "VPS Connect"],
    icons=["house", "chat-dots", "book", "cpu"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#0e1117"},
        "icon": {"color": "#00ffcc", "font-size": "20px"}, 
        "nav-link": {"font-size": "14px", "text-align": "center", "margin":"0px", "--hover-color": "#262730"},
        "nav-link-selected": {"background-color": "#ff0055"}, # Midabka cas ee TikTok-ka u eg
    }
)

# =========================================================
# 2. PAGE 1: HOME (DASHBOARD & STATS)
# =========================================================
if selected == "Home":
    st.title("🏠 AI Trading Monitor")
    st.write("Saxiib, halkaan waxaad ka arki kartaa xawaaraha iyo natiijada trades-ka rasmiga ah.")
    
    # Kaararka Natiijooyinka (Stats Cards)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Trades", value="42", delta="Maanta +5")
    col2.metric(label="Win / Loss Rate", value="76% / 24%", delta="Faa'iido")
    col3.metric(label="Xawaaraha Khadka", value="12 ms", delta="Aad u dhakhso badan", delta_color="inverse")
    
    st.markdown("---")
    st.subheader("📊 Live Positions")
    trades_data = {
        "Pair": ["EURUSD", "GBPUSD"],
        "Nooca": ["BUY", "SELL"],
        "Lots": [0.50, 0.30],
        "P&L ($)": [65.00, -14.20]
    }
    st.dataframe(pd.DataFrame(trades_data), use_container_width=True)

# =========================================================
# 3. PAGE 2: AI CHAT (KALA SHEEKAYSO AI-GA)
# =========================================================
elif selected == "AI Chat":
    st.title("💬 Kala Sheekayso AI Agent-ka")
    st.write("Weaydii AI-ga wax kasta oo ku saabsan suuqa ama go'aamadii uu qaatay.")
    
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Halow saxiib! Waxaan baaray suuqa. EURUSD waxaan u iibsaday sababtoo ah waxaa jirtay Liquidity sweep iyo RSI divergence. Maxaad kale oo aad rabtaa inaad ogaato?"}
        ]
        
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    if user_input := st.chat_input("Qor fariintaada..."):
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.chat_messages.append({"role": "user", "content": user_input})
        
        with st.chat_message("assistant"):
            st.write("Saxiib, xogta aan hadda falanqeeyey waxay muujinaysaa in saamaynta aad sheegtay ay sax tahay. Waxaan journal-ka ku dhex qoray inaan dhowro xeerkaas.")
        st.session_state.chat_messages.append({"role": "assistant", "content": "Saxiib, xogta aan hadda falanqeeyey waxay muujinaysaa in saamaynta aad sheegtay ay sax tahay. Waxaan journal-ka ku dhex qoray inaan dhowro xeerkaas."})

# =========================================================
# 4. PAGE 3: JOURNAL & MATHEMATICS (KHALADAADKA IYO XISAABTA)
# =========================================================
elif selected == "Journal":
    st.title("📓 AI Journal & Error Fixer")
    st.write("Meesha uu AI-gu ku xisaabiyo khaladka uu galay si uu cashar uga barto.")
    
    st.subheader("🚨 Khaladaadkii ugu dambeeyey ee la xisabay:")
    st.error("❌ FOMO Trade (GBPUSD): Waxaan galay trade-ka anigoon sugin in shumaca (candle) uu xirmo. Khaladka xisaabta: -1.5% Risk Over-exposure.")
    st.info("💡 Sidee loo saxayaa? AI wuxuu dib u habayn ku sameeyey koodhka dhexdiisa badhanka `Execution_Lock = True` ilaa shumacu ka dhamaanayo.")
    
    st.markdown("---")
    st.subheader("✍️ Qor Journal Custom ah (Notes)")
    user_note = st.text_area("Halkan adiguna qoraal ama dhiirigelin ugu reeb AI-gaaga:")
    if st.button("Save Note to AI Memory"):
        st.success("Waa la kaydiyey saxiib! AI-gu waa uu akhriyey fariintaada.")

# =========================================================
# 5. PAGE 4: VPS CONNECT (XIRIIRINTA HADHOW)
# =========================================================
elif selected == "VPS Connect":
    st.title("⚙️ VPS & AI Agent Integration")
    st.write("Saxiib, marka aad lacag hesho, halkan ayaan ka kicin doonaa automation-ka rasmiga ah.")
    
    st.info("🔒 Xaaladda Hadda: 'Sandbox Mode' (Dashboard-ku wuxuu ku jiraa hab tijaabo ah).")
    
    st.subheader("🔗 Ku xir Server-kaaga rasmiga ah")
    vps_ip = st.text_input("VPS IP Address", placeholder="e.g., 192.168.1.100")
    api_key = st.text_input("Broker API Token / MT5 Login", type="password")
    
    if st.button("Connect Live Bot 🚀", type="primary"):
        if vps_ip and api_key:
            st.success("Hambalyo! AI Agent-kaaga waxaa loo wareejiyey VPS-ka wuxuuna hadda u shaqaynayaa 24/7.")
        else:
            st.warning("Fadlan buuxi xogta VPS-ka si xiriirku u guulaysto.")
