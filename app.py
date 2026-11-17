from flask import Flask
from uuid import UUID

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

# Dynamic Route - INT
@app.route("/user/<int:id>")
def user(id):
    return f"User ID: {id}"

# Dynamic Route - FLOAT
@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount}"

# Dynamic Route - STRING
@app.route("/student/<string:name>")
def student(name):
    return f"Student: {name}"

# Dynamic Route - UUID
@app.route("/teacher/<uuid:user_id>")
def teacher(user_id):
    return str(user_id)

# Dynamic Route - Path
@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

if __name__ == "__main__":
    app.run(debug=True)