import requests
import schedule
import time

def send_message():
    resp = requests.post(
        'https://textbelt.com/text', {
            'phone': '<Input your number with your country code>',
            'message': 'Hello Jacob this is just an automated text message',
            'key': 'textbelt',
        }
    )
    print(resp.json())

schedule.every(30).seconds().do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)