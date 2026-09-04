from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def addOne(numStr: str, idx: int) -> str:
            newNum = (int(numStr[idx]) + 1) % 10
            newChar = str(newNum)
            new = numStr[:idx] + newChar + numStr[idx+1:]
            return new
        
        def minusOne(numStr: str, idx:int) -> str:
            newNum = (int(numStr[idx]) - 1) % 10
            newChar = str(newNum)
            new = numStr[:idx] + newChar + numStr[idx+1:]
            return new
        
        visited = set()
        invalid = set(deadends)

        if "0000" in invalid:
            return -1
        
        queue = deque([("0000", 0)])
        while queue:
            num, steps = queue.popleft()
            if num == target:
                return steps
            for i in range(4):
                add = addOne(num, i)
                minus = minusOne(num, i)
                if add not in visited and add not in invalid:
                    visited.add(add)
                    queue.append((add, steps + 1))
                if minus not in visited and minus not in invalid:
                    visited.add(minus)
                    queue.append((minus, steps + 1))
        
        return - 1