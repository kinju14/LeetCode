class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                i = stack.pop(-1)
                temp_s = ''
                while i != '(':
                    temp_s = temp_s + i
                    i = stack.pop(-1)
                for _ in temp_s:
                    stack.append(_)
        return ''.join(stack)
