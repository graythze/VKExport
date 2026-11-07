import argparse
import json
import logging
import os
import time
from pathlib import Path

import methods


def env_bool(name):
    value = os.environ.get(name, "False")
    if value not in ("True", "False"):
        raise ValueError(f"{name} must be True or False")
    return value == "True"


def load_env_file():
    """Load simple KEY=VALUE entries from the project's .env file."""
    env_path = Path(__file__).with_name(".env")
    if not env_path.exists():
        return
    for line_number, raw_line in enumerate(env_path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise ValueError(f"Invalid .env line {line_number}: expected KEY=True or KEY=False")
        key, value = (part.strip() for part in line.split("=", 1))
        os.environ.setdefault(key, value)


load_env_file()

PARSE_METHODS = {
    "users_get": env_bool("PARSE_USERS_GET"),
    "wall_get": env_bool("PARSE_WALL_GET"),
    "docs_get": env_bool("PARSE_DOCS_GET"),
    "photos_get_all": env_bool("PARSE_PHOTOS_GET_ALL"),
    "notes_get": env_bool("PARSE_NOTES_GET"),
    "videos_get": env_bool("PARSE_VIDEOS_GET"),
    "friends_get": env_bool("PARSE_FRIENDS_GET"),
    "gifts_get": env_bool("PARSE_GIFTS_GET"),
    "stories_get": env_bool("PARSE_STORIES_GET"),
    "groups_get": env_bool("PARSE_GROUPS_GET"),
    "market_get": env_bool("PARSE_MARKET_GET"),
    "followers_get": env_bool("PARSE_FOLLOWERS_GET"),
    "messages_get": env_bool("PARSE_MESSAGES_GET"),
}

ALL_METHODS = (
    ("users_get", "profile", methods.users_get),
    ("wall_get", "wall", methods.wall_get),
    ("docs_get", "documents", methods.docs_get),
    ("photos_get_all", "photos", methods.photos_get_all),
    ("notes_get", "notes", methods.notes_get),
    ("videos_get", "videos", methods.videos_get),
    ("friends_get", "friends", methods.friends_get),
    ("stories_get", "stories", methods.stories_get),
    ("groups_get", "groups", methods.groups_get),
    ("market_get", "market", methods.market_get),
    ("gifts_get", "gifts", methods.gifts_get),
    ("followers_get", "followers", methods.followers_get),
    ("messages_get", "messages", methods.messages_get),
)

def create_parser():
    parser = argparse.ArgumentParser(
        description="Export VK page data to JSON files"
    )
    parser.add_argument("token", help="VK API token")
    parser.add_argument("id", help="Page ID or user domain")
    parser.add_argument("-a", "--api", default="5.82", help="API version")
    parser.add_argument("-sf", "--singlefile", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def choose_methods():
    return tuple((data_type, method) for key, data_type, method in ALL_METHODS if PARSE_METHODS[key])


def save_json(path, data):
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)


def export_data(user_id, token, api_version, selected_methods, single_file):
    timestamp = int(time.time())
    output_name = f"export{user_id}_{timestamp}"

    if single_file:
        data = {"parsing_started": timestamp}
        for data_type, method in selected_methods:
            data[data_type] = method(user_id, token, api_version)
        data["parsing_finished"] = int(time.time())
        save_json(Path(f"{output_name}.json"), data)
        return

    output_dir = Path(output_name)
    output_dir.mkdir()
    for data_type, method in selected_methods:
        started = int(time.time())
        data = {
            "id": user_id,
            "parsing_started": started,
            data_type: method(user_id, token, api_version),
            "parsing_finished": int(time.time()),
        }
        save_json(output_dir / f"{data_type}_{user_id}.json", data)


def main():
    args = create_parser().parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    user_id = methods.get_numeric_id(args.id, args.token, args.api)
    export_data(user_id, args.token, args.api, choose_methods(), args.singlefile)


if __name__ == "__main__":
    main()
