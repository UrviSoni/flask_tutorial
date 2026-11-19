from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

app.secret_key = "change-this-in-prod"

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"),500

@app.route("/test")
def test_500(error):
    result = 10/0
    return str(result)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    session['username'] = 'Urvi'
    return "Login Successful!"

@app.route("/dashboard")
def dashboard():
    username = session.get("usesrname")
    if not username:
        return "Please login first!"
    return f"Welcome! {username}"

@app.route("/logout")
def logout():
    session.pop("username", None)
    return "Logged Out!"

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
            flash("Name is required", "danger")
            return redirect(url_for('contact'))
            # return "Name is Required"
        if not email:
            flash("Email is required", "danger")
            return redirect(url_for('email'))
            # return "Email is Required"
        if not age:
            flash("Age is required", "danger")
            return redirect(url_for('contact'))
            # return "Age is Required"
        if not age.isdigit():
            return "Age must be a number"
        age = int(age)
        flash("Registration Successful !", "success")
    return render_template("contact.html")

@app.route("/registration-success")
def success():
    return "Registration Successful"

@app.route("/search")
def search():
    query = request.args.get("query")
    return f" You searched for : {query}"

if __name__ == "__main__":
    app.run(debug=False)
