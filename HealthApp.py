import streamlit as st
from streamlit_option_menu import option_menu

def streamlit_menu():
    options = ["Home", "Projects", "Contact"]
    selected = option_menu(
        menu_title=None,
        options=options,
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )
    return selected

# Create the Streamlit app
st.title("Horizontal Navbar Example")
selected = streamlit_menu()

if selected == "Home":
    st.write("You have selected Home.")
elif selected == "Projects":
    st.write("You have selected Projects.")
elif selected == "Contact":
    st.write("You have selected Contact.")
