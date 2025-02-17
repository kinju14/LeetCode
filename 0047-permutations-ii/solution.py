class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        count = dict(Counter(nums))
        print(count)
        perm = []

        def backtrack():
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                
                    backtrack()
                    count[n] += 1
                    perm.pop()
                    
        backtrack()
        return result
