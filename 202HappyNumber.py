class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0 or n == 0:
            return False
        if n == 1:
            return True
        visited = []
        while True:
            if n == 1:
                return True
            if n in visited:
                return False
            visited.append(n)
            new = 0
            while n > 0:
                new += pow(n % 10, 2)
                n = n / 10
            n = new
            
        return False
            