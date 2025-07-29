import streamlit as st 
import google.generativeai as genai
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

#configure the api key

key_variable = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key_variable)

# set up our page

st.title('HEALTH ASSISTANT FOR FITNESS 🎯')
st.header('This page will help you to get information for fitness using BMI value 📄')


st.sidebar.subheader('Height')

height = st.sidebar.text_input('Enter the height in metres : ')

st.sidebar.subheader('Weight')

weight = st.sidebar.text_input('Enter the Weight in kgs : ')


## Calculating BMI values

try:
    height = pd.to_numeric(height)
    weight = pd.to_numeric(weight)
    if height > 0 and weight >0:
        bmi = weight/(height**2)
        st.sidebar.success(f'BMI value is : {round(bmi,2)}')
    else:
        st.write('Please enter positive values.')
except:
    st.sidebar.info('please enter positive values')
    

input = st.text_input('Ask your question here❗')
submit = st.button('click here ✔️ ')
model = genai.GenerativeModel('gemini-1.5-flash')
    
    
def generate_result(bmi,input):
    if input is not None:
        
        
        prompt = f'''
        You are the health assistant now so you need to get results based on the fitness or other
        health related questions. You can suggest some diet to be followed and also some
        fitness exercises to the user. Also use the {bmi} value for better suggestions.bmi
        If any medications or medicines related questions are asked, always mention that
        'check with nearby doctors for the medications'
        '''
        
        result = model.generate_content(input+prompt)
        
    return result.text
    
if submit:
    with st.spinner('Result is loading.....'):
        response = generate_result(bmi,input)
    
    st.markdown(':green[Result]')
    st.write(response)