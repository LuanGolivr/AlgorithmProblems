class Solution:
    def checkPermutation(self, s, t)-> bool:
        if len(s) != len(t):
            return False
        
        mappingS = [0] * 26
        mappingT = [0] * 26
        
        for i in range(len(s)):
            mappingS[ord(s[i]) - ord('a')] += 1
            mappingT[ord(t[i])- ord('a')] += 1
            
        
        for i in range(26):
            if mappingS[i] != mappingT[i]:
                return False
        
        return True
    
    #TC = O(N)
    #SC = O(1)
    

s = Solution()
print(s.checkPermutation('car', 'acr'))
print(s.checkPermutation('rat', 'freeezer'))
print(s.checkPermutation('modification', 'fitioncadimo'))