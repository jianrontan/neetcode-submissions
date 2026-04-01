class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lenT = len(temperatures)
        stack = []
        res = [0 for _ in range(lenT)]
        for i in range(lenT):
            print(" ")
            print("---NEW ITERATION---")
            print("cur: ", temperatures[i])
            print("cur stack: ", stack)
            print(" ")
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                print("add to res: ", res, " + ", i - idx)
                res[idx] = i - idx
            stack.append(i)
            print(" ")
            print("new res: ", res)
            print("new stack: ", stack)
        print(" ")
        print("res: ", res)
        return res