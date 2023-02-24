class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]
        i = 0
        while i < len(path):
            st = ""
            if i + 2 < len(path) and "".join(path[i:i+3]) == "../":
                if len(stack) > 1:
                    stack.pop()
                i += 3
            elif i + 1 < len(path) and path[i:i+2] == "./":
                i += 2
            elif i + 1 < len(path) and path[i:i+2] == "//":
                i += 2
            elif path[i] == "/":
                i += 1
            else:
                while i < len(path) and path[i] != "/" :
                    st += path[i]
                    i += 1
                if st == "..":
                    if len(stack) > 1:
                        stack.pop()
                    i += 2  
                elif st == ".":
                    i += 1
                else:
                    stack.append(st+"/")
                    i += 1
        if len(stack) > 1:
            stack[-1] = stack[-1][:-1]
        return "".join(stack)
                    
        