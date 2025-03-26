import streamlit as st

def show():
    col1, col2,col3 = st.columns([2,0.5,1])
    with col1:
            st.write("##")
            st.subheader("I am DHEERAJ MAHAPATRA")
            st.header("Pursuing B.Tech from AJU")
            st.write("##")
        
    with col2:
            st.write("")
        
    with col3:
            st.write("##")
            st.image("./assests/images.jpeg", width=300)


        
        