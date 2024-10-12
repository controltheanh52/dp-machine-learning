import streamlit as st
import pandas as pd

st.title('🎈 Machine learning App by Streamlit')

st.write('Hello, my name is The Anh')
st.info('this is app builds a ML model!')

read = pd.read_csv('https://raw.githubusercontent.com/controltheanh52/penguin/refs/heads/main/penguins_cleaned.csv')
read
