class Solution:
    def isPalindrome(self, s: str) -> bool:
        testStr = ""
        for char in s:
            if char.isalnum():
                testStr += char.lower()

        lenStr = len(testStr)
        for i in range(lenStr // 2):
            if testStr[i] != testStr[lenStr - 1 - i]:
                print("left: ", testStr[i])
                print("right: ", testStr[lenStr - 1 - i])
                return False
        return True