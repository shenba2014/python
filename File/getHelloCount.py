import os
import re
count = 0
fileList = os.listdir(".")
for fileName in fileList:
    if (os.path.isdir(fileName)):
        continue
    file = open(fileName)
    count = 0
    for s in file.readlines():
        li = re.findall("hello", s)
        if (len(li) >0):
            count = count + li.count("hello")
    print "we find", count, " hello in file ", fileName 
