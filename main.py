
import pandas as pd
import streamlit as st

data = pd.read_csv('product.csv')

st.title("dashboard")
st.write("this application is about displaying product sales")

name = st.text_input("Enter your name", "Type here ...")
st.write("name")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("sales", "1,200", "12%")
with col2:
    st.metric("revenue", "$ 120,000", "10%")
with col3:
    st.metric("profit", "$ 30,000", "5%")

st.line_chart(data['sales'])\

if st.button("Click me"):
    st.header("sales table")
    st.subheader("this is a sales table")
    st.write(data)

