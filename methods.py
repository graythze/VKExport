import requests
import time


def timer():
    time.sleep(0.36)
    

def docs_get(id, token, v):
    offset = 0
    requests_all = []
    while True:
        request = requests.post("https://api.vk.com/method/docs.get", data={
            'count': 1999,
            'offset': offset,
            'owner_id': id,
            'return_tags': '1',
            'access_token': token,
            'v': v})
        print(request.json())
        if "response" in request.json():
            if len(request.json()["response"]["items"]) > 0:
                for k in request.json()["response"]["items"]:
                    print(str(k))
                    requests_all.append(k)
            timer()
        else:
            print('nothing to parse')
            timer()
            break
        offset += 1999
    return requests_all


def friends_get(id, token, v):
    offset = 0
    requests_all = []
    while True:
        request = requests.post("https://api.vk.com/method/friends.get", data={
            'user_id': id,
            'order': 'name',
            'count': '5000',
            'offset': offset,
            'fields': 'uid,first_name,last_name,deactivated,verified,sex,bdate,city,country,home_town,photo_50,'
                      'photo_100,photo_200_orig,photo_200,photo_400_orig,photo_max,photo_max_orig,online,lists,'
                      'domain,has_mobile,contacts,site,education,universities,schools,status,last_seen,'
                      'followers_count,counters,occupation,nickname,relatives,relation,personal,connections,exports,'
                      'wall_comments,activities,interests,music,movies,tv,books,games,about,quotes,can_post,'
                      'can_see_all_posts,can_see_audio,can_write_private_message,timezone,screen_name',
            'access_token': token,
            'v': v})
        print(request.json())
        if "response" in request.json():
            if len(request.json()["response"]["items"]) > 0:
                for k in request.json()["response"]["items"]:
                    print(str(k))
                    requests_all.append(k)
            else:
                break
            timer()
        else:
            print('nothing to parse')
            timer()
            break
        offset += 5000
    return requests_all


def gifts_get(id, token, v):
    offset = 0
    requests_all = []
    while True:
        request = requests.post("https://api.vk.com/method/gifts.get", data={
            'user_id': id,
            'count': 1000,
            'offset': offset,
            'access_token': token,
            'v': v})
        print(request.json())
        if "response" in request.json():
            if len(request.json()["response"]["items"]) > 0:
                for k in request.json()["response"]["items"]:
                    print(str(k))
                    requests_all.append(k)
            else:
                break
            timer()
        else:
            print('nothing to parse')
            timer()
            break
        offset += 100
    return requests_all


def notes_get(id, token, v):
    offset = 0
    requests_all = []
    while True:
        request = requests.post("https://api.vk.com/method/notes.get", data={
            'user_id': id,
            'offset': offset,
            'count': 100,
            'sort': 1,
            'access_token': token,
            'v': v})
        print(request.json())
        if "response" in request.json():
            if len(request.json()["response"]["items"]) > 0:
                for k in request.json()["response"]["items"]:
                    print(str(k))
                    requests_all.append(k)
            else:
                break
            timer()
        else:
            print('nothing to parse')
            timer()
            break
        offset += 100
    return requests_all


def photos_get_all(id, token, v):
    offset = 0
    requests_all = []
    while True:
        request = requests.post("https://api.vk.com/method/photos.getAll", data={
            'owner_id': id,
            'extended': 1,
            'offset': offset,
            'count': 200,
            'photo_sizes': 1,
            'no_service_albums': 0,
            'access_token': token,
            'v': v})
        print(request.json())
        if "response" in request.json():
            if len(request.json()["response"]["items"]) > 0:
                for k in request.json()["response"]["items"]:
                    print(str(k))
                    requests_all.append(k)
            else:
                break
            timer()
        else:
            print('nothing to parse')
            timer()
            break
        offset += 100
    return requests_all


def stories_get(id, token, v):
    request = requests.post("https://api.vk.com/method/stories.get", data={
        'owner_id': id,
        'extended': 1,
        'access_token': token,
        'v': v}).json()
    if "response" in request:
        timer()
        return request


