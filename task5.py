import uuid
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, traversal):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def bfs_traversal(root):
    queue = deque([root])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node.val)
        node.color = '#1296F0'
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def dfs_traversal(root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        order.append(node.val)
        node.color = '#1296F0'
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(8)
root.right.left = Node(12)
root.right.right = Node(20)

print("BFS Traversal Order:", bfs_traversal(root))
draw_tree(root, bfs_traversal(root))

root.color = "skyblue"
print("DFS Traversal Order:", dfs_traversal(root))
draw_tree(root, dfs_traversal(root))
