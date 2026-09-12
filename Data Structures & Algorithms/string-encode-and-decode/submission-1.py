class Solution:

    def encode(self, strs: List[str]) -> str:

        lengths = [str(len(x)) + "#" for x in strs]

        lst = []

        for i in range(len(strs)):
            lst.append(lengths[i]+strs[i])


        return ''.join(lst)

    def decode(self, s: str) -> List[str]:

        output = []

        i = 0
        while i < len(s):
            word_len = ""
            while s[i] != "#":
                word_len += s[i]
                i += 1
            
            word_len = int(word_len) 
            i += 1
            output.append(s[i:i + word_len])
            i += word_len

        return output