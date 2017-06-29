import os
def visitFiles(fileList, level):
    for fileName in fileList:
        print "%s{2}" % fileName
        if (os.path.isdir(fileName)):
            visitFiles(os.listdir(fileName), level + 1)

fileList = os.listdir(".")
visitFiles(fileList, 0)
