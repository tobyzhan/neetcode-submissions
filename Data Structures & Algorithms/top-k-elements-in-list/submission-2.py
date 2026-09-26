class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            
            else:
                freq[i] += 1

        lst = []
        
        for key, val in freq.items():
            lst.append((key,val))
        
        output = sorted(lst, key = lambda x: x[1])[::-1]

        return [x[0] for x in output[:k]]

