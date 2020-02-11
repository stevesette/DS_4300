from utils import pick_db
import os


def insert_documents(db, document_path):
    for doc in os.listdir(document_path):
        print(doc)
        # db.insert_document(doc)


def main():
    db = pick_db(0)
    insert_documents(db, os.getcwd() + '/Collections/')


if __name__ == '__main__':
    main()
