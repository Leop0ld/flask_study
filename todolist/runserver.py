from flask import Flask, render_template, request, redirect, url_for

from database import init_db
from database import db_session
from models import Todo

# Initialize Database
init_db()

# Initialize Flask app
app = Flask(__name__)

# Configure Debug mode
app.config['DEBUG'] = True


'''
@app.context_processor
def inject_user():
    return dict(user=g.user)
'''


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/todolist/')
def todolist():
    todo_list = Todo.query.all()

    context = {
        'todo_list': todo_list,
    }

    return render_template('todolist.html', context=context)


@app.route('/todolist/create/', methods=['GET', 'POST'])
def todolist_create():
    if request.method == 'POST':
        title = request.form['title']

        new_todo = Todo(title)
        db_session.add(new_todo)
        db_session.commit()

        return redirect(url_for('todolist'))

    return render_template('todolist_create.html')


if __name__ == '__main__':
    app.run()
