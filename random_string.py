
import os
import random
import string
from datetime import datetime

for files in range(10):
    def randomstring(stringLength=512):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))


    # print("Random string is", randomstring())
    now = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    print(now)
    f = open(os.getcwd() + "\\" + now + ".txt", 'w+')
    size = 100000000
    while os.path.getsize(os.getcwd() + "\\" + now + ".txt") < size:
        f.write(randomstring())
        # f.close()
