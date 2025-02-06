# from plyer import notification
# import time
#
# if __name__ == "__main__":
#     while True:
#         notification.notify(title = "It's been 5 minutes drink water", app_name = "Drinking Reminder",
#                             message = "Drink water", timeout = 5)
#         time.sleep(2)
#         break



# from winotify import Notification, audio
# import time
#
# while True:
#     toast = Notification(app_id  = "Water Drinking Reminder",
#                          title = "Message", msg = "Drink Water",
#                          duration="short")
#     toast.set_audio(audio.LoopingAlarm, loop = False)
#
#     toast.show()
#     time.sleep(3600)

import os

command = 'powershell -command "Add-Type –TypeDefinition \'using System; using System.Windows.Forms;\' -Language CSharp; [System.Windows.Forms.MessageBox]::Show(\'Drink Water\', \'Reminder\')"'
os.system(command)

os.system('powershell -command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Drink Water\');"')
