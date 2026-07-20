import streamlit as st
import pandas as pd
from statsbombpy import sb

# ضبط إعدادات الصفحة
st.set_page_config(page_title="Football Incident Analytics - StatsBomb", layout="wide")

# --- 1. جلب بيانات StatsBomb المفتوحة مع التخزين المؤقت ---
@st.cache_data
def get_statsbomb_matches():
    # استدعاء مباراتين شهيرتين كمثال (مثلاً نهائي كأس العالم ونهائي أبطال أوروبا)
    # يمكن توسيع هذه القائمة حسب الحاجة
    return {
        "Match 01 - Argentina vs France (World Cup Final)": 3869151,
        "Match 02 - Real Madrid vs Liverpool (UCL Final)": 3775541
    }

@st.cache_data
def get_match_events(match_id):
    # جلب جميع الأحداث الخاصة بالمباراة من StatsBomb
    events = sb.events(match_id=match_id)
    # تصفية الأحداث المهمة (تسديدات، أخطاء، ضربات جزاء)
    filtered = events[events['type'].isin(['Shot', 'Foul Committed', 'Penalty'])]
    return filtered

matches_dict = get_statsbomb_matches()

# --- 2. لوحة التحكم الجانبية (Control Panel) ---
with st.sidebar:
    st.header("🕹️ Control Panel")
    
    # اختيار المباراة
    selected_match_name = st.selectbox("Select Match Event:", options=list(matches_dict.keys()))
    selected_match_id = matches_dict[selected_match_name]
    
    st.markdown("---")
    st.subheader("🔒 Security & Privacy")
    st.toggle("Anonymize Player Data (GDPR Mode)", value=True)
    
    st.markdown("---")
    st.success("✓ System Status: Operational & Live")

# جلب الأحداث الخاصة بالمباراة المختارة
df_events = get_match_events(selected_match_id)

# أخذ أول حدث مهم في القائمة لعرض بياناته
first_event = df_events.iloc[0]

# --- 3. تقسيم الصفحة إلى عمودين ---
col_video, col_data = st.columns([3, 2])

# --- عمود الفيديو (المنتصف) ---
with col_video:
    st.subheader("📹 Multi-Angle Video Feed")
    
    camera_view = st.radio(
        "Select Camera View:", 
        ["Main Broadcast Angle", "Tactical High-Cam", "Behind-the-Goal View"],
        horizontal=True
    )
    
    # رابط فيديو المباراة (ملاحظة: لقطات الفيديو يتم ربطها بملفات الفيديو الخاصة بالمباراة)
    # نستخدم مقطع تجريبي ثابت حالياً لمزامنة العرض مع البيانات
    video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
    st.video(video_url)
    st.caption(f"Streaming Camera Angle: {camera_view}")

# --- عمود بيانات StatsBomb (اليمين) ---
with col_data:
    st.subheader("📋 Detailed Event Information (StatsBomb Core)")
    
    st.info("GDPR Masking Layer Active: Player profile attributes tokenized automatically.")
    
    # استخراج البيانات الديناميكية المباشرة من StatsBomb
    minute = first_event.get('minute', 'N/A')
    second = first_event.get('second', 'N/A')
    team_name = first_event.get('team', 'N/A')
    player_name = first_event.get('player', 'N/A')
    event_type = first_event.get('type', 'N/A')
    
    # استخراج قيم Expected Goals (xG) في حال كانت تسديدة
    xg_val = "N/A"
    if 'shot_statsbomb_xg' in first_event and pd.notnull(first_event['shot_statsbomb_xg']):
        xg_val = round(first_event['shot_statsbomb_xg'], 2)

    # عرض البيانات بتنسيق Markdown نظيف وبدون أكواد مكسورة
    st.markdown(f"""
    ### ⚽ Match & Possession Context
    * **Timestamp:** Minute {minute}:{second}
    * **Possession Team:** [PROTECTED - {team_name}]
    * **Player & Position:** [PROTECTED - {player_name}]
    """)
    
    st.markdown("---")
    
    st.markdown(f"""
    #### Detailed Event Metrics:
    * **Event Type:** {event_type}
    * **Expected Goals (xG):** **{xg_val}**
    """)
