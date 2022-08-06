import streamlit as stream
import sqlite3 as sql


def load_page():
   stream.markdown("## Sign Up")

   name = stream.text_input(
         "Name: ", "Your name here", 20,
         "user-name", "default",)

   surname = stream.text_input(
         "Surname: ", "Your surname here", 20,
         "user-surname", "default",)

   age = stream.slider("Age: ", 0, 40, 18,)

   email = stream.text_input(
         "Email: ", "Your email here", 100,
         "user-email", "default",)

   password = stream.text_input("password: ", "Password", 50,
            "user-password", "password")

   preferred_location = stream.radio("Preferred Location", ["Remote", "Physical"])

   employment_type = stream.radio("Employment type", ["Permanent", "Internship", "Learnership", "Temporal"])

   citizenship_status = stream.radio("Citizenship Status", ["South African", "Other"])

   if citizenship_status == "Other":
      citizenship_status = stream.text_input(
         "Citizenship: ", "Your citizenship here", 20,
         "user-citizenship", "default",)

   infor = name, surname, age, email, password, preferred_location, employment_type, citizenship_status

   save_applicant_details(infor)


def save_applicant_details(applicant_info:list):
   if stream.button("Save"):
      with sql.connect("file:database.db?mode=rwc", uri=True) as connection:
         connection.execute(
            "INSERT INTO applicants (name,surname,age,email,password,location,emplyment_type,citizenship) VALUES(?,?,?,?,?,?,?,?)",
            (applicant_info[0], applicant_info[1], applicant_info[2], applicant_info[3], applicant_info[4],
               applicant_info[5], applicant_info[6], applicant_info[7]))
         stream.text("Information saved successfully!")
