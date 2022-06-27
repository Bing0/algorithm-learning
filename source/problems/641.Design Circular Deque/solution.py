# Use Array
class MyCircularDeque:

    def __init__(self, k: int):
        self.array = [0] * (k + 1)
        self.head = 0
        self.tail = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head > 0:
            self.head -= 1
        else:
            self.head = self.capacity
        self.array[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.array[self.tail] = value
        if self.tail < self.capacity:
            self.tail += 1
        else:
            self.tail = 0
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.head < self.capacity:
            self.head += 1
        else:
            self.head = 0
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.tail > 0:
            self.tail -= 1
        else:
            self.tail = self.capacity
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        if self.tail == 0:
            return self.array[self.capacity]
        else:
            return self.array[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        if self.head <= self.tail:
            return self.tail == 0 and self.tail == self.capacity
        else:
            return self.tail + 1 == self.head

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


# Use List
class Node:
    def __init__(self, value: int = 0, prev: "Node" = None, next: "Node" = None, ):
        self.value = value
        self.next = next
        self.prev = prev


class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_length = k
        self.count = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.count == self.max_length:
            return False

        new_node = Node(value, self.head, self.head.next)
        self.head.next = new_node
        new_node.next.prev = new_node
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.count == self.max_length:
            return False

        new_node = Node(value, self.tail.prev, self.tail)
        self.tail.prev = new_node
        new_node.prev.next = new_node
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False

        to_delete = self.head.next
        self.head.next = to_delete.next
        to_delete.next.prev = self.head
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False

        to_delete = self.tail.prev
        to_delete.prev.next = self.tail
        self.tail.prev = to_delete.prev
        self.count -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.count == 0:
            return -1
        return self.head.next.value

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.count == 0:
            return -1
        return self.tail.prev.value

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.count == self.max_length

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
