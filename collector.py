import argparse
import methods
import time
import os
import json

default_api_ver = 5.82

parser = argparse.ArgumentParser(description='Use example: py collector.py <API token> <page id> -v <API ver> -s <save method> -m <parser mode> -v <verbose level>')
set_methods = parser.add_mutually_exclusive_group()
set_methods.add_argument('-c', '--custom', help="Choose custom methods")
set_methods.add_argument('-m', "--mode", type=int, choices=[1, 2, 3])
parser.add_argument('token', type=str, help='VK API token')
parser.add_argument('id', type=str, help="Page ID or user domain")
parser.add_argument('-api', '--apiver', type=str, default=default_api_ver, help='API version')
parser.add_argument('-sf', '--singlefile', action="store_true", help="Save result in single file")
parser.add_argument('-v', '--verbose', action="store_true", help="Increase output verbosity")
args = parser.parse_args()

user_id = methods.get_numeric_id(args.id, args.token, args.apiver)

data_types = (("profile", methods.users_get),
              ("wall", methods.wall_get),
              ("documents", methods.docs_get),
              ("photos", methods.photos_get_all),
              ("notes", methods.notes_get),
              ("videos", methods.videos_get),
              ("friends", methods.friends_get),
              ("stories", methods.stories_get),
              ("groups", methods.groups_get),
              ("market", methods.market_get),
              ("gifts", methods.gifts_get),
              ("followers", methods.followers_get),
              ("messages", methods.messages_get))

if args.mode == 1:
    data_types = data_types[0:9]
elif args.mode == 2:
    data_types = data_types[0:11]
elif args.mode == 3:
    data_types = data_types

if args.singlefile:
    data = {"parsing_started": int(time.time())}
    for data_type, method in data_types:
        data[data_type] = method(user_id, args.token, args.apiver, args.verbose)
    data["parsing_finished"] = int(time.time())
    with open(f"export{user_id}_{int(time.time())}.json", mode="w", encoding="utf-8") as file:
        file.write(json.dumps(data))
elif args.custom:
    path = f"export{user_id}_{int(time.time())}"
    os.mkdir(path)
    for single_method in args.custom.split(","):
        for data_type, method in data_types:
            if data_type == single_method:
                data = {"id": user_id,
                        "parsing_started": int(time.time()),
                        data_type: method(user_id, args.token, args.apiver, args.verbose),
                        "parsing_finished": int(time.time())}
                with open(f"{path}\\{data_type}_{user_id}.json", mode="w", encoding="utf-8") as file:
                    file.write(json.dumps(data))
else:
    path = f"export{user_id}_{int(time.time())}"
    os.mkdir(path)
    for data_type, method in data_types:
        data = {"id": user_id,
                "parsing_started": int(time.time()),
                data_type: method(user_id, args.token, args.apiver, args.verbose),
                "parsing_finished": int(time.time())}
        with open(f"{path}\\{data_type}_{user_id}.json", mode="w", encoding="utf-8") as file:
            file.write(json.dumps(data))
