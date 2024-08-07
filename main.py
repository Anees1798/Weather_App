import streamlit as st
import plotly.express as px
from backend import get_data

# Add Title, Text_input , slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")

place = st.text_input("place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="select the number of forecasted days")

option = st.selectbox("select data to view",
                      ("temperature", "sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# get the temperature/sky data
filtered_data = get_data(place, days)

# create a temperature plot
if place:
    if option == "temperature":
        temperature = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperature,
                         labels={"x": "Dates", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "sky":
        sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
        images ={"Clouds": "images/cloud.png", "Clear": "images/clear.png",
                 "Rain": "images/snow.png", "Snow": "images/snow.png"}
        sky_image = [images[condition] for condition in sky_condition]
        st.image(sky_image, width=115)







