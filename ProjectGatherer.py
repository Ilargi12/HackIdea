import requests
from bs4 import BeautifulSoup
import glo


class ProjectGatherer:
    def __init__(self, url=''):
        self.url = url

    def set_url(self, url):
        self.url = url

    def project_names_with_descriptions(self):
        r = requests.get(self.url)
        html_content = r.text
        soup = BeautifulSoup(html_content, 'lxml')

        try:
            div = soup.find('div', class_='topic p-responsive container-xl')
            if not div:
                div = soup.find('div', class_='topic p-responsive container-lg')
            articles = div.find_all('article')

            project_names = []
            project_urls = []

            for article in articles:
                div_low = article.find('div', class_='px-3')
                if div_low:
                    div_low_low = div_low.find('div', class_='d-flex flex-auto')
                    a = div_low_low.find('a', class_='text-bold')
                    path_list = a['href'].split('/')
                    project_names.append(path_list[-1])
                    project_urls.append(glo.github_url + a['href'])
        except:
            return []

        project_data = list(zip(project_names, project_urls))
        return project_data
