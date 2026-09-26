class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            
            else:
                freq[nums[i]] += 1


        buckets = [[] for _ in range(len(nums)+1)]

        for key, val in freq.items():
            buckets[val].append(key)
        
        out = []
        
        for i in range(len(nums), 0, -1):
            if not buckets[i]:
                continue
            if len(out) < k:
                for v in buckets[i]:
                    out.append(v)
                
        
        return out

