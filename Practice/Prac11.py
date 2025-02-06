from asyncio import timeout

from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(title = "It's been 5 minutes drink water", app_name = "Drinking Reminder",
                            message = "Drink water", timeout = 5)
        time.sleep(2)
        break