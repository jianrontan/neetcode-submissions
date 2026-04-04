class Solution:
    def isHappy(self, n: int) -> bool:
        strN = str(n)
        history = set()
        cur = 0
        while True:
            print(" ")
            print("num:", strN)
            for i in strN:
                cur += int(i) * int(i)
            print("cur:", cur)
            if cur not in history:
                history.add(cur)
            else:
                return False
            print("history:", history)
            if cur == 1:
                return True
            strN = str(cur)
            cur = 0