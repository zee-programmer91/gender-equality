import streamlit as stream


def run():

   username = stream.text_input(
         "Username: ", "Username", 50,
         "user-username", "default", "e.g username123")

   password = stream.text_input("password: ", "Password", 50,
            "user-password", "password")

   infor = username, password

   stream.button("Sign Up", "SignUpButtton", "Save Details", save_applicant_details,infor)


def save_applicant_details(applicant_info:list):
   pass
