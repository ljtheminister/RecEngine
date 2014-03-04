import cPickle as pickle
import numpy as np
import pandas as pd
import os
import sklearn
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from tempfile import mkdtemp



def load_pickled_data(pickled_file):
    return pickle.load(open(pickled_file, 'rb'))

filename = 'user_artist_dict.p' 
data = load_pickled_data(filename)
users = pd.read_pickle('users_series.p')
artists = pd.read_pickle('artists_series.p')
user_map = pd.read_pickle('user_map')
artist_map = pd.read_pickle('artist_map')
#songs = pd.read_pickle('songs_series.p')

N = len(users)
M = len(artists) 

#mapname = os.path.join(mkdtemp(), 'user_artist.dat')
mapname = 'user_artist.dat'
fp = np.memmap(mapname, dtype='float32', mode='w+', shape=(N,M))

for user, artist in data.keys():
    try:
	user_idx = user_map[user]
	artist_idx = artist_map[artist]
	fp[user_idx, artist_idx] = data[user, artist]
    except:
	pass

fp.flush()

K_
k_means = KMeans(n_clusters=K, max_iter=500, n_jobs=-1
k_means_batch = MiniBatchKMeans(n_clusters=K, max_iter=500, n_jobs=-1


'''
class CollaborativeFiltering():


def get_artists():


def plot_histogram():
def main():
addQ = pickle.load(open('AddQ_mat_binary.p', 'rb'))


hist, bins = np.historgram(addQ_full.values(), bins=4)
center = (bins[:-1] + bins[1:])/2
plt.bar(center, hist, align='center')
plt.show()
    
songid_set = set()
uid_set = set()

for songid, uid in addQ.keys():
    songid_set.add(songid)
    uid_set.add(uid)    

pickle.dump(songid_set, open('songid_set.p', 'wb'))
pickle.dump(uid_set, open('uid_set.p', 'wb'))

songs = pd.Series(list(songid_set))
users = pd.Series(list(uid_set))
songs.to_pickle('songs_series.p')
users.to_pickle('users_series.p')

songid_list = list(songid_set)
uid_list = list(uid_set)


songlist_file = open('songids.txt', 'wb')
userlist_file = open('uids.txt', 'wb')
for songid in songid_list:
    songlist_file.write("%s\n" % songid)

for uid in uid_list:
    userlist_file.write("%s\n" % uid)

'''
