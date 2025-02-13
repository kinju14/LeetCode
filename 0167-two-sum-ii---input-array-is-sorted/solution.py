class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2: return [1, 2]
        i, j = 0, len(numbers) - 1
        while True:
            val = target - numbers[i]

            while numbers[j] > val:
                j -= 1
            
            if numbers[j] == val:
                return [i+1, j+1]
            
            i += 1


        # while i<j:
        #     val = target - numbers[j]
        #     while numbers[i] < val:
        #         i += 1
        #     if numbers[i] == val:
        #         return [i+1, j+1]
        #     j -= 1

        
