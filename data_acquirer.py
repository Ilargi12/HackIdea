from TopicGatherer import TopicGatherer


if __name__ == '__main__':
    topic_gatherer = TopicGatherer()
    topics = topic_gatherer.gather_topics()
    for x in topics:
        print(x)
