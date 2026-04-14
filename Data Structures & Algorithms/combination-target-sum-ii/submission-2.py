class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        cand_set = set()
        self.target = target
        self.res = []
        candidates.sort()
        self.candidates = candidates
        for i in range(len(candidates)):
            if candidates[i] in cand_set:
                continue
            cand_set.add(candidates[i])
            self.comb([candidates[i]], i + 1, candidates[i])
        return self.res

    def comb(self, comb: List[int], idx: int, total: int) -> None:
        if total == self.target:
            self.res.append(comb[:])
            return
        for i in range(idx, len(self.candidates)):
            if i > idx and self.candidates[i] == self.candidates[i - 1]:
                continue
            if total + self.candidates[i] > self.target:
                break
            comb.append(self.candidates[i])
            self.comb(comb, i + 1, total + self.candidates[i])
            comb.pop()