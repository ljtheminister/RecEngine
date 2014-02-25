import cPickle as pickle
import numpy as np
import pandas as pd
from tempfile import mkdtemp
import os.path as path
import settings
import os
import subprocess

def load_pickled_file(filename):
    data = pickle.load(open(filename, 'rb'))
    return data

def pickle_file(ds, filename):
    pickle.dump(ds, open(filename, 'wb'))

def read_data():
    filename = './data/AddQ_mat_binary.p'
    data = load_pickled_file(filename)
    users = []
    songs = []
    with open('uids.txt', 'rb') as uids:
	for line in uids:
	    users.append(line.split()[0])
    with open('songids.txt', 'rb') as songids:
	for line in songids:
	    songs.append(line.split()[0])
    N = len(users)
    M = len(songs)
    return data, users, songs

def load_data():
    users = pd.read_table('uids.txt', header=None)
    songs = pd.read_table('songids.txt', header=None)
    users = pd.Series(users[0])
    songs = pd.Series(songs[0])
    return users, songs


def query_metadata(query):
    #artist = subprocess.check_output(query+" | tail -n +2, shell=True)
    artist = subprocess.Popen(query+" | tail -n +2", stdout=subprocess.PIPE, shell=True).communicate()[0] #for Python < 2.7
    return artist

def find_idx_Series(value, series):
    try:
	idx = series[series==value].index[0]
    except:
	idx = None
    return idx

def make_binary(mat):
    for key in mat.keys():
        mat[key] = 1
    return mat

def user_song_data():

# load/read data
#filename = './data/AddQ_mat_binary.p'
filename = 'AddQ_mat_binary.p'
data = load_pickled_file(filename)

# instantiate new data structures to be filled
artist_set = set()
user_artist = defaultdict(int)

# login details/settings
login = setings.login
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

song, user = data.keys()[0]
query = '%s"%s"'%(base_cmd, base_query%(table_name, song))
artist = query_metadata(query)




# aggregating data
for song, user in data.keys():
query = base_cmd + base_query%(table_name, song)
artist = query_metadata(query)
    if artist:
	user_artist[(user, artist)] = 1
	artist_set.update(artist)


#saving the data
artist_series = pd.Series(list(artist))
artist_series.to_pickle('artist_series.p')
#artist_series = pd.read_pickle('artist_series.p')
pickle.dump(user_artist, open('user_artist_dict.p', 'wb'))

user_artist_binary_dict = make_binary(user_artist)
pickle.dump(user_artist, open('user_artist_dict.p', 'wb'))


'''
users, songs = load_data()

N = len(users)
M = len(songs)

user_map = dict()
song_map = dict()

for idx in range(N):
    user_map[users.ix[idx]] = idx

for idx in range(M):
    song_map[songs.ix[idx]] = idx

pickle.dump(user_map, open('user_map', 'wb'))
pickle.dump(song_map, open('song_map', 'wb'))
user_map = pickle.load(open('user_map', 'rb'))
song_map = pickle.load(open('song_map', 'rb'))
'''

'''
user_map = load_pickled_file('user_map')
song_map = load_pickled_file('song_map')



mapname = path.join(mkdtemp(), 'binary.dat')
fp = np.memmap(mapname, dtype='float32', mode='w+', shape=(N,M))

for song, user in data.keys():
    song_idx = find_idx_Series(song, songs)
    user_idx = find_idx_Series(user, users) 
    if song_idx == None or user_idx == None:
	pass
    else:
	 fp[user_idx][song_idx] = 1
'''





'''
mat = np.zeros((N,M))
mat = pd.DataFrame(mat)
mat.index = users

mat.columns = songs

for song, user in data.keys():
    mat.ix[user, song] = 1
mat.save('mat.pd')
'''
