class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapNums = {}
        lenNums = len(numbers)
        for i in range(lenNums):
            if numbers[i] not in mapNums:
                mapNums[numbers[i]] = i
        for i in range(lenNums):
            comp = target - numbers[i]
            if comp in mapNums and i != mapNums[comp]:
                if i < mapNums[comp]:
                    return [i+1,mapNums[comp]+1]
                else:
                    return [mapNums[comp]+1,i+1]