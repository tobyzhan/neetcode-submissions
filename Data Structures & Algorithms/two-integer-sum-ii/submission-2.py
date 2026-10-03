class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointers, sorted array, o(n) time, o(1) space
        #dont need hash map since its already sorted, hash map takes o(n) space

        l = 0 
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target and l < r: 
                return [l + 1, r + 1]
            
            if numbers[l] + numbers[r] > target:
                r -= 1
            
            if numbers[l] + numbers[r] < target:
                l += 1
            
        
        return []

        
        