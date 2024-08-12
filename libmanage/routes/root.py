from libmanage import app

@app.route("/")
def hello_world():
    return "Welecome to the API"