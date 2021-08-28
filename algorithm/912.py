class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = LinkedNode(0, 0)
        self.tail = LinkedNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if not key in self.cache.keys():
            return -1
        node = self.cache.get(key)
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            node = self.cache.get(key)
            node.value = value
            self.cache[key] = node
            self.move_to_head(node)
        else:
            node = LinkedNode(key, value)
            self.add_head(node)
            self.size += 1
            self.cache[key] = node
            if self.size > self.capacity:
                tail = self.remove_tail()
                self.cache.pop(tail.key)
                self.size -= 1

    def move_to_head(self, node: LinkedNode):
        self.remove(node)
        self.add_head(node)

    def remove(self, node: LinkedNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_head(self, node: LinkedNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_tail(self) -> LinkedNode:
        node = self.tail.prev
        self.remove(node)
        return node
