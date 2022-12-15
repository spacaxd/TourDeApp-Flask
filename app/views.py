from flask import Blueprint, render_template, redirect, url_for, request

from .db import get_db
from datetime import date

views = Blueprint("views", __name__)



@views.route('/')
def index():  # put application's code here
    return render_template("index.html")


@views.route('createRecord', methods=["POST"])
def add_record():

    name = request.form.get("name")
    time = request.form.get("time")
    conn = get_db()
    conn.execute('INSERT INTO record (name, time) VALUES (?, ?)',
                 (name, time))
    conn.commit()
    conn.close()

    return "lol"


@views.route('/addRecordForm/')
def add_record_form():

    return render_template("addRecordForm.html")


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
