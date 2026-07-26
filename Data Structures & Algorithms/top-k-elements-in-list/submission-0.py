class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}

        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in dct.items():
            freq[count].append(num)
        
        i = len(freq) - 1
        j = 0
        out = []
        while j < k and i >= 0:
            for num in freq[i]:
                j += 1

                out.append(num)
                if j == k:
                    break

            i -= 1
        return out

        



        