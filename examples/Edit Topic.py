import capture

client = capture.Client()
client.login_token("< Your Token Here! >")
client.edit_topic(
    "< TopicId Here >",
    bio="< Topic Bio Here >",
    name="< Topic Name Here >",
    categoryId=1,  # What is your topic about?
    mute=False,  # Mute the topic noti?
    sound=False  # Off the topic noti sound?
)
