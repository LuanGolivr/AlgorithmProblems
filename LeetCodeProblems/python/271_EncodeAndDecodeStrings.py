class Solution:
    def encode(self, str):
        res = ""
        for s in str:
            res += str(len(s)) + "#" + s
        
        return res
    
    
    def decode(self, str):
        res, i = [], 0
        
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            lenght = int(str[i: j])
            res.append(str[j + 1: j + 1 + lenght])
            i = j + 1 + lenght
        
        return res