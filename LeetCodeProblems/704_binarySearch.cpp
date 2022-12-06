#include <vector>

/*
    Time complexity: O(log N) Size we're using binary search the TC goes around log N
    Space complexity: O(1) We're not storing anything.
*/

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r){
            int m = (l + r)/ 2;

            if(nums[m] == target){
                return m;
            }
            else if(nums[m] > target){
                r = m - 1;
            }else {
                l = m + 1;
            }
        }

        return -1; 
    }
};