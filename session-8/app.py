from flask import Flask,render_template, request, redirect


app = Flask(__name__)

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

    return f"yourname is :{name}, ur password is: {password}"

@app.route("/product/<id>")
def products(id):
    products = ["book", "pen", "door", "phone"]
    x = products[int(id)]
    return {"id":x} 

if __name__ == "__main__":
    app.run()