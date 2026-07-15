# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        newHead = None
        prev = None
        start = head
        def reverse(node, count):
            nonlocal newHead, start, prev
            if node.next == None:
                start = None
                return False
            if count >= k - 1:
                if newHead == None:
                    newHead = node.next
                if prev:
                    prev.next = node.next
                start = node.next.next
                node.next.next = node
                if count == 1:
                    node.next = start
                    prev = node
                return True
            else:
                nodeNext = node.next
                if reverse(nodeNext, count + 1):
                    nodeNext.next = node
                else:
                    return False
                if count == 1:
                    node.next = start
                    prev = node
                return True
        
        while start != None:
            reverse(start, 1)

        return newHead