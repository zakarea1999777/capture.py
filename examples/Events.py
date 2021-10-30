import capture

client = capture.Client()
client.login_token("< Your Token Here! >")


@client.event("on_ready")
def on_ready(data: capture.objects.Event):
    print("ready!")
    # ( Do something useful )


@client.event("on_ping")
def on_ping(data: capture.objects.Event):
    print("pong!")
    # ( Do something useful )


@client.event("on_message")
def on_message(data: capture.objects.Event):
    print("Message claimed!")
    # ( Do something useful )


@client.event("on_topic_user_join")
def on_join(data: capture.objects.Event):
    print("User topic joined!")
    # ( Do something useful )


@client.event("on_topic_user_leave")
def on_leave(data: capture.objects.Event):
    print("User topic leaved!")
    # ( Do something useful )


@client.event("on_message_delete")
def on_delete(data: capture.objects.Event):
    print("Message deleted!")
    # ( Do something useful )


@client.event("on_typing_status")
def on_typing(data: capture.objects.Event):
    print("User typing!")
    # ( Do something useful )


@client.event("on_message_edit")
def on_edit(data: capture.objects.Event):
    print("Message edited")
    # ( Do something useful )


client.launch()
