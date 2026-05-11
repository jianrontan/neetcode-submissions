# aabbcdeedc
# a a b b c d e e d c
# a a bb c d e e d c
# a a b b c d ee d c
# a a b b c deed c
# a a b b cdeedc
# aa b b c d e e d c
# aa bb c d e e d c
# aa bb c d ee d c
# aa bb c deed c

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def isPalindrome(string):
            print(string)
            for i in range(len(string) // 2):
                if string[i] != string[len(string) - 1 - i]:
                    return False
            return True
        
        def split(i, j):
            if i == len(s):
                res.append(temp[:])
                return
            if j >= len(s):
                return
            # don't cut
            split(i, j + 1)
            # if palindrome, we add to temp
            if isPalindrome(s[i:j+1]):
                temp.append(s[i:j+1])
                split(j + 1, j + 1)
                temp.pop()
        
        split(0, 0)
        
        return res