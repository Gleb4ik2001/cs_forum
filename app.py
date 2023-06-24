from flask import Flask, render_template, session, request, redirect, url_for , flash
from decouple import config
from database.connection import Connection
from database.models.users import Users
from database.models.authors import Authors
from database.models.articles import Articles


app = Flask(__name__)
app.config["SECRET_KEY"] = '3ghj123j3jhghj#ghghjG#K#2klfhd'

my_connection:Connection= Connection(
    host = 'localhost',
    port = 5432,
    user = 'postgres',
    password = 'admin',
    dbname = 'cs_forum'
)

@app.route("/",methods=["POST","GET"])
def index():
    if "logged_in" in session and session["logged_in"] and session['status']=="user":
        articles =Articles.get_all_articles(
            conn=my_connection.conn,
        )
        return render_template("index.html",articles = articles)
    elif "logged_in" in session and session["logged_in"] and session['status']=="author":
        return render_template('index_author.html')
    else:
        return redirect(url_for('login_func'))


@app.route("/login",methods=["POST","GET"])
def login_func():
    if request.method=="POST":
        login = str(request.form.get("login"))
        password = str(request.form.get("password"))
        status = str(request.form.get("status"))
        if login and password and status:
            if status =="user":
                if Users.login_user(conn=my_connection.conn,login=login,password=password) == 0:
                    session["logged_in"] = True
                    session["login"] = login
                    session['status'] = 'user'
                    return redirect(url_for("index"))
                else:
                    return "<h1>No such user in database</h1>"
            elif status =="author":
                if Authors.login_author(conn=my_connection.conn,login=login,password=password) == 0:
                    session["logged_in"] = True
                    session["login"] = login
                    session['status'] = 'author'
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


@app.route('/write_an_article',methods = ["POST","GET"])
def write_article():
    if request.method=="POST":
        if request.form.get('header') and request.form.get('article'):
            id_ = Authors.get_id(conn=my_connection.conn,login=session['login'])
            if Articles.insert_article(conn=my_connection.conn,author_id=id_,header=request.form.get("header"),article=request.form.get('article'))==0:
                return redirect(url_for("index"))
            else:
                return "Something went wrong"
        print(id_)
    return render_template("write_article.html")


@app.route('/logout',methods=['GET'])
def logout():
    session["logged_in"]= False
    return redirect(url_for("index"))


if __name__=="__main__":
    my_connection.create_table()
    app.run()