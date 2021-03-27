import requests
from bs4 import BeautifulSoup


class DescriptionAcquirer:
    def __init__(self, url=''):
        self.url = url

    def set_url(self, url):
        self.url = url

    def acquire_description(self):
        r = requests.get(self.url)
        html_content = r.text
        soup = BeautifulSoup(html_content, 'lxml')

        readme = soup.find('div', id='readme')
        div = readme.find('div', class_='Box-body px-5 pb-5')
        art = div.find('article', class_='markdown-body entry-content container-lg')
        ps = art.find_all('p')

        description = ''

        for p in ps:
            if not p.a:
                description = description + ' ' + p.text

        return description
