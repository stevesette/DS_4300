from utils import pick_db


def main():
    db = pick_db(0)
    run_queries(db)


def run_queries(db):
    collection = 'Watches'
    query = {'dialcolor': 'beige', 'brand': 'Tommy Hilfiger', 'diameter': 44, 'is_available': 1}
    db.run_query(collection, query)


if __name__ == '__main__':
    main()
