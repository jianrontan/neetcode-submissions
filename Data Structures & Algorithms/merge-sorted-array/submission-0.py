class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, write = m - 1, n - 1, m + n - 1

        while p1 >= 0 or p2 >= 0:
            if p1 >= 0 and p2 >= 0:
                nums1[write] = max(nums1[p1], nums2[p2])
                if nums1[p1] >= nums2[p2]:
                    p1 -= 1
                else:
                    p2 -= 1
                write -= 1
            elif p1 >= 0:
                nums1[write] = nums1[p1]
                p1 -= 1
                write -= 1
            elif p2 >= 0:
                nums1[write] = nums2[p2]
                p2 -= 1
                write -= 1