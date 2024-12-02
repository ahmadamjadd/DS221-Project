from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
import requests
from werkzeug.utils import secure_filename
import os
import pandas as pd
from absolute_grading import *
app = Flask(__name__)
app.secret_key = 'hello'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("form.html")

@app.route("/upload", methods=["POST", "GET"])
def upload_file():
    if 'csv_file' not in request.files:
        return redirect(request.url)
    file = request.files['csv_file']
    if file and allowed_file(file.filename):
        # Secure the filename and save it to the upload folder
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('calculate_grades', filename=filename))
    else:
        return "Invalid file format. Please upload a CSV file."
    
@app.route("/grades", methods=["GET"])
def calculate_grades():
    filename = request.args.get('filename')
    if filename:
        df = pd.read_csv(f"uploads/{filename}")
        grades = generate_grade_report(df)
        rows = grades.values.tolist()
        columns = grades.columns.tolist()
        return render_template("grades.html", columns=columns, rows=rows)
    else:
        return "No file uploaded"