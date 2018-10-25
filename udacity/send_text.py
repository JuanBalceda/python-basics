# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACec5fc1210ba3ae3fc47bc8398755ecbf'
auth_token = '91770268a10335669eb4bca122a249a1'
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="Join Earth's mightiest heroes. Like Juan Balceda.",
                     from_='+34931071750',
                     to='+34663853066')

print(message.sid)