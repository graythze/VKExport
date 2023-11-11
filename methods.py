import traceback
import sys
import requests
import time
import logging

time_wait = 1/3


def make_request(method, data, method_offset, token, v):
    data["access_token"] = token
    data["v"] = v
    offset = 0
    requests_all = []
    while True:
        request = requests.post(f"https://api.vk.com/method/{method}", data=data).json()
        logging.info(f"Received {method} request. Offset: {offset}")
        logging.debug(request)
        if "response" in request and len(request["response"]["items"]) > 0:
            requests_all.extend(iter(request["response"]["items"]))
            logging.debug(data["offset"])
            if method_offset > 0:
                offset += method_offset
                data["offset"] = offset
                time.sleep(time_wait)
        else:
            logging.info(f"{method} parsing ended")
            time.sleep(time_wait)
            break
    return requests_all


def get_numeric_id(id, token, v):
    try:
        request = requests.post("https://api.vk.com/method/utils.resolveScreenName", data={
            "screen_name": id,
            "access_token": token,
            "v": v}).json()
        if "response" in request:
            if id.isnumeric():
                if int(id) > 0:
                    return id
                elif int(id) < 0:
                    return id
            else:
                if "response" in request:
                    if request["type"] == "group":
                        return str(request["response"]["object_id"] * (-1))
                    elif request["type"] == "user":
                        return str(request["response"]["object_id"])
        elif "error" in request:
            exit(f"\n{request['error']['error_msg']}\n")
    except Exception:
        sys.exit(traceback.print_exc())


def docs_get(id, token, v):
    data = {"count": 2000,
            "offset": 0,
            "owner_id": id,
            "return_tags": 1}
    return make_request("docs.get", data, 2000, token, v)


def friends_get(id, token, v):
    data = {"user_id": id,
            "order": "name",
            "count": 5000,
            "offset": 0,
            "fields": "uid,first_name,last_name,deactivated,verified,sex,bdate,city,country,home_town,photo_max,"
                      "photo_max_orig,online,lists,can_see_all_posts,can_see_audio,can_write_private_message,timezone,"
                      "domain,has_mobile,contacts,site,education,universities,schools,status,last_seen,screen_name,"
                      "followers_count,counters,occupation,nickname,relatives,relation,personal,connections,exports,"
                      "wall_comments,activities,interests,music,movies,tv,books,games,about,quotes,can_post"}
    return make_request("friends.get", data, 5000, token, v)


def gifts_get(id, token, v):
    data = {"user_id": id,
            "count": 1000,
            "offset": 0}
    return make_request("gifts.get", data, 1000, token, v)


def notes_get(id, token, v):
    data = {"user_id": id,
            "offset": 0,
            "count": 100,
            "sort": 1}
    return make_request("notes.get", data, 100, token, v)


def photos_get_all(id, token, v):
    data = {"owner_id": id,
            "extended": 1,
            "offset": 0,
            "count": 200,
            "photo_sizes": 1,
            "no_service_albums": 0}
    return make_request("photos.getAll", data, 200, token, v)


def stories_get(id, token, v):
    data = {"owner_id": id,
            "extended": 1,}
    return make_request("stories.get", data, 0, token, v)


def users_get(id, token, v):
    request = requests.post("https://api.vk.com/method/users.get", data={
        "user_ids": id,
        "fields": "uid,first_name,last_name,deactivated,verified,sex,bdate,city,country,home_town,photo_max,"
                  "photo_max_orig,online,lists,domain,has_mobile,can_write_private_message,timezone,screen_name,"
                  "contacts,site,education,universities,schools,status,last_seen,followers_count,counters,occupation,"
                  "nickname,relatives,relation,personal,connections,exports,wall_comments,activities,interests,music,"
                  "movies,tv,books,games,about,quotes,can_post,can_see_all_posts,can_see_audio",
        "access_token": token,
        "v": v}).json()
    logging.debug(request)
    logging.info("got users_get/profile request")
    if "response" in request:
        time.sleep(time_wait)
        return request["response"]


def videos_get(id, token, v):
    data = {"owner_id": id,
            "count": 200,
            "offset": 0,
            "extended": 1}
    return make_request("video.get", data, 200, token, v)


def followers_get(id, token, v):
    data = {"user_id": id,
            "offset": 0,
            "count": 1000,
            "fields": "uid,first_name,last_name,deactivated,verified,sex,bdate,city,country,home_town,last_seen,status,"
                      "photo_max,photo_max_orig,online,lists,domain,has_mobile,counters,occupation,nickname,relatives,"
                      "contacts,site,education,universities,schools,status,relation,personal,connections,exports,"
                      "followers_count,can_see_all_posts,can_see_audio,can_write_private_message,timezone,screen_name,"
                      "wall_comments,activities,interests,music,movies,tv,books,games,about,quotes,can_post"}
    return make_request("users.getFollowers", data, 1000, token, v)


def groups_get(id, token, v):
    data = {"user_id": id,
            "extended": 1,
            "fields": "id,name,screen_name,is_closed,deactivated,is_admin,admin_level,is_member,invited_by,type,"
                      "has_photo,photo_50,photo_100,photo_200,activity,age_limits,can_create_topic,can_message,"
                      "can_post,can_see_all_posts,can_upload_doc,can_upload_video,city,contacts,counters,country,"
                      "cover,description,fixed_post,main_album_id,main_section,market,members_count,place,"
                      "public_date_label,site,status,trending,verified,wiki_page",
            "offset": 0,
            "count": 1000}
    return make_request("groups.get", data, 1000, token, v)


def messages_get(id, token, v):
    count = 0
    ids = ""
    requests_all = []
    while True:
        for k in range(count, 100 + count):
            ids += f"{str(k)},"
        request = requests.post("https://api.vk.com/method/messages.getById", data={
            "message_ids": ids,
            "extended": 1,
            "fields": "uid,first_name,last_name,deactivated,verified,sex,bdate,city,country,home_town,photo_max,"
                      "photo_max_orig,online,lists,domain,has_mobile,can_write_private_message,timezone,screen_name,"
                      "contacts,site,education,universities,schools,status,last_seen,followers_count,counters,occupation,"
                      "nickname,relatives,relation,personal,connections,exports,wall_comments,activities,interests,music,"
                      "movies,tv,books,games,about,quotes,can_post,can_see_all_posts,can_see_audio",
            "access_token": token,
            "v": v}).json()
        logging.debug(request)
        logging.debug(ids)
        logging.info(f"got messages.getById request for {ids}")
        if "response" in request and len(request["response"]["items"]) > 0:
            requests_all.append(request["response"])
            ids = ""
            count += 100
            time.sleep(time_wait)
        else:
            logging.info("nothing to parse")
            time.sleep(time_wait)
            break
    return requests_all


def wall_get(id, token, v):
    data = {"owner_id": id,
            "offset": 0,
            "count": 100,
            "filter": "all",
            "extended": 1}
    return make_request("wall.get", data, 100, token, v)


def market_get(id, token, v):
    data = {"owner_id": id,
            "count": 200,
            "offset": 0,
            "extended": 1}
    return make_request("market.get", data, 200, token, v)


def photos_get_all_comments(id, token, v):
    data = {"owner_id": id,
            "count": 100,
            "offset": 0,
            "need_likes": 1}
    return make_request("photos.getAllComments", data, 100, token, v)
