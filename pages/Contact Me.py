import streamlit as st

st.set_page_config(
    page_title="Get in Touch!",
    page_icon="🤝",
)
st.balloons()
st.toast("Welcome", icon = "🎉")

st.markdown(
    """
    <a href="https://www.linkedin.com/in/sharazar/" target="_blank">
        <button style="
            background-color: #0073E6; 
            color: white; 
            border: none; 
            padding: 10px 20px; 
            text-align: center; 
            text-decoration: none; 
            font-size: 16px; 
            border-radius: 5px;
            cursor: pointer;
        ">
            Visit LinkedIn
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
