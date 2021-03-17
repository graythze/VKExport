import requests
import time


def timer():
    time.sleep(0.36)
    

def docs_get(id, token, v):
    offset = 0
    requests_all = []
    while True:
        request = requests.post("https://api.vk.com/method/docs.get", data={
            'count': '1999',
            'offset': str(offset),
            'owner_id': str(id),
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
        elif "response" not in request.json():
            print('nothing')
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
            'offset': str(offset),
            'fields': 'nickname, domain, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig,'
                      'has_mobile, contacts, education, online, relation, last_seen, status, can_write_private_message,'
                      'can_see_all_posts, can_post, universities',
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
        elif "response" not in request.json():
            print('nothing')
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
            'count': '1009',
            'offset': str(offset),
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
        elif "response" not in request.json():
            print('nothing')
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
            'offset': str(offset),
            'count': '100',
            'sort': '1',
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
        elif "response" not in request.json():
            print('nothing')
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
            'extended': '1',
            'offset': str(offset),
            'count': '200',
            'photo_sizes': '1',
            'no_service_albums': '0',
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
        elif "response" not in request.json():
            print('nothing')
            timer()
            break
        offset += 100
    return requests_all


def stories_get(id, token, v):
    request = requests.post("https://api.vk.com/method/stories.get", data={
        'owner_id': id,
        'extended': '1',
        'access_token': token,
        'v': v}).json()
    if "response" in request:
        timer()
        return request


def users_get(id, token, v):
    request = requests.post("https://api.vk.com/method/users.get", data={
        'user_ids': id,
        'fields': 'verified,sex,bdate,city,country,home_town,photo_max_orig,domain,wall_comments,contacts,site,'
                  'education,universities,schools,status,last_seen,followers_count,has_photo,occupation,nickname,'
                  'relatives,relation,personal,connections,exports,activities,interests,music,movies,tv,books,games,'
                  'about,quotes,can_post,can_see_all_posts,can_see_audio,can_write_private_message,'
                  'can_send_friend_request,screen_name,maiden_name,crop_photo,career,can_be_invited_group,counters,'
                  'military,is_closed',
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
            'count': '200',
            'offset': str(offset),
            'extended': '1',
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
        elif "response" not in request.json():
            print('nothing')
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
            'offset': str(offset),
            'count': '1000',
            'fields': 'photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, '
                      'photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, lists, domain, '
                      'has_mobile, contacts, site, education, universities, schools, status, last_seen, '
                      'occupation, nickname, relatives, relation, personal, connections, exports, followers_count,'
                      'wall_comments, activities, interests, music, movies, tv, books, games, about, quotes, can_post, '
                      'can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, '
                      'timezone, screen_name, maiden_name, crop_photo, '
                      'career, military',
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
        elif "response" not in request.json():
            print('nothing')
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
            'extended': '1',
            'fields': 'city, country, place, description, wiki_page, members_count, counters, start_date, '
                      'finish_date, can_post, can_see_all_posts, activity, status, contacts, links, fixed_post, '
                      'verified, site, can_create_topic',
            'offset': str(offset),
            'count': '100',
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
        elif "response" not in request.json():
            print('nothing')
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
            'extended': '1',
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
        elif "response" not in request.json():
            print('nothing')
            timer()
            break
        print(ids)





