import capture

client = capture.Client()
info = client.sign_up("< UserName Here >")
print(info.token)
