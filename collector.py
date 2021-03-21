import methods
import settings
import time

token = settings.VK_TOKEN
user_id = str(settings.PAGE_TO_PARSE)
v = str(settings.V)


def timer():
    time.sleep(0.36)


data = {'id': user_id, 'request_time': int(time.time())}


data['main_profile'] = methods.users_get(user_id, token, v)

data['documents'] = methods.docs_get(user_id, token, v)

data['photos'] = methods.photos_get_all(user_id, token, v)

data['notes'] = methods.notes_get(user_id, token, v)

data['videos'] = methods.videos_get(user_id, token, v)

data['friends'] = methods.friends_get(user_id, token, v)

data['gifts'] = methods.gifts_get(user_id, token, v)

data['stories'] = methods.stories_get(user_id, token, v)

data['groups'] = methods.groups_get(user_id, token, v)

''' be careful with followers_get. don't use it if you don't want
to parse ALL FOLLOWERS '''
# data['followers'] = methods.followers_get(verified_id, token, v)

''' be careful with messages_get. don't use it if you don't want
to parse OWN MESSAGES '''
# data['messages'] = methods.messages_get(token, v)


with open('export' + str(user_id) + "_" + str(int(time.time())) + ".json", mode='w', encoding='utf-8') as file:
    file.write(str(data))


print(data)
