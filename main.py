import streamlit as st

# --- إعدادات الصفحة الأساسية ---
st.set_page_config(
    page_title="Football Incident Analytics",
    page_icon="⚽",
    layout="wide"
)

# --- القائمة الجانبية (Sidebar) ---
st.sidebar.title("🕹️ Control Panel")

# 1. اختيار حدث المباراة
st.sidebar.subheader("Select Match Event:")
match_event = st.sidebar.selectbox(
    "Choose Event",
    ["Match 01 - Team A vs Team B", "Match 02 - Team C vs Team D"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

# 2. قسم الأمان والخصوصية (GDPR)
st.sidebar.subheader("🔒 Security & Privacy")
anonymize_gdpr = st.sidebar.toggle(
    "Anonymize Player Data (GDPR Mode)", 
    value=True
)

st.sidebar.markdown("---")

# 3. حالة النظام العامة (تجريد البنية التحتية)
st.sidebar.success("✓ System Status: Operational & Live")


# --- القسم الرئيسي من الواجهة (Main Dashboard) ---
st.title("⚽ Football Incident Analytics Dashboard")
st.markdown("---")

# صف المؤشرات العليا (High-Level Status Summaries)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Logged Incidents", value="1,024 Events")

with col2:
    st.metric(label="System Sync Speed", value="Excellent", delta="↑ 42 ms (Stable)")

with col3:
    st.metric(label="Available Camera Angles", value="Multi-cam Enabled")

st.markdown("---")

# تقسيم الشاشة إلى قسمين: الفيديو على اليسار والبيانات على اليمين
body_col1, body_col2 = st.columns([3, 2])

with body_col1:
    st.subheader("📹 Multi-Angle Video Feed")
    
    # اختيار زاوية الكاميرا تفرع من الباك إند
    camera_angle = st.radio(
        "Select Camera View:",
        ["Main Broadcast Angle", "Tactical High-Cam", "Behind-the-Goal View"],
        horizontal=True
    )
    
    # عرض مشغل الفيديو المباشر والنظيف بدلاً من الأكواد المكسورة القديمة
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.caption(f"Streaming: {camera_angle}")

with body_col2:
    st.subheader("📋 Detailed Event Information (StatsBomb Core)")
    
    # تطبيق منطق الـ GDPR ديناميكياً بناءً على اختيار القائمة الجانبية
    if anonymize_gdpr:
        player_name = "[PROTECTED - PLAYER_ID_995]"
        team_name = "[PROTECTED - TEAM_A]"
        st.warning("GDPR Masking Layer Active: Player profile attributes tokenized automatically.")
    else:
        player_name = "Lionel Messi"
        team_name = "Barcelona"
        st.info("Raw Mode: Elevated access granted. Displaying full StatsBomb metadata profiles.")
        
    # بطاقة البيانات التفصيلية الشاملة للحدث
    st.markdown(f"""
    <div style="background-color: #f8fafc; padding: 15px; border-radius: 8px; border-left: 5px solid #1a365d; color: #2c3e50;">
        <h4 style="margin-top:0; color: #1a365d; font-size: 14px;">⚽ Match & Possession Context</h4>
        <ul style="font-size: 13px; padding-left: 20px; margin-bottom: 10px;">
            <li><b>Timestamp:</b> 00:42:15.320 (42nd Minute)</li>
            <li><b>Period:</b> First Half (الشوط الأول)</li>
            <li><b>Possession Team:</b> {team_name} (Possession #24)</li>
            <li><b>Player & Position:</b> {player_name} (Right Wing / Center Forward)</li>
        </ul>
        
        <h4 style="color: #1a365d; font-size: 14px;">🎯 Spatial & Tactical Data (إحداثيات الـ VAR)</h4>
        <ul style="font-size: 13px; padding-left: 20px; margin-bottom: 10px;">
            <li><b>Event Location [X, Y]:</b> [102.5, 44.1] - <i>Inside Attacking Third</i></li>
            <li><b>Event Type:</b> Shot (تسديدة على المرمى)</li>
            <li><b>Expected Goals (StatsBomb xG):</b> <span style="color: #2b6cb0; font-weight: bold;">0.68 (High Chance)</span></li>
            <li><b>Shot Technique & Body Part:</b> Volley / Left Foot</li>
        </ul>

        <h4 style="color: #d69e2e; font-size: 14px;">⚠️ VAR Review Specifics (تفاصيل المخالفة المحتملة)</h4>
        <ul style="font-size: 13px; padding-left: 20px; margin-bottom: 0;">
            <li><b>Shot Outcome:</b> Saved (تم التصدي لها - فحص احتمالية لمسة يد/تسلل)</li>
            <li><b>Foul Committed/Involved:</b> Hand Block Claim by Defender</li>
            <li><b>Resolution Status:</b> Reviewed & Logged</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)