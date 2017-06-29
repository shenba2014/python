import configparser
config = configparser.ConfigParser()
config.read("profiles.ini")
sections = config.sections()
print "sections in profiles.ini ", sections
for section in sections:
    print "items in section:" + section
    items = config.options(section)
    for item in items:
        print section  + ":" + item, "=", config.get(section, item) 
    print ""