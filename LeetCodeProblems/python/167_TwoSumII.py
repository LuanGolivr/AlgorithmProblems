class Solution:
    def twoSum(self, numbers, target):
        ans = []
        left = 0
        right = len(numbers)- 1

        while left < right:
            value = numbers[left] + numbers[right]

            if value == target:
                ans.append(left+ 1)
                ans.append(right + 1)
                return ans
            elif value > target:
                right -= 1
            else:
                left += 1