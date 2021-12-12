from typing import List


class Node:
    def __init__(self, val=None, left: "Node" = None, right: "Node" = None):
        self.val = val  # (l,r,h)
        self.height = 1
        self.left = left
        self.right = right
        self.count = 1


class BST:
    def __init__(self):
        self.head = None
        self.max_height = 0

    def __insert(self, val, curr: Node) -> Node:
        if curr is None:
            return Node(val)

        if curr.val == val:
            curr.count += 1
            return curr

        if val < curr.val:
            curr.left = self.__insert(val, curr.left)
        else:
            curr.right = self.__insert(val, curr.right)

        curr.height = 1 + max(self.height(curr.left), self.height(curr.right))
        factor = self.height(curr.left) - self.height(curr.right)

        # Case 1 - Left Left
        if factor > 1 and val < curr.left.val:
            return self.rotate_right(curr)

        # Case 2 - Right Right
        if factor < -1 and val > curr.right.val:
            return self.rotate_left(curr)

        # Case 3 - Left Right
        if factor > 1 and val > curr.left.val:
            curr.left = self.rotate_left(curr.left)
            return self.rotate_right(curr)

        # Case 4 - Right Left
        if factor < -1 and val < curr.right.val:
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

    def __delete(self, val, curr: Node, clear: bool) -> Node:
        if not curr:
            return None

        if val < curr.val:
            curr.left = self.__delete(val, curr.left, clear)
        elif val > curr.val:
            curr.right = self.__delete(val, curr.right, clear)
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
            curr.right = self.__delete(min_node.val, curr.right, True)

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

    def __range_search(self, low, high, curr: Node, ans):
        if curr is None or low >= high:
            return

        if low >= curr.val[1]:
            self.__range_search(low, high, curr.right, ans)
            return
        if high <= curr.val[0]:
            self.__range_search(low, high, curr.left, ans)
            return

        ans.append(curr.val)
        self.__range_search(low, curr.val[0], curr.left, ans)
        self.__range_search(curr.val[1], high, curr.right, ans)

    def add(self, left: int, right: int, height: int) -> int:
        crossing = []

        self.__range_search(left, right, self.head, crossing)

        new_height = 0
        for _, _, h in crossing:
            new_height = max(new_height, h)

        new_height += height
        self.head = self.__insert((left, right, new_height), self.head)

        for cross in crossing:
            l, r, h = cross
            self.head = self.__delete(cross, self.head, False)
            if l < left:
                self.head = self.__insert((l, left, h), self.head)
            if right < r:
                self.head = self.__insert((right, r, h), self.head)

        self.max_height = max(self.max_height, new_height)
        return self.max_height


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        result = []
        bst = BST()

        for left, length in positions:
            result.append(bst.add(left, left + length, length))

        return result
