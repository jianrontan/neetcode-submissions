# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        startNode = None
        nextNode = None
        if list1.val <= list2.val:
            startNode = ListNode(list1.val)
            nextNode = startNode
            list1 = list1.next
        else:
            startNode = ListNode(list2.val)
            nextNode = startNode
            list2 = list2.next

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                nextNode.next = ListNode(list1.val)
                nextNode = nextNode.next
                list1 = list1.next
            else:
                nextNode.next = ListNode(list2.val)
                nextNode = nextNode.next
                list2 = list2.next
        
        if list1 is None and list2 is not None:
            while list2 is not None:
                nextNode.next = ListNode(list2.val)
                nextNode = nextNode.next
                list2 = list2.next
        elif list2 is None and list1 is not None:
            while list1 is not None:
                nextNode.next = ListNode(list1.val)
                nextNode = nextNode.next
                list1 = list1.next

        return startNode
                