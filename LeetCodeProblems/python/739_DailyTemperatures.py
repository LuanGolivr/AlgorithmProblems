class Solution:
    def dailyTemperatures(self, temperatures):

        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp = stack.pop()
                ans[temp[1]] = i - temp[1]

            stack.append([temperatures[i], i])
        
        return ans
    
    #TC = O(N)