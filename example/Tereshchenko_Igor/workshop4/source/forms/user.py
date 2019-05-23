from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField, DateField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError


class UserForm(Form):

   name = StringField("Name: ",[
                                    validators.DataRequired("Please enter your name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

   password = PasswordField("Password:", [
                                             validators.DataRequired("Please enter your password."),
                                             validators.Length(3, 10, "Password should be from 3 to 10 symbols")
                                          ])

   email = StringField("Email: ",[
                                 validators.DataRequired("Please enter your name."),
                                 validators.Email("Wrong email format")
                                 ])

   birthday = DateField("Birthday: ", [ validators.DataRequired("Please enter your birthday.")])

   studybook = StringField("Study Book: ",[
                                             validators.DataRequired("Please enter your study book."),
                                             validators.Length(6,6,"6 symbols allowed")
                                          ])

   study_year = DateField("Study year: ", [ validators.DataRequired("Please enter your study year.")])

   submit = SubmitField("Register")