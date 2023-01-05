class Solution:
    def twoSum(self, nums, target):
        caching = {}
        ans = []

        for i in range(len(nums)):
            val = target - nums[i]
            if val in caching:
                ans.append(caching[val])
                ans.append(i)
                return ans
            else:
                caching[nums[i]] = i
        
        #TC = O(N)
        #SC = O(N)