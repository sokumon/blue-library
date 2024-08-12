from flask import Flask, render_template, redirect, request, session
from libmanage import app, db
from libmanage.dbschema import User
from libmanage.handlers.users import create_user
from libmanage.handlers.books import create_book
from libmanage.handlers.members import create_member
from libmanage.handlers.transactions import create_transaction
from datetime import datetime
import json
import uuid

def handle_creation(func, data, **extra_fields):
    status = {}
    print(data)
    try:
        id = uuid.uuid4().hex
        if func(id, **data, **extra_fields):
            status = {
                "message": "Success"
            }
        else:
            status = {
                "message": "Failed to create record"
            }
    except KeyError:
        status = {
            "message": "No proper keys"
        }
    return json.dumps(status)

@app.post("/create/<table_name>")
def create(table_name):
    data = request.get_json()
    
    if table_name == "users":
        return handle_creation(create_user, data)
    
    elif table_name == "books":
        return handle_creation(create_book, data)
    
    elif table_name == "members":
        return handle_creation(create_member, data)
    
    elif table_name == "transactions":
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y")
        return handle_creation(create_transaction, data, date_time=date_time)
