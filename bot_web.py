import streamlit as st
st.title("🤖 Bernard's Math Bot")
name = st.text_input("What is your name?")
if name:
    st.write(f"Welcome {name}!")
    ans = st.number_input("What is 20 - 10?", value=0)
    if st.button("Check"):
        if ans == 10:
            st.success("Correct!")
        else:
            st.error("Try again!")

