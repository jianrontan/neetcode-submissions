class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        last = [1]
        for i in range(1, numRows):
            next = [1]
            for j in range(1, i):
                next.append(last[j - 1] + last[j])
            next.append(1)
            res.append(next)
            last = next
        return res