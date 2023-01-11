class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []

        for value in tokens:
            if any(map(str.isdigit, value)):
                stack.append(int(value))
            else:
                secondValue = stack.pop()
                firstValue = stack.pop()

                if value == "+":
                    value = firstValue + secondValue
                
                elif value == "-":
                    value = firstValue - secondValue
                
                elif value == '*':
                    value = firstValue * secondValue
                
                else:
                    value = int(firstValue / secondValue)
                
                stack.append(value)
        
        return stack[-1]
    

s = Solution()
s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])