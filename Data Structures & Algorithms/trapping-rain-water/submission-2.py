class Solution:
    def trap(self, height: List[int]) -> int:
        lenH = len(height)
        if lenH <= 2:
            return 0
        res, left, right = 0, 0, lenH - 1
        maxLeft, maxRight = height[left], height[right]
        while left < right:
            maxLeft = max(height[left], maxLeft)
            maxRight = max(height[right], maxRight)
            if maxLeft >= maxRight:
                right -= 1
                res += max(min(maxLeft, maxRight) - height[right], 0)
            elif maxRight > maxLeft:
                left += 1
                res += max(min(maxLeft, maxRight) - height[left], 0)
        return res