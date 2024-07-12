class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if len(s) == 1:
            return 0            

        to_find = ['ab','ba'] if x>y else ['ba','ab']
        score = 0

        for ch in to_find:
            n = len(s)
            stack = [s[0]]
            i = 1
            while i < n:
                if len(stack) == 0:
                    stack.append(s[i])
                    continue
                if stack[-1] == ch[0] and s[i] == ch[1]:
                    if stack.pop() == 'b':
                        score += y
                    else:
                        score += x
                else:
                    stack.append(s[i])
                i += 1
            s = ''.join(stack)


        return score
        
