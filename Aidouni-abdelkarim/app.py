from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")


def about():
    return render_template("about.html")
@app.route("/prodect/<id>")
def prodect(id):
    prodect = ["book", "pen", "phone"]
    x= prodect[int(id)]
    return {"id":x}
@app.route("/submit/")
def submit():
    name=request.form.get("name")
    password=request.form.get("password")
    return f"Hello {name}!,Your password is: {password}."

if __name__ == "__main__":
    app.run()


