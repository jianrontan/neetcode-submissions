class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            lenS = len(s)
            res += str(lenS) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        numStr, num = "", 0
        i = 0
        while i < len(s):
            if s[i] == "#":
                num = int(numStr)
                res.append(s[i + 1:i + 1 + num])
                i = i + 1 + num
                numStr, num = "", 0
            else:
                numStr += s[i]
                i += 1
        return res