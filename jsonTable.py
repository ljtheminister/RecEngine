import json
import cPickle as pickle

def read_json_byline(filename):
    data = []
    with open(filename) as f:
	for line in f:
	    data.append(json.loads(line))
    return data

def search_json(json_obj, search_field, search_value):
    if json_obj[search_field] == search_value:
	return json_obj
    else:
	return None

def search_json_table(json_table, search_field, search_value, return_value):
    for json_dict in json_table:
	result = search_json(json_dict, search_field, search_value)
	if result is not None:
	    return result[return_value]


def main():
filename = 'production.json'
table = read_json_byline(filename)
addQ = pickle.load(open('AddQ_mat_binary.p', 'rb'))
user_artist_keys = []
for song, user in addQ.keys():
    artist = search_json_table(table, 'pid', song, 'singers')
    user_artist_keys.append((user, artist))
pickle.dump(user_artist_keys, open('user_artist_key.p', 'wb'))


