import streamlit as st
import pandas as pd
import numpy as np


st.header('Select box')
check=st.selectbox('What is your favorite color?', options=['Red', 'Blue', 'Green'])
st.write('Your favorite color is', check)
