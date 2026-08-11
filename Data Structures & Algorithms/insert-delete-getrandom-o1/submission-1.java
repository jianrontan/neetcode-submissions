class RandomizedSet {
    Random rand;
    Map<Integer, Integer> valIn;
    List<Integer> list;

    public RandomizedSet() {
        this.rand = new Random();
        this.valIn = new HashMap<>();
        this.list = new ArrayList<>();
    }
    
    public boolean insert(int val) {
        boolean present = this.valIn.containsKey(val);
        if (!present) {
            this.list.add(val);
            this.valIn.put(val, this.list.size() - 1);
        }
        return !present;
    }
    
    public boolean remove(int val) {
        boolean present = this.valIn.containsKey(val);
        if (present) {
            int idx = this.valIn.get(val);
            this.list.set(idx, this.list.get(this.list.size() - 1));
            this.valIn.put(this.list.get(idx), idx);
            this.list.remove(this.list.size() - 1);
            this.valIn.remove(val);
        }
        return present;
    }
    
    public int getRandom() {
        return this.list.get(this.rand.nextInt(this.list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */