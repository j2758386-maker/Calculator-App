import streamlit as st

st.title("Calculator")

num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")

col1, col2, col3, col4= st.columns(4)

with col1:
    if st.button("+"):
        st.success(num1 + num2)
with col2:
    if st.button("-"):
        st.success(num1 - num2)
with col3:
    if st.button("*"):
        st.success(num1 * num2)
with col4:
    if st.button("/"):
        if num2 != 0:
            st.success(num1 / num2)
        else:
            st.error("Cannot divide by zero")
