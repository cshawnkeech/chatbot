import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write('a first attempt at making a table')
st.write(df)

df  # note that

x = st.slider('x')  # this is a widget
st.write(x, 'squared is', x * x)

if st.checkbox('Show dataframe'):

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    chart_data
