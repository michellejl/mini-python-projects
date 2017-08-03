from twilio.rest import Client
import secrets

account_sid = secrets.account_sid
auth_token  = secrets.auth_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=secrets.my_number,
    from_=secrets.my_twilio_number,
    body="Hello from Python!")

print(message.sid)