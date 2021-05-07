import streamlit as st
import s3fs
import time
import os

start_time = time.time()

# Create connection object.
# `anon=False` means not anonymous, i.e. it uses auth to pull data.
fs = s3fs.S3FileSystem(anon=False)

f"Creating fs took {time.time() - start_time} s"

start_time_read = time.time()

# Retrieve file contents.
@st.cache(ttl=600)
def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode("utf-8")


content = read_file("testbucket-jrieke/myfile.csv")
st.write(content)

# Print results.
for line in content.strip().split("\n"):
    name, pet = line.split(",")
    st.write(f"{name} has a :{pet}:")

# for line in f:
#     name, pet = line.decode("utf-8").strip().split(",")
#     st.write(f"{name} has a :{pet}:")

f"Reading file took {time.time() - start_time_read} s"
