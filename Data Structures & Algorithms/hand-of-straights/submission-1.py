class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hands = {}

        for n in hand:
            if n not in hands:
                hands[n] = 0
            hands[n] += 1
        
        while hands:
            for n in hands:
                if n - 1 not in hands:
                    for i in range(n, n + groupSize):
                        if i not in hands:
                            return False
                        else:
                            hands[i] -= 1
                            if hands[i] == 0:
                                hands.pop(i)
                    break
        
        return True