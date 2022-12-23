from datetime import date

from flask import Blueprint, render_template, request

from .db import get_db

views = Blueprint("views", __name__)


@views.route('/')
def index():  # put application's code here
    return render_template("index.html")


@views.route('/records/')
def display_records():
    conn = get_db()
    records = conn.execute('SELECT * FROM records').fetchall()
    conn.close()
    return render_template('records.html', records=records)


@views.route('/dashboard/', methods=["POST", "GET"])
def dashboard():
    if request.method == "POST":
        print(request.form)
        owner = "max"
        createdate = date.today()
        timespent = request.form["timespent"]
        language = request.form["language"]
        rating = request.form["rating"]
        description = request.form["description"]
        conn = get_db()
        conn.execute('INSERT INTO records (owner, createDate, timeSpent, language, rating, description)'
                     'VALUES (?, ?, ?, ?, ?, ?)',
                     (owner, createdate, timespent, language, rating, description))
        conn.commit()
        conn.close()

    return render_template("dashboard.html")
