print "%d %s" % (2, "c")

print "format by dictionary"
print("%(version)s: %(num).1f" % {"version": "1.2", "num": 2})

print "align"
word = "version3.0"
print word.center(30)
print word.center(30, "*")
