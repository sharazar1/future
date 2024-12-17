import streamlit as st
import time
from matplotlib import pyplot as plt
import numpy as np

# from datetime import time
st.title("This is a Title")
st.header("This is a Header")
st.checkbox(label="This is a checkbox", key="T&C accepted", help="Check to accept T&C")

radio_btn = st.radio(label="In which country do you live?", options=("US & Canada", "UK", "Europe", "Middle East"))
print(radio_btn)


def clicked():
    print("Button clicked")


btn = st.button("Click me", on_click=clicked)

select = st.selectbox("What is your favourite car", options=("BMW", "AUDI", "Ferrari"))

print(select)

multi_select = st.multiselect("What is your facourite Thing to drink?",
                              options=("Cofee", "Tea", "Water", "Cold Drinks"))
st.write(multi_select)

allowed_img_ext = ["png", "jpg", "jpeg", "heic"]

uploaded_image = st.file_uploader("Upload an Image please", type=allowed_img_ext, accept_multiple_files=True)
if uploaded_image is not None:
    st.image(uploaded_image)

st.slider(label="This is a slider", min_value=1, max_value=10)

text_small = st.text_input(label="Enter ssome text", max_chars=10)
# text_big = st.text_area(label="Enter big text")
st.text(text_small)
print(text_small)
dt = st.date_input("Enter your date")
tm = st.time_input("Enter Time")
# Progress Bars
bar = st.progress(50)
for i in range(10):
    bar.progress((i + 1) * 10)
    time.sleep(1)

st.markdown("<h1 style ='text-align: center;'>Contact Me</h1>", unsafe_allow_html=True)
# 2 methods for forms
form1 = st.form("Contact")

form1.text_input("Your Name")
# Always create submit button
form1._form_submit_button("Submit Form")

# 2nd method
with st.form("Form 2", clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    st.text_input("Email Address!")
    st.text_input("Password")
    st.text_input("input password again")
    s_state = st.form_submit_button("Submit")
    if s_state:
        if f_name == "" and l_name == "":
            st.warning("Please check all fields")
        else:
            st.success("Submitted Successfully!")

opt = st.sidebar.radio("Select any Graph", options=("Line", "Bar"))
x = np.linspace(0,10,100)
bar_x = np.array([1,2, 3,4,5])
if opt == "Line":
    st.markdown("<h1 style='text-align: center;'>Line Chart</h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x, np.sin(x))
    plt.plot(x,np.cos(x), '--')
    st.write(fig)
elif opt == "Bar":
    st.markdown("<h1 style='text-align: center;'>Bar Chart</h1>")
    fig = plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.bar(x, x * 10)
    st.write(fig)