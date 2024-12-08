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
    scaling = request.form.get('scaling')
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
            
            session['filename'] = filename
            session['selected_option'] = selected_option
            session['selected_method'] = selected_method
            session['scaling'] = scaling
            
            return redirect(url_for('calculate_grades', filename=filename, selected_option=selected_option, selected_method=selected_method, scaling=scaling))
    
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
    scaling = int(request.args.get('scaling'))

    if filename:

        df = pd.read_csv(f"uploads/{filename}")

        if option == "Relative":

            if type == "fixed":
                grades = grade_with_hec_thresholds(df)
            elif type == "custom":
                return render_template("relative_threshold.html", option=option)
            
        elif option == "Absolute":
            if type == "fixed":
                grades = grade_with_hec_absolute(df, scaling=scaling)
            elif type == "custom":
                return render_template("absolute_threshold.html", option=option)
        rows = grades.values.tolist()
        columns = grades.columns.tolist()
        return render_template("grades.html", columns=columns, rows=rows)
    else:
        return "No file uploaded"
    
@app.route("/absolute_grading", methods=["GET", "POST"])
def custom_marks():
    if request.method == "POST":

        # Collect data from the form
        grade_A_plus_min = request.form.get("grade_A_plus_min")
        grade_A_plus_max = request.form.get("grade_A_plus_max")
        
        grade_A_min = request.form.get("grade_A_min")
        grade_A_max = request.form.get("grade_A_max")
        
        grade_A_minus_min = request.form.get("grade_A_minus_min")
        grade_A_minus_max = request.form.get("grade_A_minus_max")
        
        grade_B_plus_min = request.form.get("grade_B_plus_min")
        grade_B_plus_max = request.form.get("grade_B_plus_max")
        
        grade_B_min = request.form.get("grade_B_min")
        grade_B_max = request.form.get("grade_B_max")
        
        grade_B_minus_min = request.form.get("grade_B_minus_min")
        grade_B_minus_max = request.form.get("grade_B_minus_max")
        
        grade_C_plus_min = request.form.get("grade_C_plus_min")
        grade_C_plus_max = request.form.get("grade_C_plus_max")
        
        grade_C_min = request.form.get("grade_C_min")
        grade_C_max = request.form.get("grade_C_max")
        
        grade_C_minus_min = request.form.get("grade_C_minus_min")
        grade_C_minus_max = request.form.get("grade_C_minus_max")
        
        grade_D_min = request.form.get("grade_D_min")
        grade_D_max = request.form.get("grade_D_max")
        
        # Create a dictionary with all the collected marks ranges
        grade = {
            "A_plus": (int(grade_A_plus_min), int(grade_A_plus_max)),
            "A": (int(grade_A_min), int(grade_A_max)),
            "A_minus": (int(grade_A_minus_min), int(grade_A_minus_max)),
            "B_plus": (int(grade_B_plus_min), int(grade_B_plus_max)),
            "B": (int(grade_B_min), int(grade_B_max)),
            "B_minus": (int(grade_B_minus_min), int(grade_B_minus_max)),
            "C_plus": (int(grade_C_plus_min), int(grade_C_plus_max)),
            "C": (int(grade_C_min), int(grade_C_max)),
            "C_minus": (int(grade_C_minus_min), int(grade_C_minus_max)),
            "D": (int(grade_D_min), int(grade_D_max))
        }


        filename = session.get('filename')
        scaling = int(session.get('scaling'))
        if filename:
            df = pd.read_csv(f"uploads/{filename}")
            marks = grade_with_custom_absolute(df, grade, scaling=scaling)
            rows = marks.values.tolist()
            columns = marks.columns.tolist()
            return render_template("grades.html", columns=columns, rows=rows)
    else:
        return render_template("absolute_threshold.html")
    
@app.route("/relative_grading", methods=["GET", "POST"])
def custom_relative_marks():
    if request.method == "POST":

        # Collect data from the form
        grade_A_plus_min = request.form.get("grade_A_plus_min")
        grade_A_plus_max = request.form.get("grade_A_plus_max")
        
        grade_A_min = request.form.get("grade_A_min")
        grade_A_max = request.form.get("grade_A_max")
        
        grade_A_minus_min = request.form.get("grade_A_minus_min")
        grade_A_minus_max = request.form.get("grade_A_minus_max")
        
        grade_B_plus_min = request.form.get("grade_B_plus_min")
        grade_B_plus_max = request.form.get("grade_B_plus_max")
        
        grade_B_min = request.form.get("grade_B_min")
        grade_B_max = request.form.get("grade_B_max")
        
        grade_B_minus_min = request.form.get("grade_B_minus_min")
        grade_B_minus_max = request.form.get("grade_B_minus_max")
        
        grade_C_plus_min = request.form.get("grade_C_plus_min")
        grade_C_plus_max = request.form.get("grade_C_plus_max")
        
        grade_C_min = request.form.get("grade_C_min")
        grade_C_max = request.form.get("grade_C_max")
        
        grade_C_minus_min = request.form.get("grade_C_minus_min")
        grade_C_minus_max = request.form.get("grade_C_minus_max")
        
        grade_D_min = request.form.get("grade_D_min")
        grade_D_max = request.form.get("grade_D_max")
        
        # Create a dictionary with all the collected marks ranges
        grade = {
            "A_plus": (int(grade_A_plus_min), int(grade_A_plus_max)),
            "A": (int(grade_A_min), int(grade_A_max)),
            "A_minus": (int(grade_A_minus_min), int(grade_A_minus_max)),
            "B_plus": (int(grade_B_plus_min), int(grade_B_plus_max)),
            "B": (int(grade_B_min), int(grade_B_max)),
            "B_minus": (int(grade_B_minus_min), int(grade_B_minus_max)),
            "C_plus": (int(grade_C_plus_min), int(grade_C_plus_max)),
            "C": (int(grade_C_min), int(grade_C_max)),
            "C_minus": (int(grade_C_minus_min), int(grade_C_minus_max)),
            "D": (int(grade_D_min), int(grade_D_max))
        }


        filename = session.get('filename')
        if filename:
            df = pd.read_csv(f"uploads/{filename}")
            marks = grade_with_custom_relative(df, grade)
            rows = marks.values.tolist()
            columns = marks.columns.tolist()
            return render_template("grades.html", columns=columns, rows=rows)
    else:
        return render_template("relative_threshold.html")