
import streamlit as st
import templates

import sign_in
import sign_up

page_names_to_funcs = {
    "Sign In": sign_in,
    "Sign Up": sign_up ,
}

def app():
    st.markdown("# Applicants")
    st.sidebar.markdown("# Notes for Applicants 🎉")
    st.sidebar.markdown(" Equal tech is a gender neutral recruitment app that helps you secure a job without bias.")

    st.sidebar.title('Sign In / Sign Up')
    selection = st.sidebar.radio("Go to", list(page_names_to_funcs.keys()))
    page = page_names_to_funcs[selection]
    page.run()
