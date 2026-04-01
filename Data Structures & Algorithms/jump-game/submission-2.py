class Solution:
    def findJumps(self, nums: List[int], cur: int, target: int, res: int) -> int:
        print(" ")
        print("cur: ", cur)
        print("nums[cur]: ", nums[cur])
        if cur == target:
            return 1
        if cur < len(nums):
            for i in range(nums[cur]):
                nextId = cur + i + 1
                if nextId > target:
                    print("nextId > target: ", nextId, " from: ", cur)
                    return 0
                elif nextId < target:
                    print("nextId < target: ", nextId, " from: ", cur)
                    res += self.findJumps(nums, nextId, target, res)
                else:
                    print("nextId == target", nextId)
                    return 1
            return res
        else:
            print("terminated at cur >= len(nums)")
            return 0     

    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        cur = 0
        res = self.findJumps(nums, cur, target, 0)
        print(" ")
        print("res: ", res)
        if res > 0:
            return True
        else:
            return False