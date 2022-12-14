from gendiff.modules.generate_diff import generate_diff


def test_gendiff_json():
    with open('gendiff/tests/fixtures/gendiff_result.txt', 'r') as file:
        result = file.read().strip()
    filepath1 = 'gendiff/tests/fixtures/file1.json'
    filepath2 = 'gendiff/tests/fixtures/file2.json'
    assert generate_diff(filepath1, filepath2) == result


def test_gendiff_yaml():
    with open('gendiff/tests/fixtures/gendiff_result.txt', 'r') as file:
        result = file.read().strip()
    filepath1 = 'gendiff/tests/fixtures/file1.yml'
    filepath2 = 'gendiff/tests/fixtures/file2.yml'
    assert generate_diff(filepath1, filepath2) == result
