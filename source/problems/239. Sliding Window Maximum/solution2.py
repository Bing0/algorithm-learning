from typing import List


class Node:
    def __init__(self, val: int = 0, height: int = 1, left: "Node" = None, right: "Node" = None):
        self.val = val
        self.height = height
        self.left = left
        self.right = right
        self.count = 1


class AVL:
    def __init__(self):
        self.head = None

    def insert(self, num: int, curr: Node) -> Node:
        if curr is None:
            return Node(num)

        if curr.val == num:
            curr.count += 1
            return curr

        if num < curr.val:
            curr.left = self.insert(num, curr.left)
        else:
            curr.right = self.insert(num, curr.right)

        curr.height = 1 + max(self.height(curr.left), self.height(curr.right))
        factor = self.height(curr.left) - self.height(curr.right)

        # Case 1 - Left Left
        if factor > 1 and num < curr.left.val:
            return self.rotate_right(curr)

        # Case 2 - Right Right
        if factor < -1 and num > curr.right.val:
            return self.rotate_left(curr)

        # Case 3 - Left Right
        if factor > 1 and num > curr.left.val:
            curr.left = self.rotate_left(curr.left)
            return self.rotate_right(curr)

        # Case 4 - Right Left
        if factor < -1 and num < curr.right.val:
            curr.right = self.rotate_right(curr.right)
            return self.rotate_left(curr)

        return curr

    def height(self, node: Node) -> int:
        if node:
            return node.height
        return 0

    def rotate_right(self, node: Node) -> Node:
        left = node.left
        node.left = left.right
        left.right = node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left.height = 1 + max(self.height(left.left), self.height(left.right))
        return left

    def rotate_left(self, node: Node) -> Node:
        right = node.right
        node.right = right.left
        right.left = node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right.height = 1 + max(self.height(right.left), self.height(right.right))
        return right

    def add(self, num: int):
        curr = self.head
        self.head = self.insert(num, curr)

    def delete(self, num: int, curr: Node, clear: bool) -> Node:
        if not curr:
            return None

        if num < curr.val:
            curr.left = self.delete(num, curr.left, clear)
        elif num > curr.val:
            curr.right = self.delete(num, curr.right, clear)
        else:
            curr.count -= 1
            if not clear and curr.count > 0:
                return curr

            if curr.left is None:
                return curr.right
            if curr.right is None:
                return curr.left

            min_node = curr.right
            while min_node.left:
                min_node = min_node.left
            curr.val = min_node.val
            curr.count = min_node.count
            curr.right = self.delete(min_node.val, curr.right, True)

        curr.height = 1 + max(self.height(curr.left), self.height(curr.right))
        factor = self.height(curr.left) - self.height(curr.right)

        # Left
        if factor > 1:
            factor = self.height(curr.left.left) - self.height(curr.left.right)
            # Left
            if factor >= 0:
                return self.rotate_right(curr)
            # right
            else:
                curr.left = self.rotate_left(curr.left)
                return self.rotate_right(curr)
        # right
        elif factor < -1:
            # Left
            if factor >= 0:
                curr.right = self.rotate_right(curr.right)
                return self.rotate_left(curr)
            # right
            else:
                return self.rotate_left(curr)
        return curr

    def remove(self, num: int):
        curr = self.head
        self.head = self.delete(num, curr, False)

    def max_num(self) -> int:
        curr = self.head
        ans = -1

        while curr:
            ans = curr.val
            curr = curr.right

        return ans

    def inorder(self, node: Node, stack: List[int]):
        if not node:
            return

        self.inorder(node.left, stack)
        stack.append(node.val)
        self.inorder(node.right, stack)

    def print_all(self):
        stack = []
        self.inorder(self.head, stack)
        # print(stack)
        return stack


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        avl = AVL()

        for i in range(k):
            avl.add(nums[i])

        ans.append(avl.max_num())
        for i in range(k, len(nums)):
            avl.add(nums[i])
            avl.remove(nums[i - k])
            ans.append(avl.max_num())

        return ans
