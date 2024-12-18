from random import randint

import pandas as pd
import streamlit as st
import numpy as np
import time
import altair as alt

import streamlit as st

st.header('st.write')
st.subheader('Text input')
st.write('*Hello*, *World!* :sunglasses:')
st.subheader('Display numbers')
st.write(1234)
st.subheader('Display DataFrame')
data=pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10,20,30,40]
})
st.write(data)
#st.subheader('Accept multiple arguments')
st.write('Below is DataFrame:')
st.write(data)
st.write('Above is dataframe:')
st.subheader('Display Charts')

data_chart=pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c']
)
chart=alt.Chart(data_chart).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.write(chart)