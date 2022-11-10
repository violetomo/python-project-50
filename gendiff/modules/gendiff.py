import json
import pathlib
from pathlib import Path


def generate_diff(file1, file2):
    dir_path = Path.home()
    filepath1 = next(Path(dir_path).rglob(file1))
    filepath2 = next(Path(dir_path).rglob(file2))
    file1_dict = json.load(open(filepath1, encoding='utf-8'))
    file2_dict = json.load(open(filepath2, encoding='utf-8'))
    f1_d_sorted = dict(sorted(file1_dict.items()))
    f2_d_sorted = dict(sorted(file2_dict.items()))
    diff = ''
    diff_dict = {}
    for key in f1_d_sorted:
        if key not in f2_d_sorted:
            diff_dict['- '+key] = f1_d_sorted[key]
        elif key in f2_d_sorted and f1_d_sorted[key] == f2_d_sorted[key]:
            diff_dict['  '+key] = f1_d_sorted[key]
        else:
            diff_dict['- '+key] = f1_d_sorted[key]
            diff_dict['+ '+key] = f2_d_sorted[key]
    for key in f2_d_sorted:
        if key not in f1_d_sorted:
            diff_dict['+ '+key] = f2_d_sorted[key]
    for key in diff_dict:
        diff += f'\n {key}: {str(diff_dict[key]).lower()}'
    diff = '{' + diff + '\n}'
    return diff
