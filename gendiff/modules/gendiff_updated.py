from typing import Any


KEY_STATES = {'ADDED': 'added',
              'NESTED': 'nested',
              'REMOVED': 'removed',
              'UNCHANGED': 'unchanged',
              'UPDATED': 'updated'
}


def add_node(key: str | int | float| tuple | frozenset, 
             node_type: str,
             value: Any=None, 
             old_value: Any=None,
             children: list=None) -> dict:

    node_pattern = {
        'key': key,
        'value': {
            'old': old_value,
            'new': value
        },
        'node type': node_type
    }

    if children is not None:
        node_pattern['children'] = children

    return node_pattern


def get_ast_tree(data1: dict, data2: dict) -> dict:
    united_keys = sorted(set(data1.keys()) | set(data2.keys()))
    ast_tree = []

    for key in united_keys:

        if key in data1 and key not in data2:
            ast_tree.append(
                add_node(key,
                         KEY_STATES['REMOVED'],
                         old_value=data1[key])
            )

        elif key not in data1 and key in data2:
            ast_tree.append(
                add_node(key,
                         KEY_STATES['ADDED'],
                         value=data2[key])
            )

        elif data1[key] == data2[key]:
            ast_tree.append(
                add_node(key,
                         KEY_STATES['UNCHANGED'],
                         old_value=data1[key])
            )

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            child_diff = get_ast_tree(data1[key], data2[key])
            ast_tree.append(
                add_node(key,
                         KEY_STATES['NESTED'],
                         children=child_diff)
            )

        else:
            ast_tree.append(
                add_node(key,
                         KEY_STATES['UPDATED'],
                         value=data2[key],
                         old_value=data1[key])
            )

    return ast_tree
