from database.connection import Connection

class Users:
    login :str
    password :str

    @staticmethod
    def registrate_user(
        conn:Connection,
        login : str,
        password : str
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    INSERT INTO users(
                        login,
                        password
                    ) VALUES(
                        '{login}',
                        '{password}'
                    );
                """)
                return 0
        except Exception as e:
            print("ERROR:",e)
            return 1

            
    @staticmethod
    def login_user(
        conn:Connection,
        login:str,
        password:str
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    SELECT * FROM users WHERE login = '{login}' AND password = '{password}';
                """)
                result = cur.fetchall()
                if len(result)>0:
                    print("User successfully logged in")
                    return 0
                else:
                    print("Login error")
                    return 1
        except Exception as e:
            print("ERROR:",e)
            return 1
    @staticmethod
    def get_user_id(
        conn:Connection,
        login:str
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    SELECT id FROM users WHERE login = '{login}'
                """)
                res:list = cur.fetchone()
                return res
        except Exception as exc:
            print("ERROR:",exc)
            return 1