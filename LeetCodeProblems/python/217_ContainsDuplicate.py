class Solution:
    def containsDuplicate(self, nums) -> bool:
        caching = set()

        for value in nums:
            if value not in caching:
                caching.add(value)
            else:
                return True

        return False

    #TC: O(N)
    #SC: O(N)