
import numpy as np
import pandas as pd
import streamlit as st
import time 

st.title('I have to get this right')

@st.cache_data
def load_data():
   return pd.read_csv('random_data1.csv')

def show_data(data):
   st.subheader('Filtering maybe?')

   filtered_df = data.copy()

   for col in data.columns:
      if data[col].dtype == 'string':
         options = data[col].dropna().unique().tolist()
         selected = st.multiselect(f"filtered by {col}", options, default = options)
         filtered_df = filtered_df[filtered_df[col].isin(selected)]

   st.write(f"Showing {len(filtered_df)} of {len(data)} rows")
   st.dataframe(filtered_df) 

   return filtered_df

yay = load_data()

st.markdown("Doing the same but for a specific Column Instead lets choose, Locaton") 
def show_data_loc(data):
   st.subheader('Filtering maybe?')

   filtered_df = data.copy()

   location_options = data['Location'].unique().tolist()
   selected_locations = st.multiselect(f"filtered by", location_options, default = location_options, key = "location_filter")
   filtered_df = filtered_df[filtered_df['Location'].isin(selected_locations)]

   st.write(f"Showing {len(filtered_df)} of {len(data)} rows")
   st.dataframe(filtered_df)

   return filtered_df

filtered_yay = show_data_loc(yay)

# Some examples of what you can now do with it:

# # Summary statistics of filtered data
# st.subheader("Summary Statistics")
# st.write(filtered_yay.describe())

# # Plot only the filtered data
# st.subheader("Chart of Filtered Data")
# st.bar_chart(filtered_yay['Voltage'])

# # Show filtered row count
# st.write(f"You have {len(filtered_yay)} rows after filtering")

# # Use it in further calculations
# st.write(filtered_yay['Current'].mean())

import datetime
import streamlit as st

event_time = st.datetime_input(
    "Schedule your event",
    datetime.datetime(2025, 11, 19, 16, 45),
)
st.write("Event scheduled for", event_time)







