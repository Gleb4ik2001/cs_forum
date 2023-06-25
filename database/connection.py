import psycopg2

class Connection:
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"instance"):
            cls.instance = super(Connection,cls).__new__(cls)
        return cls.instance
    
    def __init__(
        self,
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
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.password,
                dbname = self.dbname,
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
                        login VARCHAR(32) UNIQUE NOT NULL,
                        password VARCHAR(32) NOT NULL
                    );
                    CREATE TABLE IF NOT EXISTS authors(
                        id SERIAL PRIMARY KEY,
                        login VARCHAR(32) UNIQUE NOT NULL,
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
                        article_id INTEGER UNIQUE REFERENCES articles(id)
                    );
                    CREATE TABLE IF NOT EXISTS users_articles_rating(
                        user_id INTEGER REFERENCES users(id),
                        article_id INTEGER REFERENCES articles(id),
                        rating INTEGER CHECK(rating >=0 AND rating<=5)
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
