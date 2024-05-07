import streamlit as st
from streamlit_chat import message
import requests
import chat
from analysis import analyze
from streamlit_lottie import st_lottie
import json
st.set_page_config(
    page_title="Crop Recommendation Bot",
    page_icon=":robot:"
)

st.header("Crop Recommendation Bot")

#to upload from website
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    


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



if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hello!", key="input")
    return input_text 


user_input = get_text()
if user_input=="suggest a best suited crop":
    form = st.form("my_form",clear_on_submit=False)
    n = form.slider('Select the value of Nitrogen Level',
    0, 150)
    p = form.slider('Select the value of Phosphorus Level',
    0, 100)
    k = form.slider('Select the value of Potassium Level',
    0, 100)
    temp = form.slider('Select the value of Temperature Level',
    0.0, 50.0)
    humidity = form.slider('Select the value of Humidity Level',
    0.0, 100.0)
    ph = form.slider('Select the value of PH Level',
    0.0, 10.0)
    rainfall = form.slider('Select the value of Rainfall Level',
    0.0, 200.0)
    submit = form.form_submit_button("Submit")
    if submit:
        st.session_state.past.append("suggest me a best suited crop")
        best_crop = "The best crop to grow with these parameters is " + analyze(n,p,k,temp,humidity,ph,rainfall)
        st.session_state.generated.append(best_crop)
    
elif user_input!="suggest me a best suited crop":
    print(chat.initialization(user_input))
    st.session_state.past.append(user_input)
    st.session_state.generated.append(chat.initialization(user_input))

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))