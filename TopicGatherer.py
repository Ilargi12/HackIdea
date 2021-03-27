import requests
from bs4 import BeautifulSoup
import glo


class TopicGatherer:
    def __init__(self):
        pass

    def gather_topics(self):
        topic_urls = []
        topic_names = []
        r = 1
        page = 1

        while r:
            r = requests.get(glo.topics_url, params={'page': page})
            page += 1
            r.encoding = 'utf-8'
            html_content = r.text
            soup = BeautifulSoup(html_content, 'lxml')
            if not soup:
                return

            all_topics = soup.find_all('li', class_='py-4 border-bottom')
            if len(all_topics) == 0:
                break

            for topic in all_topics:
                topic_names.append(topic.a['href'][8:])
                topic_urls.append(glo.github_url + topic.a['href'])

        topic_data = list(zip(topic_names, topic_urls))
        return topic_data


if __name__ == '__main__':
    gatherer = TopicGatherer()
    topics = gatherer.gather_topics()
    print('Number of topics:', len(topics))
    for topic in topics:
        print(topic[0], topic[1])
