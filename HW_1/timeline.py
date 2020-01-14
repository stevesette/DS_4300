from random import seed
from random import randint
import datetime as dt

from odbc_wrappers.MySQLConnector import MySQLConnector


def pick_db(mysql=True):
    if mysql:
        return MySQLConnector
    else:
        # TODO add redis connector
        return None


def timeline(db_conn, loops):
    with db_conn() as db:
        start = dt.datetime.now()
        for i in range(loops):
            user = randint(0, 2179)
            db.get_timeline(user)
        return (dt.datetime.now() - start) / loops


def main():
    seed(10)
    db_conn = pick_db()
    # try 50 loops
    print(timeline(db_conn, 50))


if __name__ == "__main__":
    main()
