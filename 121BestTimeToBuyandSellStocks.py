class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l <= 1: return 0
        max = 0
        res = 0
        for i in range(1, l):
            n = prices[i] - prices[i-1]
            max = max + n if max + n > 0 else 0
            res = res if res > max else max
        return res