import streamlit as st

st.title("Rectangle")

width = st.number_input("Width")
height = st.number_input("Height")
if st.button("Calculate Area"):
    st.write(f"area = {width * height}")