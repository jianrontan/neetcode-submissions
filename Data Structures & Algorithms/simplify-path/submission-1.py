class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for char in path:
            print(" ")
            print(char)
            print(stack)
            if char == "/":
                if len(stack) > 0 and stack[-1] == "..":
                    if len(stack) > 1:
                        stack.pop()
                    stack.pop()
                    stack.append("")
                elif len(stack) > 0 and stack[-1] == ".":
                    stack.pop()
                    stack.append("")
                elif len(stack) > 0 and stack[-1] == "":
                    continue
                else:
                    stack.append("")
            else:
                stack[-1] += char
        
        if len(stack) > 0 and stack[-1] == "..":
            if len(stack) > 1:
                stack.pop()
            stack.pop()
        elif len(stack) > 0 and stack[-1] == ".":
            stack.pop()
        elif len(stack) > 0 and stack[-1] == "":
            stack.pop()
        
        return "/" + "/".join(stack)