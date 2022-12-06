#include <iostream>
#include <vector>
#include <unordered_set>

/*
    The problem is pretty simple you just have to find whether there is a duplicate number or not
    if there is you must return true if there is not you return false.

    Time Complexity: O(N) because we're iterate and visiting every single element only once.
    Space Complecity: O(N) because we're going to store every single element we've visited before to ensure that don't have a duplicate number.

*/


class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> caching;

        for(int i = 0; i < nums.size(); i++){
            
            if(caching.find(nums[i]) != caching.end()){
                return true;
            }

            caching.insert(nums[i]);
        }

        return false;
    }
};