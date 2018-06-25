import json


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file_object:
        return json.load(file_object)


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    try:
        alco_shops = load_data('alco_shops.json')
    except TypeError:
        print('File path is not valid')

    try:
        print(json.dumps(alco_shops, sort_keys=True, indent=4, ensure_ascii=False))
    except TypeError:
        print('File is not valid')
