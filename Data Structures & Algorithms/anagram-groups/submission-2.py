class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dct = {}

        for s in strs:

            if "".join(sorted(s)) not in dct:
                dct["".join(sorted(s))] = [s]
            
            elif "".join(sorted(s)) in dct:
                dct["".join(sorted(s))].append(s)
            
        

        return [val for key, val in dct.items()]
        