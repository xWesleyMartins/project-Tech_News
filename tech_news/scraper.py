import time
import requests
import parsel
import bs4
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}
    try:
        res = requests.get(url, headers=headers, timeout=3)
        res.raise_for_status()
        return res.text
    except (requests.exceptions.Timeout, requests.exceptions.HTTPError):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = parsel.Selector(text=html_content)
    return selector.css("h2 a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(text=html_content)
    next_page = selector.css("nav .next::attr(href)").get()
    return next_page if next_page else None


# Requisito 4
def scrape_news(html_content):
    soup = bs4.BeautifulSoup(html_content, "html.parser")

    url_element = soup.find("link", {"rel": "canonical"})
    url = url_element["href"] if url_element else None

    title_element = soup.find(class_="entry-title")
    title = title_element.text.rstrip() if title_element else None

    timestamp_element = soup.find(class_="meta-date")
    timestamp = timestamp_element.text[:10] if timestamp_element else None

    writer_element = soup.find(class_="author").find("a")
    writer = writer_element.text if writer_element else None

    reading_time_element = soup.find(class_="meta-reading-time")
    reading_time = (
        int(reading_time_element.text[:2]) if reading_time_element else None
    )

    summary_element = soup.find(class_="entry-content").find("p")
    summary = summary_element.text.rstrip() if summary_element else None

    category_element = soup.find(class_="category-style").find(class_="label")
    category = category_element.text if category_element else None

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    news_posted = []
    next_page_url = "https://blog.betrybe.com/"

    while len(news_posted) < amount and next_page_url:
        html_content = fetch(next_page_url)
        url_list = scrape_updates(html_content)
        next_page_url = scrape_next_page_link(html_content)

        for url in url_list:
            news_posted.append(scrape_news(fetch(url)))

            if len(news_posted) == amount:
                break

    create_news(news_posted)
    return news_posted[:amount]
