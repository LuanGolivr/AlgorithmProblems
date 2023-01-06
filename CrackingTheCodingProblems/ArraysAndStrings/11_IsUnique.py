class Solution:
    def IsUnique(self, strng) -> bool:
        count = [0] * 26
        
        for letter in strng:
            count[ord(letter) - ord('a')] += 1
        
        for i in range(26):
            if count[i] > 1:
                return False
        
        return True
    
    #TC = O(N) where N is the length of the string
    #SC = O(1)



s = Solution()
s.IsUnique('abcdef')
s.IsUnique('hgtikdddh')

