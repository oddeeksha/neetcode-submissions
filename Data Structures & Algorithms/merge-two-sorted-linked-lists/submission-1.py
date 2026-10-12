# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy_curr = dummy
        if not list1 and not list2:
            return None
        while list1 and list2:
            if list1.val < list2.val:
                dummy_curr.next = list1
                list1 = list1.next
            else:
                dummy_curr.next = list2
                list2 = list2.next
            dummy_curr = dummy_curr.next
        if list1:
            dummy_curr.next = list1
        if list2:
            dummy_curr.next = list2
        return dummy.next

        