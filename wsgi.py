from app import app as application
from repository import db


if __name__ == "__main__":
    application.run()
    with application.app_context():
        db.create_all()
