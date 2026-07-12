class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            unique.add(num)
        
        res = 0
        for num in unique:
            if num - 1 not in unique:
                cur = num
                curCount = 0
                while cur in unique:
                    curCount += 1
                    cur += 1
                    res = max(res, curCount)
        
        return res