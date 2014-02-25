import cPickle as pickle
'''
import numpy as np
import pandas as pd
from tempfile import mkdtemp
'''
import os.path as path
import settings
import os
import subprocess
from collections import defaultdict

def load_pickled_file(filename):
    data = pickle.load(open(filename, 'rb'))
    return data

def pickle_file(ds, filename):
    pickle.dump(ds, open(filename, 'wb'))

def query_metadata(query):
    #artist = subprocess.check_output(query+" | tail -n +2, shell=True)
    try:
	artist = subprocess.Popen(query+" | tail -n +2", stdout=subprocess.PIPE, shell=True).communicate()[0] #for Python < 2.7
	return artist
    except:
	return None

# load/read data
#filename = './data/AddQ_mat_binary.p'
filename = 'AddQ_mat_binary.p'
data = load_pickled_file(filename)

# instantiate new data structures to be filled
artist_set = set()
user_artist = defaultdict(int)

# login details/settings
login = settings.login
machine = settings.machine
login_pwd = settings.login_pwd
db_host = settings.host
db_user = settings.user
db_pwd = settings.pwd
db = settings.db

# just choose one of these table names
table_name = 'yin'
#table_name = 'yang'

# setup query
base_cmd = 'mysql -h %s -u %s -p%s %s -e '%(db_host, db_user, db_pwd, db)
base_query = "SELECT singers from %s where pid='%s'"

# aggregating data
for song, user in data.keys()[:10]:
    query = '%s"%s"'%(base_cmd, base_query%(table_name, song))
    artist = query_metadata(query)
    if artist:
        user_artist[(user, artist)] = 1
        artist_set.update(artist)
    print artist

'''
#saving the data
artist_series = pd.Series(list(artist))
artist_series.to_pickle('artist_series.p')
#artist_series = pd.read_pickle('artist_series.p')
'''
pickle_file(list(artist), 'artist_list.p')
pickle_file(user_artist, 'user_artist_dict.p')
