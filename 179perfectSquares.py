import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1, 2, 3]
        if n <= 2:
            return dp[n]
        
        for i in range(4, n+1):
            mini = 10000
            for j in range(1, int(math.sqrt(i))+1):
                mini = min(mini, dp[i-j*j])
            dp.append(mini+1)
        
        # for i in range(len(dp)): print("%d %d" % (i, dp[i]))
        return dp[n]