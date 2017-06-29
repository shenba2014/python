import os
file = open("test.html", 'a')
file.writelines("<a>a link</a>")
file.close()
files = os.listdir(".")
for filename in files:
    li = os.path.splitext(filename)
    if (li[1] == ".html"):
        newname = li[0] + ".htm"
        os.rename(filename, newname)

