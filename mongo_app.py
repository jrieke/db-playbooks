import streamlit as st
import pymongo
import time

# Initialize connection.
# This doesn't take any time and apparently it also doesn't check the connection at all. 
# (Only fails on query if mongo is not running.)
start_time = time.time()
client = pymongo.MongoClient(**st.secrets["mongo"])
f"Connection took {time.time() - start_time} s"

# Pull data from the collection.
@st.cache(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.cache
    return items


start_time_query = time.time()
items = get_data()
f"Query took {time.time() - start_time_query} s"

# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['pet']}:")