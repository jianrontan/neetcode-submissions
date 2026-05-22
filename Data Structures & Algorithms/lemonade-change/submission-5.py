class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            if bill == 10:
                if fives < 1:
                    return False
                fives -= 1
                tens += 1
            if bill == 20:
                if fives < 1:
                    return False
                if tens < 1 and fives < 3:
                    return False
                if tens > 0:
                    fives -= 1
                    tens -= 1
                else:
                    fives -= 3
            
        return True