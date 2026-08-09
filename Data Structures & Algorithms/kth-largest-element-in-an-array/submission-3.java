class Solution {
    private void swap(int[] nums, int a, int b) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }

    public int findKthLargest(int[] nums, int k) {
        int target = nums.length - k;
        int left = 0, right = nums.length;
        Random rand = new Random();

        while (left < right) {
            int pivot = rand.nextInt(left, right);
            swap(nums, pivot, right - 1);

            int i = left, j = left;
            while (j < right - 1) {
                if (nums[j] < nums[right - 1]) {
                    swap(nums, i, j);
                    i++;
                }
                j++;
            }
            swap(nums, right - 1, i);
            if (i == target) {
                return nums[i];
            } else if (i < target) {
                left = i + 1;
            } else {
                right = i;
            }
        }
        return -1;
    }
}
