class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0
        

        for num in num_set:

            if num - 1 not in num_set:
                seq = 1
                while num + seq in num_set:
                    seq += 1
            
                if seq > max_seq:
                    max_seq = seq
        
        return max_seq
            

            
