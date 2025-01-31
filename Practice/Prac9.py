# import win32com.client as wincl

import win32com.client as win

# l = ["Nikul", "Pritesh", "Jay"]
#
# speaker = win.Dispatch("SAPI.SpVoice")
#
# for i in l:
#
#     speaker.speak(f"Hello {i}")


# speaker_number = 1
# spk = win.Dispatch("SAPI.SpVoice")
# vcs = spk.GetVoices()
# SVSFlag = 11
# print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
# spk.Voice
# spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
# for i in l:
#     spk.Speak(f"Hello {i}")


spk = win.Dispatch("SAPI.SpVoice")

l = ["Nikul", "Pritesh", "Jay"]

# for i in l:
#     spk.speak(f"Hello {i}")

for name in l:
    names = name.split()
    hello = f"Hello {names[0]}"
    spk.Speak(hello)

print("Hello to all")