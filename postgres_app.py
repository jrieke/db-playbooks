import streamlit as st
import psycopg2
import time

start_time = time.time()
# Initialize connection. 
conn = psycopg2.connect(
    "dbname={dbname} user={user} password={password}".format(**st.secrets["postgres"])
)
cur = conn.cursor()
f"Initiating connection took {time.time() - start_time} s"

start_time_query = time.time()
# Perform query.
query = "SELECT * from mytable;"
cur.execute(query)
for row in cur.fetchall():
    st.write(f"{row[0]} has a :{row[1]}:")
f"Query took {time.time() - start_time_query} s"
