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
    return render_template('index2.html')

@app.route('/landingPage', methods=['POST'])
def landingPage():
    landingPage = request.form['landingPage']
    cursor.execute('''UPDATE test SET col2='{}' WHERE col2 IS NULL;'''.format(landingPage)) #this query structure will be continued throughout
    connection.commit()
    return render_template('index2.html')

@app.route('/domain', methods=['POST'])
def domain():
    domain = request.form['domain'].lower().replace(' ', '_')
    return render_template('index2.html')

@app.route('/adspend', methods=['POST'])
def adspend():
    adspend = int(request.form['adspend'].lower().replace(' ', '_'))
    return render_template('index2.html')

@app.route('/hardcosts', methods=['POST'])
def hardcosts():
    hardcosts = int(request.form['hardcosts'].lower().replace(' ', '_'))
    return render_template('index2.html')

@app.route('/customer', methods=['GET'])
def customer():
    customer = request.form.get('customer')
    cursor.execute('''INSERT INTO test (testcol) VALUES ('{}');'''.format(customer))
    connection.commit()
    return render_template('index2.html')

@app.route('/model', methods=['GET'])
def model():
    model = request.form.get('model')
    cursor.execute('''INSERT INTO test (testcol) VALUES ('{}');'''.format(model))
    connection.commit()
    return render_template('index2.html')

@app.route('/source', methods=['GET'])
def source():
    source = request.form.get('source')
    cursor.execute('''INSERT INTO test (testcol) VALUES ('{}');'''.format(source))
    connection.commit()
    return render_template('index2.html')

@app.route('/email', methods=['POST'])
def email():
    email = request.form['email']
    return render_template('index2.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)