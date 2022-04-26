class Solution:
    def plusOne(self, digits):
        ans = []
        stringValue = ''

        for values in digits:
            stringValue = stringValue + str(values)

        newValue = int(stringValue) + 1
        stringValue = str(newValue)
        
        for values in stringValue:
            ans.append(int(values))
        
        return ans



digits = [1,2,3]
s = Solution()
s.plusOne(digits)