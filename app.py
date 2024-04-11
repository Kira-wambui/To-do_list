from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from user import User

app = Flask(__name__)
app.secret_key = '0740880031@Kira'  # Change this to a random secret key

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

# Other routes and functions...

if __name__ == "__main__":
    app.run(debug=True)
