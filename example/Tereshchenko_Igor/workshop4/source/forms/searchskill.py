from flask_wtf import Form
from wtforms import TextField, StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError


class LoginForm(Form):

   email = StringField("Email",[ validators.DataRequired("Please enter your email address."),  validators.Email("Please enter your email address.")])

   password = StringField("Password Of Student", [validators.DataRequired("Please enter your login.")])

   submit = SubmitField("Send")