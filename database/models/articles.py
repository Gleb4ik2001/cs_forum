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

    @staticmethod
    def get_all_articles(conn:Connection):
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT articles.header, articles.article , authors.login FROM articles
                    INNER JOIN authors ON authors.id = articles.author_id;
                """)
                res :list= cur.fetchall()
                return res
        except Exception as exc:
            print("ERROR:",exc)
            return 1