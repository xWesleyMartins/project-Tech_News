from tech_news.database import search_news
from tech_news.database import get_collection
import datetime


# Requisito 7
def search_by_title(title):
    regex_query = {"title": {"$regex": title, "$options": "i"}}
    news_searching = search_news(regex_query)

    result = [(news["title"], news["url"]) for news in news_searching]
    return result


# Requisito 8
def search_by_date(date):
    try:
        dt = datetime.date.fromisoformat(date)
        date_str = dt.strftime("%d/%m/%Y")
        query = {"timestamp": date_str}
        projection = {"_id": False, "title": True, "url": True}
        result = get_collection().find(query, projection)
        return [(item["title"], item["url"]) for item in result]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
