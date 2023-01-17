class Solution:
    def findMin(self, nums) -> int:
        ans = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (left + right) // 2

            if nums[left] <= nums[m] <= nums[right]:
                ans = min(ans, nums[m])
                right = m - 1
            
            elif nums[right] <= nums[m]:
                left = m + 1
            
            elif nums[left] > nums[m]:
                right = m
        return ans
            