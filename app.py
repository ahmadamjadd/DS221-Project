from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import requests

app = Flask(__name__)
app.secret_key = 'hello'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"



@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("index.html", name=name)
    
    return render_template("form.html")
