# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        left, right = head, head
        gap = 0
        while right.next != None:
            right = right.next
            gap += 1
            if gap > n:
                left = left.next
        if n == gap + 1:
            return head.next
        else:
            left.next = left.next.next
        return head