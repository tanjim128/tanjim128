import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is my first Streamlit app.')

import streamlit as st

st.title('Hello Streamlit!')
st.write('Welcome to my Streamlit app.')

# Adding a simple interactive widget
name = st.text_input('Enter your name:')
if name:
    st.write(f'Hello {name}!')
