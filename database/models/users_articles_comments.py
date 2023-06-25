from database.connection import Connection

class Users_Articles_Comments:
    conn:Connection
    user_id : int
    article_id : int
    comment : str

    @staticmethod
    def insert_article(
        conn:Connection,
        user_id : int,
        article_id : int,
        comment : str
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    INSERT INTO users_articles_comments(
                        user_id,
                        article_id,
                        comment
                    ) VALUES(
                        {user_id},
                        {article_id},
                        '{comment}'
                    )
                """)
                print("Comment successfully inserted")
                return 0
        except Exception as exc:
            print("ERROR COMMENT INSERTING:",exc)
            return 1
        
    @staticmethod
    def get_comments_by_article_id(
        conn:Connection,
        article_id:int
    ):
        try:
             with conn.cursor() as cur:
                cur.execute(f"""
                    SELECT users.login , users_articles_comments.article_id , users_articles_comments.comment FROM users_articles_comments
                    INNER JOIN users ON users.id = users_articles_comments.user_id
                    INNER JOIN articles ON articles.id = users_articles_comments.article_id
                    WHERE users_articles_comments.article_id = {article_id}
                """)
                res: list = cur.fetchall()
                return res
        except Exception as exc:
            print("ERROR COMMENTS FINDING:",exc)
            return []