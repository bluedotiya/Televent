import os
import time
from pathlib import Path
from requests import get
from config import PATH, TELEGRAM_SEND_MESSAGE_URL


def sleep(sec):
    time.sleep(sec)


def main():
    old_content = os.listdir(PATH).__len__()
    while True:
        content = os.listdir(PATH)
        if content.__len__() > old_content:
            paths = sorted(Path(PATH).iterdir(), key=os.path.getctime, reverse=True)
            new_file_name = paths[0].name
            print(new_file_name)
            old_content = content.__len__()
            get(TELEGRAM_SEND_MESSAGE_URL.format(f'{new_file_name[:-4]} fell in the net!  :D'), stream=True)
            sleep(15)
        elif content.__len__() < old_content:
            old_content -= 1
        else:
            sleep(15)


if __name__ == "__main__":
    main()
