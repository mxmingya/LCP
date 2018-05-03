class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
            
        def helper(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            return helper(x*x, n/2) if n % 2 == 0 else x*helper(x*x, n/2)
        
        return helper(x, n)
        
       