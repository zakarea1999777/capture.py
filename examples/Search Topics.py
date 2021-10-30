import capture

client = capture.Client()
client.login_token("< Your Token Here! >")
topics = client.search_topic("< Text You Want To Search Here >")

for topicTitle, topicId in zip(topics.title, topics.topicId):
    print(topicTitle)
