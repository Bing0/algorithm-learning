# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        res = None

        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return None
            if slow == fast:
                break
        if fast is None:
            return None

        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next

        return slow
