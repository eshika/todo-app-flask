from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize app
app = Flask(__name__)

# /// = relative path, //// = absolute path
# Initialize db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Declare todo class, which stores an id, task, and whether there is completed
class Todo(db.Model):
    # Id represents the task number (unique to the task)
    id = db.Column(db.Integer, primary_key=True)
    # Title represents the task name
    title = db.Column(db.String(100))
    # Complete represents whether or not the task is complete
    complete = db.Column(db.Boolean)

# Default to rendering the base html template
@app.route("/")
def home():
    # Get all items in the db currently and store them as todo_list
    todo_list = Todo.query.all()
    # Get current number of tasks
    num_tasks = len(todo_list)
    # Get current number of completed tasks
    num_completed = len(list(filter(lambda x: x.complete, todo_list)))
    # Render the home page template with the current todo list in the db
    return render_template("base.html", todo_list=todo_list, num_tasks=num_tasks, num_completed=num_completed)

# When the form is submitted
@app.route("/add", methods=["POST"])
def add():
    # Get task name from the form
    title = request.form.get("title")
    # Create new todo with title from form 
    new_todo = Todo(title=title, complete=False)
    # Add new todo to the db
    db.session.add(new_todo)
    # Push the new todo to the db
    db.session.commit()
    # Redirect to home page
    return redirect(url_for("home"))

# When a task is updated
@app.route("/update/<int:todo_id>")
def update(todo_id):
    # Identify the todo to be updated
    todo = Todo.query.filter_by(id=todo_id).first()
    # Change the complete status
    todo.complete = not todo.complete
    # Push the updated todo to the db
    db.session.commit()
    # Redirect to home page
    return redirect(url_for("home"))

# When a task is deleted
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # Identify the todo to be deleted
    todo = Todo.query.filter_by(id=todo_id).first()
    # Delete the todo from the db
    db.session.delete(todo)
    # Push the updated todo to the db
    db.session.commit()
    # Redirect to home page
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.create_all()
    # Run app 
    app.run(debug=True)
