class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] == nums[1] and nums[1] == nums[2] and nums[2] == nums[0]:
            return "equilateral"
        elif nums[0] != nums[1] and nums[1] != nums[2] and nums[2] != nums[0]:
            if(nums[0]+nums[1] > nums[2] and nums[1]+nums[2] > nums[0] and nums[2]+nums[0] > nums[1]):
                return "scalene"
            else:
                return "none"
        else:
            if(nums[0]+nums[1] > nums[2] and nums[1]+nums[2] > nums[0] and nums[2]+nums[0] > nums[1]):
                return "isosceles"
            else:
                return "none"
        return "none"
