import requests
import random

def request_image(query: str) -> str:
    access_key = "4c318a9ee328465ba9c5ecb6d039a779"  # Замените на ваш ключ доступа к API Bing
    endpoint = "https://api.bing.microsoft.com/v7.0/images/search"
    
    headers = {
        "Ocp-Apim-Subscription-Key": access_key
    }
    params = {
        "q": query,  # Поисковый запрос
        "count": 50,  # Количество изображений в ответе (максимум 150)
        "offset": 0,  # Сдвиг для пагинации результатов
        "imageType": "Photo"  # Фильтр для поиска только фотографий
    }
    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()
    print(data)

    if data['value']:  # Проверка на наличие изображений
        photo = random.choice(data['value'])  # Случайный выбор одного из изображений
        print(photo['contentUrl'])
        return photo['contentUrl']  # Возвращаем URL контента изображения
    else:
        return "No image found"
