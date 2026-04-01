class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif not stack:
                return False
            elif char == ')':
                comp = stack.pop()
                if comp != '(':
                    return False
            elif char == '}':
                comp = stack.pop()
                if comp != '{':
                    return False
            elif char == ']':
                comp = stack.pop()
                if comp != '[':
                    return False
        if not stack:
            return True
        else:
            return False