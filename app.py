# pylint: disable=missing-module-docstring
import duckdb as db
import pandas as pd
import streamlit as st


import io


CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie,2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = db.sql(ANSWER_STR).df()

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ? Hum",
        ("Joins", "Groupby", "Window functions"),
        index=None,
        placeholder="Select a thing",
    )
    st.write("You selected", option)

st.header("enter your code :")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = db.sql(query).df()
    st.dataframe(result)

    #    if len(result.columns) != len(solution_df.columns):
    #        st.write("Some columns are missing")

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"result has a {n_lines_difference} lines difference with the solution_df"
        )

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected :")
    st.dataframe(solution_df)

with tab3:
    st.write(ANSWER_STR)
