import re
pattern = re.compile(r"[\(]?\d{3}[\)]?\d{8}|\d{3}-?\d{8}")
tel1 = "(010)38779983"
tel2 = "010-38779983"
print 'match phone number', pattern.findall(tel1)
print 'match phone number', pattern.findall(tel2)
print "try finditer", pattern.finditer(tel2)