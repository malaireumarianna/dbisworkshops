from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/api/<action>', methods = [ 'GET'])
def apiget(action):
    true_values = ["user", "info", "all"]
    if action == "user":
        return render_template("user.html", user=user_dictionary)

    elif action == "info":
        return render_template("info.html", info=info_dictionary)

    elif action == "all":
        return render_template("all.html", user=user_dictionary, info=info_dictionary)

    else:
        return render_template("404.html", action_value=action, true_v=true_values)


@app.route('/api', methods=['POST'])
def apipost():
   if request.form["action"] == "user_update":

      user_dictionary["login"] = request.form["log"]
      user_dictionary["PASS"] = request.form["PAS"]
      user_dictionary["NICKNAME"] = request.form["NICK"]
      user_dictionary["first_name"] = request.form["first"]

      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "info_update":

      info_dictionary["COMPANYNAME"] = request.form["COMPANY"]
      info_dictionary["JOBNAME"] = request.form["JOB"]
      info_dictionary["LINKTOJOB"] = request.form["LINK"]

      return redirect(url_for('apiget', action="all"))



if __name__ == '__main__':
    user_dictionary = {
       "login": "malaireumariana1@gmail.com",
        "PASS": "marianna",
        "NICKNAME": "liry11",
        "first_name": "MARY",
         }


    info_dictionary = {
        "COMPANYNAME": "GENESIS",
        "JOBNAME": "PYTHON PROGRAMMER",
        "LINKTOJOB": "https://www.work.ua/jobs/3873445/"
    }
    app.run()