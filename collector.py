import methods
import settings
import time

token = settings.VK_TOKEN
user_id = str(settings.PAGE_TO_PARSE)
v = str(settings.V)


def timer():
    time.sleep(0.36)


data = {'id': user_id, 'request_time': int(time.time())}


a = methods.users_get(user_id, token, v)
data['main_profile'] = a

a = methods.docs_get(user_id, token, v)
data['documents'] = a

a = methods.photos_get_all(user_id, token, v)
data['photos'] = a

a = methods.notes_get(user_id, token, v)
data['notes'] = a

a = methods.videos_get(user_id, token, v)
data['videos'] = a

a = methods.friends_get(user_id, token, v)
data['friends'] = a

a = methods.gifts_get(user_id, token, v)
data['gifts'] = a

a = methods.stories_get(user_id, token, v)
data['stories'] = a

a = methods.groups_get(user_id, token, v)
data['groups'] = a

''' be careful with followers_get. don't use it if you don't want
to parse ALL FOLLOWERS '''
# a = methods.followers_get(verified_id, token, v)
# data['followers'] = a

''' be careful with messages_get. don't use it if you don't want
to parse OWN MESSAGES '''
# a = methods.messages_get(token, v)
# data['messages'] = a


with open('export' + str(user_id) + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))


print(data)
