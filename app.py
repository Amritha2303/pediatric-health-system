from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# DATABASE CONNECTION
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# LOGIN PAGE
@app.route("/")
def home():
    return render_template("login.html")


# LOGIN CHECK
@app.route("/login", methods=["POST"])
def login():

    child_id = request.form["health_id"]   # value entered by parent

    conn = get_db()

    child = conn.execute(
        "SELECT * FROM children WHERE child_id = ?",
        (child_id,)
    ).fetchone()

    conn.close()

    if child:
        return render_template("dashboard.html", child=child)
    else:
        return "Child not found"


# RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)