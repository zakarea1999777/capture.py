import capture

client = capture.Client()
client.login_token("< Your Token Here! >")
gifs = client.get_trending_gif()

for gifTitle, gifId, gifUrl in zip(gifs.title, gifs.id, gifs.url):
    print(gifTitle)
