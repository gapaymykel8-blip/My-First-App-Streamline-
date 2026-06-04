
import numpy as np
import pandas as pd
import streamlit as st
import time 

st.title('I have to get this right')

df = pd.read_csv('Blue Spectra(in).csv')

@st.cache_data
def show_data(data):
    st.header("Data analysis")
    st.success("Fetched data from API!")
    st.write("Here is a plot of the data:")
    st.write("And here is the raw data:")
    st.dataframe(data)

yay = show_data(df)
yay

