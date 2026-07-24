class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in dct:
                return [dct[difference], i]

            else:
                dct[nums[i]] = i
        