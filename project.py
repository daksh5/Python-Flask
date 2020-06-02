"""Vraj Shah"""

from flask import Flask, render_template, request, redirect
import csv
import smtplib
from support import *


app = Flask(__name__)


@app.route("/") #if user will go http://127.0.0.1:5000/ then open inde.html from template
def hello():
    return render_template('index.html')


@app.route("/register", methods=['POST']) #When user will submit the form of index.html then it will come here
def home():

    if not request.form.get("name") or not request.form.get("department") or not request.form.get("id") or not request.form.get("email"):
        return render_template('fail.html')  #checkin that user was forgot to enter something or not

    name = request.form.get("name")
    department = request.form.get("department")
    id = request.form.get("id")
    email = request.form.get("email")

    file  = open("data.csv","a")
    f = open("data.csv","r")
    reder_record = csv.reader(f)
    student_record = list(reder_record)
    r=[]

    for x in range(len(student_record)):
        r = student_record[x][0]

    if (request.form.get("id")) in r:
        f.close()
        file.close()
        return render_template('exist.html')
    else:
        writer = csv.writer(file) #entering the student info in data.cvs file"""
        writer.writerow((request.form.get("id"),request.form.get("name"),
        request.form.get("department"),request.form.get("email")))
        file.close()
        f.close()
        mail(email) #support.py function to send a email to student"""
        return render_template('successful.html')


@app.route("/registered") #when student will hit he/she can see all the previous student who did registerd"""
def registered():

    try:
        s = listdata() #supprt.py function that list all the data"""
        return render_template('registered.html', students=s)
    except IOError:
        print("File not accessible")
    return render_template('file not exist.html')


if __name__ == "__main__":
    app.run(debug = True)
