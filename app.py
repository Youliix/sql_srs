import streamlit as st
import pandas as pd

import duckdb

data = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["SQL SELECT", "SQL INSERT", "SQL UPDATE"])

with tab1:
    sql_query = st.text_area(label="Input content")
    result = duckdb.query(sql_query).df()
    st.dataframe(result)
