import streamlit as stream
from sign_in import authenticate


def run_sign_in():
   stream.title("Equality Is The Goal Now")

   stream.write(
   """This fight is an ongoing thing that we as an organization would like you to be part of as we fight together
   to get closer to the goal that we as women have been striving for - EQUALITY!
   """)

   stream.button("Sign In", "SignIn", "Click here to sign in", authenticate)


if __name__ == "__main__":
   run_sign_in()
