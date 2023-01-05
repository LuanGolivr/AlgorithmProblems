class Solution:
    def isAnagram(self, s, t) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        

        for j in range(26):
            if count[j]:
                return False
        
        return True


        #TC = O(N)
        #SC = O(1)