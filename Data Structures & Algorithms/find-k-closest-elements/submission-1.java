class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int left = 0, right = arr.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] >= x) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        int idx;
        if (right == 0) {
            idx = 0;
        } else if (right == arr.length) {
            idx = arr.length - 1;
        } else if (x - arr[right - 1] <= arr[right] - x) {
            idx = right - 1;
        } else {
            idx = right;
        }

        left = idx - 1;
        right = idx + 1;
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