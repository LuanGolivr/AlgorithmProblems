class Solution:
    def carFleet(self, target, position, speed):
        pair = []
        
        for i in range(len(position)):
            pair.append((position[i], speed[i]))
        
        stack = []
        
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
    
        #TC: O(N * log N)
        #SC: O(N)
        
            