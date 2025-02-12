class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        d = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in d:
                if stack and stack[-1] == d[ch]:
                    stack.pop()
                else: return False
            else:
                stack.append(ch)

        return True if not stack else False
