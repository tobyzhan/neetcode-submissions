class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for i in range(len(strs)):

            

            if tuple(sorted(strs[i])) not in dct:
                dct[tuple(sorted(strs[i]))] = [strs[i]]
            
            elif tuple(sorted(strs[i])) in dct:
                dct[tuple(sorted(strs[i]))].append(strs[i])


        out = []
        for key, val in dct.items():
            out.append(val)
        return out 