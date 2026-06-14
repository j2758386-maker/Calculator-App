import streamlit as st

st.title("Calculator")

num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")

op = st.selectbox("Operator", ["+", "-", "*", "/"])

if st.button("Calculate"):
    if op == "+":
        st.success(num1 + num2)
    elif op == "-":
        st.success(num1 - num2)
    elif op == "*":
        st.success(num1 * num2)
    elif op == "/":
        if num2 != 0:
            st.success(num1 / num2)
        else:
            st.error("Cannot divide by zero")