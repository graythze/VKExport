import argparse
import methods
import time
import os


def timer():
    time.sleep(0.36)


parser = argparse.ArgumentParser(description='Use example: python collector.py <API token> <page id>')
parser.add_argument('token',
                    type=str,
                    help='Enter your VK API token')
parser.add_argument('page',
                    type=str,
                    help='Enter page ID or custom domain of user')
parser.add_argument('-a', '--apiver',
                    type=float,
                    default=5.82,
                    help='Enter API version (5.82 is set by default)')
args = parser.parse_args()

token = args.token
v = str(args.apiver)
user_id = str(methods.get_numeric_id(args.page, token, v))

path = "export" + str(user_id) + "_" + str(int(time.time()))
os.mkdir(path)


def create_file(name, data):
    with open(path + str(name) + user_id + "_" + str(int(time.time())) + ".json", mode="w", encoding="utf-8") as file:
        file.write(str(data))


data = {"id": user_id, "parsing_started": int(time.time()), "main_profile": methods.users_get(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/profile", data)

data = {"id": user_id, "parsing_started": int(time.time()), "wall": methods.wall_get(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/wall", data)

data = {"id": user_id, "parsing_started": int(time.time()), "documents": methods.docs_get(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/documents", data)

data = {"id": user_id, "parsing_started": int(time.time()), "photos": methods.photos_get_all(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/photos", data)

data = {"id": user_id, "parsing_started": int(time.time()), "notes": methods.notes_get(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/notes", data)

data = {"id": user_id, "parsing_started": int(time.time()), "videos": methods.videos_get(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/videos", data)

data = {"id": user_id, "parsing_started": int(time.time()), "friends": methods.friends_get(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/friends", data)

data = {"id": user_id, "parsing_started": int(time.time()), "gifts": methods.gifts_get(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/gifts", data)

data = {"id": user_id, "parsing_started": int(time.time()), "stories": methods.stories_get(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/stories", data)

data = {"id": user_id, "parsing_started": int(time.time()), "groups": methods.groups_get(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/groups", data)

data = {"id": user_id, "parsing_started": int(time.time()), "market": methods.market_get(user_id, token, v),
        "parsing_finished": int(time.time())}
create_file("/market", data)

""" be careful with followers_get. don't use it if you don't want to parse ALL FOLLOWERS """
# data = {"id": user_id, "parsing_started": int(time.time()), "followers": methods.followers_get(user_id, token, v),
#         "parsing_finished": int(time.time())}
# create_file("/followers", data)

""" be careful with messages_get. don't use it if you don't want to parse OWN MESSAGES """
# data = {"id": user_id, "parsing_started": int(time.time()), "groups": methods.messages_get(token, v),
#         "parsing_finished": int(time.time())}
# create_file("/ownMessages", data)
