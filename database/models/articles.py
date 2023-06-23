from database.connection import Connection

class Articles:
    id: int
    author_id: int
    header:str
    article:str

    @staticmethod
    def insert_article(
        conn:Connection,
        author_id:int,
        header:str,
        article:str
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                    INSERT INTO articles(
                        author_id,
                        header,
                        article
                    ) VALUES(
                        {author_id},
                        '{header}',
                        '{article}'
                    )
                """)
                print('Article successfully inserted')
                return 0 
        except Exception as exc:
            print("ERRORrrr:",exc)
            return 1
