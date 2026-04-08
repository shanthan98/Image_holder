import streamlit as st

# Page config
st.set_page_config(
    page_title="Español - Coming Soon",
    layout="centered"
)

# Styling (optional but makes it look premium)
st.markdown("""
    <style>
    .main {
        text-align: center;
        padding-top: 100px;
    }
    .title {
        font-size: 42px;
        font-weight: bold;
        color: #4B3F72;
    }
    .text {
        font-size: 18px;
        margin-top: 20px;
    }
    .footer {
        margin-top: 40px;
        font-size: 14px;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

# Content
st.markdown('<div class="title">🌐 Español</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="text">'
    'Spanish version coming soon.<br><br>'
    'Versión en español próximamente.<br><br>'
    'We are working to make this dashboard accessible in Spanish.<br>'
    'Estamos trabajando para ofrecer este tablero en español.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="footer">Expected release: Summer 2026</div>',
    unsafe_allow_html=True
)

# Back button
st.markdown("---")

dashboard_url = "https://app.powerbigov.us/view?r=eyJrIjoiNGU4Y2U4ZTctOTFmNS00NDA5LWI5ODMtZjY4YjY5YWM0ZDNlIiwidCI6IjVjNWUxOWY2LWE2YWItNGI0NS1iMWQwLWJlNDYwOGE5YTY3ZiJ9"

st.markdown(f"""
<a href="{dashboard_url}" target="_blank">
    <button style="
        padding:10px 20px;
        border-radius:8px;
        border:1px solid #ccc;
        background-color:#f5f5f5;
        font-size:16px;
        cursor:pointer;">
        ⬅ Back to Dashboard
    </button>
</a>
""", unsafe_allow_html=True)
