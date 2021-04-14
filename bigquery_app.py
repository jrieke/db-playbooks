import os
import json
import time
import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd

# st.write("env variable:", os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

# key_file = "/Users/jrieke/Downloads/striped-fulcrum-282122-d54eddf1d36d.json"
# with open(key_file) as f:
#     json_acct_info = json.load(f)

# st.write("secrets:", st.secrets["bigquery_key"][:70] + "...")

# # Retrieve and convert key file content.
# start_time = time.time()
# bigquery_key_json = json.loads(st.secrets["bigquery_key"], strict=False)
# credentials = service_account.Credentials.from_service_account_info(bigquery_key_json)
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["bigquery_key"]
)

# # Create API client.
# # TODO: Should this be cached? Uses only 1-3 ms, whereas query uses ~1.5 s.
client = bigquery.Client(credentials=credentials)
# print(time.time() - start_time)

# # Perform query.
# # TODO: Or should this be cached?!
query = "SELECT * FROM `striped-fulcrum-282122.example_dataset.example_table`"
start_time_query = time.time()
query_job = client.query(query)
rows = query_job.result()
f"Google package took {time.time() - start_time_query} s"

# Print results.
rows = [("Mary", "dog"), ("John", "cat"), ("Robert", "bird")]
for row in rows:
    st.write(row[0], "has a", f":{row[1]}:")


# Using pandas.
start_time_pd = time.time()
df = pd.read_gbq(query, credentials=credentials)
f"Pandas took {time.time() - start_time_pd} s"
df
