from flask import Flask, render_template, request,flash, make_response

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']

        resp = make_response()
        resp.set_cookie('userID', user)

        return resp



@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return name


if __name__ == '__main__':
    app.run(debug=True)