from time import sleep
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"User-agent": "Fake user-agent"}, timeout=3
        )
        sleep(1)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    result = []
    for quote in selector.css(".entry-title"):
        link = quote.css("a::attr(href)").get()
        result.append(link)
    return result


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css(".next ::attr(href)").get()
    if next_page is None:
        return None
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
