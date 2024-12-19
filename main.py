import streamlit as st

from datetime import date, time, datetime

st.header('st.slider')
age=st.slider('How old are you?', 0,130,25)
st.write('I am',age,'years old')

st.header('Range slider')
select=st.slider('Select a range of values',0,100,[25,75])
st.write('Values:',select)

st.header('Range time slider')
timerange=st.slider('Shedule your appointment',value=(time(11,30), time(12, 45)))
st.write('You`re sheduled for:',timerange)

st.header('Datetime slider')
daterange=st.slider(
    'When do you start?',
    value=datetime(2020,1, 1, 9, 30 ),
    format='MM/DD/YY - hh:mm'
)
st.write('Start time:',daterange)
