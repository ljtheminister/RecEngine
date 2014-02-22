import os
import sys
import cPickle as pickle

from collections import defaultdict

mat = defaultdict(int)

def aggregate_data(root_dir, start_date=None, end_date=None, event=None):
    for root, dirs, files in os.walk(root_dir):
	dirs = dirs_date_range(dirs, start_date, end_date)	
	for file_name in files:
	    file_path = root + '/' + file_name
	    print file_path
	    with open(file_path, 'rb') as f:
		for line in f:
		    songid, uid, _, _ = line.split('\x01')
			mat[(songid, uid)] += 1

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

def dirs_events(dirs, event):
    if event is None:
	return dirs


def main():


for root, dirs, files in os.walk('./'):
    print 'root: ', root
    print 'dirs: ', dirs
    print 'files: ', files
    dirs = [d for d in dirs if d > '.git']

