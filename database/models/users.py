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
                print("User", login, "successfully created")
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
                    print(result)
                    print("User successfully logged in")
                    return 0
                else:
                    print("Login error")
                    return 1
        except Exception as e:
            print("ERROR:",e)
            return 1