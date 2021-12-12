# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists)
        mid = len(lists) // 2
        first = self.mergeKLists(lists[:mid])
        second = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists([first, second])

    def mergeTwoLists(self, lists: List[ListNode]) -> ListNode:
        merged = None
        tail = None
        a = lists[0]
        b = lists[1]

        next_item = None
        while a or b:
            if not b or (a and b.val >= a.val):
                next_item = a
                a = a.next
            else:
                next_item = b
                b = b.next

            if tail:
                tail.next = next_item
                tail = next_item
            else:
                merged = next_item
                tail = next_item
            next_item.next = None
        return merged