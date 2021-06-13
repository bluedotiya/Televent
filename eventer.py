from requests import get
from config import TELEGRAM_SEND_MESSAGE_URL


def condition():
    return True


def message():
    return "True"


def main():
    if condition():
        get(TELEGRAM_SEND_MESSAGE_URL.format(message()), stream=True)


if __name__ == "__main__":
    main()
