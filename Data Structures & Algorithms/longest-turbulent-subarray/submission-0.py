class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        res = 1
        cur = 1

        increasing = None
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                if increasing == True:
                    cur += 1
                else:
                    cur = 2
                increasing = False
            elif arr[i] < arr[i + 1]:
                if increasing == False:
                    cur += 1
                else:
                    cur = 2
                increasing = True
            else:
                increasing = None
                cur = 1
            res = max(res, cur)
        
        return res