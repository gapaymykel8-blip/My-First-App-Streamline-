
import numpy as np
import pandas as pd
import streamlit as st
import time 

st.title('I have to get this right')

@st.cache_data
def load_data():
   return pd.read_csv('random_data.csv')

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

yay = load_data()
show_data(yay)

st.markdown("Doing the same but for a specific Column Instead lets choose, Locaton") 
def show_data_loc(data):
   st.subheader('Filtering maybe?')

   filtered_df = data.copy()

   location_options = data['Location'].unique().tolist()
   selected_locations = st.multiselect(f"filtered by", location_options, default = location_options)
   filtered_df = filtered_df[filtered_df['Location'].isin(selected_locations)]

   st.write(f"Showing {len(filtered_df)} of {len(data)} rows")
   st.dataframe(filtered_df) 

show_data_loc(yay)

filtered_yay = show_data_loc(yay)

st.write(filtered_yay.describe())  


st.markdown("Going to try and make the tables selectable but caching seems to work, with csv files i dont see why it shouldnt work with the code") 

import streamlit as st
import pandas as pd
import time

if "dfa" not in st.session_state:
    st.session_state["dfa"] = pd.DataFrame(
        {
            "Par": ["Apple", "Strawberry", "Banana"],
            "Cat1": ["good", "good", "bad"],
            "Cat2": ["healthy", "healthy", "unhealthy"],
            "Active": [False, False, False],
        }
    )


def active_dfa():
    return st.session_state["dfa"][st.session_state["dfa"]["Active"] == True].copy()


def get_index(row):
    return active_dfa().iloc[row].name


def commit():
    for row in st.session_state.editor["edited_rows"]:
        row_index = get_index(row)
        for key, value in st.session_state.editor["edited_rows"][row].items():
            st.session_state["dfa"].at[row_index, key] = value


st.header("Filter and edit data")
name = st.text_input("Search for ...", on_change=commit)
if name == "":
    st.session_state["dfa"].Active = True
else:
    st.session_state["dfa"].Active = False
    st.session_state["dfa"].loc[
        st.session_state["dfa"]["Par"].str.contains(name, case=False), "Active"
    ] = True

edited_dfa = st.data_editor(
    active_dfa(), column_order=["Par", "Cat1", "Cat2"], key="editor"
)

st.button("Save", on_click=commit)

print(edited_dfa)

st.markdown("This can be used at the end to flter out the different telescopes possibly, but ideally we would be able to filter out all the other telescopes we are not concered with before we do the rest of the computations")


title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

