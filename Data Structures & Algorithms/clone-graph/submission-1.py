"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        nodes = {}

        def clone(node):
            if node in nodes:
                return nodes[node]
            copy = Node(node.val)
            nodes[node] = copy
            copy.neighbors = [clone(n) for n in node.neighbors]
            return copy
        return clone(node)