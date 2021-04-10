import settings
import methods
import time
import os

token = settings.VK_TOKEN
v = str(settings.V)
user_id = str(methods.get_numeric_id(settings.PAGE_TO_PARSE, token, v))


def timer():
    time.sleep(0.36)


path = 'export' + str(user_id) + '_' + str(int(time.time()))
os.mkdir(path)


data = {'id': user_id, 'parsing_started': int(time.time()), 'main_profile': methods.users_get(user_id, token, v)}
data['parsing_finished'] = int(time.time())
with open(path + '/profile' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

data = {'id': user_id, 'parsing_started': int(time.time()), 'wall': methods.wall_get(user_id, token, v)}
data['parsing_finished'] = int(time.time())
with open(path + '/wall' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

data = {'id': user_id, 'parsing_started': int(time.time()), 'documents': methods.docs_get(user_id, token, v)}
data['parsing_finished'] = int(time.time())
with open(path + '/documents' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

data = {'id': user_id, 'parsing_started': int(time.time()), 'photos': methods.photos_get_all(user_id, token, v)}
data['parsing_finished'] = int(time.time())
with open(path + '/photos' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

data = {'id': user_id, 'parsing_started': int(time.time()), 'notes': methods.notes_get(user_id, token, v)}
data['parsing_finished'] = int(time.time())
with open(path + '/notes' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

data = {'id': user_id, 'parsing_started': int(time.time()), 'videos': methods.videos_get(user_id, token, v)}
data['parsing_finished'] = int(time.time())
with open(path + '/videos' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

data = {'id': user_id, 'parsing_started': int(time.time()), 'friends': methods.friends_get(user_id, token, v)}
data['parsing_finished'] = int(time.time())
with open(path + '/friends' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

data = {'id': user_id, 'parsing_started': int(time.time()), 'gifts': methods.gifts_get(user_id, token, v)}
data['parsing_finished'] = int(time.time())
with open(path + '/gifts' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

data = {'id': user_id, 'parsing_started': int(time.time()), 'stories': methods.stories_get(user_id, token, v)}
data['parsing_finished'] = int(time.time())
with open(path + '/stories' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

data = {'id': user_id, 'parsing_started': int(time.time()), 'groups': methods.groups_get(user_id, token, v)}
data['parsing_finished'] = int(time.time())
with open(path + '/groups' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

''' be careful with followers_get. don't use it if you don't want
to parse ALL FOLLOWERS '''
# data = {'id': user_id, 'parsing_started': int(time.time()), 'followers': methods.followers_get(user_id, token, v)}
# data['parsing_finished'] = int(time.time())
# with open(path + 'followers' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
#     file.write(str(data))

''' be careful with messages_get. don't use it if you don't want
to parse OWN MESSAGES '''
# data = {'id': user_id, 'parsing_started': int(time.time()), 'groups': methods.messages_get(token, v)}
# data['parsing_finished'] = int(time.time())
# with open(path + 'ownMessages_' + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
#     file.write(str(data))


print(data)
