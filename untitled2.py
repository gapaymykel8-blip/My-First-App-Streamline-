
import numpy as np
import pandas as pd
import streamlit as st
import time 

st.title('I have to get this right')

data = pd.readcsv('Blue Spectra(in).csv')

@st.cache_data
def show_data():
    st.header("Data analysis")
    data = api.get(...)
    st.success("Fetched data from API!")
    st.write("Here is a plot of the data:")
    st.line_chart(data)
    st.write("And here is the raw data:")
    st.dataframe(data)
