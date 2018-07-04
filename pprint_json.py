import json
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file_object:
        return json.load(file_object)


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    alco_shops = load_data(sys.argv[1])
    print(pretty_print_json(alco_shops))
