class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxSeq = 0
        seq = 0
        dct = {}

        for n in nums:
            dct[n] = 1
        
        for i in range(len(nums)):
            seq = 0
            nextNum = nums[i] 

            if nextNum - 1 not in dct.keys():
                while nextNum in dct.keys():
                    seq += 1
                    nextNum += 1
                
                if seq > maxSeq:
                    maxSeq = seq
        
        return maxSeq
            

            

        

        