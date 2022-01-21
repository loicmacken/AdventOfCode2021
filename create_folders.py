import os

for i in range(1,26):
    path = 'day ' + str(i)
    if not os.path.exists(path):
        os.mkdir(path)