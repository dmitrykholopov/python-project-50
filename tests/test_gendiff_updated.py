from json import load as json_load

from gendiff.modules.gendiff_updated import get_ast_tree


def test_gendiff():
    file1_path = 'tests/fixtures/file1_nested.json'
    file2_path = 'tests/fixtures/file2_nested.json'
    res_path = 'tests/fixtures/result2_nested.txt'
    data1 = json_load(open(file1_path))
    data2 = json_load(open(file2_path))

    with open(res_path) as f:
        result = f.read()

    assert str(get_ast_tree(data1, data2)) == result
