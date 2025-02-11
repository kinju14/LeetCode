class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # if len(part) > len(s): return s
        # partLen = len(part)
        # stack = [s[i] for i in range(partLen-1)]

        # for i in range(partLen-1, len(s)):
        #     stack.append(s[i])
        #     if s[i] == part[-1] and len(stack) >= partLen and ''.join(stack[-partLen:]) == part:
        #         count = partLen
        #         while count > 0:
        #             stack.pop()
        #             count -= 1
        
        # return ''.join(stack)

        while part in s:
            s = s.replace(part, "", 1)
        return s



