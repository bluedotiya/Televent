from requests import get
from config import NEWEGG_LINK, TELEGRAM_SEND_MESSAGE_URL
import random
import time


while True:
    web_request = get(NEWEGG_LINK)
    if web_request.status_code != 200:
        get(TELEGRAM_SEND_MESSAGE_URL.format(f'NewEgg sent me Error {web_request.status_code} :('), stream=True)
    elif 'We have found 0 items that match.' in str(web_request.content):
        pass
    else:
        while True:
            get(TELEGRAM_SEND_MESSAGE_URL.format('BUYBUYBUY'), stream=True)
    interval_length = random.randrange(5, 10, 1)
    time.sleep(interval_length * 60)
