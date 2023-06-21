import psycopg2

class Connection:
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"instance"):
            cls.instance = super(Connection,cls).__new__(cls)
        return cls.instance
    
    def __init__(
        self,
<<<<<<< HEAD
        host : str,
        port : int,
        user :str,
        password : str,
        dbname : str
    ):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
=======
        host,
        port,
        username,
        password,
        db_name
    ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name
>>>>>>> 2774067a83b8e019cebe881f9c2bd2bc5f91a65a
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                host = self.host,
                port = self.port,
<<<<<<< HEAD
                user = self.user,
                password = self.password,
                dbname = self.dbname,
=======
                user = self.username,
                password = self.password,
                dbname = self.db_name
>>>>>>> 2774067a83b8e019cebe881f9c2bd2bc5f91a65a
            )
            self.conn.autocommit = True
            print('Database has been connecnted successfully')
        except Exception as e:
            print('ERROR:',e)
    
    def create_table(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users(
                        id SERIAL PRIMARY KEY,
                        login VARCHAR(32) NOT NULL,
                        password VARCHAR(32) NOT NULL
                    );
                    CREATE TABLE IF NOT EXISTS authors(
                        id SERIAL PRIMARY KEY,
                        login VARCHAR(32) NOT NULL,
                        password VARCHAR(32) NOT NULL
                    );
                    CREATE TABLE IF NOT EXISTS articles(
                        id SERIAL PRIMARY KEY,
                        author_id INTEGER REFERENCES authors(id),
                        header VARCHAR(100) NOT NULL,
                        article TEXT
                    );
                    CREATE TABLE IF NOT EXISTS authors_articles(
                        author_id INTEGER REFERENCES authors(id),
                        article_id INTEGER REFERENCES articles(id)
                    );
                    CREATE TABLE IF NOT EXISTS users_articles_rating(
                        user_id INTEGER REFERENCES users(id),
                        article_id INTEGER REFERENCES articles(id),
                        rating INTEGER CHECK(rating >=0 AND rating<=10)
                    );
                    CREATE TABLE IF NOT EXISTS users_articles_comments(
                        user_id INTEGER REFERENCES users(id),
                        article_id INTEGER REFERENCES articles(id),
                        comment VARCHAR(100) NOT NULL
                    );
                """)
                print('All tables successfully created') 
        except Exception as e:
            print("ERROR:",e)
<<<<<<< HEAD
=======

# conn=Connection(
#     host= 'localhost',
#     port = 5432,
#     username = 'postgres',
#     db_name = 'cs_forum',
#     password='admin'
# )
# print(conn.create_table())
>>>>>>> 2774067a83b8e019cebe881f9c2bd2bc5f91a65a
