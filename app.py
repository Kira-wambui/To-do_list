from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_restful import Api, Resource, reqparse
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.exceptions import NotFound, Unauthorized, BadRequest
from user import User
from todo_list import TodoList

app = Flask(__name__)
app.secret_key = '0740880031@Kira'  # Change this to a random secret key

api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(username):
    return User.get(username)

todo_list = TodoList()

# Define request parsers
register_parser = reqparse.RequestParser()
register_parser.add_argument('username', type=str, required=True, help='Username is required')
register_parser.add_argument('password', type=str, required=True, help='Password is required')

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, required=True, help='Username is required')
login_parser.add_argument('password', type=str, required=True, help='Password is required')

task_parser = reqparse.RequestParser()
task_parser.add_argument('task', type=str, required=True, help='Task data is required')

# API resource for user registration
class Register(Resource):
    def post(self):
        args = register_parser.parse_args()
        username = args['username']
        password = args['password']
        if User.get(username):
            raise BadRequest('User already exists')
        user = User(username, password)
        user.save()  # Implement the save method in your User class
        return {'message': 'User registered successfully'}, 201

# API resource for user login
class Login(Resource):
    def post(self):
        args = login_parser.parse_args()
        username = args['username']
        password = args['password']
        user = User.get(username)
        if user and user.check_password(password):
            login_user(user)
            return {'message': 'Login successful'}, 200
        else:
            raise Unauthorized('Invalid username or password')

# API resource for user logout
class Logout(Resource):
    @login_required
    def post(self):
        logout_user()
        return {'message': 'Logout successful'}, 200

# API resource for managing tasks in the todo list
class Tasks(Resource):
    @login_required
    def get(self):
        tasks = todo_list.view_tasks()
        return jsonify(tasks)

    @login_required
    def post(self):
        args = task_parser.parse_args()
        task = args['task']
        todo_list.add_task(task)
        return {'message': 'Task added successfully'}, 201

    @login_required
    def put(self, task_id):
        try:
            todo_list.mark_completed(task_id)
            return {'message': 'Task marked as completed'}, 200
        except IndexError:
            raise NotFound('Task not found')

# Add API resources to the API
api.add_resource(Register, '/api/register')
api.add_resource(Login, '/api/login')
api.add_resource(Logout, '/api/logout')
api.add_resource(Tasks, '/api/tasks', '/api/tasks/<int:task_id>')

@app.route("/")
@login_required
def index():
    tasks = todo_list.view_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
@login_required
def add_task():
    task = request.form["task"]
    todo_list.add_task(task)
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
@login_required
def complete_task(task_id):
    try:
        todo_list.mark_completed(task_id)
        return redirect(url_for("index"))
    except IndexError:
        raise NotFound('Task not found')

# Error handling for 404 Not Found
@app.errorhandler(NotFound)
def not_found_error(error):
    return render_template('error.html', message='Page not found'), 404

# Error handling for 401 Unauthorized
@app.errorhandler(Unauthorized)
def unauthorized_error(error):
    return render_template('error.html', message='Unauthorized access'), 401

# Error handling for 400 Bad Request
@app.errorhandler(BadRequest)
def bad_request_error(error):
    return render_template('error.html', message='Bad request'), 400

if __name__ == "__main__":
    app.run(debug=True)
