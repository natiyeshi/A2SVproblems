class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        
        stack=[]
        
        for index, val in enumerate(temperatures):
            while stack and val>stack[-1][0]:
                v, i=stack.pop()
                output[i]=index - i
            stack.append([val,index])
        return output
    
