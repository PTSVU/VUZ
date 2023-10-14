import requests
from bs4 import BeautifulSoup
import re

url = "https://www.mirea.ru/schedule/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

results = soup.find("div", class_="schedule"). \
    find(string="Институт информационных технологий"). \
    find_parent("div"). \
    find_parent("div"). \
    findAll("a", class_="uk-link-toggle")  # получить ссылки
links = []

mirea_site = "https://www.mirea.ru"
mirea_page = requests.get(mirea_site)
soup3 = BeautifulSoup(mirea_page.text, "html.parser")
week_str = soup3.find("div", class_="bonus_cart-title").text
week_number = re.search("(\d+)-я неделя", week_str).group(1)
