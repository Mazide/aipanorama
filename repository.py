from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Создаем экземпляр SQLAlchemy

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(150))
    author = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(100))

    def __repr__(self):
        return f"<Article {self.title}>"
