import json
import pandas as pd
import streamlit as st

dbfile = "tasks.json"

def add_todo(name, date):
    d = {
        "name": name,
        "date": date.strftime("%Y/%m/%d")
    }
    with open(dbfile, "a") as f:
        json.dump(d, f)
        f.write("\n")
        
   
def load_data():
    return pd.read_json(dbfile, lines=True)

st.write("# Todo App")
st.write("List of my Todos")

name = st.text_input("Name")
date = st.date_input("Due Date")
if st.button("Add Todo"):
    add_todo(name, date)
    
df = load_data()
st.write(df)

st.write("## Mark it Done")
done_task = st.selectbox("Task", df["name"].values)
if st.button("Done!"):
    pass