class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (left + right) // 2

            if nums[m] == target:
                return m
            
            if nums[left] <= nums[m]:
                if target > nums[m] or target < nums[left]:
                    left = m + 1
                else:
                    right = m - 1
            else:
                if target < nums[m] or target > nums[right]:
                    right = m - 1
                else:
                    left = m + 1
        
        return -1