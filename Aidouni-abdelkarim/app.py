from flask import Flask, render_template,request,redirect
from pathlib import Path
import json



app = Flask(__name__)
users= {}




FILE_NAME= "disc.json"
FILE_PATH=Path("",FILE_NAME)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/prodect/<id>")
def prodect(id):
    prodect = ["book", "pen", "phone"]
    x= prodect[int(id)]
    return {"id":x}

@app.route("/submit/", methods=["POST"])
def submit():
    name=request.form.get("name")
    password=request.form.get("password")
    if users.get(name) is None:
        users[name] = password
    if password in users.values():
        return render_template("profile.html")
    else:
        return render_template("form.html")


@app.route("/profile",methods=["POST"])

def profile():
    name=request.form.get("name")
    age=request.form.get("age")
    jobs=request.form.get("jobs")
    salery=request.form.get("salery")
    disc = {name: {"name": name, "age": age, "jobs": jobs, "salery": salery}}
    disc[f"{name}"] ={"name":name,"age":age,"jobs":jobs,"salery":salery}
    with open(FILE_PATH, "w") as file:
        json.dump(disc, file)

    return disc
@app.route("/ajouter/", methods=["POST"])
def ajouter():
    return render_template("profile.html")



if __name__ == "__main__":
    app.run()


