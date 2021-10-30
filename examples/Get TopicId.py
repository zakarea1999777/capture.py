import capture

client = capture.Client()
client.login_token("< Your Token Here >")
topicId = client.get_topic_id("< Topic Url Here >")
print(topicId)
