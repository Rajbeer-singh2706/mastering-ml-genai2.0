import streamlit as st
import os
import sys

## telling pyton that , its a base or ROOT path --> reference is stored in python , now python knows it 
## Now we can refer it anywhere 
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print("BASE_DIR: {BASE_DIR}")

sys.path.append(BASE_DIR)

## Now DB is searched in BASE_DIR 

from db.database import init_db

init_db()

st.set_page_config(page_title="DocManager",layout="wide")

st.title("🗂️ Smart PDF Document Manager")

st.divider()

tabs = st.tabs(["Upload", "Search & View", "Analytics"])

with tabs[0]:
    # logic of upload
    pass

with tabs[1]:
    # logic of Search & View
    pass

with tabs[2]:
    # logic of Analytics
    pass