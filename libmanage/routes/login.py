from libmanage import app
from flask import Flask, render_template, redirect, request, session
from libmanage.dbschema import User
import json
@app.post("/login")
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    user = User.query.filter_by(username=username).first()
    if user:
        if user.password == password:
            status = {
                "code": 200,
                "message":"Successful login"
            }
            return json.dumps(status)
    status = {
        "code":404,
        "message":"User Not Found"
    }
    return json.dumps(status)
