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

if "sep" in args.save:
    path = f"export{user_id}_{int(time.time())}"
    os.mkdir(path)
    for data_type, method in data_types:
        data = {"id": user_id,
                "parsing_started": int(time.time()),
                data_type: method(user_id, args.token, args.ver),
                "parsing_finished": int(time.time())}
elif "sin" in args.save:
    data = {"parsing_started": int(time.time())}
    for data_type, method in data_types:
        data[data_type] = method(user_id, args.token, args.ver)
    data["parsing_finished"] = int(time.time())
    with open(f"export{user_id}_{int(time.time())}.json", mode="w", encoding="utf-8") as file:
        file.write(json.dumps(data))
