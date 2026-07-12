class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        comp = 0
        for i in range(1, len(nums)):
            swap = comp + (i * k) % len(nums)
            if swap == comp:
                comp += 1
                swap += 1
                continue
            temp = nums[swap]
            nums[swap] = nums[comp]
            nums[comp] = temp