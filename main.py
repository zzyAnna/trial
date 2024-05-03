from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/customize")
def customize():
    return render_template("customize.html")

@app.route("/instrument")
def instrument():
    return render_template("instrument.html")

@app.route("/style")
def style():
    return render_template("style.html")

@app.route("/era")
def era():
    return render_template("era.html")

if __name__ == "__main__":
    app.app_context().push()
    app.run(debug=True)

