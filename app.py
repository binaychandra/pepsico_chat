import streamlit as st

def main():
    # Set page title
    st.title("Personalized Greeting App")

    # Ask user for their name
    name = st.text_input("Enter your name")

    # Display personalized greeting
    if name:
        st.write(f"Hello, {name}! Welcome to Streamlit.")

if __name__ == "__main__":
    main()
