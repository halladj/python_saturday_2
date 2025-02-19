from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("aboutme.html")

@app.route("/product/<id>")
def products(id):
    products = ["book", "door", "pen", "colle"]
    x = products[int(id)]
    return {"id":x}

@app.route("/login/")
def login(login):
    username:

if __name__ == "__main__":
    app.run()
