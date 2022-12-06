#include <vector>
#include <algorithm>

/*
    Time complexity: O(N) we're just going through every single element once.
    Space complexity: O(1) we're not storing anything.
*/

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int ans = 0;

        int i = 0;
        for(int k = 0; k < prices.size(); k++){
            
            if(prices[k] < prices[i]){
                i = k;
            } else {
                int value = prices[k] - prices[i];
                ans = std::max(ans, value);
            }
        }

        return ans;
    }
};