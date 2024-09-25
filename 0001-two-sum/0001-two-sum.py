class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueMap = {}
        for index, n in enumerate(nums):
            difference = target - n
            if difference in valueMap:
                return [valueMap[difference], index]
            valueMap[n] = index
        return
        