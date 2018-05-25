class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        res = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                res += i
                res += num / i
            if i * i == num:
                res -= i
            if res > num:
                return False
        return res == num