class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        isArithmetic = True
        n = len(arr)
        arr = sorted(arr)
        diff = arr[0] - arr[1]
        for i in range(2, n):
            if (arr[i-1] - arr[i]) != diff:
                return False
            
        return True
