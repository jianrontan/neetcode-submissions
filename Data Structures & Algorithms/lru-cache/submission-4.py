class Node:
    def __init__(self, key=None, value=None, prv=None, nxt=None):
        self.key = key
        self.value = value
        self.prv = prv
        self.nxt = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node()
        self.tail = Node(prv=self.head)
        self.head.nxt = self.tail
        self.capacity = capacity
        self.count = 0

    def get(self, key: int) -> int:
        node = self.cache.get(key, -1)
        if node != -1:
            node.prv.nxt = node.nxt
            node.nxt.prv = node.prv
            newSecond = self.head.nxt
            self.head.nxt = node
            node.prv = self.head
            node.nxt = newSecond
            newSecond.prv = node
            return node.value
        else:
            return node

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, -1)
        if node != -1:
            self.get(key)
            node.value = value
        else:
            self.count += 1
            if self.count > self.capacity:
                evictKey = self.tail.prv.key
                self.cache.pop(evictKey)
                self.tail.prv = self.tail.prv.prv
                self.tail.prv.nxt = self.tail
                self.count -= 1
            newNode = Node(key, value, self.head, self.head.nxt)
            self.head.nxt = newNode
            newNode.nxt.prv = newNode
            self.cache[key] = newNode