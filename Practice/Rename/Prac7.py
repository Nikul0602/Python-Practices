## RENAMING AND CHANGING EXTANTIONS OF FILE USING OS MODULE

import os

files = os.listdir()
i = 20
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"{file}", f"{i}.png")
    i = i + 1

