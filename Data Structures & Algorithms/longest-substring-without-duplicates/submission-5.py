class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenS = len(s)
        if lenS == 1:
            return 1
        elif lenS == 0:
            return 0

        chars = {}
        minIdx = 0
        res = 0
        for i in range(lenS):
            char = s[i]
            if char in chars:
                minIdx = max(chars[char] + 1, minIdx)
            chars[char] = i
            if i - minIdx > res:
                res = i - minIdx
        return res + 1