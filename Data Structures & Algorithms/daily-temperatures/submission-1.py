class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lenT = len(temperatures)
        stack = []
        for i in range(lenT):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                temperatures[idx] = i - idx
            stack.append(i)
        while stack:
            idx = stack.pop()
            temperatures[idx] = 0
        return temperatures