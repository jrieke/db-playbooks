import streamlit as st
import s3fs
import time

start_time = time.time()

# Create connection object. 
# `anon=False` means not anonymous, i.e. it uses auth to pull data.
fs = s3fs.S3FileSystem(anon=False)

f"Creating fs took {time.time() - start_time} s"

start_time_read = time.time()

# Retrieve file contents and write to streamlit app. 
with fs.open("testbucket-jrieke/myfile.csv") as f:
    for line in f:
        name, pet = line.decode("utf-8").strip().split(",")
        st.write(f"{name} has a :{pet}:")

f"Reading file took {time.time() - start_time_read} s"
