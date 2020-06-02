import csv
import smtplib

def mail(email): #function for sending mail to student"""
    message = "Congratulation are registered!!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("svraj157@gmail.com","Usa@1234")
    server.sendmail("svraj157@gmail.com",email,message)

def listdata(): #list all the student who already registered"""
    file = open("data.csv","r")
    reder = csv.reader(file)
    students = list(reder)
    file.close()
    return students
