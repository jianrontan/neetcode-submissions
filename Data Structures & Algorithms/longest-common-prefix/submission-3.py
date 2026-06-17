class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start = strs[0]

        if len(start) < 1:
            return ""

        res = ""
        for i in range(len(start)):
            for string in strs:
                if i >= len(string) or start[i] != string[i]:
                    return res
            res += start[i]
        
        return res