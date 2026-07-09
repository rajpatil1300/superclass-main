import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    with st.container(border=True):
        
        # Using string concatenation in parentheses prevents ANY hidden spaces from forming
        header_html = (
            "<div style='padding-bottom: 10px;'>"
            f"<h3 style='margin: 0; color: #1e293b !important; font-size: 1.5rem; font-family: \"Outfit\", sans-serif; font-weight: 700;'>{name}</h3>"
            f"<p style='color: #64748b !important; font-family: \"Outfit\", sans-serif; margin: 10px 0 15px 0;'>"
            f"Code: <span style='background: #E0E3FF; color: #5865F2 !important; padding: 3px 8px; border-radius: 6px; font-weight: 700;'>{code}</span> &nbsp;|&nbsp; Section: {section}"
            "</p>"
        )
        
        if stats:
            header_html += "<div style='display: flex; gap: 10px; flex-wrap: wrap;'>"
            for icon, label, value in stats:
                header_html += (
                    f"<div style='background: #fdf2f8; padding: 5px 12px; border-radius: 12px; font-size: 0.9rem; border: 1px solid #fce7f3; font-family: \"Outfit\", sans-serif;'>"
                    f"{icon} <b style='color: #1e293b !important;'>{value}</b> <span style='color: #475569 !important;'>{label}</span>"
                    "</div>"
                )
            header_html += "</div>"
            
        header_html += "</div>"
        
        st.markdown(header_html, unsafe_allow_html=True)
        
        if footer_callback:
            footer_callback() 