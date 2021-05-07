import streamlit as st
import psycopg2
import time

start_time = time.time()
# Initialize connection.

# This here DOES already connect to the database, so it should probably be cached.
@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def create_conn():
    return psycopg2.connect(*st.secrets["postgres"])


conn = create_conn()

f"Initiating connection took {time.time() - start_time} s"

start_time_query = time.time()
# Perform query.
@st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


results = run_query("SELECT * from mytable;")

for row in results:
    st.write(f"{row[0]} has a :{row[1]}:")
f"Query took {time.time() - start_time_query} s"
