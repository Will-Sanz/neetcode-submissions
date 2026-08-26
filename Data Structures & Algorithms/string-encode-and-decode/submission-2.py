import string
class Solution:

    # encode with length of string + '#'
    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            encode += str(len(string))
            encode += '#'
            encode += string
        return encode
        
    # when you hit a #, read the length and then the next that many characters
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i: j])
            start = j + 1
            res.append(s[start: start + length])
            i = start + length
        return res

        


        
        
