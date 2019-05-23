from flask import Flask, render_template, request
from example.Tereshchenko_Igor.workshop4.source.forms.user import UserForm

from example.Tereshchenko_Igor.workshop4.source.dao.userhelper import *
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def user():
    form = UserForm()


    allUsers = getUsers()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('user.html', form=form, users = allUsers)
        else:
            user_id , status = newUser(
                                            USER_STUDYBOOK=request.form["studybook"],
                                            USER_BIRTHDAY=request.form["birthday"],
                                            USER_EMAIL=request.form["email"],
                                            USER_NAME=request.form["name"],
                                            USER_PASSWORD=request.form["password"],
                                            USER_YEAR=request.form["study_year"]
                                       )

            return render_template('user.html', form=form, users=allUsers)


    return render_template('user.html', form=form, users = allUsers)


if __name__ == '__main__':
    app.run(debug=True)