import streamlit as stream


def authenticate():
   saved_username = "testUsername123"
   saved_password = "p@ssW0rd"

   username, password = get_user_credentials()

   if username == saved_username:
      if password == saved_password:
         stream.write(
         "Welcome to the website")
      else:
         stream.write(
         "Sorry. Incorrect password. Please make sure you entered the right password")
   else:
      stream.write(
         "Sorry. Username not in system. Please make sure you entered the right username")


def get_user_credentials():
   username = stream.text_input(
         "username: ", "Enter your username here", 50,
         "username", "default", "e.g username123")

   password = stream.text_input("password: ", "Enter your passqord here", 50,
            "username", "password")

   return username, password

stream.button("Sign In", "SignInButtton", "Sign In to website", authenticate)