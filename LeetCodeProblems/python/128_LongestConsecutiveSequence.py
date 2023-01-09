class Solution:
    def longestConsecutive(self, nums):
        caching = set()

        for value in nums:
            caching.add(value)

        ans = 0
        for value in nums:
            if value - 1 not in caching:
                sequence = 1
                current = value
                while (current + 1) in caching:
                    current += 1
                    sequence += 1
                
                ans = max(ans, sequence)
            
        
        return ans