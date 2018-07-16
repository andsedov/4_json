import json
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file_object:
        return json.load(file_object)


def pretty_format_json(data_from_json):
    return json.dumps(data_from_json, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    try:
        data_from_json = load_data(sys.argv[1])
        print(pretty_format_json(data_from_json))
    except IndexError:
        sys.exit('File name must be specified on the command line')
    except ValueError:
        sys.exit('File must be a json')
    except FileNotFoundError:
        sys.exit('No such file or directory')