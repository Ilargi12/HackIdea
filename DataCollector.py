from TopicGatherer import TopicGatherer
from ProjectGatherer import ProjectGatherer
from DescriptionAcquirer import DescriptionAcquirer
import pickle
import sys


class DataCollector:
    def __init__(self, topics, projects_per_topic):
        self.data = {}
        self.projects_per_topic = projects_per_topic
        self.topics = topics
        pass

    def collect_data(self):
        self.data.clear()

        topic_gatherer = TopicGatherer()
        topics = topic_gatherer.gather_topics()
        project_gatherer = ProjectGatherer()
        description_acquirer = DescriptionAcquirer()

        limit = self.topics
        for topic in topics:
            name = topic[0]
            self.data[name] = {}
            print(name)

            project_gatherer.set_url(topic[1])
            projects = project_gatherer.project_names_with_descriptions(limit=self.projects_per_topic)

            for project in projects:
                project_name = project[0]
                print('    ', project_name)
                description_acquirer.set_url(project[1])
                description = description_acquirer.acquire_description()
                self.data[name][project_name] = description

            limit -= 1
            if limit == 0:
                break

    def get_data(self):
        return self.data


if __name__ == '__main__':
    '''
    argv[1] = how many topics to include
    argv[2] = how many projects per topic to include
    in order to get as many as possible provide 0 0, or some big numbers
    '''
    topics = int(sys.argv[1])
    projects_per_topic = int(sys.argv[2])

    if topics == 0:
        topics = 1000
    if projects_per_topic == 0:
        projects_per_topic = 1000

    data_collector = DataCollector(topics, projects_per_topic)
    data_collector.collect_data()
    data = data_collector.get_data()

    with open('data.pickle', 'wb') as file:
        pickle.dump(data, file)
