from gendiff.modules.generate_diff import generate_diff


def test_gendiff():
    with open('gendiff/tests/fixtures/gendiff_result.txt', 'r') as file:
        result = file.read().strip()
    assert generate_diff('gendiff/tests/fixtures/file1.json', 'gendiff/tests/fixtures/file2.json') == result
