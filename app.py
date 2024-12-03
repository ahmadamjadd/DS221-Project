from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
import requests
from werkzeug.utils import secure_filename
import os
import pandas as pd
from absolute_grading import *
from relativegrading import *
app = Flask(__name__)
app.secret_key = 'hello'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

Session(app)

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
    selected_option = request.form.get('options')
    selected_method = request.form.get('type')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # Save the uploaded folder
        upload_folder = app.config['UPLOAD_FOLDER']
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        try:
            # Read the head
            df = pd.read_csv(f"uploads/{filename}", nrows=1)
            columns = df.columns.tolist()
            format = ["name", "reg", "marks"]
            if [col.lower() for col in columns] != format:
                os.remove(file_path)
                warnings = "Enter in specified format"
                return render_template("form.html", warnings=warnings)
            
            return redirect(url_for('calculate_grades', filename=filename, selected_option=selected_option, selected_method=selected_method))
    
        except Exception as e:
            os.remove(file_path) 
            warnings = f"Error reading the CSV file. {str(e)}"
            return render_template("form.html", warnings=warnings)
    else:
        return "Invalid file format. Please upload a CSV file."
    
@app.route("/grades", methods=["GET"])
def calculate_grades():
    filename = request.args.get('filename')
    option = request.args.get('selected_option')
    type = request.args.get('selected_method')

    if filename:

        df = pd.read_csv(f"uploads/{filename}")

        if option == "Relative":

            if type == "fixed":
                grades = grade_with_hec_thresholds(df)
            elif type == "custom":
                return render_template("relative_threshold.html", option=option)
            
        elif option == "Absolute":
            if type == "fixed":
                grades = generate_grade_report(df)
            elif type == "custom":
                return render_template("absolute_threshold.html", option=option)
        rows = grades.values.tolist()
        columns = grades.columns.tolist()
        return render_template("grades.html", columns=columns, rows=rows)
    else:
        return "No file uploaded"