# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast1 = head
        fast2 = head.next
        while slow is not None and fast1 is not None and fast2 is not None:
            slow = slow.next
            if fast1.next is None:
                fast1 = None
            else:
                fast1 = fast1.next.next
            if fast2.next is None:
                fast2 = None
            else:
                fast2 = fast2.next.next
            if slow == fast1 or slow == fast2:
                return True
        return False