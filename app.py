# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import streamlit as st
import random

st.markdown("<style>body {background: linear-gradient(#141418,#3c3f45);background-size: 100% 100%;}</style>", unsafe_allow_html=True)

st.title("Hello from GrishteSync!")

if st.button('Click me'):
    st.write(random.choice(['🐶', '🐱', '🐔', '🐷', '🐴']))

st.markdown("<footer><p style='text-align: center;'>Made with GrishteSync | Suryasticsai | suryasticsai@gmail.com<br><img src='https://i.ibb.co/RGmb4FKk/1781072041102.png' width='50'></p></footer>", unsafe_allow_html=True)