class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for op in logs:
            if op == './': pass
            elif op == '../':
                if count > 0: count -=1 
            else: count +=1
        return count

