"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copies = {}
        curr = head
        while curr and curr not in copies:
                copies[curr] = Node(curr.val)
                curr = curr.next
        for ori, new in copies.items():
            new.next = copies.get(ori.next, None)
            new.random = copies.get(ori.random, None)
        return copies[head]