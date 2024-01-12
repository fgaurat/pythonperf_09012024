from flask import Flask,render_template
from UserDAO import UserDAO

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/index_old")
def index_old():
    dao = UserDAO("./formation.db")
    users = dao.findAll()

    html=""
    for user in users:
        html+=f"<li>{user.last_name}, {user.first_name}</li>"
    
    return "<ul>"+html+"</ul>"


@app.route("/")
def index():
    dao = UserDAO("./formation.db")
    users = dao.findAll()

    return render_template('user_list.html',users=users)
