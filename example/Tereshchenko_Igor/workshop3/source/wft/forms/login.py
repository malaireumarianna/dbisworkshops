from flask_wtf import Form
from wtforms import TextField, StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, DateField,PasswordField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError


class LoginForm(Form):


   studybook = StringField("Study Book: ",[ validators.DataRequired("Please enter your study book.")])
   study_year = DateField("Study year: ", [ validators.DataRequired("Please enter your study year.")])

   password = PasswordField("Password Of Student", [validators.DataRequired("Please enter your password.")])

   submit = SubmitField("Send")