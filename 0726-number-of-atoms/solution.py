class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        n = len(formula)
        d = {}
        i = 0

        def appendDictItemsToStack(stack):
            for k, v in d.items():
                stack.append(k)
                stack.append(v)
            return stack

        while i < n:
            curr_ch = formula[i]
            if i+1 < n and formula[i+1].islower():
                stack.append(curr_ch + formula[i+1])
                i += 1

            elif curr_ch == ')':
                mul_num = ''
                if i+1 < n and formula[i+1].isdigit(): 
                    while i+1 < n and formula[i+1].isdigit():
                        mul_num += formula[i+1]
                        i += 1
                    i -= 1
                    mul_num = int(mul_num)
                while len(stack) > 0:
                    ch = stack.pop()
                    if ch == '(':
                        if mul_num != '':
                            d.update((k, v * mul_num) for k, v in d.items())
                            i += 1
                        stack = appendDictItemsToStack(stack)
                        d = {}
                        break
                    if type(ch) == int or ch.isdigit():
                        if stack[-1] not in d:
                            d[stack[-1]] = int(ch)
                        else:
                            d[stack[-1]] += int(ch)
                        stack.pop()
                    elif ch not in d: d[ch] = 1
                    else: d[ch] += 1
                
            elif curr_ch.isdigit():
                temp_num = curr_ch
                while i+1 < n and formula[i+1].isdigit():
                    temp_num += formula[i+1]
                    i += 1
                stack.append(temp_num)
            
            else:
                stack.append(curr_ch)

            i += 1

        while len(stack) > 0:
            ch = stack.pop()
            if type(ch) == int or ch.isdigit():
                if stack[-1] in d:
                    d[stack[-1]] += int(ch)
                else:
                    d[stack[-1]] = int(ch)
                stack.pop()
            elif ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        d = sorted(d.items())
        s = ''
        for [k,v] in d:
            if v == 1:
                s += str(k)
            else:
                s += str(k) + str(v) 

        return s
        
