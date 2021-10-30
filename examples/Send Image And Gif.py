import capture

client = capture.Client()
client.login_token("< Your Token Here! >")

# Send image
with open("file.png", "rb") as f:
    client.send_message("< TopicId Here >", photo=f)

# Send gif
# gif provider name i think you can only send (tenor)
client.send_message("< TopicId Here >", gifId="< GifId Here >", gifProvider="tenor")

