import sys
print sys.modules.keys()
print()
print sys.modules.values()
print()
print sys.modules["os"]
d=sys.modules.copy()
import copy,string
print zip(set(sys.modules)-set(d))