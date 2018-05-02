def sum_nodes(node):
    if not node:
        return 0

    return sum_nodes(node.left) + node.data + sum_nodes(node.right)