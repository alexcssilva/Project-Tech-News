from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    titles = list()
    search_title = search_news({"title": {"$regex": title, "$options": "i"}})

    for _title in search_title:
        titles.append((_title["title"], _title["url"]))
    return titles


# Requisito 7
def search_by_date(date):
    try:
        data = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        scrapes = search_news({"timestamp": {"$regex": data, "$options": "i"}})

        return [(article["title"], article["url"]) for article in scrapes]

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    scrapes = search_news(
        {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
    )

    return [(article["title"], article["url"]) for article in scrapes]


# Requisito 9
def search_by_category(category):
    scrapes = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )

    return [(article["title"], article["url"]) for article in scrapes]
