from database.connection import Connection

class Users_Articles_Rating:
    user_id:int
    article_id : int
    rating : int

    @staticmethod
    def insert_rating(
        conn:Connection,
        user_id : int,
        article_id : int,
        rating : int
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    INSERT INTO users_articles_rating(
                        user_id,
                        article_id,
                        rating
                    ) VALUES(
                        {user_id},
                        {article_id},
                        {rating}
                    )
                """)
                print("Rating successfully iserted")
                return 0
        except Exception as exc:
            print("ERROR RATING INSERTING:",exc)
            return 1