# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right:
            return head
        
        dummy = ListNode(next=head)
        cur, leftEdge, rightEdge = dummy, None, None
        for i in range(right):
            if i + 1 == left:
                leftEdge = cur
            cur = cur.next
            if i + 1 == right:
                rightEdge = cur.next
        
        flip = leftEdge.next
        nxt = flip.next
        while True:
            following = nxt.next
            nxt.next = flip
            if following == rightEdge:
                break
            flip = nxt
            nxt = following

        newLeftEdge = leftEdge.next
        leftEdge.next = nxt
        newLeftEdge.next = rightEdge

        return dummy.next