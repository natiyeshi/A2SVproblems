class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    sum_ = 0
                    while stack and stack[-1] != "(":
                        sum_ += stack.pop()
                    if stack:
                        stack.pop()
                    stack.append(2*sum_)
            
        return sum(stack)    
                        
       
                