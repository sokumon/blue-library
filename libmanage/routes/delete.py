from flask import Flask, render_template, redirect, request, session
from libmanage import app, db
from libmanage.dbschema import User
from libmanage.handlers.users import delete_user
from libmanage.handlers.books import delete_book
from libmanage.handlers.members import delete_member
from libmanage.handlers.transactions import delete_transaction
import json

def handle_delete(func, data):
    status = {}
    try:
        if "id" in data:
            func(data["id"])
            status = {
                "message": "Success"
            }
        else:
            status = {
                "message": "Send the unique id"
            }
    except Exception as error:
        print(error)
        status = {
            "message": "No proper keys"
        }
    return json.dumps(status)

@app.post("/delete/<table_name>")
def delete(table_name):
    data = request.get_json()
    
    if table_name == "users":
        return handle_delete(delete_user, data)
    
    elif table_name == "books":
        return handle_delete(delete_book, data)
    
    elif table_name == "members":
        return handle_delete(delete_member, data)
    
    elif table_name == "transactions":
        return handle_delete(delete_transaction, data)
