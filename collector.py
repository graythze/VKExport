import argparse
import methods
import time


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
                    help='Enter API version (8.82 is set by default)')
args = parser.parse_args()

token = args.token
v = str(args.apiver)
user_id = str(methods.get_numeric_id(args.page, token, v))

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
