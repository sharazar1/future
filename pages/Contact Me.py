import streamlit as st

st.set_page_config(
    page_title="Get in Touch!",
    page_icon="🤝",
)

if st.button("Go to Google"):  # Create the button
    st.markdown(
        """
        <a href="https://https://www.linkedin.com/in/sharazar/" target="_blank"></a>
        """,
        unsafe_allow_html=True,
    )
