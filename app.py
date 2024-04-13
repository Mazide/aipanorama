from flask import Flask, render_template, request, redirect, url_for

from repository import db, Article
from image_search import request_image
from chatgpt import request_article

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///var/data/site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True  # Включаем логирование SQL-запросов

    db.init_app(app)  # Инициализация SQLAlchemy с приложением Flask
    return app

app = create_app()

@app.route('/')
def home():
    print("home screen")
    return render_template('index.html')

@app.route('/article/<int:article_id>')
def article(article_id):
    # Загрузка статьи по ID
    print("load article")
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', article=article)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        image = request_image(title)
        article = request_article(title, image)
        
        print("article created")

        db.session.add(article)
        db.session.commit()

        print("article saved")
        
        # Перенаправляем на страницу с этой статьей
        return redirect(url_for('article', article_id=article.id))
    return redirect(url_for('home'))




if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создаем таблицы в базе данных
    app.run(debug=True)
