import streamlit as st
import pandas as pd
import duckdb as db
import io

CSV = '''
beverage,price
orange juice, 2.5
Expresso,2
Tea,3
'''
beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = '''
food_item, food_price
cookie, 2.5
chocolatine, 2
muffin, 3
'''

food_items = pd.read_csv(io.StringIO(CSV2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = db.sql(answer).df()

with st.sidebar:
    option = st.selectbox(
        "What would you like to review ? Hum",
        ("Joins", "Groupby", "Window functions"),
        index=None,
        placeholder="Select a thing"
    )
    st.write('You selected', option)

st.header("enter your code :")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = db.sql(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected :")
    st.dataframe(solution)

with tab3:
    st.write(answer)