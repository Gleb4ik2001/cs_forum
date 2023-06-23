from database.connection import Connection

class Authors:
    id: int
    login: str
    password:str

    @staticmethod
    def login_author(
        conn:Connection,
        login:str,
        password:str
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    SELECT * FROM authors WHERE login ='{login}' AND password = '{password}'
                ;""")
                result = cur.fetchall()
                if len(result)>0:
                    print("User successfully logged in")
                    return 0
                else:
                    print("This user does not exists")
                    return 1
        except Exception as e:
            print("ERROR:",e)
            return 1


    @staticmethod
    def insert_author(
        conn:Connection,
        login:str,
        password:str
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    SELECT * FROM authors WHERE login = '{login}'
                """)
                result = cur.fetchall()
                if len(result)==0:
                    try:
                        cur.execute(f"""
                            INSERT INTO authors(
                                login,
                                password
                            ) VALUES(
                                '{login}',
                                '{password}'
                            )
                        """)
                        print("Author successfully created")
                        return 0
                    except Exception as e:
                        print("ERROR:",e)
                        return 1
                else:
                    print("Author already exists")
                    return 1
        except Exception as e:
            print("ERROR:",e)
            return 1
        
    @staticmethod
    def get_id(
        conn:Connection,
        login:str
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    SELECT id FROM authors WHERE login = '{login}'
                """)
                res = (cur.fetchall())
                print("Success")
                print(res)
                return int(res[0][0])
        except Exception as exc:
            print("ERROR:",exc)
            
