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
  X_raw = read.drop('species', axis =  1)
  X_raw
  st.write('**y**')
  y_raw = read.species
  y_raw

with st.expander('Data visualization'):
  #"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"
  st.scatter_chart(data = read, x_raw = "bill_length_mm", y_raw = "body_mass_g", color = 'species')


#data preparations
with st.sidebar:
  #,"bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g",
  st.header('input the feature')

  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox('sex', ('male', 'female'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (mm)', 2700.0,  6300.0, 4207.0)

  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}

  input_read = pd.DataFrame(data, index =[0])
#encode x
encode = ['island', 'sex']
read_penguins = pd.get_dummies(input_penguins, prefix = encode)

input_row = read_penguins[:1]

#encode y
target_mapper  = {'Adelie': 0.
                 'Chinstrap': 1,
                  'Gentoo': 2};

def target_encode(val)
  return target_mapper[val]


  input_penguins = pd.concat([input_read, X], axis = 0)
with st.expander('input features'):
  st.write('**input penguin**')
  input_read
  st.write('**Combined penguins data**')
  input_penguins
  st.write('**Encoded input penguin**')
  input_row


