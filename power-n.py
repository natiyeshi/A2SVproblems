class Solution(object):
    def myPow(self, x, n):
        if n == 0 :
            return 1
        if n < 0 and x != 0 :
            x = 1/x
            n = abs(n)
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x * self.myPow(x*x,n/2)
        
