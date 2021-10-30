import capture

client = capture.Client()
client.login_token("< Your Token Here! >")
user = client.get_user_info("< UserID Here >")
print(user.name)
