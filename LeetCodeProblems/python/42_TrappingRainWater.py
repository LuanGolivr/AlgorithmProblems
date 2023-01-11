class Solution:
    def trap(self, height) -> int:     
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        current = 0
        for i in range(len(height)):
            maxLeft[i] = current
            current = max(current, height[i])
        
        current = 0
        for j in range(len(height) - 1, -1, -1):
            maxRight[j] = current
            current = max(current, height[j])
        
        ans = 0

        for k in range(len(height)):
            value = min(maxLeft[k], maxRight[k]) - height[k]

            if value > 0:
                ans += value
        
        return ans
    
    #TC: O(N)
    #SC: O(N)
    
    def trap2(self, height):
        if not height: return 0
        
        left, right  = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        ans = 0
        
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                ans += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                ans += maxRight - height[right]
        
        return ans
    #TC: O(N)
    #SC: O(1)        

        

height = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
s.trap(height)