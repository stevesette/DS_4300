from odbc_wrappers.MongoConnector import MongoConnector


def pick_db(db_strategy):
    if db_strategy == 0:
        return MongoConnector
    else:
        raise RuntimeError("Only acceptable option for pick_db is 0")
