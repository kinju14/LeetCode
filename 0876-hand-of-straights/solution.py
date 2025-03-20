class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) % groupSize:
        #     return False

        countChars = Counter(hand)

        for n in sorted(countChars):
            while countChars[n]:
                count = 1
                countChars[n] -= 1
                while count < groupSize:
                    if not countChars[n+count]:
                        return False
                    countChars[n+count] -= 1
                    count += 1

        return True

