import streamlit as st

st.set_page_config(page_title="S Calcu",page_icon="🔢")

st.title("Calculator")

num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")
st.write("---")

col1, col2, col3, col4= st.columns(4)
result=None

with col1:
    if st.button("➕"):
        result=num1 + num2
with col2:
    if st.button("➖"):
        result=num1 - num2
with col3:
    if st.button("✖️"):
        result=num1 * num2
with col4:
    if st.button("➗"):
        if num2 != 0:
            result=num1 / num2
        else:
            st.error("Cannot divide by zero")

if result is not None:
    st.success(f"Result:{result}")
