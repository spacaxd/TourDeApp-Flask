from flask import Blueprint, render_template, redirect, url_for, request
from .db import get_db

views = Blueprint("views", __name__)


@views.route('/')
def index():  # put application's code here
    return render_template("index.html")


@views.route('/addRecord/', methods=["POST"])
def add_record():
    name = request.form.get("name")
    time = request.form.get("time")
    conn = get_db()
    conn.execute('INSERT INTO record (name, time) VALUES (?, ?)',
                 (name, time))
    conn.commit()
    conn.close()
    return redirect(url_for('views.index'))


@views.route('/addRecordForm/')
def add_record_form():
    return render_template("addRecordForm.html")


@views.route('/records/')
def display_records():
    conn = get_db()
    records = conn.execute('SELECT * FROM record').fetchall()
    conn.close()
    return render_template('records.html', records=records)
