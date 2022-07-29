from flask import Blueprint, request
from . import db
import json, psycopg2

main = Blueprint('main', __name__)

def connection():
    conn = psycopg2.connect(
            host="localhost",
            database="flask_db",
            user='postgres',
            password='w1llres0lve')
    
    return conn

@main.route("/")
def display():
    conn = connection()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM employees''')

    result = cur.fetchall()
    conn.commit()
    conn.close()
    cur.close()

    return json.dumps(result), 200

@main.route("/create", methods=['POST'])
def create():
    conn = connection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE employees (employee_id int, name varchar(25), salary double)''')
    conn.commit()
    conn.close()
    cur.close()

    return "Table created", 200

@main.route("/insert", methods=['POST'])
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

@main.route("/update", methods=['PUT'])
def update():
    conn = connection()
    cur = conn.cursor()
    id = request.form['id']
    name = request.form['name']
    salary = request.form['salary']
    if name:
        cur.execute('''UPDATE employees SET name='{}' WHERE employee_id={} '''.format(name,id))
    if salary:
        cur.execute('''UPDATE employees SET salary={} WHERE employee_id={} '''.format(salary,id))
    conn.commit()
    conn.close()
    cur.close()

    return "Values updated", 200

@main.route("/delete", methods=['DELETE'])
def delete():
    conn = connection()
    cur = conn.cursor()
    id = request.form['id']
    cur.execute('''DELETE FROM employees WHERE employee_id={}'''.format(id))
    conn.commit()
    conn.close()
    cur.close()

    return "Record deleted", 200

# @main.route("/hello")
# def hello():
#     return "<h1>Hello!</h1>"