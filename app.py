from flask import Flask, request, jsonify, render_template
import mysql.connector
from getpass import getpass
from mysql.connector import connect

connection = connect(host='localhost', user='root', password='Raptor//Kona9', database='leads')
cursor = connection.cursor()
connection2 = connect(host='localhost', user='root', password='Raptor//Kona9', database='fox_data_consulting')
cursor2 = connection2.cursor()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/name', methods=['POST'])
def name():
    name = request.form['name'].lower()
    cursor.execute('''INSERT INTO test (col1) VALUES ('{}');'''.format(name))
    connection.commit()
    return name

@app.route('/landingPage', methods=['POST'])
def landingPage():
    landingPage = request.form['landingPage']
    cursor.execute('''UPDATE test SET col2='{}' WHERE col1 IS NULL;'''.format(landingPage)) #'''INSERT INTO test (col2) VALUES ('{}');'''.format(landingPage))
    connection.commit()
    return landingPage

'''@app.route('/predict', methods=['POST'])
def predict():
    name = get_name()
    landingPage = get_landingPage()
    cursor.execute('INSERT INTO test (col1, col2) VALUES ('{}', '{}');'.format(name, landingPage))
    connection.commit()
    return render_template('index.html')'''

if __name__ == "__main__":
    app.run(debug=True, threaded=True)