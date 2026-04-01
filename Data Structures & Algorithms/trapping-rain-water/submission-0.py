class Solution:
    def trap(self, height: List[int]) -> int:
        lenH = len(height)
        if lenH <= 2:
            return 0
        maxLeft = height[0]
        leftMax = [maxLeft]
        for i in range(1, lenH):
            maxLeft = max(height[i], maxLeft)
            leftMax.append(maxLeft)
        maxRight = height[-1]
        rightMax = [maxRight]
        for i in range(lenH - 1, -1, -1):
            maxRight = max(height[i], maxRight)
            rightMax.append(maxRight)
        rightMax.reverse()

        res = 0
        for i in range(lenH):
            res += min(leftMax[i], rightMax[i]) - height[i]
        
        return res