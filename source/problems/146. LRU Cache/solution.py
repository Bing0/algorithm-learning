class Node:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]

        # move to end
        self.remove(node)
        self.insert_at_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value

            # move to end
            self.remove(node)
            self.insert_at_end(node)
        else:
            node = Node()
            node.key = key
            node.value = value
            self.map[key] = node

            # insert to end
            self.insert_at_end(node)
            # delete
            if len(self.map) > self.capacity:
                first = self.head.next
                self.remove(first)
                del self.map[first.key]

    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def insert_at_end(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)