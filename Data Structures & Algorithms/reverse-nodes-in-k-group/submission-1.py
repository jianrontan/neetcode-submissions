# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = ListNode(next=head)
        groupPrev = prev

        while True:
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if kth == None:
                    return prev.next
            groupNext = kth.next

            node, cur = groupNext, groupPrev.next
            while cur != groupNext:
                nex = cur.next
                cur.next = node
                node = cur
                cur = nex
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp