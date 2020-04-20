#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:45:52 2020

@author: caoyuru
"""

from flask import Flask, render_template, request, jsonify   
from flaskext.mysql import MySQL  
import requests


mysql = MySQL()
app = Flask(__name__)
app.config['SECRET_KEY'] = '26ed2a694605ee4333b290e5ad9de2a418a8113b50feae77'

# MySQL Configuration
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
#app.config['MYSQL_DATABASE_DB'] = 'feedback'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")
    
    

@app.route('/chat', methods=["GET", "POST"])
def chat():
    """
    chat end point that performs NLU using rasa.ai
    and constructs response from response.py
    """
    user_message = request.form["text"]
   # try:

        #response = requests.post('http://35.211.139.242:5000/conversations/' + session_id + '/respond',
                                 #json={"query": user_message})
    #conn = mysql.connect()
    print(user_message)
    response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": user_message})
    response = response.json()
    #bot = response[0]["text"]
    #cursor = conn.cursor()
    #cursor.execute('''INSERT INTO responses (user,bot) VALUES (%s,%s)''',
    #(user_message, bot))
    #conn.commit()
    #cursor.close()
    
    return jsonify({"status": "success", "response": response[0]["text"]})
    '''except Exception as e:
        print(e)
        return jsonify({"status": "success", "response": "Sorry I am not trained to do that yet..."})'''
    

    
if __name__ == "__main__":
    app.run(debug=True)