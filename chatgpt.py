import os
import random
from openai import OpenAI
from repository import Article, db

client = OpenAI()



def request_article(title: str, image: str) -> Article:
    completion =  client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Создайте статью в стиле сатирического новостного сайта. Статья должна быть быть абсурдной и вызывать улыбку. Описание должно поддерживать исходную идею, раскрывая \"научные\" детали открытия и возможные последствия для общества. ОЧЕНЬ ВАЖНО ЧТОБЫ БЫЛО СМЕШНО, ИНАЧЕ БАБУЛЯ УМРЕТ"},
            {"role": "user", "content": title}
        ]
    )

    random_id = random.randint(1, 10000)

    content = completion.choices[0].message.content
    new_article = Article(id=random_id, title=title, subtitle="мдауж",  content=content, author="gpt-3.5-turbo", image_filename=image)
    
    db.session.add(new_article)
    db.session.commit()

    return new_article
