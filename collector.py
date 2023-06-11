import argparse
import methods
import time
import os

default_api_ver = 5.82

parser = argparse.ArgumentParser(description='Use example: python collector.py <API token> <page id> -a <API ver> -s <save option>')
parser.add_argument('token',
                    type=str,
                    help='VK API token')
parser.add_argument('page',
                    type=str,
                    help="Page ID or custom user domain")
parser.add_argument('-a', '--api',
                    type=float,
                    default=default_api_ver,
                    help=f'Enter API version ({default_api_ver} is set by default)')
parser.add_argument('-s', '--save',
                    type=str,
                    default='sep',
                    help='Save as single file or file separated by method (separate file is used by default)')
args = parser.parse_args()

token = args.token
v = str(args.api)
user_id = str(methods.get_numeric_id(args.page, token, v))

if args.save == "sep":
    path = f"export{user_id}_{int(time.time())}"
    os.mkdir(path)

    def create_file(name, data):
        with open(f"{path}/{name}{user_id}_{int(time.time())}.json", mode="w", encoding="utf-8") as file:
            file.write(str(data))

    data_types = [("main_profile", methods.users_get),
                  ("wall", methods.wall_get),
                  ("documents", methods.docs_get),
                  ("photos", methods.photos_get_all),
                  ("notes", methods.notes_get),
                  ("videos", methods.videos_get),
                  ("friends", methods.friends_get),
                  ("gifts", methods.gifts_get),
                  ("stories", methods.stories_get),
                  ("groups", methods.groups_get),
                  ("market", methods.market_get)]

    for data_type, method in data_types:
        data = {"id": user_id,
                "parsing_started": int(time.time()),
                data_type: method(user_id, token, v),
                "parsing_finished": int(time.time())}
        create_file(data_type, data)
else:
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

    with open(f"export{user_id}_{int(time.time())}.json", mode="w", encoding="utf-8") as file:
        file.write(str(data))

# data["followers"] = methods.followers_get(user_id, token, v)

# data["messages"] = methods.messages_get(token, v)
