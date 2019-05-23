from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/api/<action>', methods = [ 'GET'])
def apiget(action):

   if action == "user":
      return render_template("user.html",user=user_dictionary)

   elif action == "car":
      return render_template("car.html", car=car_dictionary)

   elif action == "all":
      return render_template("all.html", user=user_dictionary, car=car_dictionary)

   else:
      return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():


   # <button type="submit" form="form_user" name="action" value="user_update">Submit</button>
   # send name="action" and value="user_update" to POST

   if request.form["action"] == "user_update":

      user_dictionary["user_name"] = request.form["first_name"]
      user_dictionary["user_age"] = request.form["age"]

      return redirect(url_for('apiget', action="all"))



if __name__ == '__main__':

   user_dictionary = {
            "user_name":"Bob",
            "user_age": 20,
          }

   car_dictionary = {
           "car_brand": "Ford",
           "car_model": "Mustang",
           "car_year": 1964
         }

   app.run()