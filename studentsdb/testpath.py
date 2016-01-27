import os
dirname = os.path.dirname(os.path.dirname(__file__))
realpath = os.path.dirname(os.path.realpath(__file__))
abspath = os.path.dirname(os.path.abspath(__file__))
mypath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print dirname
print realpath
print abspath
print mypath
