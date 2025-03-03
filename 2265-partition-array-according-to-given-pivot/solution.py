class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s = []
        l = []
        c = 0

        for i in nums:
            if i < pivot:
                s.append(i)
            elif i > pivot:
                l.append(i)
            else:
                c += 1
        
        return s + [pivot] * c + l
