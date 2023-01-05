class Solution:
    def topKFrequent(self, nums, k):
        ans = []
        mapping = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            mapping[nums[i]] = 1 + mapping.get(nums[i], 0)

        for key, val in mapping.items():
            frequency[val].append(key)

        for j in range(len(frequency) - 1, 0, -1):
            for value in frequency[j]:
                ans.append(value)
                if len(ans) == k:
                    return ans

        return ans  