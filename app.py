import streamlit as st
import pandas as pd
import duckdb as db

st.write("""
# SQL SRS
Space Repetition System
""")

option = st.selectbox(
    "What would you like to review ,",
    ("Joins", "Groupby", "Window functions"),
    index=None,
    placeholder="Select a thing"
)

st.write('You selected', option)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

sql_query = st.text_area(label="entrez votre input")
try:
    result=db.query(sql_query).df()
    st.write(f"Vous avez entré la query suivante: {sql_query}")
    st.dataframe(result)
except:
    st.write("Vous n'avez pas encore rentré de réponse")

