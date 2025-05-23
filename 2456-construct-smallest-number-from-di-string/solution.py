class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []

        for i in range(len(pattern) + 1):
            stack.append(i+1)

            while stack and (i == len(pattern) or pattern[i] == 'I'):
                result.append(str(stack.pop()))

        return ''.join(result)


