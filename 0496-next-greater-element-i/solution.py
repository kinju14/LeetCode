class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict()
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                num = stack.pop()
                d[num] = n
            stack.append(n)
        # print(d)

        res = []
        for n in nums1:
            res.append(d.get(n, -1))
        
        return res


