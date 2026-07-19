class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letters = {}
        for i, ch in enumerate(order):
            letters[ch] = i
        
        prev = words[0]
        for i in range(1, len(words)):
            cur = words[i]
            for j in range(min(len(cur), len(prev))):
                if letters[cur[j]] < letters[prev[j]]:
                    return False
                elif letters[cur[j]] > letters[prev[j]]:
                    break
            else:
                if len(prev) > len(cur):
                    return False
            
            prev = cur
        
        return True