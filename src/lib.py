node_ls = []


class Node:
    pass


class Group:
    pass


def touch_node(group_name, node_name):
    node_ls.append(Node())
    if group_name is None:
        node_ls[len(node_ls) - 1].group = "group"
    else:
        node_ls[len(node_ls) - 1].group = group_name
    if node_name is None:
        node_ls[len(node_ls) - 1].name = f"node{(len(node_ls)) - 1}"
    else:
        node_ls[len(node_ls) - 1].name = f"{node_name}{len(node_ls) - 1}"
