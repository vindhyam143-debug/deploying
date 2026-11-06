from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message":"Api is working"}

@app.route("/hello")
def hello():
    return {"message":"Hello BCA"}

@app.route("/students")
def students():
    return [
        {"id":1, "name": "rahul"},
        {"id":2, "name": "priya"},
        {"id":3, "name": "megala"},
        {"id":4, "name": "vikas"},
        {"id":5, "name": "rinku"},
    ]

if __name__ == "_main_":
    app.run(debug=True)