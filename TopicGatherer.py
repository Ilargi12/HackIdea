import requests
from bs4 import BeautifulSoup
import glo


class TopicGatherer:
    def __init__(self):
        pass

    def gather_topics(self):
        r = requests.get(glo.topics_url)
        r.encoding = 'utf-8'
        html_content = r.text
        soup = BeautifulSoup(html_content, 'lxml')

        all_topics = soup.find_all('li', class_='py-4 border-bottom')

        topic_urls = []
        topic_names = []

        for topic in all_topics:
            topic_names.append(topic.a['href'][8:])
            topic_urls.append(glo.github_url + topic.a['href'])

        topic_data = zip(topic_names, topic_urls)
        return topic_data
