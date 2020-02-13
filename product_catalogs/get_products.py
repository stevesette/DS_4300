from utils import pick_db


def main():
    db = pick_db(0)
    query_vals = run_queries(db)
    print(query_vals)


def run_queries(db_conn):
    with db_conn() as db:
        collection = 'Watches'
        query = {'dial_color': 'beige', 'brand': 'Tommy Hilfiger', 'diameter': 40, 'is_available': 1}
        return db.run_query(collection, query)


if __name__ == '__main__':
    main()
