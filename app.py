<<<<<<< HEAD
from flask import Flask, render_template, session ,request
from decouple import config
from database.connection import Connection
from database.models.users import Users
from database.models.authors import Authors
=======
from flask import Flask, render_template, session
from decouple import config
from database.connection import Connection
>>>>>>> 2774067a83b8e019cebe881f9c2bd2bc5f91a65a


app = Flask(__name__)

<<<<<<< HEAD
my_connection:Connection= Connection(
    host = 'localhost',
    port = 5432,
    user = 'postgres',
    password = 'admin',
    dbname = 'cs_forum'
)
=======
conn:Connection= Connection(
    host = config("DB_HOST",str),
    port = config("DB_PORT",int),
    username = config("DB_USERNAME",str),
    password = config("DB_PASSWORD",str),
    db_name = config("DB_NAME",str)
)
print(conn.create_table())
>>>>>>> 2774067a83b8e019cebe881f9c2bd2bc5f91a65a

@app.route("/",methods=["POST","GET"])
def index():
    return render_template("index.html")


<<<<<<< HEAD
@app.route("/login",methods=["POST","GET"])
def login():
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
                # return render_template("index.html")
            elif radio =="author":
                print(Authors.insert_author(conn=my_connection.conn,login=login,password=password))
                # return render_template("index.html")
            else:
                return "<h1>Something goes wrong,try again</h1>"
    return render_template("registrate.html")




if __name__=="__main__":
    my_connection.create_table()
=======
if __name__=="__main__":
>>>>>>> 2774067a83b8e019cebe881f9c2bd2bc5f91a65a
    app.run()