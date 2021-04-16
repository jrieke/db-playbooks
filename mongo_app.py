import streamlit as st
import pymongo

# Initialize connection.
client = pymongo.MongoClient(**st.secrets["mongo"])
db = client.mydb

# Perform query.
for item in db.mycollection.find():
    st.write(f"{item['name']} has a :{item['pet']}:")