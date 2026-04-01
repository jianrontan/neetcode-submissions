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
            print(" ")
            print("window: ", s[l:i+1])
            print("cur char: ", char)
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
            print("new counts: ", counts)
            print("maxCount: ", maxCount)
            if counts[char] > maxCount:
                print("maxCount updated to: ", counts[char])
                maxCount = counts[char]
            else:
                if (i - l + 1) <= maxCount + k:
                    print("window size <= most frequent + k")
                    print(i - l + 1, " <= ", maxCount + k)
                else:
                    print("left += 1")
                    print("new counts: ", counts)
                    counts[s[l]] -= 1
                    l += 1
        return maxCount + min(k, lenS - maxCount)