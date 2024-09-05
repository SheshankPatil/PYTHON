import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
        title="please drink water",
        message="drink water now",
        app_icon="/home/peace/Desktop/PYTHON/LEETCODE /icon.ico",
        timeout=2
    )
        time.sleep(6)
