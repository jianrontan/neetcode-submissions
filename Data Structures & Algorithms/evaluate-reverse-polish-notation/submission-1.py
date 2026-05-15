class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(" ")
            print("stack:", stack)
            if token == "+":
                secondOp = int(stack.pop())
                firstOp = int(stack.pop())
                stack.append(firstOp + secondOp)
            elif token == "-":
                secondOp = int(stack.pop())
                firstOp = int(stack.pop())
                stack.append(firstOp - secondOp)
            elif token == "*":
                secondOp = int(stack.pop())
                firstOp = int(stack.pop())
                stack.append(firstOp * secondOp)
            elif token == "/":
                secondOp = int(stack.pop())
                firstOp = int(stack.pop())
                stack.append(firstOp / secondOp)
            else:
                stack.append(token)
        return int(stack[0])