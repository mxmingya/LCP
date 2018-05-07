class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step1 = 1
        step2 = 2
        # max = 0
        if n == 1:
            return step1
        if n == 2:
            return step2
        while(n > 1):
            temp = step1
            step1 = step2
            step2 = temp + step1
            n -= 1
        return step1
        
        