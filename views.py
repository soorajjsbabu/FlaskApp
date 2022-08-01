from flask import Blueprint, request
from . import db
from .models import employee
import json

main = Blueprint('main', __name__)

@main.route("/")
def display():
    employee_details = employee.query.all()
    details = []

    for employee_detail in employee_details:
        details.append({'id':employee_detail.id,'name':employee_detail.name,'salary':employee_detail.salary})

    return json.dumps(details), 200

@main.route("/insert", methods=['POST'])
def insert():
    eid = request.form['id']
    ename = request.form['name']
    esalary = request.form['salary']
    new_data = employee(id=eid,name=ename,salary=esalary)
   
    db.session.add(new_data)
    db.session.commit()

    return "Values inserted", 200

@main.route("/update", methods=['PUT'])
def update():
    eid = request.form['id']
    ename = request.form['name']
    esalary = request.form['salary']
    if ename:
        db.session.query(employee).filter(employee.id == eid).update({'name':ename})
        db.session.commit()
    if esalary:
        db.session.query(employee).filter(employee.id == eid).update({'salary':esalary})
        db.session.commit()

    return "Values updated", 200

@main.route("/delete", methods=['DELETE'])
def delete():
    eid = request.form['id']
    db.session.query(employee).filter(employee.id == eid).delete()
    db.session.commit()
    
    return "Record deleted", 200

# @main.route("/hello")
# def hello():
#     return "<h1>Hello!</h1>"