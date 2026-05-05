class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += 1
            left, right = i, i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
                else:
                    break
            left, right = i - 1, i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
                else:
                    break
        return res