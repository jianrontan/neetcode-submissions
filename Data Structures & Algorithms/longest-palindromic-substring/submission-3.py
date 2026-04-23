class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLen = 0
        self.resLeft, self.resRight = 0, 0

        def find(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    if self.maxLen < (right - left + 1):
                        self.maxLen = right - left + 1
                        self.resLeft, self.resRight = left, right
                    left -= 1
                    right += 1

        for i in range(len(s)):
            left, right = i - 1, i + 1
            find(left, right)
            left, right = i - 1, i
            find(left, right)
        
        return s[self.resLeft:self.resRight+1]