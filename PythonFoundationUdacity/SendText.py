from twilio import rest

account_sid = "ACbb02b1b770cd713e74cccd88b8bd70c7"
auth_token = "b54e282a6d11a55a1b1a70f28ca1657b"

client = rest.Client(account_sid, auth_token)
client.api.account.messages.create(
    to="+14076688387",
    from_="+13212047609",
    body="This is my test message!"
)