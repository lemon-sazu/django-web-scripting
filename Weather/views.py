from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def index(req):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Accept-Language": "en"
    }
    results = requests.get(
        'https://www.prothomalo.com/collection/latest', headers=headers)
    soup = BeautifulSoup(results.text, "lxml")
    news = soup.find_all(
        'div', class_='bn-story-card customStoryCard9-m__base__1rOCp')

    # heading = []
    sub_heading = []
    # for title in soup.find_all('h2', attrs={'class', 'headline'}):
    #     heading.append(title.text)

    for new in news:
        title = new.find('h2', class_='headline').text
        sub_title = new.find('h4').text
        link = new.find('a').get('href')
        time = new.find('time', class_='published-time').text

        # heading.append(title)
        sub_heading.append(
            {'title': title, 'sub': sub_title, 'link': link, 'time': time})

    return render(req, 'news/index.html', {'news': sub_heading})
