# ABCDEFGHIJK
# ACEGIK
# BDFHJ

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        zigZag = ["" for _ in range(numRows)]
        r = 0
        step = 1
        for ch in s:
            zigZag[r] += ch
            if r == 0:
                step = 1
            elif r == numRows - 1:
                step = -1
            r += step
        
        return "".join(zigZag)