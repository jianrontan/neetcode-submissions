class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        for i in range(n):
            num = nums[i]
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        # freq: {7: 2}

        buckets = [[] for _ in range(n + 1)]
        print(buckets)
        for key in freq:
            # bucket = 2
            bucket = freq[key]
            # buckets[2]
            buckets[bucket].append(key)
            # print(buckets)

        res = []
        for i in range(n):
            lenB = len(buckets[n - i])
            for j in range(lenB):
                res.append(buckets[n - i][j])
            if len(res) == k:
                return res
        return res