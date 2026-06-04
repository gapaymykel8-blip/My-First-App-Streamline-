
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

import streamlit as st
import pandas as pd

if'dfa' not in st.session_state:
    st.session_state['dfa']= pd.DataFrame({"Par":["Apple","Strawberry","Banana"],"Cat1":["good","good","bad"],"Cat2":["healthy","healthy","unhealthy"],'Active':[False,False,False]})
    st.session_state.rerun = False
    
def rerun():
    st.session_state.rerun = True

name=st.text_input("Search for ...")
if name == '':
    st.session_state['dfa'].Active=True
else:
    st.session_state['dfa'].Active=False
    st.session_state['dfa'].loc[st.session_state['dfa']['Par'].str.contains(name,case=False),'Active']=True

active_dfa = st.session_state['dfa'][st.session_state['dfa']['Active']==True].copy()
edited_dfa = st.data_editor(active_dfa,column_order=['Par','Cat1','Cat2'],on_change=rerun)
    
if st.session_state.rerun:
    st.session_state.rerun = False
    st.rerun()

