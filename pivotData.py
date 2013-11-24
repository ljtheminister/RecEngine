import os
import sys
import pickle

from collections import defaultdict


def main(root_dir):

data_dict = defaultdict(int)

for root, dirs, files in os.walk(root_dir):
    print root
    for file_name in files:
        file_path = root + '/' + file_name
        f = open(file_path, 'rb')

        for line in f:
            uid, songid, platform, count= line.split('\x01')
            data_dict[(uid,songid)] += int(count)

	pickle.dump(data_dict, open('data_dict.p', 'wb'))

pickle.dump(data_dict, open('data_dict.p', 'wb'))


if name == '__main__':
    root_dir = sys.argv[1]
    main(root_dir)
