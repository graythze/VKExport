import argparse
import methods
import time
import os
import json
import logging

parser = argparse.ArgumentParser(description='usage: collector.py VK_TOKEN durov -api 5.82 -c wall,photos,notes -sf -v')

set_methods = parser.add_mutually_exclusive_group()
set_methods.add_argument('-c', '--custom', help="Parse custom methods")
set_methods.add_argument('-b', '--base', action="store_true", help="Parse basic info")
set_methods.add_argument('-e', '--extra', action="store_true", help="Parse basic + extra info")
set_methods.add_argument('-f', '--full', action="store_true", help="Parse full info")
parser.add_argument('token', type=str, help='VK API token')
parser.add_argument('id', type=str, help="Page ID or user domain")
parser.add_argument('-a', '--api', type=str, default=5.82, help='API version')
parser.add_argument('-sf', '--singlefile', action="store_true", help="Save result in single file")
parser.add_argument('-v', '--verbose', action="store_true", help="Increase output verbosity")
args = parser.parse_args()

if args.verbose:
    logging.basicConfig(encoding='utf-8', level=10)
else:
    logging.basicConfig(encoding='utf-8', level=20)

user_id = methods.get_numeric_id(args.id, args.token, args.api)

data_types = (
    ("profile", methods.users_get),
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
    ("messages", methods.messages_get)
)

if args.base:
    data_types = data_types[0:9]
elif args.extra:
    data_types = data_types[0:11]
elif args.full:
    pass
elif args.custom:
    custom_types = []
    for single_method in args.custom.split(","):
        for data_type, method in data_types:
            if single_method == data_type:
                custom_types.append((data_type, method))
    data_types = custom_types

if args.singlefile:
    data = {"parsing_started": int(time.time())}
    for data_type, method in data_types:
        data[data_type] = method(user_id, args.token, args.api)
    data["parsing_finished"] = int(time.time())
    with open(f"export{user_id}_{int(time.time())}.json", mode="w", encoding="UTF-8") as file:
        file.write(json.dumps(data, ensure_ascii=False))
else:
    path = f"export{user_id}_{int(time.time())}"
    os.mkdir(path)
    for data_type, method in data_types:
        data = {"id": user_id,
                "parsing_started": int(time.time()),
                data_type: method(user_id, args.token, args.api),
                "parsing_finished": int(time.time())}
        with open(f"{path}\\{data_type}_{user_id}.json", mode="w", encoding="UTF-8") as file:
            file.write(json.dumps(data, ensure_ascii=False))
