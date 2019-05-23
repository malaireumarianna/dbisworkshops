from flask import Flask, render_template, request, flash, session, url_for, redirect
from example.Tereshchenko_Igor.workshop3.source.wft.forms.login import LoginForm

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
      return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"

   return "You are not logged in <br><a href = '/login'></b>" + "click here to log in</b></a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''

               <form action = "" method = "post" id="form_user">
                  <p><input type = "text" name = "username"/></p>

               </form>
               
               <button type="submit" form="form_user" >Submit</button>
        '''

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)