
import numpy as np
import pandas as pd
import streamlit as st
import time 

st.title('I have to get this right')

df = pd.read_csv('dummy_data.csv')

@st.cache_data
def show_data(data):
    st.header("Data analysis")
    st.write("And here is the raw data:")
    st.dataframe(data)

yay = show_data(df)

st.markdown("Going to try and make the tables selectable but caching seems to work, with csv files i dont see why it shouldnt work with the code") 

options = st.multiselect(
    "Pick a Number", 
    [yay],
)

st.write("Your number is:", options)

