import json
import yaml
from yaml.loader import SafeLoader
from pathlib import Path


def find_and_sort(file):
    dir_path = Path.home()
    file_path = next(Path(dir_path).rglob(file))
    format_of_file = file[-4:len(file)]
    if format_of_file == 'json':
        file_dict = json.load(open(file_path, encoding='utf-8'))
    else:
        file_dict = yaml.load(open(file_path, encoding='utf-8'), Loader=SafeLoader)  # noqa E501
    dict_sorted = dict(sorted(file_dict.items()))
    return dict_sorted
