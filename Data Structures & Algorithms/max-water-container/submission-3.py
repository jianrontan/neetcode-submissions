class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left, right = 0, len(heights) - 1

        while left < right:
            leftBar = heights[left]
            rightBar = heights[right]
            res = max(res, (right - left) * min(leftBar, rightBar))
            
            if leftBar > rightBar:
                right -= 1
            elif leftBar < rightBar:
                left += 1
            else:
                left += 1

        return res