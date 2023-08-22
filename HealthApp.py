import streamlit as st
from streamlit_option_menu import option_menu

# ... (previous code)

# Add a dropdown to select the example type
example_type = st.selectbox("Select Example Type", ["Sidebar Menu", "Horizontal Menu", "Horizontal Menu with Custom Style"])

def streamlit_menu(example=1):
    if example == "Sidebar Menu":
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                # ... (previous code)
            )
        return selected

    if example == "Horizontal Menu":
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            # ... (previous code)
        )
        return selected

    if example == "Horizontal Menu with Custom Style":
        # 3. horizontal menu with custom style
        selected = option_menu(
            # ... (previous code)
        )
        return selected

selected = streamlit_menu(example=example_type)

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")
