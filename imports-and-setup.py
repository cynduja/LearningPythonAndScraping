import sys
print ("I am using python", sys.version)
dirname = 'data-hold/stuff'
print ("I am making a new local directory named", dirname)
import os
os.makedirs(dirname, exist_ok = True)