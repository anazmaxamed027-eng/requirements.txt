import streamlit as st
import pandas as pd
import random
from streamlit_option_menu import option_menu

# Habaynta shaashadda moobilka
st.set_page_config(page_title="Forex AI Agent", page_icon="🤖", layout="centered")

# =========================================================
# NIDAAMKA LOGIN-KA (PASSWORD PROTECTION)
# =========================================================
# Meeshaan ku qor password-ka aad rabto saxiib (Hadda waa 'saxiib123')
PASSWORD_UKU_TALAGALAY = "pio54321"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Forex AI - Login")
    st.write("Saxiib, fadlan qor furaha sirta ah si aad u gasho dashboard-ka.")
    
     user_password = st.text_input("Password-ka", type=("default")
    if st.button("Gasho (Login)"):
        if user_password == PASSWORD_UKU_TALAGALAY:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Password-ku waa khalad saxiib, dib u tijaabi!")
    st.stop() # Wixii koodh ah oo ka dambeeya halkan ma fulayo ilaa laga login gareeyo

# =========================================================
# WIXII KA DAMBEEYA HALKAN WAA WEBSITE-KII CAADIGA AHAA
# =========================================================
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {bottom: 60px;}
    </style>
""", unsafe_allow_html=True)

# 1. TIKTOK-STYLE NAVIGATION BAR
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
        "nav-link-selected": {"background-color": "#ff0055"}, 
    }
)

# [Koodhkii kale ee pajjada sidiisii ayuu u qoran yahay...]
if selected == "Home":
    st.title("🏠 AI Trading Monitor")
    st.write("Saxiib, halkaan waxaad ka arki kartaa xawaaraha iyo natiijada trades-ka rasmiga ah.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Trades", value="42", delta="Maanta +5")
    col2.metric(label="Win / Loss Rate", value="76% / 24%", delta="Faa'iido")
    col3.metric(label="Xawaaraha Khadka", value="12 ms", delta="Aad u dhakhso badan", delta_color="inverse")
    
    st.markdown("---")
    st.subheader("📊 Live Positions")
    trades_data = {"Pair": ["EURUSD", "GBPUSD"], "Nooca": ["BUY", "SELL"], "Lots": [0.50, 0.30], "P&L ($)": [65.00, -14.20]}
    st.dataframe(pd.DataFrame(trades_data), use_container_width=True)

elif selected == "AI Chat":
    st.title("💬 Kala Sheekayso AI Agent-ka")
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [{"role": "assistant", "content": "Halow saxiib! Maxaad rabaa inaad i weyddiiso maanta?"}]
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]): st.write(msg["content"])
    if user_input := st.chat_input("Qor fariintaada..."):
        with st.chat_message("user"): st.write(user_input)
        st.session_state.chat_messages.append({"role": "user", "content": user_input})
        with st.chat_message("assistant"): st.write("Saxiib, waan helay fariintaada.")
        st.session_state.chat_messages.append({"role": "assistant", "content": "Saxiib, waan helay fariintaada."})

elif selected == "Journal":
    st.title("📓 AI Journal & Error Fixer")
    st.error("❌ FOMO Trade (GBPUSD): -1.5% Risk Over-exposure.")
    user_note = st.text_area("Halkan dhiirigelin ugu reeb AI-gaaga:")
    if st.button("Save Note"): st.success("Waa la kaydiyey!")

elif selected == "VPS Connect":
    st.title("⚙️ VPS & AI Agent Integration")
    vps_ip = st.text_input("VPS IP Address")
    api_key = st.text_input("Broker API Token", type="password")
    if st.button("Connect Live Bot 🚀", type="primary"): st.success("Waa la xiriiriyey!")
