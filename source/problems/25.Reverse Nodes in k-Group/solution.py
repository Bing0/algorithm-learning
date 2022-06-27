# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = ListNode(next=head)
        # update pre_tail and cur_head for each k group
        pre_tail = new_head
        cur_head = head

        while True:

            # find cur_tail
            j = k - 1
            cur_tail = cur_head
            while j > 0 and cur_tail is not None:
                cur_tail = cur_tail.next
                j -= 1
            if cur_tail is None:
                return new_head.next
            # find nxt_head
            nxt_head = cur_tail.next

            pre = nxt_head
            cur = cur_head

            while cur != nxt_head:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            pre_tail.next = pre

            # update pre_tail and cur_head for each k group
            pre_tail = cur_head
            cur_head = nxt_head


# A more clear solution is use a method    def reverse(head: ListNode, k: int) -> ListNode:


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

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
