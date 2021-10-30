import capture

client = capture.Client()
client.login_token("< Your Token Here! >")
client.send_message("< TopicId Here >", message="< Your Text Message Here >")
