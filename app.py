from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required
from user import User
from todo_list import TodoList

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    return User.get(username)

todo_list = TodoList()

@app.route("/")
@login_required
def index():
    tasks = todo_list.view_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Perform user registration logic here
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.get(username)
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("index"))
        else:
            return render_template("login.html", message="Invalid username or password.")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
