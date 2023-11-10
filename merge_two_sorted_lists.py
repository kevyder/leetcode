# 21. Merge Two Sorted Lists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = output = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                output.next = list1
                list1 = list1.next
            else:
                output.next = list2
                list2 = list2.next

            output = output.next

        if list1:
            output.next = list1
        if list2:
            output.next = list2

        return dummy.next
