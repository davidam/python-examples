from flask import *
 
# Initialize Flask function
app = Flask(__name__)
app.secret_key = "GeeksForGeeks"
 
 
# home function for index.html
@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")
 
 
# row function for profile.html
@app.route("/profile")
def row():
    return render_template("profile.html")
 
 
# write if and else condition if we provide write password then he will redirect
# us in profile page otherwise he will redirect us on same page with
# flashing massage Invalid Password
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form['pass'] != "GFG":
            error = "Invalid Password"
        else:
            flash("You are successfully login into the Flask Application")
            return redirect(url_for('row'))
 
    return render_template("login.html", error=error)
 
 
# execute command with debug function
if __name__ == '__main__':
    app.run(debug=True)