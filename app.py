from flask import Flask, render_template, session, request, redirect, url_for
from decouple import config
from database.connection import Connection
from database.models.users import Users
from database.models.authors import Authors


app = Flask(__name__)
app.secret_key = "j2h31KL!231l23kh2lkh@#hdfla"
my_connection:Connection= Connection(
    host = 'localhost',
    port = 5432,
    user = 'postgres',
    password = 'admin',
    dbname = 'cs_forum'
)

@app.route("/",methods=["POST","GET"])
def index():
    return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login_func():
    if request.method=="POST":
        login = str(request.form.get("login"))
        password = str(request.form.get("password"))
        status = str(request.form.get("status"))
        if login and password and status:
            if status =="user":
                if Users.login_user(conn=my_connection.conn,login=login,password=password)==0:
                    session["login"] = login
                    session["password"] = password
                    return redirect(url_for("index"))
                else:
                    return "<h1>No such user in database</h1>"
            elif status =="author":
                if Authors.login_author(conn=my_connection.conn,login=login,password=password) == 0:
                    session["login"] = login
                    session["password"] = password
                    return redirect(url_for("index"))
                else:
                    return "<h1>Something went wrong</h1>"     
    return render_template("login.html")


@app.route("/registrate",methods=["POST","GET"])
def registrate():
    if request.method=="POST":
        login = str(request.form.get("login"))
        password = str(request.form.get("password"))
        radio = str(request.form.get("status"))
        if login and password and radio:
            if radio == "user":
                print(Users.registrate_user(conn=my_connection.conn,login=login,password=password))
                return redirect(url_for("login_func"))
            elif radio =="author":
                print(Authors.insert_author(conn=my_connection.conn,login=login,password=password))
                return redirect(url_for("login_func"))
            else:
                return "<h1>Something goes wrong,try again</h1>"
    return render_template("registrate.html")




if __name__=="__main__":
    my_connection.create_table()
    app.run()