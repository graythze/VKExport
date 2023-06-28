import argparse
import methods
import time
import os
import json

default_api_ver = 5.82

parser = argparse.ArgumentParser(description='Use example: python collector.py <API token> <page id> -v <API ver> -s <save option>')
parser.add_argument('token',
                    type=str,
                    help='VK API token')
parser.add_argument('page',
                    type=str,
                    help="Page ID or custom user domain")
parser.add_argument('-v', '--ver',
                    type=str,
                    default=default_api_ver,
                    help=f'Enter API version ({default_api_ver} is set by default)')
parser.add_argument('-s', '--save',
                    type=str,
                    default='sep',
                    help='Save as single file or file separated by method (separate file is used by default)')
args = parser.parse_args()

def create_file(name, data):
    with open(f"{path}/{name}{user_id}_{int(time.time())}.json", mode="w", encoding="utf-8") as file:
        file.write(str(data))

user_id = methods.get_numeric_id(args.page, args.token, args.ver)

if "sep" in args.save:
    path = f"export{user_id}_{int(time.time())}"
    os.mkdir(path)
    data_types = [("profile", methods.users_get),
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
                  # ("followers", methods.followers_get),
                  # ("messages", methods.messages_get)]

    for data_type, method in data_types:
        data = {"id": user_id,
                "parsing_started": int(time.time()),
                data_type: method(user_id, args.token, args.ver),
                "parsing_finished": int(time.time())}
        create_file(data_type, json.dumps(data))
elif "sin" in args.save:
    data = {"id": user_id,
            "parsing_started": int(time.time()),
            "main_profile": methods.users_get(user_id, args.token, args.ver),
            "wall": methods.wall_get(user_id, args.token, args.ver),
            "documents": methods.docs_get(user_id, args.token, args.ver),
            "photos": methods.photos_get_all(user_id, args.token, args.ver),
            "notes": methods.notes_get(user_id, args.token, args.ver),
            "videos": methods.videos_get(user_id, args.token, args.ver),
            "friends": methods.friends_get(user_id, args.token, args.ver),
            "gifts": methods.gifts_get(user_id, args.token, args.ver),
            "stories": methods.stories_get(user_id, args.token, args.ver),
            "groups": methods.groups_get(user_id, args.token, args.ver),
            "market": methods.market_get(user_id, args.token, args.ver),
            "parsing_finished": int(time.time())}
    with open(f"export{user_id}_{int(time.time())}.json", mode="w", encoding="utf-8") as file:
        file.write(json.dumps(data))
