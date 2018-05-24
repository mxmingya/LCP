class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost or len(cost) == 0:
            return 0
        
        l = len(cost)
        if l == 1:
            return cost[0]
        
        step2, step1 = cost[0], cost[1]
        
        for i in range(2, l):
            temp = step1
            step1 = cost[i] + min(step1, step2)
            step2 = temp
            
        
        return min(step1, step2)

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost or len(cost) == 0:
            return 0
        
        l = len(cost)
        if l == 1:
            return cost[0]
        
        dp = [cost[0], cost[1]]
        
        for i in range(2, l):
            dp.append(cost[i] + min(dp[i-1], dp[i-2]))
        
        return min(dp[-1], dp[-2])