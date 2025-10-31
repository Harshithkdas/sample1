import streamlit as st

# Set page title
st.set_page_config(page_title="Welcome App", page_icon="👋")

# Display a welcome message
st.title("👋 Welcome to My Streamlit App!")
st.write("Hello there! This is a simple Streamlit app displaying a welcome message.")

# Add some extra UI
name = st.text_input("Enter your name:")
if name:
    st.success(f"Welcome, {name}! 🎉 Glad to have you here.")

# Optional button
if st.button("Say Hello"):
    st.balloons()
    st.write("Have a great day!")
