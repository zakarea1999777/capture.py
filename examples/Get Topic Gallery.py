import capture

client = capture.Client()
client.login_token("< Your Token Here! >")
photos = client.get_topic_photos("< TopicId Here >")

for photo, photoId in zip(photos.photo, photos.photoId):
    print(photo)
