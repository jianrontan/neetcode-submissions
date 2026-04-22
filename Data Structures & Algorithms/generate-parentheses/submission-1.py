# 1: ()
# 2: ()(), (()) - adjacent and outside
# 3: ()()(), (())(), ()(()) - adjacent
#    ((())), (()())  - outside

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        combis = set()
        hi = n-1
        while hi >= 0:
            prevHi = self.generateParenthesis(hi)
            prevLo = self.generateParenthesis(n - hi - 1)
            for combiHi in prevHi:
                for combiLo in prevLo:
                    combis.add("(" + combiLo + ")" + combiHi)
            hi -= 1
        return list(combis)