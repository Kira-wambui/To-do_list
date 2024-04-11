from flask import Flask, render_template, request, redirect, url_for
from todo_list import TodoList

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

todo_list = TodoList()

@app.route("/")
def index():
    tasks = todo_list.view_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]
    todo_list.add_task(task)
    return redirect(url_for("index"))

@app.route("/complete/<int:task_idx>")
def complete_task(task_idx):
    todo_list.mark_completed(task_idx)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
