from requests import get
from config import TELEGRAM_SEND_MESSAGE_URL


def condition():
    message = ''
    with open('/var/tmp/stats_gpu_fan_jq') as fan_speed_handle:
       fan_speed = fan_speed_handle.readlines()[1]
    with open('/var/tmp/stats_gpu_temp_jq') as gpu_temp_handle:
        gpu_temp = gpu_temp_handle.readlines()[1]
    if int(gpu_temp) > 55:
        message += f"GPU is Overheating at: {gpu_temp}\t"
    if int(fan_speed) > 30:
        message += f"Fan speed is Under Performing at: {fan_speed}\t"
    if message.__len__() > 0:
        condition_sw = True
    else:
        condition_sw = False
    return message, condition_sw


def main():
    msg, condition_var = condition()
    if condition_var:
        get(TELEGRAM_SEND_MESSAGE_URL.format(msg), stream=True)


if __name__ == "__main__":
    main()
