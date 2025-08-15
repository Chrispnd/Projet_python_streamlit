# pylint: disable=missing-module-docstring
import duckdb as db
import streamlit as st
import os

if "data" not in os.listdir():
    print("Creating folder data")
    os.mkdir("data")

if "sql_database" not in os.listdir("data"):
    exec(open("init_db.py").read())

conn = db.connect(database = "data/sql_database.duckdb", read_only = False)

with st.sidebar:
    available_themes = conn.execute("SELECT DISTINCT theme FROM memory_state").df()
    theme = st.selectbox(
        "What would you like to review ? Hum",
        available_themes["theme"],
        index=None,
        placeholder="Select a thing",
    )
    st.write("You selected", theme)

    if theme:
        exercise = conn.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}' ORDER BY last_reviewed ASC").df()
    else:
        exercise = conn.execute(f"SELECT * FROM memory_state ORDER BY last_reviewed ASC").df()

    st.write(exercise)
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = conn.execute(answer).df()

st.header("enter your code :")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = conn.execute(query).df()
    st.dataframe(result)

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
    exercise_tables = (exercise.loc[0, "tables"])
    for table in exercise_tables:
        st.write(f"table : {table}")
        donnees_tables = conn.execute(f"SELECT * FROM {table}").df()
        st.dataframe(donnees_tables)

with tab3:
    st.write(answer)
