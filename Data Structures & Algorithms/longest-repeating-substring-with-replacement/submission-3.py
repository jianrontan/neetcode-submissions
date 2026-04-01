# ABCDCCDCABCDAADCBB 3
# ABDC|C -> AAAA -> 4
# BCDCC -> 
# CDCCDCA|B -> CCCCCCC -> 7
# DCCDCABC ->
# CCDCABCD ->
# CDCABCDA ->
# DCABCDAA ->
# CABCDAAD ->
# ABCDAADC ->
# BCDAADCB ->
# CDAADCBB ->
# return 7

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lenS = len(s)
        counts = {}
        maxCount = 0
        l = 0
        for i in range(lenS):
            char = s[i]
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
            if counts[char] > maxCount:
                maxCount = counts[char]
            if (i - l + 1) > maxCount + k:
                counts[s[l]] -= 1
                l += 1
        return lenS - l