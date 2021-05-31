import settings
import methods
import time

token = settings.VK_TOKEN
v = str(settings.V)
user_id = str(methods.get_numeric_id(settings.PAGE_TO_PARSE, token, v))


def timer():
    time.sleep(0.36)


data = {"id": user_id,
        "parsing_started": int(time.time()),
        "main_profile": methods.users_get(user_id, token, v),
        "wall": methods.wall_get(user_id, token, v),
        "documents": methods.docs_get(user_id, token, v),
        "photos": methods.photos_get_all(user_id, token, v),
        "notes": methods.notes_get(user_id, token, v),
        "videos": methods.videos_get(user_id, token, v),
        "friends": methods.friends_get(user_id, token, v),
        "gifts": methods.gifts_get(user_id, token, v),
        "stories": methods.stories_get(user_id, token, v),
        "groups": methods.groups_get(user_id, token, v),
        "market": methods.market_get(user_id, token, v),
        "parsing_finished": int(time.time())}


""" be careful with followers_get. don't use it if you don't want to parse ALL FOLLOWERS """
# data["followers"] = methods.followers_get(user_id, token, v)

""" be careful with messages_get. don't use it if you don't want to parse OWN MESSAGES """
# data["messages"] = methods.messages_get(token, v)


with open("export" + str(user_id) + "_" + str(int(time.time())) + ".json", mode="w", encoding="utf-8") as file:
    file.write(str(data))


print(data)
