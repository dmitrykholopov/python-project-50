from gendiff.modules.data_loader import load_files_data
from gendiff.modules.gendiff_updated import get_ast_tree


def make_diff() -> callable:
    data1, data2 = load_files_data()
    print(get_ast_tree(data1, data2))
