class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newString = ''

        for i in range(len(s)):
            if s[i].isalnum():
                newString += s[i]
        
        left = 0
        right = len(newString) - 1

        while left <= right:
            if newString[left] != newString[right]:
                return False
            
            left += 1
            right -= 1
        
        return True