from flask import Flask, render_template, session
from decouple import config
from database.connection import Connection


app = Flask(__name__)

conn:Connection= Connection(
    host = config("DB_HOST",str),
    port = config("DB_PORT",int),
    username = config("DB_USERNAME",str),
    password = config("DB_PASSWORD",str),
    db_name = config("DB_NAME",str)
)
print(conn.create_table())

@app.route("/",methods=["POST","GET"])
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.run()