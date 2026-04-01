# 7 1 7 3 3 4  2  2  2
# 7 7 7 7 7 7  7  7  7
# 7 7 7 7 9 12 12 12 12
# 7 7 7 7 9 12 12 12 14

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lenH = len(heights)
        if lenH == 0:
            return 0
        elif lenH == 1:
            return heights[0]

        res = 0
        stack = []
        rightMin = [0 for _ in range(lenH)]
        leftMin = [0 for _ in range(lenH)]
        for i in range(lenH):
            cur = heights[i]
            while stack and cur < heights[stack[-1]]:
                idx = stack.pop()
                rightMin[idx] = i
            stack.append(i)
        while stack:
            idx = stack.pop()
            rightMin[idx] = lenH
        
        stack = []
        for i in range(lenH -1, -1, -1):
            cur = heights[i]
            while stack and cur < heights[stack[-1]]:
                idx = stack.pop()
                leftMin[idx] = i
            stack.append(i)
        while stack:
            idx = stack.pop()
            leftMin[idx] = -1
        
        res = 0
        for i in range(lenH):
            res = max(heights[i] * (rightMin[i] - leftMin[i] - 1), res)
        return res
