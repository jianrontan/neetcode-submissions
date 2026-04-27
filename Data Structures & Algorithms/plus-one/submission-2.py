class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        if digits[-1] == 10:
            digits[-1] = 0
            carry = 1
        i = -2
        while carry == 1 and i >= -len(digits):
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
            i -= 1
        if carry == 1:
            return [1, 0] + digits[1:]
        return digits