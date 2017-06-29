import os
def visitFiles(path):
    for root,dirs, files in os.walk(path):
        for filePath in files:
            print os.path.join(root, filePath)

if __name__ == "__main__":
    path = "."
    visitFiles(path)
