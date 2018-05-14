class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 2]
        
        for i in range(3, n+1):
            res = 0
            for j in range(1, i+1):
                res += dp[j-1] * dp[i-j]
            dp.append(res)
        
        return dp[n]