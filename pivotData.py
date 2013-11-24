import os
import sys
import pickle


from collections import defaultdict

data_dict = defaultdict(int)

rootdir = sys.argv[1]

for root, subFolders, files in os.walk(rootdir):
    for folder in subFolders:
	print str(folder)
	'''
	for f in files:
	    print str(f)
	'''
