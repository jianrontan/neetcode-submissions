class Solution:
    def toIndex(self, c: chr) -> int:
        return ord(c) - 97

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashChars = {}
        for anagram in strs:
            numChars = [0] * 26
            for char in anagram:
                numChars[self.toIndex(char)] += 1
            tupleNumChars = tuple(numChars)
            if tupleNumChars not in hashChars:
                hashChars[tupleNumChars] = []
            hashChars[tupleNumChars].append(anagram)
        res = []
        for key in hashChars:
            res.append(hashChars[key])
        return res