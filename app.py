from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

# Static Route
@app.route("/users")
def users():
    return "Welcome to User Page"

# Dynamic Route
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

# Multiple Dynamic Parameter Route
@app.route("/student/<name>/<course>")
def student(name, course):
    return f"{name} is learning {course}"

#Static Route
@app.route("/contact")
def contact():
    return "Welcome to Contact US Page"

if __name__ == "__main__":
    app.run(debug=True)