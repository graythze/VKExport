import argparse
import json
import logging
import time
from pathlib import Path

import methods


ALL_METHODS = (
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
    ("messages", methods.messages_get),
)

BASE_METHODS = ALL_METHODS[:-3]
EXTRA_METHODS = ALL_METHODS[:-1]


def create_parser():
    parser = argparse.ArgumentParser(
        description="Export VK page data to JSON files"
    )
    methods_group = parser.add_mutually_exclusive_group()
    methods_group.add_argument("-c", "--custom", help="Comma-separated methods")
    methods_group.add_argument("-b", "--base", action="store_true")
    methods_group.add_argument("-e", "--extra", action="store_true")
    methods_group.add_argument("-f", "--full", action="store_true")
    parser.add_argument("token", help="VK API token")
    parser.add_argument("id", help="Page ID or user domain")
    parser.add_argument("-a", "--api", default="5.82", help="API version")
    parser.add_argument("-sf", "--singlefile", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def choose_methods(args):
    if args.base:
        return BASE_METHODS
    if args.extra:
        return EXTRA_METHODS
    if args.custom:
        names = {name.strip() for name in args.custom.split(",")}
        return tuple(item for item in ALL_METHODS if item[0] in names)
    return ALL_METHODS


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
    export_data(user_id, args.token, args.api, choose_methods(args), args.singlefile)


if __name__ == "__main__":
    main()
