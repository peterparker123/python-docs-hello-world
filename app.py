from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("Hello RK!")
    return "Hello, Andoria!"

