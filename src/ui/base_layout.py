
import streamlit as st

def style_background_home():
    st.markdown("""
    <style>
        .stApp {
            background: #5865F2 !important;
        }
        /* ONLY on the home screen, force text to be white */
        h1, h2, h3, h4, p, span {
            color: white !important;
        }
        .stApp div[data-testid="stColumn"] {
            background-color: #E0E3FF !important;
            padding: 2.5rem !important;
            border-radius: 5rem !important;
        }
        /* Make the text inside the white columns dark again */
        .stApp div[data-testid="stColumn"] h1, 
        .stApp div[data-testid="stColumn"] h2, 
        .stApp div[data-testid="stColumn"] p {
            color: #1e293b !important;
        }
    </style>
    """, unsafe_allow_html=True)
  

def style_background_dashboard():
    st.markdown("""
    <style>
        .stApp {
            background: #E0E3FF !important;
        }
        /* On the dashboard, text should naturally be dark */
        h1, h2, h3, h4, p, span {
            color: #1e293b !important;
        }
    </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        MainMenu, footer, [data-testid="stHeader"] {
            visibility: hidden;
        }    
                
        .block-container {
            padding-top: 1.5rem !important;
        }

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 1.5rem !important; 
            line-height: 1.1 !important;
            margin-bottom: 0.5rem !important;
            white-space: nowrap !important; 
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif;
        }

        /* Standardize Buttons */
        button[kind="primary"] {
            border-radius: 1.5rem !important;
            background-color: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background-color: #EB459E !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background-color: black !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button:hover {
            transform: scale(1.05);
        }
    
        /* Target the bordered containers to act as our Subject Cards */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: white !important;
            border-radius: 15px !important;
            border-left: 8px solid #EB459E !important;
            border-top: none !important;
            border-right: none !important;
            border-bottom: none !important;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05) !important;
        }
      
        /* Remove excess padding from the inner block so our HTML controls the spacing */
        div[data-testid="stVerticalBlockBorderWrapper"] > div {
            padding: 1.5rem !important;
        }
    </style>
    """, unsafe_allow_html=True)
