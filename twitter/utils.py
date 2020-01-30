from odbc_wrappers.MySQLConnector import MySQLConnector
from odbc_wrappers.RedisConnector1 import RedisConnector1
from odbc_wrappers.RedisConnector2 import RedisConnector2


def pick_db(db_strategy):
    if db_strategy == 0:
        return MySQLConnector
    elif db_strategy == 1:
        return RedisConnector1
    elif db_strategy == 2:
        return RedisConnector2
    else:
        raise RuntimeError("Only acceptable options for pick_db are 0, 1, or 2")
