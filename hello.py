import streamlit as st
import numpy as np
import pandas as pd

st.header("My first Streamlit App")

option = st.sidebar.selectbox(
    'Choose an option',
     ['Greet', 'Display a picture'])


if option == 'Greet':
    name = st.text_input('What is your name?')
    if name == '':
        st.write('')
    else:
        st.write(f'# Hello, {name}, have a great day!')
        

else:
    try:
        url = st.text_input('Insert the URL of the image')
        st.image(url)
    except:
        st.error('Please paste a URL')
