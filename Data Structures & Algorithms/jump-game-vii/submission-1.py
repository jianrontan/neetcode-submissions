class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        visitable = [False for _ in range(len(s))]
        visitable[0] = True
        count = 0

        for j in range(1, len(s)):
            if j - minJump >= 0 and visitable[j - minJump]:
                count += 1
            if j - maxJump - 1 >= 0 and visitable[j - maxJump - 1]:
                count -= 1
            visitable[j] = (s[j] == '0' and count > 0)
        
        return visitable[len(s) - 1]