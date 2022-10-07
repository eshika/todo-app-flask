# CS 279 Programming HW5

This repo contains the code for a basic To Do App website made with Flask. The main code file is `app.py` and `templates/base.html`

On this To Do App website, users can create and complete tasks which are added to a To Do List. This site also has the functionality of being able to delete tasks. The site also displays a counter of the total number of tasks and the number of completed tasks. 

## Usage

Install Flask

```
$ pip install Flask
$ pip install Flask-SQLAlchemy
```
Set environment variables in terminal
```
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```
or on Windows

```
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```
Run the app
```
$ flask run
```


## References

This site was created using the following tutorials:
* https://www.python-engineer.com/posts/flask-todo-app/
* https://github.com/python-engineer/flask-todo
* https://blog.devgenius.io/how-to-create-a-todo-application-with-flask-21b71651c7dc
