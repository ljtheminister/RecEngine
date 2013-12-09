import os
import sys
import cPickle as pickle

from collections import defaultdict


def main(root_dir, dict_file):

    data_dict = defaultdict(int)

    for root, dirs, files in os.walk(root_dir):
	for file_name in files:
	    file_path = root + '/' + file_name
	    print file_path
	    with open(file_path, 'rb') as f:
		for line in f:
		    uid, songid, platform, count= line.split('\x01')
		    data_dict[(uid,songid)] += int(count)

    pickle.dump(data_dict, open(dict_file, 'wb'))


if __name__ == '__main__':
    root_dir, dict_file = sys.argv[1], sys.argv[2]
    main(root_dir, dict_file)
