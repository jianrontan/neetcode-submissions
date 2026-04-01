class Solution:
    def getSum(self, a: int, b: int) -> int:
        num_bits = 11
        bits_a = []
        bits_b = []

        for bit_pos in range(num_bits - 1, -1, -1):
            bit_value_a = (a >> bit_pos) & 1
            bit_value_b = (b >> bit_pos) & 1
            bits_a.append(bit_value_a)
            bits_b.append(bit_value_b)
        
        bits_res = []
        carry = 0
        for bit_pos in range(num_bits - 1, -1, -1):
            cur_a = bits_a[bit_pos]
            cur_b = bits_b[bit_pos]
            if cur_a == 1 and cur_b == 1:
                if carry == 1:
                    bits_res.append(1)
                else:
                    bits_res.append(0)
                carry = 1
            elif cur_a == 0 and cur_b == 0:
                if carry == 1:
                    bits_res.append(1)
                else:
                    bits_res.append(0)
                carry = 0
            else:
                if carry == 1:
                    bits_res.append(0)
                    carry = 1
                else:
                    bits_res.append(1)
                    carry = 0

        bits_res.reverse()
        res = 0
        for bit in bits_res:
            res = (res << 1) | bit
        if res >> 10 == 0:
            return res
        else:
            return ~(res ^ 2047)