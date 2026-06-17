class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start = strs[0]

        if len(start) < 1:
            return ""

        res = ""
        for i in range(len(start)):
            prefix = start[:i + 1]
            for string in strs:
                if prefix != string[:i + 1]:
                    return res
            res = prefix
        
        return res