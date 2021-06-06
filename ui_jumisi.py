from fastapi import FastAPI

app = FastAPI()
import random


@app.get("/")
def home():
    return "Negizgi bet"


@app.get("/today")
def today():
    return "Bugingi kun - ertengi kunnin bastamasi"


@app.get("/quotes")
def sozder():
    quotes = ['Стремитесь не к успеху, а к ценностям, которые он дает. Альберт Эйнштейн',
              'Сложнее всего начать действовать, все остальное зависит только от упорства. Амелия Эрхарт',
              'Логика может привести Вас от пункта А к пункту Б, а воображение — куда угодно. Альберт Эйнштейн',
              '80% успеха - это появиться в нужном месте в нужное время. Вуди Аллен',
              'Наука — это организованные знания, мудрость — это организованная жизнь. Иммануил Кант',
              'Свобода ничего не стоит, если она не включает в себя свободу ошибаться. Махатма Ганди'
    ]
    result = random.choice(quotes)
    print(result)
    return result

sozder()
