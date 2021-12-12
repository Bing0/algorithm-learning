class Node:
    val = None
    prev = None
    next = None

    def __init__(self, val=None, prev: "Node" = None, next: "Node" = None):
        self.val = val
        self.prev = prev
        self.next = next


def neighborhood(nums: list[int]) -> list[list[int]]:
    head = Node()
    tail = Node()
    head.next = tail
    tail.prev = head

    relation = {}

    tmp = []
    for i in range(len(nums)):
        tmp.append((nums[i], i))

    for num in sorted(tmp):
        curr = Node(num, None, tail)
        prev = tail.prev
        prev.next = curr
        curr.prev = prev
        tail.prev = curr
        relation[num[0]] = curr

    result = []

    for num in reversed(nums):
        node = relation[num]
        prev = node.prev
        nxt = node.next

        if prev.val:
            if nxt.val:
                if num - prev.val[0] < nxt.val[0] - num:
                    result.append([num - prev.val[0], prev.val[1]])
                elif num - prev.val[0] == nxt.val[0] - num:
                    result.append([num - prev.val[0], max(prev.val[1], nxt.val[1])])
                else:
                    result.append([nxt.val[0] - num, nxt.val[1]])
            else:
                result.append([num - prev.val[0], prev.val[1]])
        else:
            if nxt.val:
                result.append([nxt.val[0] - num, nxt.val[1]])
        prev.next = nxt
        nxt.prev = prev

    return result