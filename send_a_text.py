from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC868513fba3dcfe568595b98b3b67739e"
# Your Auth Token from twilio.com/console
auth_token  = "5c4b1f3f76f257a835ebbff35d668e9d"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14088594549", 
    from_="+18312221359",
    body="Hello from Shaunak!")

print(message.sid)