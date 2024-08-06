import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="select the number of forecasted days")

option = st.selectbox("select data to view",
                      ("temperature", "sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["22-08-2024", "23-08-2024", "25-08-2024"]
    temperature = [10,12,17]
    temperature = [i * days for i in temperature]
    return dates, temperature


d, t = get_data(days)

figure = px.line(x=d, y=t,
        labels={"x": "Dates", "y": "Temperature (C)"})

st.plotly_chart(figure)