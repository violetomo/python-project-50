from gendiff.modules.find_and_sort import find_and_sort


def generate_diff(file1, file2):
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
