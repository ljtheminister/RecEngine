import os
import sys
import cPickle as pickle

from collections import defaultdict

'''
import os
root_dir = './'
for root, dirs, files in os.walk(root_dir):
    print 'root', root
    print 'dirs', dirs
    print 'files', files
'''

def aggregate_data1(root_dir, event, start_date=None, end_date=None):

    mat = defaultdict(int)

    for root, dirs, files in os.walk(root_dir):
	dirs = dirs_date_range(dirs, start_date, end_date)	
	for file_name in files:
	    file_path = root + '/' + file_name
	    print file_path
	    with open(file_path, 'rb') as f:
		for line in f:
		    songid, uid, _, _ = line.split('\x01')
		    mat[(songid, uid)] += 1
    return mat

def dirs_date_range(dirs, start_date=None, end_date=None):
    if start_date is None and end_date is None:
	pass
    elif start_date is None: #only start_date
	dirs = [dir for dir in dirs if dir[3:] <= end_date]	
    elif end_date is None: #only an end_date
	dirs = [dir for dir in dirs if dir[3:] >= start_date]	
    else: #both start_date and end_date
	dirs = [dir for dir in dirs if dir[3:] >= start_date and dir[3:] <= end_date]	
    return dirs

def aggregate_data(root_dir, events_filter, start_date=None, end_date=None):
    mat = defaultdict(int)
    dates = dirs_date_range(os.listdir(root_dir))
    for date in dates:
	date_path = root_dir + '/' + date
	events = os.listdir(date_path)
	events = set(events).intersection(set(events_filter))
	for event in events:
	    event_path = date_path + '/' + event
	    filenames = os.listdir(event_path)
	    for filename in filenames:
		file_path = event_path + '/' + filename
		print file_path
		with open(file_path, 'rb') as f:
		    for line in f:
			songid, uid, count = line.split('\x01')
			mat[(songid, uid)] += int(count)
    return mat    

def user_songids(mat):
    user_set = list()
    song_set = list()
    for key in mat.keys():
	user, songid = key
	user_set.append(user)
	song_set.append(songid)

    user_set = set(user_set)
    song_set = set(songid_set)
    return user_set, song_set

def make_binary(mat):
    for key in mat.keys():
	mat[key] = 1
    return mat




def main():
    root_dir = '../songid_uid_event_english'
    event = ['ev=sidebar%3Aadd%3Aqueue']
    mat = aggregate_data(root_dir, event)
    pickle.dump(mat, open('AddQ_mat.p', 'wb'))
