from flask import Flask, render_template, redirect, request, session
from libmanage import app,db
from libmanage.dbschema import User,Book
from libmanage.handlers.users import read_all_users
from libmanage.handlers.books import read_all_books
from libmanage.handlers.members import read_all_members
from libmanage.handlers.transactions import read_all_transactions
import json 

@app.get("/read/<table_name>")
def read_get(table_name):
    status = []
    values = None
    if table_name == "users":
        values = read_all_users()
    elif table_name == "books":
        values = read_all_books()
    elif table_name == "members":
        values = read_all_members()
    elif table_name == "transactions":
        values = read_all_transactions()
        return json.dumps(values) 
    
    for value in values:
        value.__dict__.pop('_sa_instance_state',None)
        temp = value.__dict__.copy()
        status.append(temp)
    return json.dumps(status)