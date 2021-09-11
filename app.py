from flask import Flask, request, jsonify, render_template
import mysql.connector
#from getpass import getpass
from mysql.connector import connect

connection = connect(host='us-cdbr-east-04.cleardb.com', 
    user='b7a35a7346aea6', 
    password='a2aa8c36', 
    database='heroku_38066fac900fae9')
cursor = connection.cursor()
connection2 = connect(host='us-cdbr-east-04.cleardb.com', 
    user='b7a35a7346aea6', 
    password='a2aa8c36', 
    database='heroku_38066fac900fae9')
cursor2 = connection2.cursor()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/name', methods=['POST'])
def name():
    name = request.form['name'].lower()
    #may need try except loop for repeating values
    cursor.execute('''INSERT INTO survey (name) VALUES ('{}');'''.format(name)) #will also be written to connection2
    connection.commit()
    cursor2.execute('''INSERT INTO leads (name) VALUES ('{}');'''.format(request.form['name'])) #will also be written to connection2
    connection2.commit()
    return render_template('index2.html', n_text=request.form['name'])

@app.route('/landingPage', methods=['POST'])
def landingPage():
    landingPage = request.form['landingPage']
    cursor.execute('''UPDATE survey SET landingPage='{}' WHERE landingPage IS NULL;'''.format(landingPage))
    connection.commit()
    return render_template('index2.html', n_text='Compleate', lp_text=request.form['landingPage'])

@app.route('/domain', methods=['POST'])
def domain():
    domain = request.form['domain'].lower().replace(' ', '_')
    cursor.execute('''UPDATE survey SET domain='{}' WHERE domain IS NULL;'''.format(domain))
    connection.commit()
    return render_template('index3.html')

@app.route('/adspend', methods=['POST'])
def adspend():
    adspend = int(request.form['adspend'].replace('$', '').replace(',', ''))
    try:
        cursor.execute('''UPDATE survey SET adspend='{}' WHERE adspend IS NULL;'''.format(adspend))
        connection.commit()
        return render_template('index3.html', as_text=adspend)
    except:
        return 'Please use only numbers, commas, and dollar signs, press the back arrow at the top of the page to return to the survey'

@app.route('/hardcosts', methods=['POST'])
def hardcosts():
    hardcosts = int(request.form['hardcosts'].replace('$', '').replace(',', ''))
    try:
        cursor.execute('''UPDATE survey SET hardcosts='{}' WHERE hardcosts IS NULL;'''.format(hardcosts))
        connection.commit()
        return render_template('index3.html', as_text='Compleate', h_text=request.form['hardcosts'])
    except:
        return 'Please use only numbers, commas, and dollar signs, press the back arrow at the top of the page to return to the survey'

@app.route('/revenue', methods=['POST'])
def revenue():
    revenue = int(request.form['revenue'].replace('$', '').replace(',', ''))
    try:
        cursor.execute('''UPDATE survey SET revenue='{}' WHERE revenue IS NULL;'''.format(revenue))
        connection.commit()
        return render_template('index4.html')
    except:
        return 'Please use only numbers, commas, and dollar signs, press the back arrow at the top of the page to return to the survey'

@app.route('/customer', methods=['POST'])
def customer():
    inp = request.form['customer']
    if inp == 'no':
        customer = 0
    if inp == 'yes':
        customer = 1
    cursor.execute('''UPDATE survey SET customer='{}' WHERE customer IS NULL;'''.format(customer))
    connection.commit()
    return render_template('index4.html', c_text=request.form['customer'])

@app.route('/model', methods=['POST'])
def model():
    model = request.form['model']
    cursor.execute('''UPDATE survey SET model='{}' WHERE model IS NULL;'''.format(model))
    connection.commit()
    return render_template('index4.html', c_text='Compleate', m_text=request.form['model'])

@app.route('/source', methods=['POST'])
def source():
    source = request.form['source']
    cursor.execute('''UPDATE survey SET source='{}' WHERE source IS NULL;'''.format(source))
    connection.commit()
    return render_template('index4.html', c_text='Compleate', m_text='Compleate', s_text=request.form['source'])

@app.route('/email', methods=['POST'])
def email():
    email = request.form['email']
    cursor2.execute('''UPDATE leads SET email='{}' WHERE email IS NULL;'''.format(email))
    connection2.commit()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)