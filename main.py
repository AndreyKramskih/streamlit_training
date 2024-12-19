import streamlit as st
import pandas as pd
import numpy as np


st.header('st.checkbox')
st.write('What would you like to order?')
ice_cream=st.checkbox('Ice cream')
coffee=st.checkbox('Coffee')
cola=st.checkbox("Cola")

if ice_cream:
    st.write("Great! Here's some more 🍦")
if coffee:
    st.write("Okay, here's some coffee ☕")
if cola:
    st.write("Here you go 🥤")
