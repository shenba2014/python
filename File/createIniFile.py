import configparser
config = configparser.ConfigParser()
config.add_section("my section")
config.set("my section", "count", "2")
file = open("demo.ini", 'a')
config.write(file)
file.close()