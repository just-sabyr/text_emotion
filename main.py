# Import the modules
import text2emotion as te
import streamlit as st

text = st.text_input('Enter text to analize: ')

if st.button('Find emotions in the text'):
    st.text(te.get_emotion(text))

