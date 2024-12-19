import streamlit as st
import pandas as pd
import numpy as np


st.header('st.multiselect')
value=st.multiselect('What are you favorite colors?', options=['Green', 'Yellow', 'Red', 'Blue'])
st.write('You selected:',value)