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
            print(" ")
            print("char: ", char)
            if char in chars:
                minIdx = max(chars[char] + 1, minIdx)
                print("char in hashset minidx: ", minIdx)
            chars[char] = i
            print("chars[char]: ", i)
            print("i - minidx: ", i-minIdx)
            if i - minIdx > res:
                res = i - minIdx
            print("res: ", res + 1)
        return res + 1