def users_get(id, token, v):
    request = requests.post("https://api.vk.com/method/users.get", data={
        'user_ids': id,
        'fields': 'uid,first_name,last_name,deactivated,verified,sex,bdate,city,country,home_town,photo_50,photo_100,'
                  'photo_200_orig,photo_200,photo_400_orig,photo_max,photo_max_orig,online,lists,domain,has_mobile,'
                  'contacts,site,education,universities,schools,status,last_seen,followers_count,counters,occupation,'
                  'nickname,relatives,relation,personal,connections,exports,wall_comments,activities,interests,music,'
                  'movies,tv,books,games,about,quotes,can_post,can_see_all_posts,can_see_audio,'
                  'can_write_private_message,timezone,screen_name',
        'access_token': token,
        'v': v}).json()
    if "response" in request:
        timer()
        return request


def videos_get(id, token, v):
    offset = 0
    requests_all = []
    while True:
        request = requests.post("https://api.vk.com/method/video.get", data={
            'owner_id': id,
            'count': 200,
            'offset': offset,
            'extended': 1,
            'access_token': token,
            'v': v})
        print(request.json())
        if "response" in request.json():
            if len(request.json()["response"]["items"]) > 0:
                for k in request.json()["response"]["items"]:
                    print(str(k))
                    requests_all.append(k)
            else:
                break
            timer()
        else:
            print('nothing to parse')
            timer()
            break
        offset += 100
    return requests_all


def followers_get(id, token, v):
    offset = 0
    requests_all = []
    while True:
        request = requests.post("https://api.vk.com/method/users.getFollowers", data={
            'user_id': id,
            'offset': offset,
            'count': 1000,
            'fields': 'uid,first_name,last_name,deactivated,verified,sex,bdate,city,country,home_town,photo_50,'
                      'photo_100,photo_200_orig,photo_200,photo_400_orig,photo_max,photo_max_orig,online,lists,'
                      'domain,has_mobile,contacts,site,education,universities,schools,status,last_seen,'
                      'followers_count,counters,occupation,nickname,relatives,relation,personal,connections,exports,'
                      'wall_comments,activities,interests,music,movies,tv,books,games,about,quotes,can_post,'
                      'can_see_all_posts,can_see_audio,can_write_private_message,timezone,screen_name',
            'access_token': token,
            'v': v})
        print(request.json())
        if "response" in request.json():
            if len(request.json()["response"]["items"]) > 0:
                for k in request.json()["response"]["items"]:
                    print(str(k))
                    requests_all.append(k)
            else:
                break
            timer()
        else:
            print('nothing to parse')
            timer()
            break
        offset += 1000
    return requests_all


def groups_get(id, token, v):
    offset = 0
    requests_all = []
    while True:
        request = requests.post("https://api.vk.com/method/groups.get", data={
            'user_id': id,
            'extended': 1,
            'fields': 'id,name,screen_name,is_closed,deactivated,is_admin,admin_level,is_member,invited_by,type,'
                      'has_photo,photo_50,photo_100,photo_200,activity,age_limits,can_create_topic,can_message,'
                      'can_post,can_see_all_posts,can_upload_doc,can_upload_video,city,contacts,counters,country,'
                      'cover,description,fixed_post,main_album_id,main_section,market,members_count,place,'
                      'public_date_label,site,status,trending,verified,wiki_page',
            'offset': offset,
            'count': 100,
            'access_token': token,
            'v': v})
        print(request.json())
        if "response" in request.json():
            if len(request.json()["response"]["items"]) > 0:
                for k in request.json()["response"]["items"]:
                    print(str(k))
                    requests_all.append(k)
            else:
                break
            timer()
        else:
            print('nothing to parse')
            timer()
            break
        offset += 100
    return requests_all


def messages_get(token, v):
    count = 0
    ids = ''
    requests_all = []
    while True:
        for k in range(0 + count, 100 + count):
            ids += str(k) + ','
        request = requests.post("https://api.vk.com/method/messages.getById", data={
            'message_ids': ids,
            'extended': 1,
            'access_token': token,
            'v': v})
        if "response" in request.json():
            if len(request.json()["response"]["items"]) > 0:
                for k in request.json()["response"]["items"]:
                    print(str(k))
                    requests_all.append(k)
                count += 100
                ids = ''
            else:
                break
            timer()
        else:
            print('nothing to parse')
            timer()
            break
        print(ids)
    return requests_all
