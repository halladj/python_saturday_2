from flask import Flask,render_template, request, redirect


app = Flask(__name__)

info = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/form/")
def form():
    return render_template("form.html")

@app.route("/submit/", methods=["POST"])
def submit():

    name = request.form.get("name")
    password = request.form.get("password")
    birth_date = request.form.get("birth_date")
    salary = request.form.get("salary")
    education = request.form.get("education")
    info.append({"name": name, "password": password, "birth_date": birth_date, "salary": salary, "education": education})
    return info


@app.route("/product/<id>")
def products(id):
    products = ["book", "pen", "door", "phone"]
    x = products[int(id)]
    return {"id":x} 

@app.route("/info/")
def info():
    return render_template("info.html")

if __name__ == "__main__":
    app.run()