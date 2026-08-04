class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {

        // replace with binary search later
        int idx = -1, diff = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length; i++) {
            if (Math.abs(arr[i] - x) < diff) {
                diff = Math.abs(arr[i] - x);
                idx = i;
            }
        }

        int left = idx - 1, right = idx + 1;
        for (int i = 0; i < k - 1; i++) {
            if (0 <= left && right < arr.length) {
                if (Math.abs(arr[left] - x) <= Math.abs(arr[right] - x)) {
                    left -= 1;
                } else {
                    right += 1;
                }
            } else if (0 <= left) {
                left -= 1;
            } else if (right < arr.length) {
                right += 1;
            }
        }

        List<Integer> res = new ArrayList<>();
        left = Math.max(0, left + 1);
        right = Math.min(arr.length - 1, right - 1);
        for (int i = left; i <= right; i++) {
            res.add(arr[i]);
        }
        return res;
    }
}