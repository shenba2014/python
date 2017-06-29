#encoding=utf-8
content = "hello world测试22"
file = open("hello.txt", 'a')
file.writelines(content)
file.writelines("\n")
file.close()