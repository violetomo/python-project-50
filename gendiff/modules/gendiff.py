import json
from pathlib import Path


def generate_diff(file1, file2):
    def find_and_sort(file):
        dir_path = Path.home()
        file_path = next(Path(dir_path).rglob(file))
        file_dict = json.load(open(file_path, encoding='utf-8'))
        dict_sorted = dict(sorted(file_dict.items()))
        return dict_sorted
    f1_d_sorted = find_and_sort(file1)
    f2_d_sorted = find_and_sort(file2)
    diff = ''
    diff_dict = {}
    for key in f1_d_sorted:
        if key not in f2_d_sorted:
            diff_dict['- ' + key] = f1_d_sorted[key]
        elif f1_d_sorted[key] == f2_d_sorted[key]:
            diff_dict['  ' + key] = f1_d_sorted[key]
        else:
            diff_dict['- ' + key] = f1_d_sorted[key]
            diff_dict['+ ' + key] = f2_d_sorted[key]
    for key in f2_d_sorted:
        if key not in f1_d_sorted:
            diff_dict['+ ' + key] = f2_d_sorted[key]
    for key in diff_dict:
        diff += f'\n {key}: {str(diff_dict[key]).lower()}'
    diff = '{' + diff + '\n}'
    return diff
