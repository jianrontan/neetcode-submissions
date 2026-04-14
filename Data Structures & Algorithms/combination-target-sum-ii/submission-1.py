class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, curr, total):
            if total == target:
                res.append(curr[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()
        
        backtrack(0, [], 0)
        return res