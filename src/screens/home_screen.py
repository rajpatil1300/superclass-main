import streamlit as st
from src.components.header import header_home
from src.components.footer import custom_footer
from src.ui.base_layout import style_base_layout,style_background_home

def home_screen():


  header_home() 
  style_background_home()
  style_base_layout()
  col1,col2 = st.columns(2,gap="large")

  with col1:
    st.header("I am Student")
    st.image("https://media.istockphoto.com/id/2167577733/vector/a-student-on-graduation-day-in-blue-graduation-uniform-vector-faceless-black-woman-female.jpg?s=612x612&w=0&k=20&c=s2yUx8Lz5Ig1lcNK135Cvkx05OAKIwZs0CkezhucaQs=",width=120)
    if st.button('Student Portal',type="primary"):
       st.session_state['login_type']='student'
       st.rerun()
  with col2:
    st.header("I am Teacher")
    st.image("https://img.freepik.com/premium-vector/faceless-girl-with-book-raised-hand-white-background-learning-concept-business-concept-vector-image_437761-246.jpg",width=120)
    if st.button('Teacher Portal',type="primary"):
      st.session_state['login_type']='teacher'
      st.rerun()

  custom_footer()