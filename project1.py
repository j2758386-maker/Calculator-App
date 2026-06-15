import streamlit as st

st.title("Calculator")

num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")

row1, row2, row3, row4= st.rows(4)

with row1:
    if st.button("+"):
        st.success(num1 + num2)
with row2:
    if st.button("-"):
        st.success(num1 - num2)
with row3:
    if st.button("*"):
        st.success(num1 * num2)
with row4:
    if st.button("/"):
        if num2 != 0:
            st.success(num1 / num2)
        else:
            st.error("Cannot divide by zero")
