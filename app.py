from random import random

from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import warnings
import numpy as np
import nltk
import joblib


from topic_modelling import Topic_modeling

import sqlite3
import random

import smtplib 
from email.message import EmailMessage
from datetime import datetime


app = Flask(__name__)


cv_bin_1 = pickle.load(open("data1_bin.pickle", 'rb'))
cv_multi_1 = pickle.load(open("data1_multi.pickle", 'rb'))

model_bin_1 = joblib.load('model_data1_bin.sav')
model_multi_1 = joblib.load('model_data1_multi.sav')


cv_bin_2 = pickle.load(open("data2_bin.pickle", 'rb'))
cv_multi_2 = pickle.load(open("data2_multi.pickle", 'rb'))

model_bin_2 = joblib.load('model_data2_bin.sav')
model_multi_2 = joblib.load('model_data2_multi.sav')

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict1',methods=['POST'])
def predict1():

    if request.method == 'POST':
        
        message = request.form['message']
        data = [message]
        vect = cv_bin_1.transform(data).toarray()
        my_prediction1 = model_bin_1.predict(vect)
        
        vect1 = cv_multi_1.transform(data).toarray()
        my_prediction2 = model_multi_1.predict(vect1)
        
        df = pd.DataFrame({'sentence':data})
        t,word = Topic_modeling(df)

        return render_template('result1.html',prediction1 = my_prediction1,prediction2 = my_prediction2,message=message,to = t, wo = word)


@app.route('/predict2',methods=['POST'])
def predict2():

    if request.method == 'POST':
        
        message = request.form['message']
        data = [message]
        vect = cv_bin_2.transform(data).toarray()
        my_prediction1 = model_bin_2.predict(vect)
        
        vect1 = cv_multi_2.transform(data).toarray()
        my_prediction2 = model_multi_2.predict(vect1)
        
        df = pd.DataFrame({'sentence':data})
        t,word = Topic_modeling(df)

        return render_template('result2.html',prediction1 = my_prediction1,prediction2 = my_prediction2,message=message,to = t, wo = word)


@app.route('/index1')
def index1():
	return render_template('index1.html')

@app.route('/index2')
def index2():
	return render_template('index2.html')

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')


@app.route("/signup")
def signup():
    global otp, username, name, email, number, password
    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')

    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")
    # otp = random.randint(1000,5000)
    # print(otp)
    # msg = EmailMessage()
    # msg.set_content("Your OTP is : "+str(otp))
    # msg['Subject'] = 'OTP'
    # msg['From'] = "vandhanatruprojects@gmail.com"
    # msg['To'] = email
    
    
    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.starttls()
    # s.login("vandhanatruprojects@gmail.com", "pahksvxachlnoopc")
    # s.send_message(msg)
    # s.quit()
    # return render_template("val.html")

@app.route('/predict_lo', methods=['POST'])
def predict_lo():
    global otp, username, name, email, number, password
    if request.method == 'POST':
        message = request.form['message']
        print(message)
        if int(message) == otp:
            print("TRUE")
            con = sqlite3.connect('signup.db')
            cur = con.cursor()
            cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
            con.commit()
            con.close()
            return render_template("signin.html")
    return render_template("signup.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("index1.html")
    else:
        return render_template("signin.html")


@app.route('/about1')
def about1():
	return render_template('about1.html')

@app.route('/about2')
def about2():
	return render_template('about2.html')

@app.route('/notebook1')
def notebook1():
	return render_template('Dataset1.html')

@app.route('/notebook2')
def notebook2():
	return render_template('Dataset2.html')



if __name__ == '__main__':
	app.run(debug=False)
