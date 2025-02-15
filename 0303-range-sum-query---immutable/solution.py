class NumArray:

    def __init__(self, nums: List[int]):
        self.num = [0] * len(nums)
        self.total = 0
        for i in range(len(nums)):
            self.total += nums[i]
            self.num[i] = self.total
        # print(self.num)


    def sumRange(self, left: int, right: int) -> int:
        if left == 0: 
            return self.num[right]
        return self.num[right] - self.num[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
