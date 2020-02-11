from utils import pick_db


def main():
    db = pick_db(0)

def run_queries(db):
    db.run_query()


if __name__ == '__main__':
    main()
