from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            
            while dq and i - dq[0] >= k:
                dq.popleft()
            
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res