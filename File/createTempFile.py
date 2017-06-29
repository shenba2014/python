import os
file = os.tmpfile()
file.writelines("some")
print file.name
print os.path.abspath("hello.txt")