class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (right + left) // 2

            if nums[m] == target:
                return m
            
            elif nums[m] < target:
                left += 1
            else:
                right -= 1
        
        return -1