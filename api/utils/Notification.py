from vonage import Client , Sms
from ..Config import Config
from pprint import pprint
def notify():
    key = Config.VONAGE_KEY
    secret = Config.VONAGE_SECRET

    client = Client(key=key, secret=secret)
    sms = Sms(client)
    responseData = sms.send_message(
        {
            "to": "+919064846599",
            "text": "A text message sent using the Nexmo SMS API",
        }
    )
    pprint(responseData)
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")