from flask import Flask, render_template, request, flash
from example.Tereshchenko_Igor.workshop3.source.wft.forms.login import LoginForm

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def contact():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('login.html', form=form)
        else:
            return 'success'


    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)