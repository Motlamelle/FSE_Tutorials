from flask import Flask, redirect, url_for, render_template, request
import sqlite3

app = Flask(__name__)
DATABASE = "contacts.db"

# def init_db():
# def index() with @app.route("/")



@app.route("/")
def home():
    return render_template("index.html", name = "John Doe")

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000, debug=True)