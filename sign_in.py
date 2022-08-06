import sqlite3 as sql
import streamlit as stream


def load_page():
   stream.markdown("## Sign In")

   email = stream.text_input(
         "email: ", "Enter your email here", 50,
         "email", "default", "e.g username123")

   password = stream.text_input("password: ", "Enter your passqord here", 50,
            "username", "password")

   arguments = email, password

   stream.button("Login", "SignInButtton", "Sign In to website", authenticate,arguments)


def authenticate(email, password):
   with sql.connect("file:database.db?mode=rwc", uri=True) as connection:
      user_details = connection.execute("SELECT * FROM applicants WHERE email = ?", (email)).fetchone()

   if user_details:
      for user_detail in user_details:
         stream.text(user_detail)
   else:
      stream.write(
         "Sorry. Username not in system. Please make sure you entered the right username")
