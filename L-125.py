class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while left <= right:
            if s[left].isalpha() and s[right].isalpha():
                if s[left].lower() != s[right].lower():
                    return False
                
                left += 1
                right -= 1
                continue
            
            if s[left].isalpha() == False:
                left += 1
            
            if s[right].isalpha() == False:
                right -= 1
        
        return True
