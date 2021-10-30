import capture

client = capture.Client()
client.login_token("< Your Token Here! >")
client.edit_profile(
    photo=open("FileName", "rb"),
    username="< Profile UserName Here >",
    bio="< Profile Bio Here >",
    location="< Profile Location Here >",
    status=True,  # Are you online now?
)
