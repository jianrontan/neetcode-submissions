# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = 0
        exp = 0
        carry = 0
        dummy1 = ListNode(0, next=l1)
        dummy2 = ListNode(0, next=l2)
        dummyRes = ListNode(0, next=None)
        startRes = dummyRes
        while dummy1.next != None or dummy2.next != None:
            if dummy1.next:
                dummy1 = dummy1.next
            else:
                dummy1.val = 0
            if dummy2.next:
                dummy2 = dummy2.next
            else:
                dummy2.val = 0
            num = dummy1.val + dummy2.val + carry
            if num > 9:
                carry = num // 10
            else:
                carry = 0
            res += (num % 10) * (10 ** exp)
            dummyRes.next = ListNode(num % 10, next=None)
            dummyRes = dummyRes.next
            exp += 1
        res += carry * (10 ** exp)
        if carry > 0:
            dummyRes.next = ListNode(carry, next=None)
            dummyRes = dummyRes.next
        return startRes.next