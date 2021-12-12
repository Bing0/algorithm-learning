# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse(head: ListNode, k: int) -> ListNode:
            prev = None
            curr = head

            while k:
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n
                k -= 1
            return prev

        curr = head
        dummy_head = ListNode(0, head)
        prev = dummy_head

        while True:
            tmp_k = k
            n = curr
            while tmp_k and n:
                n = n.next
                tmp_k -= 1

            if tmp_k != 0:
                break

            new_head = reverse(curr, k)
            prev.next = new_head
            curr.next = n
            prev = curr
            curr = n

        return dummy_head.next
