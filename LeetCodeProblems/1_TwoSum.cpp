#include <vector>
#include <unordered_map>

/*
    Time Complexity: O(N) ,because we're going to iterate through the entire array just once.
    Space Complexity: O(N) because we're going to store every single element we've visited during the iteration.

*/


class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        
        std::unordered_map<int, int> caching;
        std::vector<int> answer;

        for(int i = 0; i < nums.size(); i++){

            int value = (target - nums[i]);

            if(caching.find(value) != caching.end()){
                answer.push_back(i);
                answer.push_back(caching[value]);
                break;
            }
            caching.insert({nums[i], i});
        }

        return answer;
    }

};