# streamlit_app.py

import streamlit as st
from gsheetsdb import connect
import time

# Create a connection object.
start_time = time.time()
conn = connect()
f"Conn took {time.time() - start_time} s"

# Perform SQL query on the Google Sheet.
sheet_url = st.secrets["gsheets_url"]
start_time_query = time.time()
rows = conn.execute(f'SELECT * FROM "{sheet_url}"', headers=1)
f"Query took {time.time() - start_time_query} s"

# Print results.
for row in rows:
    st.write(f"{row.name} has a :{row.pet}:")