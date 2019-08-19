from twilio.rest import Client


def notify(code):
    # Dictionary of name/phone number pairs (redacted for obvious reasons)
    phone_numbers = {}

    # Account SID, authentication token, and Twilio phone number (also redacted)
    account_sid = ""
    auth_token = ""
    twilio_number = ""

    client = Client(account_sid, auth_token)
    for name in phone_numbers:
        message = client.messages \
                        .create(
                            body=code,
                            from_=twilio_number,
                            to=phone_numbers[name]
                        )
        print("Notified " + name + "!")
