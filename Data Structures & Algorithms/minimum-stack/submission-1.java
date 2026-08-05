class MinStack {
    class Node {
        int value;
        int min;

        public Node(int value, int min) {
            this.value = value;
            this.min = min;
        }
    }

    List<Node> stack;
    int min;

    public MinStack() {
        this.stack = new ArrayList<>();
        this.min = Integer.MAX_VALUE;
    }
    
    public void push(int value) {
        stack.add(new Node(value, this.min));
        this.min = Math.min(value, this.min);
    }
    
    public void pop() {
        Node top = this.stack.get(this.stack.size() - 1);
        this.min = top.min;
        this.stack.remove(this.stack.size() - 1);
    }
    
    public int top() {
        return this.stack.get(this.stack.size() - 1).value;
    }
    
    public int getMin() {
        return this.min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(value);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */