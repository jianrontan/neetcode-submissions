class LRUCache {

    class Node {
        int key;
        int value;
        Node next;
        Node prev;

        public Node(int key, int value, Node next, Node prev) {
            this.key = key;
            this.value = value;
            this.next = next;
            this.prev = prev;
        }
    }

    Map<Integer, Node> map;
    Node head;
    Node tail;
    int count;
    int capacity;

    public LRUCache(int capacity) {
        this.map = new HashMap<>();
        this.head = new Node(0, 0, null, null);
        this.tail = new Node(0, 0, null, this.head);
        this.head.next = this.tail;
        this.count = 0;
        this.capacity = capacity;
    }
    
    public int get(int key) {
        // look up map for key
        // get the node
        Node node = this.map.get(key);
        if (node == null) {
            return -1;
        }
        // remove the node
        this.removeNode(node);
        // stitch node to the front (head)
        this.addToFront(node);
        // return the value
        return node.value;
    }
    
    public void put(int key, int value) {
        // if not key in map
        if (!this.map.containsKey(key)) {
            // add to count
            this.count++;
            // if count > capacity
            if (this.count > this.capacity) {
                // evict node from the back (tail)
                Node curBack = this.tail.prev;
                this.removeNode(curBack);
                // remove back node from map
                map.remove(curBack.key);
                // minus from count
                this.count--;
            }
        // else if key in map
        } else {
            // get the node
            Node node = this.map.get(key);
            // remove the node
            this.removeNode(node);
        }
        // stitch node to the front (head)
        Node newNode = new Node(key, value, null, null);
        this.addToFront(newNode);
        // add to map
        this.map.put(key, newNode);
    }

    public void removeNode(Node node) {
        Node prv = node.prev;
        Node nxt = node.next;
        prv.next = nxt;
        nxt.prev = prv;
        node.next = null;
        node.prev = null;
    }

    public void addToFront(Node node) {
        Node curFront = this.head.next;
        this.head.next = node;
        curFront.prev = node;
        node.prev = this.head;
        node.next = curFront;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */