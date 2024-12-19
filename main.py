import streamlit as st
import pandas as pd
import numpy as np


st.header('Line chart')
chart=pd.DataFrame(
    np.random.randn(20,4),
    columns=['a', 'b', 'c', 'd']
)

st.line_chart(chart)