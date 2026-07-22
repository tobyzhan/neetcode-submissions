class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}

        for num in nums:
            if num not in dct.keys():
                dct[num] = 1
            
        return len(dct.keys()) != len(nums)
        