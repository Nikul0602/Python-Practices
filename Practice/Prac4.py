#CREATING A ENCODER AND DECODER USING STRING AND RANDOM MODULE

import random
import string


st = input("Enter your message: ")
words = st.split(" ")
encode = input("1 for encode and 0 for decode: ")
encode = True if (encode == "1") else False
if encode :
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            r2 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            stn = r1 + word[1:] + word[0] + r2
            nwords.append(stn)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            stn =word[3:-3]
            stn = stn[-1] + stn[:-1]
            nwords.append(stn)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))