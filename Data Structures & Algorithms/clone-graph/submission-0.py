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
        self.nodes = {}
        def clone(node):
            if node.val not in self.nodes:
                self.nodes[node.val] = Node(node.val, [])
            for neighbor in node.neighbors:
                if neighbor.val not in self.nodes:
                    clone(neighbor)
                self.nodes[neighbor.val].neighbors.append(self.nodes[node.val])
        clone(node)
        return self.nodes[1]