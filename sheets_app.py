# streamlit_app.py

import streamlit as st
from gsheetsdb import connect
import time

# Create a connection object.
start_time = time.time()
conn = connect()
f"Conn took {time.time() - start_time} s"

# Perform SQL query on the Google Sheet.
start_time_query = time.time()


@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows


sheet_url = st.secrets["gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
print(type(rows))
f"Query took {time.time() - start_time_query} s"

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")