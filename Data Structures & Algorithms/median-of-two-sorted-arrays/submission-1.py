# [0, 3, 4, 8] [1, 2, 5, 6, 7, 9]

# [1, 2, 4, 9] [0, 3, 5, 6, 7, 8]

# [1, 2 | 4, 4] [0, 3, 5 | 6, 7, 8]
# left1 = 2 elems, left2 = 3 elems
# not valid partition
# move A partition right and adjust B partition left accordingly

# [0, 1, 2, 3, 4, 4, 5, 6, 7, 8]
# [1, 2, 4 | 4] [0, 3 | 5, 6, 7, 8]
# left = 3 + 2 = 5 elems, right = 1 + 4 = 5 elems
# valid partition

# median = max of left partition + min of right partition
# = (4 + 5) / 2 = 4.5

# [1,2,3,7] [4,5,6]
#      ^       ^
#        ^  ^

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        half = (m + n) // 2
        lo, hi = 0, m
        par1 = (lo + hi) // 2
        par2 = half - par1
        print("half, start par1 & par2: ", half, par1, par2)
        while lo <= hi:
            par1 = (lo + hi) // 2
            par2 = half - par1
            # left array left partition > right array right partition
            l1 = nums1[par1 - 1] if par1 > 0 else float('-inf')
            r1 = nums1[par1]     if par1 < m else float('inf')
            l2 = nums2[par2 - 1] if par2 > 0 else float('-inf')
            r2 = nums2[par2]     if par2 < n else float('inf')
            print(" ")
            print("left array left partition: ", l1)
            print("right array right partition: ", r2)
            print("left array right partition: ", r1)
            print("right array left partition: ", l2)
            if l1 > r2:
                hi = par1 - 1
            # right array left partition > left array right partition
            elif l2 > r1:
                lo = par1 + 1
            else:
                if (m + n) % 2 == 1:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
