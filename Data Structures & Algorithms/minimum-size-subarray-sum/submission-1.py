class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0]

        cur = 0
        for num in nums:
            cur += num
            prefix.append(cur)

        res = float('inf')
        for i in range(len(prefix)):
            left, right = i, len(prefix) - 1
            while left <= right:
                mid = (left + right) // 2
                if prefix[mid] - prefix[i] >= target:
                    right = mid - 1
                    res = min(res, mid - i)
                else:
                    left = mid + 1
        
        return 0 if res == float('inf') else res