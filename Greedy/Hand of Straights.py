class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        groupCount = len(hand) // groupSize
        count = 0
        while len(hand) != 0:
            card = hand.pop(0)
            size = 1
            i = 0
            while size != groupSize and i < len(hand):
                if hand[i] == card:
                    i += 1
                elif hand[i] == card + 1:
                    card = hand.pop(i)
                    size += 1
                else:
                    return False
            count += 1

        return count == groupCount

solution = Solution()
hand = [1,2,3,6,2,3,4,7,8]
print(solution.isNStraightHand(hand, 3))