from TopicGatherer import TopicGatherer
from ProjectGatherer import ProjectGatherer
from DescriptionAcquirer import DescriptionAcquirer
import pickle
import os
import sys
import glo


class DataCollector:
    def __init__(self, first, last):
        self.data = {}
        self.first = first
        self.last = last
        pass

    def collect_store_data(self, topics):
        self.data.clear()

        project_gatherer = ProjectGatherer()
        description_acquirer = DescriptionAcquirer()

        for i in range(self.first, self.last + 1):
            topic = topics[i]
            name = topic[0]
            self.data[name] = {}

            project_gatherer.set_url(topic[1])
            projects = project_gatherer.project_names_with_descriptions()

            for project in projects:
                project_name = project[0]
                description_acquirer.set_url(project[1])
                description = description_acquirer.acquire_description()
                print('    ', project[0], '...descripted')
                self.data[name][project_name] = description

            with open(os.path.join(glo.pickles_path, (name + '.pickle')), 'wb') as file:
                pickle.dump(self.data[name], file)

            print(name, '...pickled')

    def get_data(self):
        return self.data


if __name__ == '__main__':
    '''
    argv[1] = first topic index
    argv[2] = last topic index
    '''
    first = int(sys.argv[1])
    last = int(sys.argv[2])

    topic_gatherer = TopicGatherer()
    topics = topic_gatherer.gather_topics()

    data_collector = DataCollector(first, last)
    data_collector.collect_store_data(topics)
