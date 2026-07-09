import streamlit as st

def header_home():
    logo_url = "https://www.kindpng.com/picc/m/34-343936_transparent-student-logo-png-png-download.png"
    st.markdown(f"""
      <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px; margin-top: 30px;'> 
                <img src='{logo_url}' style='height: 100px;' />
                <h1 style='text-align: center; color: #E0E3FF; margin-top: 10px;'>SUPER<br>CLASS</h1>
      </div>
    """, unsafe_allow_html=True)
    
def header_dashboard():
    logo_url = "https://www.kindpng.com/picc/m/34-343936_transparent-student-logo-png-png-download.png"
    st.markdown(f"""
      <div style='display: flex; flex-direction: row; align-items: center; justify-content: flex-start; gap: 15px; margin-top: 30px;'> 
               <img src='{logo_url}' style='height: 85px; border-radius: 10px;' />
                <h2 style='text-align: left; color: #5865F2; line-height: 0.9; margin: 0;'>SUPER<br>CLASS</h2>
      </div>
    """, unsafe_allow_html=True)