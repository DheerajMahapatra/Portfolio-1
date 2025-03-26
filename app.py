import streamlit as st
import pages.home
import pages.about
import pages.project
# from pages import Home,about,project
from streamlit_option_menu import option_menu

# st.write("#")
st.set_page_config(layout="wide")
st.subheader("Hey Guys:wave:")
# st.title("Data Science Portfolio")
# st.write("HELLO!")
# st.write("This is my Portfolio. I make it using Streamlit & I gonna explain about my self with the help of this Portfolio.")

st.write("___")

selected=option_menu("", ["Home", "About", "Project", "Contect Me"], orientation="horizontal", icons=["house", "person", "tools", "chat-left-text-fill"], default_index=1)


if selected == "Home":
    pages.home_show()
        
        


elif selected == "About":
    pages.about_show()


elif selected == "Project":
    pages.project_show()