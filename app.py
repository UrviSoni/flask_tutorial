from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Urvi"
    course = "Flask"
    city = "Ahmedabad"
    age = 29
    return render_template("index.html", name=name, course=course, city=city, age=age)

if __name__ == "__main__":
    app.run(debug=True)
