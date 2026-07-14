class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hands = {}

        for n in hand:
            if n not in hands:
                hands[n] = 0
            hands[n] += 1
        
        for n in sorted(hands):
            if hands[n] > 0:
                need = hands[n]
                for i in range(n, n + groupSize):
                    if i in hands and hands[i] >= need:
                        hands[i] -= need
                    else:
                        return False
        
        return True