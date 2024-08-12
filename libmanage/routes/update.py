from flask import Flask, render_template, redirect, request, session
from libmanage import app, db
from libmanage.dbschema import User
from libmanage.handlers.users import update_user
from libmanage.handlers.books import update_book
from libmanage.handlers.members import update_member
from libmanage.handlers.transactions import update_transaction
import json

def handle_update(func, data):
    status = {}
    try:
        if "id" in data:
            id = data["id"]
            del data["id"]
            func(id, data)
            status = {
                "message": "Success"
            }
        else:
            status = {
                "message": "Send the unique id"
            }
    except KeyError:
        status = {
            "message": "No proper keys"
        }
    return json.dumps(status)

@app.post("/update/<table_name>")
def update(table_name):
    data = request.get_json()
    
    if table_name == "users":
        return handle_update(update_user, data)
    
    elif table_name == "books":
        return handle_update(update_book, data)
    
    elif table_name == "members":
        return handle_update(update_member, data)
    
    elif table_name == "transactions":
        return handle_update(update_transaction, data)
