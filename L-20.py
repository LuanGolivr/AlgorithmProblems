class Solution:
    def isValid(self, s):
        stack = []
        top = -1
        
        for chac in s:
            if top == -1:
                stack.append(chac)
                top += 1
            elif chac == "]" and stack[top] == "[":
                stack.pop()
                top -= 1
            elif chac == "}" and stack[top] == "{":
                stack.pop()
                top -= 1
            elif chac == ")" and stack[top] == "(":
                stack.pop()
                top -= 1
            else:
                stack.append(chac)
                top += 1
        
        if len(stack) <= 0:
            return True
        else:
            return False