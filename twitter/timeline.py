from random import seed
from random import randint
import datetime as dt

from utils import pick_db


def timeline(db_conn, loops):
    with db_conn() as db:
        start = dt.datetime.now()
        for i in range(loops):
            user = randint(0, 2179)
            db.get_timeline(user)
        return loops / (dt.datetime.now() - start).total_seconds()


def main():
    seed(10)
    db_conn = pick_db(0)
    # try 50 loops
    print(timeline(db_conn, 50))


if __name__ == "__main__":
    main()
