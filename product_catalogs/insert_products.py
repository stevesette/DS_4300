from utils import pick_db
import os
import json


def insert_files(db_conn, document_path):
    with db_conn() as db:
        for doc in os.listdir(document_path):
            with open(f"{document_path}/{doc}", 'r') as f:
                db.insert_file(filename=doc, filedata=json.load(f))


def main():
    db = pick_db(0)
    insert_files(db, os.getcwd() + '/Collections/')


if __name__ == '__main__':
    main()
