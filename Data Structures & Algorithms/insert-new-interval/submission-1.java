class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int start = newInterval[0], end = newInterval[1];

        int left = 0, right = intervals.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (intervals[mid][1] >= start) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        int startBoundary = left;

        left = 0;
        right = intervals.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (intervals[mid][0] > end) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        int endBoundary = left - 1;
        boolean overlap = false;
        if (startBoundary <= endBoundary) {
            overlap = true;
        }

        int size = intervals.length + 1;
        if (overlap) {
            size -= (endBoundary - startBoundary + 1);
        }
        int[][] res = new int[size][2];
        int k = 0;
        for (int i = 0; i < startBoundary; i++) {
            res[i][0] = intervals[i][0];
            res[i][1] = intervals[i][1];
            k++;
        }

        res[k][0] = overlap ? Math.min(intervals[startBoundary][0], start) : start;
        res[k][1] = overlap ? Math.max(intervals[endBoundary][1], end) : end;
        k++;
        
        for (int i = endBoundary + 1; i < intervals.length; i++) {
            res[k][0] = intervals[i][0];
            res[k][1] = intervals[i][1];
            k++;
        }

        return res;
    }
}
