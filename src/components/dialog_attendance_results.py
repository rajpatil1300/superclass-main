import streamlit as st
from src.database.db import enroll_student_to_subject, create_attendance
from src.database.config import supabase 
from PIL import Image
import time

def show_attendance_result(df, logs):
    st.write('Please review attendance before confirming.')
    
    st.dataframe(df, hide_index=True, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Discard', width='stretch'):
            # Use .pop() or check if key exists to prevent errors if the state isn't set yet
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()
 
    with col2:
        if st.button('Confirm & Save', width='stretch', type='primary'):
            try:
                create_attendance(logs)
                st.toast("Attendance taken successfully! ✅")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error(f'Sync failed! Error: {e}')

@st.dialog("Attendance Reports")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs)