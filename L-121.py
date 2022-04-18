class Solution:
    def maxProfit(self, prices):
        mx = 0
        left, right = 0, 1
        
        while right < len(prices):
            if prices[left] < prices[right]:
                summ = prices[right] - prices[left]
                mx = max(mx, summ)
            else:
                left = right
            right +=1
        return mx



    #Here we're using two pointer to move throughtout the array and we're gonna checking the values of this 2 pointer , our goal is find the best time to buy and sell
    # so the main focus here is , if the right pointer has a minor value than left pointer the just update the left pointer. otherwise we got in a variable the diference between right - left and we assign in the mx variable the maximum between the max itself and this summ.

    # the Time complexity is O(n)