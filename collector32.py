import methods
import settings
import time

token = settings.VK_TOKEN
user_id = str(settings.PAGE_TO_PARSE)
v = str(settings.V)


def timer():
    time.sleep(0.36)


a = methods.users_get(user_id, token, v)
data = {'id': user_id, 'request_time': int(time.time()), 'main_profile': a}
with open('profile' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

a = methods.docs_get(user_id, token, v)
data = {'id': user_id, 'request_time': int(time.time()), 'documents': a}
with open('documents' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

a = methods.photos_get_all(user_id, token, v)
data = {'id': user_id, 'request_time': int(time.time()), 'photos': a}
with open('photos' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

a = methods.notes_get(user_id, token, v)
data = {'id': user_id, 'request_time': int(time.time()), 'notes': a}
with open('notes' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

a = methods.videos_get(user_id, token, v)
data = {'id': user_id, 'request_time': int(time.time()), 'videos': a}
with open('videos' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

a = methods.friends_get(user_id, token, v)
data = {'id': user_id, 'request_time': int(time.time()), 'friends': a}
with open('friends' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

a = methods.gifts_get(user_id, token, v)
data = {'id': user_id, 'request_time': int(time.time()), 'gifts': a}
with open('gifts' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

a = methods.stories_get(user_id, token, v)
data = {'id': user_id, 'request_time': int(time.time()), 'stories': a}
with open('stories' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

a = methods.groups_get(user_id, token, v)
data = {'id': user_id, 'request_time': int(time.time()), 'groups': a}
with open('groups' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))

''' be careful with followers_get. don't use it if you don't want
to parse ALL FOLLOWERS '''
# a = methods.followers_get(user_id, token, v)
# data = {'id': user_id, 'request_time': int(time.time()), 'followers': a}
# with open('followers' + user_id + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
#     file.write(str(data))

''' be careful with messages_get. don't use it if you don't want
to parse OWN MESSAGES '''
# a = methods.messages_get(token, v)
# data = {'id': user_id, 'request_time': int(time.time()), 'groups': a}
# with open('ownMessages_' + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
#     file.write(str(data))


print(data)
