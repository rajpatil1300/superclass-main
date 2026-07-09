import streamlit as st
import datetime

def custom_footer():
    current_year = datetime.datetime.now().year
    
    footer_html = f"""
    <style>
        .custom-footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: rgba(0, 0, 0, 0.15); /* Slightly dark transparent background */
            padding: 15px 0;
            text-align: center;
            z-index: 100;
            backdrop-filter: blur(5px); /* Adds a subtle blur effect to whatever is behind it */
        }}
        
        .custom-footer p {{
            margin: 0;
            font-family: 'Outfit', sans-serif;
            color: rgba(255, 255, 255, 0.8) !important; /* Soft white text */
            font-size: 0.9rem;
            font-weight: 400;
        }}
        
        .custom-footer a {{
            color: white !important;
            text-decoration: none;
            margin: 0 15px;
            font-weight: 600;
            transition: color 0.25s ease-in-out;
        }}
        
        /* Adds a nice hover effect using the pink from your secondary buttons */
        .custom-footer a:hover {{
            color: #EB459E !important; 
        }}
        
        /* Ensures the main content doesn't get hidden behind the fixed footer */
        .block-container {{
            padding-bottom: 80px !important;
        }}
    </style>
    
    <div class="custom-footer">
        <p>
            &copy; {current_year} <strong>SUPER CLASS</strong> 
            | <a href="#" target="_blank">Privacy Policy</a> 
            | <a href="#" target="_blank">Terms of Service</a> 
            | <a href="#" target="_blank">Help Center</a>
        </p>
    </div>
    """
    
    st.markdown(footer_html, unsafe_allow_html=True)