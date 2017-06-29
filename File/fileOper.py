import re
file = open("test.txt", "r")
file2 = open("test2.txt", "a")
lines = file.readlines()
size = 0
for line in lines:
    for byte in line:
        size = size + len(byte)
    if ("\n" in line):
        print line[:len(line) - 1]
    else:
        print line
    file2.write(line.replace("2014", "euro2014"))

file.close()
file2.close()
print size,"bytes"
