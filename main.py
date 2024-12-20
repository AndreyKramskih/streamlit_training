import streamlit as st

st.title('st.secrets')

st.write(st.secrets["my_cool_secrets"]["message"])