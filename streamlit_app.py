import streamlit as st
import pandas as pd

st.title('🎈 Machine learning App by Streamlit')

st.write('Hello, my name is The Anh')
st.info('this is app builds a ML model!')

with st.expander('data'):
  st.write('**RAW DATA**')
  read = pd.read_csv('https://raw.githubusercontent.com/controltheanh52/penguin/refs/heads/main/penguins_cleaned.csv')
  read

  st.write('**X**')
  X = read.drop('species', axis =  1)

  st.write('**y**')
  y = read.species
  y

with st.expander('Data visualization'):
  #"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"
  st.scatter_chart(data = read, x = "bill_length_mm", y = "body_mass_g", color = 'species')
