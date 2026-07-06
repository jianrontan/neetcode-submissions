class Node:
    def __init__(self, key=None, value=None, prv=None, nxt=None):
        self.key = key
        self.value = value
        self.prv= prv
        self.nxt = nxt

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node(prv=self.head)
        self.head.nxt = self.tail
        self.count = 0

    def insertFront(self, node: Node) -> None:
        nodeNxt = self.head.nxt
        self.head.nxt = node
        node.prv = self.head
        node.nxt = nodeNxt
        nodeNxt.prv = node

    def get(self, key: int) -> int:
        node = self.cache.get(key, -1)
        if node == -1:
            return -1
        nodeNxt = node.nxt
        node.prv.nxt = nodeNxt
        nodeNxt.prv = node.prv
        self.insertFront(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        self.count += 1
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            nodeNxt = node.nxt
            node.prv.nxt = nodeNxt
            nodeNxt.prv = node.prv
            self.count -= 1
        else:
            node = Node(key=key, value=value)
        if self.count > self.capacity:
            evict = self.tail.prv
            evict.prv.nxt = self.tail
            self.tail.prv = evict.prv
            self.cache.pop(evict.key)
            self.count -= 1
        self.insertFront(node)
        self.cache[key] = node