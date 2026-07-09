class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        vals = {0: 1}
        count = 0
        res = 0
        for i in range(len(nums)):
            num = nums[i]
            count += num
            prefix.append(count)

            complement = count - k
            if complement in vals:
                res += vals[complement]
            
            if count not in vals:
                vals[count] = 0
            vals[count] += 1
        
        return res