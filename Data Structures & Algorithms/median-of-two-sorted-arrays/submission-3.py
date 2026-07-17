class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) >= len(nums2):
            small, big = nums2, nums1
        else:
            small, big = nums1, nums2

        half = (len(nums1) + len(nums2)) // 2

        left, right = 0, len(small)
        
        while True:
            i = (left + right) // 2
            j = half - i

            sLeft = small[i - 1] if i > 0 else float('-inf')
            sRight = small[i] if i < len(small) else float('inf')
            bLeft = big[j - 1] if j > 0 else float('-inf')
            bRight = big[j] if j < len(big) else float('inf')

            if sLeft > bRight:
                # small's left more than big's right, took too little from big, shift left
                right = i
            elif bLeft > sRight:
                # big's left more than small's right, took too little from small, shift right
                left = i + 1
            else:
                break
        
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (max(sLeft, bLeft) + min(sRight, bRight)) / 2
        else:
            return min(sRight, bRight)