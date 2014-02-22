import cPickle as pickle
import numpy as np
import pandas as pd

    
def load_pickled_file(filename):
    data = pickle.load(open(filename, 'rb'))
    return data


filename = 'AddQ_mat_binary.p'
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

mat = np.zeros((N,M))
mat = pd.DataFrame(mat)
mat.index = users
mat.columns = songs

for song, user in data.keys():
    mat.ix[user, song] = 1
mat.save('mat.pd')

