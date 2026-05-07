# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        slow.next = None

        prev, curr = None, l2
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        l1, l2 = head, prev
        while l2:
            l1Next = l1.next
            l2Next = l2.next
            l1.next = l2
            l2.next = l1Next
            l1 = l1Next
            l2 = l2Next