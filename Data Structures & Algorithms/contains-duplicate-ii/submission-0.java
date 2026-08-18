class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {

        Deque<Integer> dq = new ArrayDeque<>();
        Set<Integer> set = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (set.size() >= k + 1) {
                int removal = dq.pollFirst();
                set.remove(removal);
            }
            if (!set.contains(nums[i])) {
                set.add(nums[i]);
                dq.offer(nums[i]);
            } else {
                return true;
            }
        }

        return false;
    }
}