class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == '+':
                right = stack.pop()
                stack.append(stack.pop() + right)

            elif ch == '-':
                right = stack.pop()
                stack.append(stack.pop() - right)

            elif ch == '*':
                right = stack.pop()
                stack.append(stack.pop() * right)

            elif ch == '/':
                right = stack.pop()
                stack.append(int(stack.pop() / right))
            else:
                stack.append(int(ch))
        
        return stack[0]
