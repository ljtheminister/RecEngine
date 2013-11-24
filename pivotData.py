import os
import sys
import pickle


from collections import defaultdict

data_dict = defaultdict(int)

rootdir = sys.argv[1]

for root, dirs, files in os.walk(rootdir):
    print root
    print dirs
    for file_name in files:
        file_path = root + '/' + file_name
        f = open(file_path, 'rb')

        for line in f:
            uid, songid, platform, count= line.split('\x01')
            data_dict[(uid,songid)] += int(count)

