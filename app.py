from flask import Flask, request, jsonify, render_template
import mysql.connector
#from getpass import getpass
from mysql.connector import connect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)