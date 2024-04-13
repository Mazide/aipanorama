from flask import Flask, render_template, request, redirect, url_for

from repository import db, Article
from chatgpt import request_article

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Инициализация SQLAlchemy с приложением Flask
    return app

app = create_app()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/article/<int:article_id>')
def article(article_id):
    # Загрузка статьи по ID
    article = Article.query.get_or_404(article_id)
    print(article.content)
    return render_template('article.html', article=article)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        article = request_article(title)
        # Перенаправляем на страницу с этой статьей
        return redirect(url_for('article', article_id=article.id))
    return redirect(url_for('home'))




if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создаем таблицы в базе данных
    app.run(debug=True)
