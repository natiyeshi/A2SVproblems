class Solution:
    def cal(self,a: int,b: int, op: str) -> int:
        if op == "*":return a * b
        if op == "/":return a / b
        if op == "-":return a - b
        if op == "+":return a + b
            
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] == "/" or tokens[i] == "*"  or tokens[i] == "+"  or tokens[i] == "-" :
                a = stack.pop()
                b = stack.pop()
                stack.append(int(self.cal(b,a,tokens[i])))
            else:
                stack.append(int(tokens[i]))
        return stack[0]