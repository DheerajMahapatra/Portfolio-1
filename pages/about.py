import streamlit as st

def show():
    col1, col2, col3 = st.columns([2,0.5,1])
    with col1:
        st.write("##")
        st.header("DHEERAJ MAHAPATRA")
        st.subheader("About my Education & Qualification")
        
        
    with col2:
        st.write("")
        
    with col3:
        st.image("./assests/download.jpeg")
        
    st.write("___")
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.subheader('''
        EDUCATION
        - Bachlor of Technology - Comuter Science
            - AJU(ARKA Jain University)
            - 2023-2027
            
        - 12th with PCM(Physics,Chemistry,Mathematics) & Computer Science
            - S.N.S.V.M(Sant Nandlal Smriti Vidya Mandir)
            - 2021-2023
            
        - 10th
            - B.D.S.L.Saraswati Vidya Mandir
            _ 2021
            
        ''')
        
    
    with col5:
        st.write("")
    
    with col6:
        st.subheader('''
        SKILLS
        - Python
        - C++
        - Java
        - C''')