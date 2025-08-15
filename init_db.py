import io
import pandas as pd
import duckdb

conn = duckdb.connect(database = "data/sql_database.duckdb", read_only = False)

# ----------------------
# EXERCISES LIST
# ----------------------

data = {
    "theme" : ["cross_joins", "cross_joins"]
    ,"exercise_name" : ["beverages_and_food", "cars"]
    ,"tables" : [["beverages", "food_items"], ["model", "paint"]]
    ,"last_reviewed" : ["2025-08-15", "2025-08-12"]
}
memory_state_df = pd.DataFrame(data)
conn.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")

# ----------------------
# CROSS JOIN EXERCISES
# ----------------------

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))
conn.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

CSV2 = """
food_item,food_price
cookie,2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))
conn.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

# CAR exercice
CSV = """
model, price
classe_a, 10000
classe_b, 15000
classe_c, 20000
"""
model = pd.read_csv(io.StringIO(CSV))
conn.execute("CREATE TABLE IF NOT EXISTS model AS SELECT * FROM model")

CSV2 = """
paint_colour,paint_price
red_rosso,2000
blue_ocean,1300
grey_montana,700
"""

paint = pd.read_csv(io.StringIO(CSV2))
conn.execute("CREATE TABLE IF NOT EXISTS paint AS SELECT * FROM paint")

conn.close()