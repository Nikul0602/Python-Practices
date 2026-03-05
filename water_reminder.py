import time
import signal
import sys
import winsound
from plyer import notification
from datetime import datetime

interval_minutes = 60

running = True


def shutdown_handler(signum, frame):
    global running
    print("\n🛑 Water Reminder is shutting down...")
    running = False
    sys.exit(0)


signal.signal(signal.SIGTERM, shutdown_handler)
signal.signal(signal.SIGINT, shutdown_handler)

print("💧 Water Reminder Started Successfully!")

while running:


    notification.notify(
        title="Hydration Reminder 💧",
        message=f"It's {datetime.now().strftime('%H:%M')} - Drink water!",
        timeout=10
    )
    # Play Windows default notification sound
    winsound.PlaySound("SystemNotification", winsound.SND_ALIAS)

    print(f"Reminder sent at {datetime.now().strftime('%H:%M:%S')}")

    time.sleep(interval_minutes * 60)