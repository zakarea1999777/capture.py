import capture

client = capture.Client()
client.login_token("< Your Token Here! >")
topics = client.get_topics()

for topicTitle, topicId in zip(topics.title, topics.topicId):
    print(topicTitle)
