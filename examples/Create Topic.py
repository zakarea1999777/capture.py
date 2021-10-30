import capture

client = capture.Client()
client.login_token("< Your Token Here! >")
client.create_topic(
    bio="< Topic Bio Here >",
    name="< Topic Name here >",
    isChannel=False,  # is the topic a channel?
    isPrivate=False  # is it private?
)
