class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pt1, pt2 = 0, 0
        res = ""

        while pt1 < len(word1) or pt2 < len(word2):
            if pt1 < len(word1):
                res += word1[pt1]
                pt1 += 1
            if pt2 < len(word2):
                res += word2[pt2]
                pt2 += 1
        
        return res