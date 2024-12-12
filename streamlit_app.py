import streamlit as st

st.title("This is a Title")
st.header("This is a Header")
st.checkbox(label="This is a checkbox", key="T&C accepted", help="Check to accept T&C")

radio_btn= st.radio(label = "In which country do you live?", options = ("US & Canada", "UK", "Europe", "Middle East"))
print(radio_btn)
def clicked():
    print("Button clicked")

btn = st.button("Click me", on_click = clicked)

select=st.selectbox("What is your favourite car", options=("BMW", "AUDI", "Ferrari"))

print(select)

multi_select = st.multiselect("What is your facourite Thing to drink?", options=("Cofee", "Tea", "Water", "Cold Drinks"))
st.write(multi_select)

allowed_img_ext = ["png", "jpg", "jpeg", "heic"]

uploaded_image = st.file_uploader("Upload an Image please", type=allowed_img_ext, accept_multiple_files= True)
if uploaded_image is not None:
    st.image(uploaded_image)

st.slider(label="This is a slider", min_value=1, max_value=10)

text_small = st.text_input(label="Enter ssome text", max_chars=10)
#text_big = st.text_area(label="Enter big text")
st.text(text_small)
print(text_small)