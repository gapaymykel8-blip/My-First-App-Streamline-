import streamlit as st
import numpy as np

st.title('What will this look like?') 

# Your data array
cities = np.array(["New York", "London", "Tokyo", "Paris", "Sydney"])

st.title("Fetch Data from an Array")

# User selects an item from the array
selected_city = st.selectbox("Choose a city:", cities)

# Fetch and use the selected data
st.write(f"You fetched: **{selected_city}**")

st.markdown('Fun lets try with a dictionary')

import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((50, 20)), columns=("col %d" % i for i in range(20))
)

st.dataframe(df)

import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame(np.random.randn(15, 3), columns=["A", "B", "C"])
chart = st.line_chart(df)

for tick in range(10):
    time.sleep(0.5)
    new_row = pd.DataFrame(np.random.randn(1, 3), columns=["A", "B", "C"])
    chart.add_rows(new_row)

st.button("Regenerate")
