# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17, target: 10
# 1 2 3 4 5 6 7 8
# 9 10 11 12 13 14 15 16 17
# 9 10 11 12

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIdx = 0
        maxIdx = len(nums) - 1
        while True:
            print(" ")
            print("maxIdx: ", maxIdx)
            print("minIdx: ", minIdx)
            idx = (maxIdx + minIdx) // 2
            print("idx: ", idx ," is: ", nums[idx])
            if maxIdx == minIdx:
                if nums[maxIdx] == target:
                    return maxIdx
                else:
                    return -1
            if nums[idx] < target:
                minIdx = idx + 1
            elif nums[idx] > target:
                maxIdx = idx
            else:
                return idx