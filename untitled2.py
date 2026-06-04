import streamlit as st
import numpy as np

st.title('What will this look like?') 
st.markdown('Suggesting improvements to the streamlit app, that Sir Arcy developed') 

# Your data array
cities = np.array(["New York", "London", "Tokyo", "Paris", "Sydney"])

st.title("Fetch Data from an Array")

# User selects an item from the array
selected_city = st.selectbox("Choose a city:", cities)

# Fetch and use the selected data
st.write(f"You fetched: **{selected_city}**")

