from app import app as application
from repository import db


if __name__ == "__main__":
    application.run()
    print("create_all_tables")
    db.create_all()
