import capture

client = capture.Client()
client.login_token("< Your Token Here! >")
users = client.search_mention_users("< Text You Want To Search Here >")

for userName, userId in zip(users.username, users.userId):
    print(userName)
