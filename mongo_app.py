import streamlit as st
import pymongo

# Initialize connection.
client = pymongo.MongoClient(
    st.secrets["mongo"]["url"],
    st.secrets["mongo"]["port"],
    username=st.secrets["mongo"]["username"],
    password=st.secrets["mongo"]["password"],
)
db = client.mydb

# Perform query.
for item in db.mycollection.find():
    st.write(f"{item['name']} has a :{item['pet']}:")