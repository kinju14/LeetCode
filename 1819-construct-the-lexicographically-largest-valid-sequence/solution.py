class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0] * (2 * n -1)
        placed = set()

        def lexValid(idx: int):
            if idx == len(result):
                return True

            for num in range(n, 0, -1):
                if num in placed:
                    continue
                if num > 1 and (idx+num >= len(result) or result[idx+num] != 0):
                    continue
                
                placed.add(num)
                result[idx] = num
                if num != 1:
                    result[idx+num] = num
                
                nextIdx = idx+1
                while nextIdx < len(result) and result[nextIdx]:
                    nextIdx += 1

                if lexValid(nextIdx):
                    return True

                placed.remove(num)
                result[idx] = 0
                if num != 1:
                    result[idx+num] = 0
            
            return False
        
        lexValid(0)
        return result
