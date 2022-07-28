from crypt import methods
import json
from flask import Flask, jsonify
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from requests import post
import psycopg2
 
app = Flask(__name__)

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='postgres',
        password='w1llres0lve')

cur = conn.cursor()

app = Flask(__name__)

@app.route("/")
def display():
    cur.execute('''SELECT * FROM employees''')

    result = cur.fetchall()
    conn.commit()
    conn.close()
    cur.close()

    return jsonify(result), 200

@app.route("/create", methods=['post'])
def create():
    cur.execute('''CREATE TABLE employees (employee_id int, name varchar(25), salary double)''')
    conn.commit()
    conn.close()
    cur.close()

    return "Table created", 200

@app.route("/insert/<int:id>/<string:name>/<int:salary>", methods=['POST'])
def insert(id, name, salary):
    query = "INSERT INTO employees VALUES ({},'{}',{})".format(id, name, salary)

    print(query)
    return "Values inserted", 200

# @app.route("/insert", methods=['post'])
# def insert():
#     cur.execute('''INSERT INTO employees VALUE (4,'Harry Potter',550000) ''')
#     conn.commit()
#     conn.close()
#     cur.close()

#     return "Values updated", 200

@app.route("/update", methods=['put'])
def update():
    cur.execute('''UPDATE employees SET name='Peter Parker' WHERE employee_id=3 ''')
    conn.commit()
    conn.close()
    cur.close()

    return "Values updated", 200

@app.route("/delete", methods=['delete'])
def delete():
    cur.execute('''DELETE FROM employees WHERE employee_id=4''')
    conn.commit()
    conn.close()
    cur.close()

    return "Values deleted", 200

# @app.route("/hello")
# def hello():
#     return "<h1>Hello!</h1>"