from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    health_id = request.form["health_id"]

    conn = get_db()
    child = conn.execute(
        "SELECT * FROM children WHERE health_id = ?",
        (health_id,)
    ).fetchone()

    if child:
        return render_template("dashboard.html", child=child)
    else:
        return "Child not found"

if __name__ == "__main__":
    app.run(debug=True)