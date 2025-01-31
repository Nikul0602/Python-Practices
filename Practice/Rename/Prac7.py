## RENAMING AND CHANGING EXTANTIONS OF FILE USING OS MODULE

import os

files = os.listdir()
i = 1
for file in files:
    if file.endswith(".pdf"):
        print(file)
        os.rename(f"{file}", f"{i}.png")
    i += 1

