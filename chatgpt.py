import random
from openai import OpenAI
from repository import Article, db

client = OpenAI(api_key='')


def request_article(title: str) -> Article:
    completion =  client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Создайте статью в стиле сатирического новостного сайта. Заголовок должен быть абсурдным и вызывать улыбку. Описание должно поддерживать исходную идею, раскрывая \"научные\" детали открытия и возможные последствия для общества"},
            {"role": "user", "content": title}
        ]
    )

    random_id = random.randint(1, 10000)

    content = completion.choices[0].message.content
    new_article = Article(id=random_id, title=title, subtitle="мдауж",  content=content, author="gpt-3.5-turbo", image_filename="")
    
    db.session.add(new_article)
    db.session.commit()

    return new_article
