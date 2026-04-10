from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = {}
        have = {}
        l = 0
        resL, resR = -1, 1000
        for char in t:
            need[char] = need.get(char, 0) + 1
        needCount, haveCount = len(need), 0

        for r, char in enumerate(s):
            if char in need:
                have[char] = have.get(char, 0) + 1
                if have[char] == need[char]:
                    haveCount += 1
                while l <= r and haveCount == needCount:
                    if resR - resL > r - l:
                        resL, resR = l, r
                    if s[l] in have:
                        if have[s[l]] == need[s[l]]:
                            haveCount -= 1
                        have[s[l]] -= 1
                    l += 1
        if resL != -1:
            return s[resL:resR+1]
        else:
            return ""