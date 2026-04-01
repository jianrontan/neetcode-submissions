class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        if lenS != lenT:
            return False
        hashS = {}
        hashT = {}
        for i in range(lenS):
            if s[i] not in hashS:
                hashS[s[i]] = 0
            hashS[s[i]] += 1
        for i in range(lenT):
            if t[i] not in hashT:
                hashT[t[i]] = 0
            hashT[t[i]] += 1
        for key in hashS:
            if key in hashS and key in hashT:
                if hashS[key] != hashT[key]:
                    return False
            else:
                return False
        return True