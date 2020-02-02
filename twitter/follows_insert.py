import csv

from utils import pick_db


def read_follows(filename):
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        return [x for x in reader]


def upload_all_follows(db_conn, following):
    with db_conn() as db:
        for follow in following:
            db.insert_following(follow)


def main():
    db_type = pick_db(1)
    following_data = read_follows("following.csv")
    upload_all_follows(db_type, following_data)


if __name__ == "__main__":
    main()
