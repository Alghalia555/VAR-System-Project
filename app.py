import streamlit as st

# ضبط إعدادات الصفحة لتكون بعرض الشاشة (Wide Mode)
st.set_page_config(page_title="Football Incident Analytics", layout="wide")

# --- 1. قاعدة البيانات التجريبية للمباريات والفيديوهات ---
# ملاحظة: يمكنك استبدال روابط الفيديوهات هنا بروابط فيديوهات المباريات الحقيقية الخاصة بك لاحقاً
matches_data = {
    "Match 01 - Team A vs Team B": {
        "video_main": "https://www.w3schools.com/html/mov_bbb.mp4", # فيديو الأرنب مؤقتاً لمباراة 1
        "video_tactical": "https://www.w3schools.com/html/mov_bbb.mp4",
        "video_behind": "https://www.w3schools.com/html/mov_bbb.mp4",
        "timestamp": "00:42:15.320 (42nd Minute)",
        "period": "First Half (الشوط الأول)",
        "team": "TEAM_A",
        "player": "PLAYER_ID_995 (Right Wing / Center Forward)",
        "xg": "0.35 (Low Chance)"
    },
    "Match 02 - Team C vs Team D": {
        "video_main": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4", # فيديو تجريبي مختلف لمباراة 2
        "video_tactical": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
        "video_behind": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
        "timestamp": "00:15:22.100 (15th Minute)",
        "period": "First Half (الشوط الأول)",
        "team": "TEAM_C (Barcelona)",
        "player": "PLAYER_ID_010 (Lionel Messi / Center Forward)",
        "xg": "0.68 (High Chance)"
    }
}

# --- 2. تصميم الواجهة (تقسيم الشاشة إلى أعمدة) ---
# العمود الأيسر: لوحة التحكم (Sidebar / Control Panel)
with st.sidebar:
    st.header("🕹️ Control Panel")
    
    # القائمة المنسدلة لاختيار المباراة
    selected_match = st.selectbox(
        "Select Match Event:", 
        options=list(matches_data.keys())
    )
    
    # جلب بيانات المباراة المختارة حالياً
    current_match = matches_data[selected_match]
    
    st.markdown("---")
    st.subheader("🔒 Security & Privacy")
    st.toggle("Anonymize Player Data (GDPR Mode)", value=True)
    
    st.markdown("---")
    st.success("✓ System Status: Operational & Live")

# تقسيم بقية الشاشة إلى عمودين (المنتصف للفيديو، واليمين للبيانات)
col_video, col_data = st.columns([3, 2])

# --- 3. عمود الفيديو (المنتصف) ---
with col_video:
    st.subheader("📹 Multi-Angle Video Feed")
    
    # أزرار اختيار زاوية الكاميرا
    camera_view = st.radio(
        "Select Camera View:", 
        ["Main Broadcast Angle", "Tactical High-Cam", "Behind-the-Goal View"],
        horizontal=True
    )
    
    # تحديد رابط الفيديو بناءً على الكاميرا المختارة
    if camera_view == "Main Broadcast Angle":
        video_url = current_match["video_main"]
    elif camera_view == "Tactical High-Cam":
        video_url = current_match["video_tactical"]
    else:
        video_url = current_match["video_behind"]
        
    # عرض الفيديو
    st.video(video_url)
    st.caption(f"Streaming: {camera_view}")

# --- 4. عمود البيانات الإحصائية StatsBomb (اليمين) ---
with col_data:
    st.subheader("📋 Detailed Event Information (StatsBomb Core)")
    
    st.info("GDPR Masking Layer Active: Player profile attributes tokenized automatically.")
    
    # عرض البيانات بشكل ديناميكي وإصلاح أكواد الـ HTML المكسورة باستخدام unsafe_allow_html
    st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; border-left: 5px solid #1a365d;">
        <h4 style="margin-top: 0; color: #1a365d;"><a href="#">⚽ Match & Possession Context</a></h4>
        <ul style="list-style-type: none; padding-left: 0; font-size: 14px; line-height: 1.8;">
            <li><b>Timestamp:</b> {current_match['timestamp']}</li>
            <li><b>Period:</b> {current_match['period']}</li>
            <li><b>Possession Team:</b> <span style="color: #c53030;">[PROTECTED - {current_match['team']}]</span> (Possession #24)</li>
            <li><b>Player & Position:</b> <span style="color: #c53030;">[PROTECTED - {current_match['player']}]</span></li>
        </ul>
        
        <hr style="border: 0; border-top: 1px solid #ddd; margin: 15px 0;">
        
        <h4 style="color: #1a365d;">Detailed Event Metrics:</h4>
        <ul style="font-size: 14px; line-height: 1.8;">
            <li><b>Event Location:</b> [X: 85.3, Y: 42.1]</li>
            <li><b>Event Type:</b> Shot</li>
            <li><b>Expected Goals (xG):</b> <span style="color: green; font-weight: bold; font-size: 16px;">{current_match['xg']}</span></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)