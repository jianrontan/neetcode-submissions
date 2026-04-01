class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        maxCount = 0
        l = 0
        for r, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            maxCount = max(counts[char], maxCount)
            if (r - l + 1) > maxCount + k:
                counts[s[l]] -= 1
                l += 1
        return len(s) - l