class Solution:
    def __init__(self):
        self.res = []

    def testSum(self, nums: List[int], target: int, combo: List[int], index: int):
        sumCombo = sum(combo)
        print(" ")
        if sumCombo == target:
            print("sumCombo == target: ", combo)
            self.res.append(combo)
        elif sumCombo < target:
            print("sumCombo < target: ", combo)
            print("min index: ", index)
            for i in range(index, len(nums)):
                comboCopy = combo.copy()
                comboCopy.append(nums[i])
                self.testSum(nums, target, comboCopy, i)
        print("sumCombo > target: ", combo)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        for index in range(len(nums)):
            print(" ")
            print("new testSum: ", nums[index])
            self.testSum(nums, target, [nums[index]], index)
        return self.res
        # # For each number
        # for i in range(len(nums)):
        #     num = nums[i]

        #     # Get max number of num without exceeding target
        #     nTests = target // num

        #     # Try out every multiple of num
        #     for j in range(nTests, 0, -1):
        #         # If target multiple of num
        #         if j * num == target:
        #             combo = [num] * j
        #             res.append(combo)
        #         # Find other combos
        #         else:
                    