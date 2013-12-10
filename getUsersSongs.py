import os
import sys
import cPickle as pickle

from collections import defaultdict


def main(root_dir, user_file, song_file):

    users = defaultdict(int)
    songs = defaultdict(int)
    
    for root, dirs, files in os.walk(root_dir):
	for file_name in files:
	    file_path = root + '/' + file_name
	    print file_path
	    with open(file_path, 'rb') as f:
		for line in f:
		    uid, songid, _, _= line.split('\x01')
		    users[uid] = 0
		    songs[uid] = 0
			

    pickle.dump(users, open(user_file, 'wb'))
    pickle.dump(songs, open(song_file, 'wb'))


if __name__ == '__main__':
    root_dir, user_file, song_file = sys.argv[1], sys.argv[2], sys.argv[3]
    main(root_dir, user_file, song_file)
