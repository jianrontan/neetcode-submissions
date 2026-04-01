class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        keyNode = self.cache[key]
        prevNode = keyNode.prev
        nextNode = keyNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
        headNext = self.head.next
        headNext.prev = keyNode
        keyNode.next = headNext
        keyNode.prev = self.head
        self.head.next = keyNode
        return keyNode.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            new = ListNode(key, value)
            if self.head.next == None and self.tail.prev == None:
                self.head.next = new
                self.tail.prev = new
                new.next = self.tail
                new.prev = self.head
            else:
                curFront = self.head.next
                self.head.next = new
                curFront.prev = new
                new.next = curFront
                new.prev = self.head
            self.cache[key] = new
            if self.count >= self.capacity:
                evict = self.tail.prev
                self.cache.pop(evict.key)
                newPrev = evict.prev
                newPrev.next = self.tail
                self.tail.prev = newPrev
            else:
                self.count += 1
        else:
            keyNode = self.cache[key]
            keyNode.val = value
            prevNode = keyNode.prev
            nextNode = keyNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            headNext = self.head.next
            headNext.prev = keyNode
            keyNode.next = headNext
            keyNode.prev = self.head
            self.head.next = keyNode

        
class ListNode:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None