def sum_nodes(node):
    if not node:
        return 0

    return sum_nodes(node.left) + node.data + sum_nodes(node.right)

# O(n) runtime --> The code touches each nodei n the tree once
# and Does a constant amount of work with each touch