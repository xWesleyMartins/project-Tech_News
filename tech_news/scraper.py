import time
import requests
import parsel


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
