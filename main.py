import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input("place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="select the number of forecasted days")

option = st.selectbox("select data to view",
                      ("temperature", "sky"))
st.subheader(f"{option} for the next {days} days in {place}")