class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque()
        res.append((digits[-1] + 1) % 10)
        carry = (digits[-1] + 1) // 10

        for n in digits[-2::-1]:
            res.appendleft((n + carry) % 10)
            carry = (n + carry) // 10

        if carry: res.appendleft(carry)

        return list(res)

