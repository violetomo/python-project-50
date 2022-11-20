import json
from pathlib import Path


def find_and_sort(file):
        dir_path = Path.home()
        file_path = next(Path(dir_path).rglob(file))
        file_dict = json.load(open(file_path, encoding='utf-8'))
        dict_sorted = dict(sorted(file_dict.items()))
        return dict_sorted
