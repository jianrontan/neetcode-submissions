class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def cIdx(char):
            return ord(char) - 97

        size = len(s1)
        target = [0 for _ in range(26)]
        for char in s1:
            target[cIdx(char)] += 1
        cur = [0 for _ in range(26)]

        for i in range(len(s2)):
            char = s2[i]
            if i < size:
                cur[cIdx(char)] += 1
            else:
                removal = s2[i - size]
                cur[cIdx(removal)] -= 1
                cur[cIdx(char)] += 1
            if cur == target:
                return True
        
        return False