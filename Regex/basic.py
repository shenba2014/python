import re
s = "hello world"
print 'findall demo'
print 'only findall',re.findall(r"^hello", s)
print 'findall and ignore case', re.findall(r"HELLO", s, re.IGNORECASE)
print 'find all words', re.findall(r"\b\w+\b", s)
print 're.sub demo'
print 're.sub', re.sub("hello", "hi", s)
print 're.sub with range', re.sub("hello", "hi", s[-4:])
print 're.sub with ignorecase', re.sub("world", "China", s[-5:], re.IGNORECASE)
print 're.subn, should return replace times', re.subn("l", "L", s)[1]
tel1 = "(010)38779983"
tel2 = "010-38779983"
print 'match phone number', re.findall(r"[\(]?\d{3}[\)]?\d{8}|\d{3}-?\d{8}", tel1)
print 'match phone number', re.findall(r"[\(]?\d{3}[\)]?\d{8}|\d{3}-?\d{8}", tel2)
