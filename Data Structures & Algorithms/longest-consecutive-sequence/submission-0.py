class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            unique.add(num)
        
        visited = set()
        def consecutive(n):
            if n in visited or n not in unique:
                return 0
            visited.add(n)
            up = consecutive(n + 1)
            down = consecutive(n - 1)
            return 1 + up + down
        
        res = 0
        for num in nums:
            cur = consecutive(num)
            res = max(res, cur)
        
        return res