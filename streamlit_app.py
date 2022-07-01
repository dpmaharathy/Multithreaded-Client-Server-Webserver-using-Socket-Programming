import streamlit as st
import streamlit_lottie
import requests
from streamlit_lottie import st_lottie 
import requests
import os
from datetime import datetime
import time

user_api = "ee938cc3477bf4e627bb49eba464e06f"


st.set_page_config(page_title="Weather API Website", page_icon="cloud",layout="centered")

def load_animation(url):
    r=requests.get(url)
    return r.json()



lottie_code= load_animation("https://assets6.lottiefiles.com/packages/lf20_cHA3rG.json")

# HEADER
st.subheader("This is our Principles of Computer Systems II Project")
st.title("Weather API")


with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("How it Works")
        st.write('''Behind the web application, we use openweathermap's API to get the weather
                    for the user's desired city.''')

    with right_column:
        st.write('##')
        st_lottie(lottie_code,height=200,width=400,quality='high',key="watch_movie")


st.write("---")

location=st.text_input("Enter Name of City",key="city")
st.write("##")






ok1 = st.button("See Weather")
if ok1:
  with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)

    with right_column:
        lottie_code= load_animation("https://assets8.lottiefiles.com/private_files/lf30_lbtOZb.json")
        st_lottie(lottie_code,height=200,width=375,quality='high',key="load")

    with left_column:
        st.header("Getting Weather Data")
        time.sleep(1)
        st.write("Feeding Data to API")
        time.sleep(1)
        st.write("Retrieving Data...")
        time.sleep(1)

  complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
  api_link = requests.get(complete_api_link)
  api_data = api_link.json()

  #create variables to store and display data
  temp_city = ((api_data['main']['temp']) - 273.15)
  weather_desc = api_data['weather'][0]['description']
  hmdt = api_data['main']['humidity']
  wind_spd = api_data['wind']['speed']
  date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

  with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)

    with right_column:
      if 'clear' in weather_desc:
        lottie_code= load_animation("https://assets7.lottiefiles.com/temp/lf20_Stdaec.json")

      elif 'storm' in weather_desc:
        lottie_code= load_animation("https://assets7.lottiefiles.com/packages/lf20_ms53nlfm.json")

      elif 'cloud' or 'haze' or 'fog' in weather_desc:
        lottie_code= load_animation("https://assets7.lottiefiles.com/packages/lf20_eqms5fs5.json")

      elif 'rain' in weather_desc:
        lottie_code= load_animation("https://assets8.lottiefiles.com/packages/lf20_61b51axd.json")

      elif 'snow' in weather_desc:
        lottie_code= load_animation("https://assets8.lottiefiles.com/packages/lf20_rpuvbltp.json")
      

      st_lottie(lottie_code,height=200,width=375,quality='high',key="weather")

    with left_column:
      st.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
      st.write("-------------------------------------------------------------")
      st.write("Current temperature is: {:.2f} deg C".format(temp_city))
      st.write("Current weather desc  :",weather_desc)
      st.write("Current Humidity      :",hmdt, '%')
      st.write("Current wind speed    :",wind_spd ,'kmph')
  



