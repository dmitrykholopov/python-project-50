from gendiff.modules.gendiff import generate_diff


def test_gendiff():
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'
    res_path = 'tests/fixtures/result1.txt'
    with open(res_path) as f:
        result = f.read()

    assert generate_diff(file1_path, file2_path) == result
