class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0
            
        def recursion(target: int, square: str, total: int, idx: int):
            if target == total and idx == len(square):
                return True

            for j in range(idx, len(square)):
                if recursion(target, square, total + int(square[idx:j+1]), j+1):
                    return True
            
            return False
            
        for i in range(1, n+1):
            num = i*i
            if recursion(i, str(num), 0, 0):
                result += num
        
        return result
