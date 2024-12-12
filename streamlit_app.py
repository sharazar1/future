import streamlit as st

st.title("This is a Title")
st.header("This is a Header")
st.checkbox(label="This is a checkbox", key="T&C accepted", help="Check to accept T&C")

radio_btn= st.radio(label = "In which country do you live?", options = ("US & Canada", "UK", "Europe", "Middle East"))
print(radio_btn)