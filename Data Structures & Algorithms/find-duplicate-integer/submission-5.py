#  0  1  2  3  4
# [1, 3, 4, 2, 2]

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while True:
            if slow == fast:
                collision = slow
                break
            else:
                slow = nums[slow]
                fast = nums[nums[fast]]

        start, collision = 0, collision
        while True:
            if start == collision:
                return start
            else:
                start = nums[start]
                collision = nums[collision]