from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form.get("name").strip()
        email = request.form.get("email").strip()
        age = request.form.get("age").strip()
        if not name:
            return "Name is Required"
        if not email:
            return "Email is Required"
        if not age:
            return "Age is Required"
        if not age.isdigit():
            return "Age must be a number"
        age = int(age)
        return "Registration Successful"
        # print("Name: ", name)
        # print("EMail: ", email)
        # print("Message: ", message)
        # return f"Hello, {name}"
    return render_template("contact.html")

@app.route("/search")
def search():
    query = request.args.get("query")
    return f" You searched for : {query}"

if __name__ == "__main__":
    app.run(debug=True)
