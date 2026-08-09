class Solution {
    public int findKthLargest(int[] nums, int k) {
        int[] arr = new int[2001];
        for (int num : nums) {
            arr[num + 1000]++;
        }

        int count = 0;
        for (int i = arr.length - 1; i >= 0; i--) {
            count += arr[i];
            if (count >= k) {
                return i - 1000;
            }
        }
        return -1;
    }
}
