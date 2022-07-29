from crypt import methods
import json
from flask import Flask, jsonify
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from requests import post
import psycopg2
 
app = Flask(__name__)

def connection():
    conn = psycopg2.connect(
            host="localhost",
            database="flask_db",
            user='postgres',
            password='w1llres0lve')
    
    return conn

@app.route("/")
def display():
    conn = connection()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM employees''')

    result = cur.fetchall()
    conn.commit()
    conn.close()
    cur.close()

    return json.dumps(result), 200

@app.route("/create", methods=['POST'])
def create():
    conn = connection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE employees (employee_id int, name varchar(25), salary double)''')
    conn.commit()
    conn.close()
    cur.close()

    return "Table created", 200

@app.route("/insert", methods=['POST'])
def insert():
    conn = connection()
    cur = conn.cursor()
    id = request.form['id']
    name = request.form['name']
    salary = request.form['salary']
    query = "INSERT INTO employees VALUES ({},'{}',{})".format(id, name, salary)
    cur.execute(query)
    conn.commit()
    conn.close()
    cur.close()
    # print(query)
    return "Values inserted", 200

@app.route("/update", methods=['PUT'])
def update():
    conn = connection()
    cur = conn.cursor()
    cur.execute('''UPDATE employees SET name='Peter Parker' WHERE employee_id=3 ''')
    conn.commit()
    conn.close()
    cur.close()

    return "Values updated", 200

@app.route("/delete/<id>", methods=['DELETE'])
def delete(id):
    conn = connection()
    cur = conn.cursor()
    cur.execute('''DELETE FROM employees WHERE employee_id={}'''.format(id))
    conn.commit()
    conn.close()
    cur.close()

    return "Values deleted", 200

# @app.route("/hello")
# def hello():
#     return "<h1>Hello!</h1>"