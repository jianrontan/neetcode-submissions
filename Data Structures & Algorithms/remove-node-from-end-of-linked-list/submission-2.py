# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        cur = head
        count = 1
        while cur.next != None:
            cur = cur.next
            count += 1

        if n == count:
            return head.next
        
        bef = None
        removal = head
        for i in range(count - n):
            bef = removal
            removal = removal.next
        
        print(" ")
        if removal.next != None:
            bef.next = removal.next
        else:
            bef.next = None
        return head