import streamlit as st
from streamlit_chat import message
import requests
import chat
from analysis import analyze
from streamlit_lottie import st_lottie
import json
st.set_page_config(
    page_title="Yield Prediction Bot",
    page_icon=":robot:"
)

st.header("Yield Prediction Bot")

#to upload from website
# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
    


# lottie_img = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_CgexnTerux.json")
# st_lottie(
#     lottie_img,
#     speed=1,
#     reverse=False,
#     loop=True,
#     quality="medium", # medium ; high
#     height=250,
#     width=350,
#     key=None,
# )

# st.markdown("[Github](https://github.com/)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ", "Hello!", key="input")
    return input_text 


user_input = get_text()
if user_input=="Predict the yield":
    form = st.form("my_form",clear_on_submit=False)
    item = form.text_input('Item:', help='Enter the crop item (e.g., maize, potatoes)')
    rain_fall = form.number_input('Average Rainfall (mm/year):', help='Enter the average rainfall in millimeters per year')
    pesticides = form.number_input('Pesticides (tonnes):', help='Enter the amount of pesticides used in tonnes')
    avg_temp = form.number_input('Average Temperature (°C):', help='Enter the average temperature in degrees Celsius')

    submit = form.form_submit_button("Submit")
    if submit:
        st.session_state.past.append("Predict the yield")
        yieldp = f"The yield for these parameters is {analyze(item, rain_fall, pesticides, avg_temp)} hg/ha"
        st.session_state.generated.append(yieldp)
    
elif user_input!="Predict the yield":
    print(chat.initialization(user_input))
    st.session_state.past.append(user_input)
    st.session_state.generated.append(chat.initialization(user_input))

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))