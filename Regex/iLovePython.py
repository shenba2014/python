import re
s = "I,love,python"
print re.findall("love", s)[0]

s = "aabbccddee"
print re.sub("dd", "ff", s)

strangeString = "ab2b3n5n2n67mm4n2"
print "number count", re.subn("\d", "*", strangeString)[1]
allChars = re.findall("[a-z]", strangeString)
charDict = {}
for char in allChars:
    if (charDict.__contains__(char)):
        charDict[char] = charDict[char] + 1
    else:
        charDict[char] = 1
print charDict
