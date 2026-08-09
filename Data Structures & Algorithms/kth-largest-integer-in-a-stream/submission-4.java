class KthLargest {
    PriorityQueue<Integer> heap;
    int k;
    int[] nums;

    public KthLargest(int k, int[] nums) {
        this.heap = new PriorityQueue<>();
        this.k = k;
        this.nums = nums;
        for (int num : nums) {
            this.heap.offer(num);
        }
        while (this.heap.size() > this.k) {
            this.heap.poll();
        }
    }
    
    public int add(int val) {
        if (this.heap.size() == 0) {
            this.heap.offer(val);
        } else if (this.heap.size() < k) {
            this.heap.offer(val);
        } else if (this.heap.peek() < val) {
            this.heap.poll();
            this.heap.offer(val);
        }
        return this.heap.peek();
    }
}
