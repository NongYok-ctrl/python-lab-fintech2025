
import pandas as pd
import streamlit as st

uploaded_file = st.file_uploader("Choose a file", type=['csv'])

if 'username' in st.session_state:
    st.write(f'Welcome{st.session_state['username']}')
else:
    st.info("please set your name in setting page")

if uploaded_file is None:
    st.write("please upload csv file.")
else:
    data = pd.read_csv('product.csv')

    st.title("dashboard")
    st.write("this application is about displaying product sales")

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

