from flask import Flask, render_template, session, request, redirect, url_for , flash
from decouple import config
from database.connection import Connection
from database.models.users import Users
from database.models.authors import Authors
from database.models.articles import Articles
from database.models.users_articles_comments import Users_Articles_Comments
from database.models.users_articles_rating import Users_Articles_Rating

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
    if request.method == "POST":
        if request.form.get("comment_content") and request.form.get("article_id"):
            return redirect(url_for('submit_comment'))
        if request.form.get('rating'):
            return redirect(url_for('insert_rating'))
    if "logged_in" in session and session["logged_in"] and session['status']=="user":
        articles = Articles.get_all_articles(conn=my_connection.conn)
        ids = Articles.get_articles_id(conn=my_connection.conn)
        comments = {}
        for i in range(len(ids)):
            comments[ids[i][0]] = Users_Articles_Comments.get_comments_by_article_id(
                conn=my_connection.conn,
                article_id=ids[i][0]
            )
        return render_template("index.html", articles=articles, comments=comments)
    elif "logged_in" in session and session["logged_in"] and session['status']=="author":
        articles = Articles.get_all_articles(conn=my_connection.conn)
        return render_template('index_author.html', articles=articles)
    else:
        return redirect(url_for('login_func'))

@app.route('/submit_comment',methods=["POST"])
def submit_comment():
    comment  = request.form.get("comment_content")
    article_id = request.form.get("article_id")
    user_id= Users.get_user_id(conn=my_connection.conn,login=session['login'])[0]

    if Users_Articles_Comments.insert_article(
        conn=my_connection.conn,
        user_id= user_id,
        article_id=article_id,
        comment=comment
    ) == 0:
        return redirect(url_for("index"))
    else:
        return "<h1> Ошибка привязки коммента к статье</h1>"
    
    
@app.route('/insert_rating',methods=["POST"])
def insert_rating():
    rating :int = int(request.form.get("rating"))
    user_id :int= int(Users.get_user_id(conn=my_connection.conn,login=session['login'])[0])
    article_id :int = request.form.get('article_id')
    if Users_Articles_Rating.insert_rating(
        conn=my_connection.conn,
        user_id= user_id,
        article_id=article_id,
        rating=rating
    ) == 0:
        return redirect(url_for("index"))
    else:
        return "<h1> Ошибка привязки коммента к статье</h1>"


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

@app.route("/get_comments",methods=["GET"])
def get_comments():
    articles =Articles.get_all_articles(
            conn=my_connection.conn,
        )
    comments = Users_Articles_Comments.get_comments_by_article_id(
            conn=my_connection.conn,
            article_id=(request.form.get("article_id"))
        )
    return render_template("index.html",articles = articles,comments = comments)


@app.route('/logout',methods=['GET'])
def logout():
    session["logged_in"]= False
    return redirect(url_for("index"))


if __name__=="__main__":
    my_connection.create_table()
    app.run()